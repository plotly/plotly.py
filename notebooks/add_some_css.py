import sys

filename = sys.argv[1]
style = "<style>div.output_area{max-height:600px; overflow:scroll}</style>\n"

with open(filename, "r") as f:
    s = f.read()

with open(filename, "w") as f:
    done = False
    for line in s.splitlines():
        f.write(line + "\n")
        if not done and (line[:6] == "<head>"):
            f.write(style)
            done = True