#!/usr/bin/env python3
"""
Script to automatically generate MkDocs reference pages for plotly.graph_objects
by inspecting the module structure and creating documentation for all classes and packages.

Usage:
    python scripts/generate_graph_objects_docs.py [--output-dir OUTPUT_DIR] [--clean]
"""

import argparse
import inspect
import os
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any
import importlib
import importlib.util

# Add the plotly package to the path
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    import plotly.graph_objects as graph_objs
except ImportError as e:
    print(f"Error importing plotly.graph_objects: {e}")
    print("Make sure you're running this script from the plotly.py repository root")
    sys.exit(1)


class GraphObjectsInspector:
    """Inspects plotly.graph_objects to discover all classes and packages."""
    
    def __init__(self):
        self.classes: Dict[str, Any] = {}
        self.packages: Dict[str, Any] = {}
        self.module_paths: Dict[str, str] = {}
        
        # Hardcoded exclusions - classes/modules to skip during documentation generation
        self.excluded_classes = [
            # Exclude the deprecated lowercase version since we have the proper cased version
            "plotly.graph_objects.Histogram2dcontour",
        ]
        self.excluded_modules = [
            # Add any modules to exclude here if needed
        ]
        
    def is_class(self, obj) -> bool:
        """Check if an object is a class."""
        return inspect.isclass(obj) and not obj.__name__.startswith('_')
    
    def get_deprecation_info(self, full_class_name: str, class_obj: Any) -> tuple[bool, str]:
        """Check if a class is deprecated and get the actual deprecation message."""
        import warnings
        
        try:
            # Capture warnings when instantiating the class
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                # Try to instantiate the class (this triggers deprecation warnings)
                class_obj()
                
                # Check if any warnings contain "deprecat"
                for warning in w:
                    if 'deprecat' in str(warning.message).lower():
                        return True, str(warning.message)
                return False, ""
        except Exception:
            # If we can't instantiate it, assume it's not deprecated
            # (it might just require parameters or have other issues)
            return False, ""
    
    def is_deprecated_class(self, full_class_name: str, class_obj: Any) -> bool:
        """Check if a class is deprecated by testing for deprecation warnings."""
        is_deprecated, _ = self.get_deprecation_info(full_class_name, class_obj)
        return is_deprecated
    
    def is_package(self, obj) -> bool:
        """Check if an object is a package/module."""
        return inspect.ismodule(obj) and not obj.__name__.split('.')[-1].startswith('_')
    
    def get_module_path(self, module) -> str:
        """Get the file path of a module."""
        try:
            return module.__file__
        except AttributeError:
            return ""
    
    def inspect_module(self, module, prefix: str = "") -> None:
        """Recursively inspect a module to find classes and packages."""
        module_name = module.__name__
        
        # Skip private modules and special modules
        if module_name.endswith('__pycache__') or module_name.startswith('_'):
            return
            
        print(f"Inspecting: {module_name}")
        
        # Get all attributes of the module
        for attr_name in dir(module):
            if attr_name.startswith('_'):
                continue
                
            try:
                attr = getattr(module, attr_name)
                full_name = f"{module_name}.{attr_name}" if prefix else f"plotly.graph_objects.{attr_name}"
                
                if self.is_class(attr):
                    # Use the public API path instead of internal module path
                    # Convert graph_objs to graph_objects in the module path
                    if module_name.startswith("plotly.graph_objs"):
                        public_full_name = module_name.replace("plotly.graph_objs", "plotly.graph_objects") + f".{attr_name}"
                    else:
                        public_full_name = f"{module_name}.{attr_name}"
                    
                    # Skip excluded classes
                    if public_full_name in self.excluded_classes:
                        print(f"  Skipping excluded class: {public_full_name}")
                        continue
                        
                    self.classes[public_full_name] = attr
                    print(f"  Found class: {public_full_name}")
                    
                elif self.is_package(attr):
                    # Check if it's actually a submodule of the current module
                    if hasattr(attr, '__file__') and attr.__file__:
                        # Convert graph_objs to graph_objects in package names too
                        public_package_name = full_name
                        if full_name.startswith("plotly.graph_objs"):
                            public_package_name = full_name.replace("plotly.graph_objs", "plotly.graph_objects")
                        
                        # Skip excluded modules
                        if public_package_name in self.excluded_modules:
                            print(f"  Skipping excluded module: {public_package_name}")
                            continue
                            
                        self.packages[public_package_name] = attr
                        self.module_paths[public_package_name] = self.get_module_path(attr)
                        print(f"  Found package: {public_package_name}")
                        
                        # Recursively inspect the package
                        self.inspect_module(attr, public_package_name)
                        
            except Exception as e:
                print(f"  Error inspecting {attr_name}: {e}")
                continue
    
    def discover_structure(self) -> None:
        """Discover the complete structure of plotly.graph_objects."""
        print("Discovering plotly.graph_objects structure...")
        
        # Add the main plotly.graph_objects module as a package
        self.packages["plotly.graph_objects"] = graph_objs
        self.module_paths["plotly.graph_objects"] = self.get_module_path(graph_objs)
        
        self.inspect_module(graph_objs)
        print(f"\nDiscovery complete:")
        print(f"  Found {len(self.classes)} classes")
        print(f"  Found {len(self.packages)} packages")


