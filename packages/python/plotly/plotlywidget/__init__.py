def _jupyter_nbextension_paths():
    return [
        {
            "section": "notebook",
            "src": "nbextension",
            "dest": "plotlywidget",
            "require": "plotlywidget/extension",
        }
    ]


__frontend_version__ = "^0.1"
