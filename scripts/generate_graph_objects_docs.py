#!/usr/bin/env python3
"""Gnerate mkdocstrings markdown pages for plotly.graph_objects."""

import argparse
import inspect
import warnings
from pathlib import Path

import plotly.graph_objects as go


def get_all_classes_and_packages():
    """Get all classes and packages from plotly.graph_objects."""
    classes = {}
    packages = {}
    
    # Excluded classes (deprecated lowercase version of Histogram2dContour)
    excluded_classes = {"plotly.graph_objects.Histogram2dcontour"}
    
    def inspect_module(module, prefix=""):
        for name in dir(module):
            if name.startswith('_'):
                continue
            obj = getattr(module, name)
            if inspect.isclass(obj):
                full_name = f"plotly.graph_objects.{name}" if not prefix else f"{prefix}.{name}"
                if full_name not in excluded_classes:
                    classes[full_name] = obj
            elif inspect.ismodule(obj) and hasattr(obj, '__file__'):
                new_prefix = f"plotly.graph_objects.{name}" if not prefix else f"{prefix}.{name}"
                packages[new_prefix] = obj
                inspect_module(obj, new_prefix)
    
    packages["plotly.graph_objects"] = go
    inspect_module(go)
    return classes, packages


def get_deprecation_info(cls):
    """Check if a class is deprecated and get the message."""
    try:
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            cls()
            for warning in w:
                if 'deprecat' in str(warning.message).lower():
                    return True, str(warning.message)
            return False, ""
    except:
        return False, ""


def generate_class_page(class_name, class_obj, output_dir):
    """Generate documentation page for a class."""
    parts = class_name.split('.')
    if len(parts) > 2:
        relative_parts = parts[2:]
        if len(relative_parts) == 1:
            file_path = output_dir / f"{parts[-1]}.md"
        else:
            parent_parts = relative_parts[:-1]
            parent_dirs = [f"{part}-package" for part in parent_parts[:-1]] + [f"{parent_parts[-1]}-package"]
            file_path = output_dir / Path(*parent_dirs) / f"{parts[-1]}.md"
    else:
        file_path = output_dir / f"{parts[-1]}.md"
    
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    content = f"# {class_name}\n\n"
    is_deprecated, deprecation_message = get_deprecation_info(class_obj)
    if is_deprecated:
        content += f"!!! info \"Deprecated\"\n"
        for line in deprecation_message.split('\n'):
            content += f"    {line}\n"
        content += "\n"
    content += f"::: {class_name}\n"
    
    if class_obj.__doc__:
        content += f"\n{class_obj.__doc__}\n"
    
    file_path.write_text(content)
    return file_path


def generate_package_index(package_name, classes, packages, output_dir):
    """Generate index page for a package."""
    parts = package_name.split('.')
    if package_name == "plotly.graph_objects":
        file_path = output_dir / "index.md"
    else:
        relative_parts = parts[2:]
        package_dirs = [f"{part}-package" for part in relative_parts[:-1]] + [f"{relative_parts[-1]}-package"]
        file_path = output_dir / Path(*package_dirs) / "index.md"
    
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Find classes and subpackages in this package
    package_classes = [name for name in classes.keys() 
                      if name.startswith(package_name + '.') and 
                      name.count('.') == package_name.count('.') + 1]
    
    subpackages = [name for name in packages.keys() 
                   if name.startswith(package_name + '.') and 
                   name.count('.') == package_name.count('.') + 1]
    
    content = f"# {package_name}\n\n"
    
    if package_classes:
        content += "## Classes\n\n"
        for class_name in sorted(package_classes):
            short_name = class_name.split('.')[-1]
            content += f"### [{short_name}]({short_name}.md)\n\n"
        content += "\n"
    
    if subpackages:
        content += "## Submodules\n\n"
        for subpackage_name in sorted(subpackages):
            short_name = subpackage_name.split('.')[-1]
            content += f"### [{short_name}]({short_name}-package/index.md)\n\n"
    content += "\n"
    
    if not package_classes and not subpackages:
        content += "This module contains no public classes or submodules.\n"
    
    file_path.write_text(content)
    return file_path


