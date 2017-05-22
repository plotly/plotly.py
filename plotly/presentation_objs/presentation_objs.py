"""
dashboard_objs
==========

A module for creating and manipulating spectacle-presentation dashboards.
"""

import copy
import random
import string
import pprint

from plotly import colors, exceptions, optional_imports

IPython = optional_imports.get_module('IPython')

HEIGHT = 700
WIDTH = 1000

CODEPANE_THEMES = ['tomorrow', 'tomorrowNight']
VALID_STYLE_KEYS = ['fontFamily', 'fontSize', 'margin', 'position',
                    'textAlign', 'opacity', 'color', 'fontStyle',
                    'fontWeight', 'lineHeight', 'minWidth', 'textDecoration',
                    'wordBreak']
VALID_PROPS_KEYS = ['theme', 'listType', 'href']
NEEDED_STYLE_KEYS = ['left', 'top', 'height', 'width']
VALID_LANGUAGES = ['cpp', 'cs', 'css', 'fsharp', 'go', 'haskell', 'java',
                   'javascript', 'jsx', 'julia', 'xml', 'matlab', 'php',
                   'python', 'r', 'ruby', 'scala', 'sql', 'yaml']

fontWeight_dict = {
    'Thin': {'fontWeight': 100},
    'Thin Italic': {'fontWeight': 100, 'fontStyle': 'italic'},
    'Light': {'fontWeight': 300},
    'Light Italic': {'fontWeight': 300, 'fontStyle': 'italic'},
    'Regular': {'fontWeight': 400},
    'Regular Italic': {'fontWeight': 400, 'fontStyle': 'italic'},
    'Medium': {'fontWeight': 500},
    'Medium Italic': {'fontWeight': 500, 'fontStyle': 'italic'},
    'Bold': {'fontWeight': 700},
    'Bold Italic': {'fontWeight': 700, 'fontStyle': 'italic'},
    'Black': {'fontWeight': 900},
    'Black Italic': {'fontWeight': 900, 'fontStyle': 'italic'},
}


def _generate_id(size):
    letters_and_numbers = string.ascii_letters
    for num in range(10):
        letters_and_numbers += str(num)
    letters_and_numbers += str(num)

    id_str = ''
    for _ in range(size):
        id_str += random.choice(list(letters_and_numbers))
    return id_str

_paragraph_styles = {'Body': {'color': '#3d3d3d',
                              'fontFamily': 'Open Sans',
                              'fontSize': 11,
                              'fontStyle': 'normal',
                              'fontWeight': 400,
                              'lineHeight': 'normal',
                              'minWidth': 20,
                              'opacity': 1,
                              'textAlign': 'center',
                              'textDecoration': 'none'},
                    'Body Small': {'color': '#3d3d3d',
                                    'fontFamily': 'Open Sans',
                                    'fontSize': 10,
                                    'fontStyle': 'normal',
                                    'fontWeight': 400,
                                    'lineHeight': 'normal',
                                    'minWidth': 20,
                                    'opacity': 1,
                                    'textAlign': 'center',
                                    'textDecoration': 'none'},
                    'Caption': {'color': '#3d3d3d',
                                 'fontFamily': 'Open Sans',
                                 'fontSize': 11,
                                 'fontStyle': 'italic',
                                 'fontWeight': 400,
                                 'lineHeight': 'normal',
                                 'minWidth': 20,
                                 'opacity': 1,
                                 'textAlign': 'center',
                                 'textDecoration': 'none'},
                    'Heading 1': {'color': '#3d3d3d',
                                   'fontFamily': 'Open Sans',
                                   'fontSize': 26,
                                   'fontStyle': 'normal',
                                   'fontWeight': 400,
                                   'lineHeight': 'normal',
                                   'minWidth': 20,
                                   'opacity': 1,
                                   'textAlign': 'center',
                                   'textDecoration': 'none'},
                 'Heading 2': {'color': '#3d3d3d',
                                'fontFamily': 'Open Sans',
                                'fontSize': 20,
                                'fontStyle': 'normal',
                                'fontWeight': 400,
                                'lineHeight': 'normal',
                                'minWidth': 20,
                                'opacity': 1,
                                'textAlign': 'center',
                                'textDecoration': 'none'},
                 'Heading 3': {'color': '#3d3d3d',
                                'fontFamily': 'Open Sans',
                                'fontSize': 11,
                                'fontStyle': 'normal',
                                'fontWeight': 700,
                                'lineHeight': 'normal',
                                'minWidth': 20,
                                'opacity': 1,
                                'textAlign': 'center',
                                'textDecoration': 'none'}}


