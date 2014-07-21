def update_keys(keys):
    """Change keys we used to support to their new equivalent."""
    updated_keys = list()
    for key in keys:
        if key in translations:
            updated_keys += [translations[key]]
        else:
            updated_keys += [key]
    return updated_keys

translations = dict(
    scl="colorscale",
    reversescl="reversescale"
)