def generate_main_index(classes, packages, output_dir):
    """Generate main index with categorized classes."""
    # Get top-level classes
    top_level = [(name.split('.')[-1], name) for name in classes.keys() 
                 if name.startswith("plotly.graph_objects.") and name.count(".") == 2]
    
    # Get top-level packages
    top_level_packages = [(name.split('.')[-1], name) for name in packages.keys()
                         if name.startswith("plotly.graph_objects.") and name.count(".") == 2]
    
    # Categories from original script
    categories = {
        "Core Objects": ["Figure", "Layout"],
        "Simple Traces": ["Scatter", "Scattergl", "Bar", "Pie", "Heatmap", "Image", "Contour", "Table"],
        "Distribution Traces": ["Box", "Violin", "Histogram", "Histogram2d", "Histogram2dContour"],
        "Finance Traces": ["Ohlc", "Candlestick", "Waterfall", "Funnel", "Funnelarea", "Indicator"],
        "3D Traces": ["Scatter3d", "Surface", "Mesh3d", "Cone", "Streamtube", "Volume", "Isosurface"],
        "Map Traces": ["Scattergeo", "Choropleth", "Scattermap", "Choroplethmap", "Densitymap", 
                      "Scattermapbox", "Choroplethmapbox", "Densitymapbox"],
        "Specialized Traces": ["Scatterpolar", "Scatterpolargl", "Barpolar", "Scatterternary", 
                             "Sunburst", "Treemap", "Icicle", "Sankey", "Splom", "Parcats", 
                             "Parcoords", "Carpet", "Scattercarpet", "Contourcarpet", "Scattersmith"]
    }
    
    # Categorize classes
    categorized = {cat: [] for cat in categories}
    uncategorized = []
    
    for short_name, full_name in top_level:
        is_deprecated, _ = get_deprecation_info(classes[full_name])
        if is_deprecated:
            continue
        found = False
        for cat, cat_classes in categories.items():
            if short_name in cat_classes:
                categorized[cat].append((short_name, full_name))
                found = True
                break
        if not found:
            uncategorized.append((short_name, full_name))
    
    # Generate content
    content = """# plotly.graph_objects

plotly.graph_objects: low-level interface to figures, traces and layout

plotly.graph_objects contains the building blocks of plotly Figure: traces (Scatter, Bar, …) and Layout

```python
>>> import plotly.graph_objects as go
```

"""
    
    for cat, class_list in categorized.items():
        if class_list:
            content += f"## {cat}\n\n"
            for short_name, full_name in sorted(class_list):
                content += f"### [{short_name}]({short_name}.md)\n\n"
            content += "\n"
    
    if uncategorized:
        content += "## Other Classes\n\n"
        for short_name, full_name in sorted(uncategorized):
            content += f"### [{short_name}]({short_name}.md)\n\n"
        content += "\n"
    
    # Add modules section
    if top_level_packages:
        content += "## Modules\n\n"
        for short_name, full_name in sorted(top_level_packages):
            content += f"### [{short_name}]({short_name}-package/index.md)\n\n"
        content += "\n"
    
    (output_dir / "index.md").write_text(content)




def main():
    parser = argparse.ArgumentParser(description='Generate MkDocs pages for plotly.graph_objects')
    parser.add_argument('--output-dir', default='docs/reference/graph_objects')
    parser.add_argument('--clean', action='store_true')
    args = parser.parse_args()
    
    output_dir = Path(args.output_dir)
    
    if args.clean and output_dir.exists():
        import shutil
        shutil.rmtree(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("Discovering classes...")
    classes, packages = get_all_classes_and_packages()
    print(f"Found {len(classes)} classes")
    print(f"Found {len(packages)} packages")
    
    print("Generating class pages...")
    for class_name, class_obj in classes.items():
        generate_class_page(class_name, class_obj, output_dir)
    
    print("Generating package index pages...")
    for package_name in packages.keys():
        if package_name != "plotly.graph_objects":  # Skip main package for now
            generate_package_index(package_name, classes, packages, output_dir)
    
    print("Generating main index...")
    generate_main_index(classes, packages, output_dir)
    
    print(f"Done! Generated documentation in {output_dir}")


if __name__ == '__main__':
    main()