class DocumentationGenerator:
    """Generates documentation pages for classes and packages."""
    
    def __init__(self, inspector: GraphObjectsInspector, output_dir: Path):
        self.inspector = inspector
        self.output_dir = output_dir
        self.generated_files: Set[Path] = set()
        
    def clean_output_dir(self) -> None:
        """Clean the output directory."""
        if self.output_dir.exists():
            import shutil
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        print(f"Cleaned output directory: {self.output_dir}")
    
    def generate_class_page(self, class_name: str, class_obj: Any) -> Path:
        """Generate a documentation page for a class."""
        # Convert module path to file path
        # e.g., "plotly.graph_objects.Bar" -> "Bar.md"
        # e.g., "plotly.graph_objects.bar.Marker" -> "bar-package/Marker.md"
        # e.g., "plotly.graph_objects.bar.hoverlabel.Font" -> "bar/hoverlabel-package/Font.md"
        
        parts = class_name.split('.')
        if len(parts) > 2:  # plotly.graph_objects.something
            # Remove "plotly.graph_objects" prefix
            relative_parts = parts[2:]
            if len(relative_parts) == 1:
                # Top-level class: plotly.graph_objects.Bar -> Bar.md
                file_path = self.output_dir / f"{parts[-1]}.md"
            else:
                # Classes inside packages
                parent_parts = relative_parts[:-1]
                if len(parent_parts) == 1:
                    # e.g., plotly.graph_objects.bar.Marker -> bar-package/Marker.md
                    parent_dir = self.output_dir / f"{parent_parts[0]}-package"
                else:
                    # e.g., plotly.graph_objects.bar.hoverlabel.Font -> bar-package/hoverlabel-package/Font.md
                    parent_dirs_with_suffix = [part + '-package' for part in parent_parts[:-1]]
                    parent_dir = self.output_dir / Path(*parent_dirs_with_suffix) / f"{parent_parts[-1]}-package"
                file_path = parent_dir / f"{parts[-1]}.md"
        else:
            file_path = self.output_dir / f"{parts[-1]}.md"
        
        # Create directory if needed
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Generate content
        content = f"# {class_name}\n\n"
        
        # Check if this is a deprecated class
        is_deprecated, deprecation_message = self.inspector.get_deprecation_info(class_name, class_obj)
        if is_deprecated:
            content += f"!!! info \"Deprecated\"\n"
            # Use the actual deprecation message, properly indented
            for line in deprecation_message.split('\n'):
                content += f"    {line}\n"
            content += "\n"
            # Still generate the reference documentation for deprecated classes
            content += f"::: {class_name}\n"
        else:
            content += f"::: {class_name}\n"
        
        # Add class docstring if available
        if class_obj.__doc__:
            content += f"\n{class_obj.__doc__}\n"
        
        # Write file
        with open(file_path, 'w') as f:
            f.write(content)
        
        self.generated_files.add(file_path)
        
        # (No legacy stub generation for class pages)
        
        return file_path
    
    def generate_package_index(self, package_name: str, package_obj: Any) -> Path:
        """Generate an index page for a package."""
        # Convert module path to file path
        parts = package_name.split('.')
        if len(parts) > 2:  # plotly.graph_objects.something
            relative_parts = parts[2:]
            # Add -package suffix to avoid conflicts with class names
            package_name_with_suffix = f"{relative_parts[-1]}-package"
            if len(relative_parts) > 1:
                # For nested packages, all parent directories should also have -package suffix
                parent_parts = [part + '-package' for part in relative_parts[:-1]]
                file_path = self.output_dir / Path(*parent_parts) / package_name_with_suffix / "index.md"
            else:
                # For top-level packages
                file_path = self.output_dir / package_name_with_suffix / "index.md"
        else:
            # This is the main plotly.graph_objects package
            file_path = self.output_dir / "index.md"
        
        # Create directory if needed
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Find classes and packages in this package
        package_classes = []
        package_subpackages = []
        
        for class_name, class_obj in self.inspector.classes.items():
            if class_name.startswith(package_name + '.') and class_name.count('.') == package_name.count('.') + 1:
                package_classes.append(class_name)
        
        for subpackage_name, subpackage_obj in self.inspector.packages.items():
            if subpackage_name.startswith(package_name + '.') and subpackage_name.count('.') == package_name.count('.') + 1:
                package_subpackages.append(subpackage_name)
        
        # Generate content
        content = f"# {package_name}\n\n"
        
        if package_obj.__doc__:
            content += f"{package_obj.__doc__}\n\n"
        
        # Add classes section with individual headings for TOC
        if package_classes:
            content += "## Classes\n\n"
            for class_name in sorted(package_classes):
                class_display_name = class_name.split('.')[-1]
                class_file_name = f"{class_display_name}.md"
                # Add individual class as H3 heading for TOC
                content += f"### [{class_display_name}]({class_file_name})\n\n"
            content += "\n"
        
        # Add submodules section
        if package_subpackages:
            content += "## Submodules\n\n"
            for subpackage_name in sorted(package_subpackages):
                subpackage_display_name = subpackage_name.split('.')[-1]
                # Always link to local stub within the -package folder to avoid relative path issues
                subpackage_folder_name = f"{subpackage_display_name}-package"
                link = f"{subpackage_folder_name}/index.md"
                # Add individual submodule as H3 heading for TOC
                content += f"### [{subpackage_display_name}]({link})\n\n"
        content += "\n"
    
        # If no classes or submodules, add a note
        if not package_classes and not package_subpackages:
            content += "This module contains no public classes or submodules.\n"
        
        # Write file
        with open(file_path, 'w') as f:
            f.write(content)
        
        self.generated_files.add(file_path)
        return file_path
    
    def generate_main_index(self) -> Path:
        """Generate the main index page for plotly.graph_objects with both classes and packages."""
        file_path = self.output_dir / "index.md"
        
        # Get top-level classes (those directly in plotly.graph_objects)
        top_level_classes = []
        for class_name, class_obj in self.inspector.classes.items():
            if class_name.startswith("plotly.graph_objects.") and class_name.count(".") == 2:
                # This is a top-level class like plotly.graph_objects.Bar
                short_name = class_name.split(".")[-1]
                top_level_classes.append((short_name, class_name))
        
        # Get top-level packages (those directly in plotly.graph_objects)
        top_level_packages = []
        for package_name, package_obj in self.inspector.packages.items():
            if package_name.startswith("plotly.graph_objects.") and package_name.count(".") == 2:
                # This is a top-level package like plotly.graph_objects.bar
                short_name = package_name.split(".")[-1]
                top_level_packages.append((short_name, package_name))
            elif not package_name.startswith("plotly.graph_objects.") and "." not in package_name:
                # This is a top-level package like "bar" (without the full path)
                top_level_packages.append((package_name, f"plotly.graph_objects.{package_name}"))
        
        # Sort both lists
        top_level_classes.sort(key=lambda x: x[0])
        top_level_packages.sort(key=lambda x: x[0])
        
        # Generate content
        content = "# plotly.graph_objects\n\n"
        content += "The main package containing all Plotly graph objects, traces, and layout components.\n\n"
        
        # Separate classes into current and deprecated
        current_classes = []
        deprecated_classes = []
        
        for short_name, full_name in top_level_classes:
            class_obj = self.inspector.classes[full_name]
            if self.inspector.is_deprecated_class(full_name, class_obj):
                deprecated_classes.append((short_name, full_name))
            else:
                current_classes.append((short_name, full_name))
        
        # Add current classes section
        if current_classes:
            content += "## Classes\n\n"
            for short_name, full_name in current_classes:
                # Add individual class as H3 heading for TOC
                content += f"### [{short_name}]({short_name}.md)\n\n"
            content += "\n"
        
        if top_level_packages:
            content += "## Modules\n\n"
            for short_name, full_name in top_level_packages:
                package_folder_name = f"{short_name}-package"
                # Add individual module as H3 heading for TOC
                content += f"### [{short_name}]({package_folder_name}/index.md)\n\n"
            content += "\n"
        
        # Add deprecated classes section at the end
        if deprecated_classes:
            content += "## Deprecated Classes\n\n"
            content += "!!! info \"Deprecated Classes\"\n"
            content += "    These classes are deprecated and may not be available for import. Please refer to the specific implementation in the appropriate submodule for current usage.\n\n"
            for short_name, full_name in deprecated_classes:
                # Add individual deprecated class as H3 heading for TOC with clean (Deprecated) format
                content += f"### [{short_name}]({short_name}.md) (Deprecated)\n\n"
            content += "\n"
        
        # Write the file
        file_path.write_text(content)
        self.generated_files.add(file_path)
        
        return file_path
    
    def generate_all_documentation(self, clean: bool = False) -> None:
        """Generate all documentation pages."""
        if clean:
            self.clean_output_dir()
        else:
            self.output_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"\nGenerating documentation in: {self.output_dir}")
        
        # Generate class pages
        print("\nGenerating class pages...")
        for class_name, class_obj in self.inspector.classes.items():
            try:
                file_path = self.generate_class_page(class_name, class_obj)
                print(f"  Generated: {file_path.relative_to(self.output_dir)}")
            except Exception as e:
                print(f"  Error generating {class_name}: {e}")
        
        # Generate package index pages
        print("\nGenerating package index pages...")
        
        # First, generate index pages for all packages except the main one
        main_package_name = "plotly.graph_objects"
        for package_name, package_obj in self.inspector.packages.items():
            if package_name != main_package_name:  # Skip the main package for now
                try:
                    file_path = self.generate_package_index(package_name, package_obj)
                    print(f"  Generated: {file_path.relative_to(self.output_dir)}")
                except Exception as e:
                    print(f"  Error generating {package_name}: {e}")
        
        # Finally, generate the main index for plotly.graph_objects (this should be last)
        try:
            file_path = self.generate_main_index()
            print(f"  Generated: {file_path.relative_to(self.output_dir)}")
        except Exception as e:
            print(f"  Error generating main index: {e}")
        
        print(f"\nDocumentation generation complete!")
        print(f"  Generated {len(self.generated_files)} files")


def main():
    parser = argparse.ArgumentParser(description='Auto-generate MkDocs pages for plotly.graph_objects')
    parser.add_argument('--output-dir', default='docs/reference/graph_objects',
                       help='Output directory for generated pages')
    parser.add_argument('--clean', action='store_true',
                       help='Clean the output directory before generating')
    
    args = parser.parse_args()
    
    # Create inspector and discover structure
    inspector = GraphObjectsInspector()
    inspector.discover_structure()
    
    # Create generator and generate documentation
    output_dir = Path(args.output_dir)
    generator = DocumentationGenerator(inspector, output_dir)
    generator.generate_all_documentation(clean=args.clean)
    
    print(f"\nAll done! Check the generated files in: {output_dir}")


if __name__ == '__main__':
    main()