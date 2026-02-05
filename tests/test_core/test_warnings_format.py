"""Test that plotly doesn't modify global warnings format (Issue #5472)"""
import warnings
import sys
from unittest import TestCase


class TestWarningsFormat(TestCase):
    """Test that importing plotly modules doesn't change warnings.formatwarning"""

    def test_import_plotly_does_not_change_warnings_format(self):
        """Importing plotly should not modify the global warnings format"""
        # Store the original format
        original_format = warnings.formatwarning
        
        # Import plotly modules that previously modified warnings.formatwarning
        # We need to reimport to test the current code state
        import importlib
        
        # Force reimport of tools module to test current state
        if 'plotly.tools' in sys.modules:
            importlib.reload(sys.modules['plotly.tools'])
        else:
            import plotly.tools
            
        # Check that warnings.formatwarning is still the original
        self.assertIs(
            warnings.formatwarning, 
            original_format,
            "Importing plotly.tools changed warnings.formatwarning globally"
        )
        
    def test_import_matplotlylib_renderer_does_not_change_warnings_format(self):
        """Importing matplotlylib.renderer should not modify the global warnings format"""
        # Store the original format
        original_format = warnings.formatwarning
        
        import importlib
        
        # Force reimport of renderer module to test current state  
        if 'plotly.matplotlylib.renderer' in sys.modules:
            importlib.reload(sys.modules['plotly.matplotlylib.renderer'])
        else:
            import plotly.matplotlylib.renderer
            
        # Check that warnings.formatwarning is still the original
        self.assertIs(
            warnings.formatwarning,
            original_format,
            "Importing plotly.matplotlylib.renderer changed warnings.formatwarning globally"
        )

    def test_warnings_format_unchanged_after_multiple_imports(self):
        """Multiple imports should not change warnings format"""
        original_format = warnings.formatwarning
        
        # Import both modules
        import plotly.tools
        import plotly.matplotlylib.renderer
        
        # Verify format is unchanged
        self.assertIs(
            warnings.formatwarning,
            original_format,
            "warnings.formatwarning was changed after importing plotly modules"
        )
