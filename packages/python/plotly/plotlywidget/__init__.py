def _jupyter_labextension_paths():
    return [{"src": "labextension", "dest": "plotlywidget"}]


def _jupyter_nbextension_paths():
    return [
        {
            "section": "notebook",
            "src": "nbextension",
            "dest": "plotlywidget",
            "require": "plotlywidget/extension",
        }
    ]
