import urllib.request
import json

if __name__ == '__main__':
    with urllib.request.urlopen('https://api.plot.ly/v2/plot-schema?sha1') as response:
        with open('resources/plotly-schema-v2.json', 'w') as f:
            f.write(json.dumps(json.load(response), indent=4))
