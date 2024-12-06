def on_page_content(html, **kwargs):
    html = html.replace("graph_objs", "graph_objects")
    return html