def _empty_slide(transition, id):
    empty_slide = {'children': [],
                  'id': id,
                  'props': {'style': {}, 'transition': transition}}
    return empty_slide


def _box(boxtype, text_or_url, left, top, height, width, id, props_attr,
         style_attr):
    children_list = []
    fontFamily = "Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace"
    if boxtype == 'Text':
        children_list = text_or_url.split('\n')
        props = {
            'isQuote': False,
            'listType': None,
            'paragraphStyle': 'Body',
            'size': 4,
            'style': {'color': '#3d3d3d',
                      'fontFamily': 'Open Sans',
                      'fontSize': 11,
                      'fontStyle': 'normal',
                      'fontWeight': 400,
                      'height': height,
                      'left': left,
                      'lineHeight': 'normal',
                      'minWidth': 20,
                      'opacity': 1,
                      'position': 'absolute',
                      'textAlign': 'center',
                      'textDecoration': 'none',
                      'top': top,
                      'width': width,
                      'wordBreak': 'break-word'}
        }
    elif boxtype == 'Image':
        props = {
            'height': 512,
            'imageName': None,
            'src': text_or_url,
            'style': {'height': height,
                      'left': left,
                      'opacity': 1,
                      'position': 'absolute',
                      'top': top,
                      'width': width},
            'width': 512
        }
    elif boxtype == 'Plotly':
        props = {
            'frameBorder': 0,
            'scrolling': 'no',
            'src': text_or_url + '.embed?link=false',
            'style': {'height': height,
                      'left': left,
                      'position': 'absolute',
                      'top': top,
                      'width': width}
        }
    elif boxtype == 'CodePane':
        props = {
            'language': 'python',
            'source': text_or_url,
            'style': {'fontFamily': fontFamily,
                      'fontSize': 13,
                      'height': height,
                      'left': left,
                      'margin': 0,
                      'position': 'absolute',
                      'textAlign': 'left',
                      'top': top,
                      'width': width},
            'theme': 'tomorrowNight'
        }

    # update props and style attributes
    for item in props_attr.items():
        props[item[0]] = item[1]
    for item in style_attr.items():
        props['style'][item[0]] = item[1]

    child = {
        'children': children_list,
        'id': id,
        'props': props,
        'type': boxtype
    }

    if boxtype == 'Text':
        child['defaultHeight'] = 36
        child['defaultWidth'] = 52
        child['resizeVertical'] = False
    if boxtype == 'CodePane':
        child['defaultText'] = 'Code'

    return child


def _return_box_position(left, top, height, width):
    scaled_top = HEIGHT * (0.01 * top)
    scaled_left = WIDTH * (0.01 * left)
    scaled_height = HEIGHT * (0.01 * height)
    scaled_width = WIDTH * (0.01 * width)

    return scaled_left, scaled_top, scaled_height, scaled_width


def _remove_extra_whitespace_from_line(line):
    while line.startswith('\n') or line.startswith(' '):
        line = line[1: ]
    while line.endswith('\n') or line.endswith(' '):
        line = line[: -1]
    return line


def _boxes_in_slide(slide):
    boxes = []
    slide_copy = copy.deepcopy(slide)
    prop_split = ';'
    prop_val_sep = '='

    while '.left' in slide_copy:
        prop_dict = {}
        left_idx = slide_copy.find('.left')
        l_brace_idx = slide_copy[left_idx: ].find('{{') + left_idx
        properties = slide_copy[left_idx + 1 : l_brace_idx].split(
            prop_split
        )

        for prop in properties:
            prop_name = prop.split(prop_val_sep)[0]
            prop_val = prop.split(prop_val_sep)[1]

            try:
                prop_val = int(prop_val)
            except ValueError:
                pass
            prop_dict[prop_name] = prop_val

        r_brace_idx = slide_copy[l_brace_idx: ].find('}}') + l_brace_idx
        box = slide_copy[l_brace_idx + 2 : r_brace_idx]
        box_no_breaks = _remove_extra_whitespace_from_line(box)
        boxes.append((box_no_breaks, prop_dict))

        slide_copy = slide_copy[r_brace_idx + 2: ]
    return boxes


