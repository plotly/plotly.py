import os
import shutil
import subprocess

here = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    # Init submodules
    subprocess.check_output(["git", "submodule", "init"])

    # Update submodules
    subprocess.check_output(["git", "submodule", "update"])

    # Replace mplexporter directory
    mpl_dst = os.path.join(
        here, "packages", "python", "plotly", "plotly", "matplotlylib", "mplexporter"
    )

    shutil.rmtree(mpl_dst, ignore_errors=True)

    shutil.copytree(
        os.path.join(here, "submodules", "mplexporter", "mplexporter"), mpl_dst
    )
