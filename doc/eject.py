import frontmatter, re, os
from pathlib import Path
import jupytext as jt

for html_path in Path("../documentation/_posts/python").glob("**/*.html"):
    if not re.match('(.*)/\d\d\d\d-\d\d-\d\d-(.*)\.html$', str(html_path)): continue
    ipynb_path = re.sub('(.*)/\d\d\d\d-\d\d-\d\d-(.*)\.html$', '\g<1>/\g<2>.ipynb', str(html_path))
    if os.path.isfile(ipynb_path):
        metadata, content = frontmatter.parse(open(html_path).read())
        if "permalink" in metadata:
            try:
                md_path = re.sub("matplotlib/(.*)/", "eject/\g<1>.md", metadata["permalink"])
                jt.writef(jt.readf(ipynb_path), md_path, fmt=".md")
                nb_fm = frontmatter.load(md_path)
                nb_fm["jupyter"]["plotly"] = metadata
                frontmatter.dump(nb_fm, md_path)
            except:
                print(metadata["permalink"], ipynb_path, "fail")
                #pass
    else:
        #print("NO NB", html_path)
        pass