class Presentation(dict):
    def __init__(self, markdown_string=None):
        self['presentation'] = {
            'slides': [],
            'slidePreviews': [None for _ in range(496)],
            'version': '0.1.3',
            'paragraphStyles': _paragraph_styles
        }
        if markdown_string:
            self._markdown_to_presentation(markdown_string)
        else:
            self._add_empty_slide()

    def _markdown_to_presentation(self, markdown_string):
        # parse out list of slides
        index = -1
        has_final_line = False
        while markdown_string[index] in ['\n', '-']:
            if markdown_string[index] == '-':
                has_final_line = True
                break
            index -= 1

        if not has_final_line:
            markdown_string += '\n---\n'

        text_blocks = markdown_string.split('\n---\n')
        list_of_slides = []
        for j, text in enumerate(text_blocks):
            if not all(char == '\n' for char in text):
                list_of_slides.append(text)

        for slide_num, slide in enumerate(list_of_slides):
            lines_in_slide = slide.split('\n')
            boxes = _boxes_in_slide(slide)

            # background image properties
            bkrd_image_dict = {}
            for line in lines_in_slide:
                # transition
                if 'transition:' in line:
                    index = line.find('transition:')
                    transition_text = line[index + len('transition:'): ]
                    transitions = transition_text.split(';')

                    while '' in transitions:
                        transitions.remove('')

                    for j, item in enumerate(transitions):
                        transitions[j] = _remove_extra_whitespace_from_line(
                            item
                        )

                    self._set_transition(transitions, slide_num)

                if 'background-image:' in line:
                    if 'url(' in line:
                        url_index = line.find('url(')
                        bkrd_url = line[url_index + len('url('): -1]

                        bkrd_image_dict['background-image:'] = bkrd_url

                for property_name in ['background-position:',
                                      'background-repeat:',
                                      'background-size:']:
                    if property_name in line:
                        index = line.find(property_name)
                        prop = line[index + len(property_name): ]
                        prop = _remove_extra_whitespace_from_line(prop)
                        bkrd_image_dict[property_name] = prop

            if 'background-image:' in bkrd_image_dict:
                self._background_image(
                    bkrd_image_dict['background-image:'],
                    slide_num,
                    bkrd_image_dict
                )

            for box in boxes:
                # missing necessary style
                for nec_key in NEEDED_STYLE_KEYS:
                    if nec_key not in box[1].keys():
                        raise exceptions.PlotlyError(
                            "You are missing '{}' as one of the necessary "
                            "style keys in your line. All the necessary "
                            "style keys are {}".format(NEEDED_STYLE_KEYS)
                        )

                # default settings
                style_attr = {}
                props_attr = {}
                for key in box[1].keys():
                    if key in VALID_STYLE_KEYS:
                        if key == 'fontWeight' and type(box[1][key]) == str:
                            try:
                                params = fontWeight_dict[box[1][key]]
                                for item in params.items():
                                    style_attr[item[0]] = item[1]
                            except KeyError:
                                raise exceptions.PlotlyError(
                                    "If 'fontWeight' is a string, it must "
                                    "belong to the values in {}".format(
                                        fontWeight_dict.keys()
                                    )
                                )
                        else:
                            style_attr[key] = box[1][key]

                    elif key in VALID_PROPS_KEYS:
                        props_attr[key] = box[1][key]
                    elif key not in NEEDED_STYLE_KEYS:
                        raise exceptions.PlotlyError(
                            "{} is not a valid styling key. The list of "
                            "valid style keys are {}".format(
                                key, VALID_STYLE_KEYS + VALID_PROPS_KEYS
                            )
                        )

                # code
                if box[0][ : 3] == '```':
                    box_lines = box[0].split('\n')
                    language = _remove_extra_whitespace_from_line(
                        box_lines[0][3 : ]
                    ).lower()
                    if language == '' or lanugage not in VALID_LANGUAGES:
                        raise exceptions.PlotlyError(
                            "The language of your code block should be "
                            "clearly indicated after the first ``` that "
                            "begins the code block. The valid languages to "
                            "choose from are in {}".format(VALID_LANGUAGES)
                        )
                    codebox = ''
                    for line in box_lines:
                        if line[0 : 3] != '```':
                            codebox += line
                            codebox += '\n'

                    props_attr['language'] = language

                    self._insert(box='CodePane',
                                 text_or_url=codebox,
                                 left=box[1]['left'],
                                 top=box[1]['top'],
                                 height=box[1]['height'],
                                 width=box[1]['width'],
                                 slide=slide_num,
                                 props_attr=props_attr,
                                 style_attr=style_attr)

                # image or plotly
                elif box[0][: 4] == 'url(':
                    url = box[0][4 : -1]

                    # TODO: needs to support on-prem server name
                    if 'https://plot.ly' in url:
                        self._insert(box='Plotly', text_or_url=url,
                                     left=box[1]['left'], top=box[1]['top'],
                                     height=box[1]['height'],
                                     width=box[1]['width'],
                                     slide=slide_num,
                                     props_attr=props_attr,
                                     style_attr=style_attr)
                    else:
                        self._insert(box='Image', text_or_url=url,
                                     left=box[1]['left'], top=box[1]['top'],
                                     height=box[1]['height'],
                                     width=box[1]['width'],
                                     slide=slide_num, props_attr=props_attr,
                                     style_attr=style_attr)

                # text
                else:
                    box_lines = box[0].split('\n')
                    text = box[0]

                    # hyperlink
                    first_line = _remove_extra_whitespace_from_line(box[0])
                    if first_line[0] == '[' and first_line[-1] == ')':
                        # extract only hypertext from text lines
                        r_bracket_idx = first_line[1 : ].find(']') + 1
                        l_paran_idx = first_line.find('(')
                        if l_paran_idx == -1:
                            raise exceptions.PlotlyError(
                                "If you are trying to place hypertext in "
                                "your presentation slide, be sure that "
                                "your text has the form '[text](url)'. "
                                "All other text outside the hypertext is "
                                "ignored if you use the the []() "
                                "notation."
                            )

                        text = first_line[1 : r_bracket_idx]
                        url = first_line[l_paran_idx + 1 : -1]
                        props_attr['href'] = url

                    self._insert(box='Text',
                                 text_or_url=text,
                                 left=box[1]['left'],
                                 top=box[1]['top'],
                                 height=box[1]['height'],
                                 width=box[1]['width'],
                                 slide=slide_num,
                                 props_attr=props_attr,
                                 style_attr=style_attr)


    def _add_empty_slide(self):
        self['presentation']['slides'].append(
            _empty_slide(['slide'], _generate_id(9))
        )

    def _add_missing_slides(self, slide):
        # add slides if desired slide number isn't in the presentation
        try:
            self['presentation']['slides'][slide]['children']
        except IndexError:
            num_of_slides = len(self['presentation']['slides'])
            for _ in range(slide - num_of_slides + 1):
                self._add_empty_slide()

    def _insert(self, box, text_or_url, left, top, height, width, slide=0,
                props_attr={}, style_attr={}):
        self._add_missing_slides(slide)

        left, top, height, width = _return_box_position(left, top, height,
                                                        width)
        new_id = _generate_id(9)
        child = _box(box, text_or_url, left, top, height, width, new_id,
                     props_attr, style_attr)

        self['presentation']['slides'][slide]['children'].append(child)

    def _color_background(self, color, slide):
        self._add_missing_slides(slide)

        loc = self['presentation']['slides'][slide]
        loc['props']['style']['backgroundColor'] = color

    def _background_image(self, url, slide, bkrd_image_dict):
        self._add_missing_slides(slide)

        loc = self['presentation']['slides'][slide]['props']

        # default settings
        size = 'stretch'
        repeat = 'no-repeat'

        if 'background-size:' in bkrd_image_dict:
            size = bkrd_image_dict['background-size:']
        if 'background-repeat:' in bkrd_image_dict:
            repeat = bkrd_image_dict['background-repeat:']

        if size == 'stretch':
            backgroundSize = '100% 100%'
        elif size == 'original':
            backgroundSize = 'auto'
        elif size == 'contain':
            backgroundSize = 'contain'
        elif size == 'cover':
            backgroundSize = 'cover'

        style = {
            'backgroundImage': 'url({})'.format(url),
            'backgroundPosition': 'center center',
            'backgroundRepeat': repeat,
            'backgroundSize': backgroundSize
        }

        for item in style.items():
            loc['style'].setdefault(item[0], item[1])

        loc['backgroundImageSrc'] = url
        loc['backgroundImageName'] = None

    def _set_transition(self, transition, slide):
        self._add_missing_slides(slide)

        valid_transitions = ['slide',  'zoom', 'fade', 'spin']
        loc = self['presentation']['slides'][slide]['props']
        loc['transition'] = transition
