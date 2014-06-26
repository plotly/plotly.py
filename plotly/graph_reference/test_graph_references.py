import json
with open('graph_objs_meta.json') as f:
    INFO = json.load(f)

types = ['data', 'plot_info', 'style', 'object']

attr_keys = ['required',
             'description',
             'examples',  # todo: do we want this?
             'type',
             'val_types',
             'streamable',
             'code',    # todo: do we want this?
             'default']  # todo: do we want this?


def test_type_exists():
    print "\n\ntesting if keys have 'type'\n"
    checks = True
    for obj_key, obj in INFO.items():
        if obj_key != 'trace':
            for attr_key, attr_dict in obj.items():
                if 'type' not in attr_dict:
                    checks = False
                    print obj_key, attr_key
    if not checks:
        raise Exception


def test_for_invalid_attr_keys():
    print "\n\ntesting if attr keys are valid\n"
    checks = True
    for obj_key, obj in INFO.items():
        if obj_key != 'trace':
            for attr_key, attr_dict in obj.items():
                for attr in attr_dict:
                    if attr not in attr_keys:
                        print obj_key, attr_key, attr
                        checks = False
    if not checks:
        raise Exception


def test_type_value():
    print "\n\ntesting if 'type' values are valid\n"
    checks = True
    for obj_key, obj in INFO.items():
        if obj_key != 'trace':
            for attr_key, attr_dict in obj.items():
                if 'type' in attr_dict:
                    if attr_dict['type'] not in types:
                        print obj_key, attr_key, attr_dict['type']
                        checks = False
    if not checks:
        raise Exception