import os

os.chdir(os.path.dirname(__file__))

for filename in os.listdir("pandas2"):
    with open(filename, encoding="utf-8") as f:
        with open(os.path.join("pandas2", filename)) as f2:
            assert f.read() == f2.read(), f"Pandas 1/2 difference in {filename}"
