import frontmatter, re, os
from pathlib import Path
import jupytext as jt

for html_path in Path("../documentation/_posts/python").glob("**/*.html"):
    if not re.match('(.*)/\d\d\d\d-\d\d-\d\d-(.*)\.html$', str(html_path)): continue
    ipynb_path = re.sub('(.*)/\d\d\d\d-\d\d-\d\d-(.*)\.html$', '\g<1>/\g<2>.ipynb', str(html_path))
    if os.path.isfile(ipynb_path):
        metadata, content = frontmatter.parse(open(html_path).read())
        if "permalink" in metadata:
            md_path = re.sub("python/(.*)/", "notebooks/\g<1>.md", metadata["permalink"])
            if not os.path.isfile(md_path): continue
            nb_fm = frontmatter.load(md_path)
            print(md_path)
            if "v4upgrade" in nb_fm["jupyter"]["plotly"]:
                metadata["v4upgrade"] = True
            nb_fm["jupyter"]["plotly"] = metadata
            frontmatter.dump(nb_fm, md_path)

    else:
        #print("NO NB", html_path)
        pass


