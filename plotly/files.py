import os

PLOTLY_DIR = os.environ.get("PLOTLY_DIR",
                            os.path.join(os.path.expanduser("~"), ".plotly"))
TEST_FILE = os.path.join(PLOTLY_DIR, ".permission_test")


def _permissions():
    try:
        if not os.path.exists(PLOTLY_DIR):
            os.mkdir(PLOTLY_DIR)
        with open(TEST_FILE, 'w') as f:
            f.write('testing\n')
        os.remove(TEST_FILE)
        return True
    except:
        return False


_file_permissions = None


def ensure_writable_plotly_dir():
    # Cache permissions status
    global _file_permissions
    if _file_permissions is None:
        _file_permissions = _permissions()
    return _file_permissions
