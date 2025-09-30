from pymdownx.superfences import fence_code_format

def python_formatter(source, language, class_name, options, md, **kwargs):
    """Custom Python code formatter that handles hide_code attribute."""
    
    html = fence_code_format(source, language, class_name, options, md, **kwargs)

    return html
