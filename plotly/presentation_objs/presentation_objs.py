"""
dashboard_objs
==========

A module for creating and manipulating spectacle-presentation dashboards.
"""

import random
import string
import pprint

from plotly import exceptions, optional_imports

IPython = optional_imports.get_module('IPython')

HEIGHT = 700
WIDTH = 1000

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
    code_themes = ['tomorrow', 'tomorrowNight']
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
    else:
        raise exceptions.PlotlyError(
            "boxtype must be either 'Text', 'Image', 'Plotly' or 'CodePane'."
        )

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


def _return_specs_for_insertion(box, position, size, margin):
    if box != 'Text':
        if size == 'small':
            scaling_factor = 4
        elif size == 'medium':
            scaling_factor = 3
        elif size == 'large':
            scaling_factor = 2
    else:
        scaling_factor = 2

    height = HEIGHT / scaling_factor
    width = WIDTH / scaling_factor

    position_to_left_top = {
        'topleft': (0 + margin, 0 + margin),
        'topright': (WIDTH - width - margin, 0 + margin),
        'bottomleft': (0 + margin, HEIGHT - height - margin),
        'bottomright': (WIDTH - width - margin, HEIGHT - height - margin),
        'center': (WIDTH / 2 - width / 2, HEIGHT / 2 - height / 2),
        'left': (0 + margin, HEIGHT / 2 - height / 2),
        'right': (WIDTH - width - margin, HEIGHT / 2 - height / 2),
        'top': (WIDTH / 2 - width / 2, 0 + margin),
        'bottom':(WIDTH / 2 - width / 2, HEIGHT - height - margin),
    }

    left, top = position_to_left_top[position]
    return left, top, height, width


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

        hashes_to_fontsize = {
            '#': 45,
            '##': 35,
            '###': 30,
            '####': 25,
        }
        for slide_num, slide in enumerate(list_of_slides):
            lines_in_slide = slide.split('\n')

            # find code snippets
            code_markers = []
            for j, line in enumerate(lines_in_slide):
                if line[0 : 3] == '```' and len(line) > 3:
                    language = line[3 : ]
                    code_start = j + 1
                if line == '```':
                    code_end = j
                    code_markers.append((code_start, code_end, language))

            # insert code snippets
            for endpts in code_markers:
                code_block = ''
                for j in range(endpts[0], endpts[1]):
                    code_block += lines_in_slide[j]
                    code_block += '\n'
                self._insert(box='CodePane',
                             text_or_url=code_block,
                             position='right', slide=slide_num,
                             size='medium', margin=40,
                             props_attr={'language': endpts[2]})

            # find markdown titles
            hashlines = []
            hashlines_indices = []
            for k, line in enumerate(lines_in_slide):
                not_in_code = (not any(k in range(endpts[0] - 1, endpts[1] + 1)
                               for endpts in code_markers))
                if '#' in line and not_in_code:
                    hash_at_line_start = False
                    for idx in range(len(line)):
                        if line[idx] == ' ':
                            pass
                        elif line[idx] == '#':
                            hash_at_line_start = True
                            break
                        else:
                            hash_at_line_start = False
                            break
                    if hash_at_line_start:
                        hashlines.append(lines_in_slide[k])
                        hashlines_indices.append(k)

            try:
                min_hashtitle_index = min(hashlines_indices)
            except ValueError:
                min_hashtitle_index = 0

            # insert markdown titles
            for h_line in hashlines:
                first_hash_index = h_line.find('#')
                last_hash_index = first_hash_index
                while h_line[last_hash_index] == '#':
                    last_hash_index += 1

                hashkey = h_line[first_hash_index : last_hash_index]
                title_fontsize = hashes_to_fontsize[hashkey]
                self._insert(box='Text',
                             text_or_url=h_line[last_hash_index + 1 : ],
                             position='top', slide=slide_num,
                             size='large', margin=40,
                             style_attr={'fontSize': title_fontsize})

            # insert images or plotly charts
            for j, line in enumerate(lines_in_slide):
                if line[0 : 2] == '![':
                    url_index = line.find('](')
                    url = line[url_index + 2 : -1]
                    if 'https://plot.ly' in url:
                        self._insert(box='Plotly', text_or_url=url,
                                     position='bottomleft', slide=slide_num,
                                     size='large', margin=40)
                    else:
                        self._insert(box='Image', text_or_url=url,
                                     position='bottomleft', slide=slide_num,
                                     size='large', margin=40)

            # TODO: add position, repeat and size features
            for line in lines_in_slide[0 : min_hashtitle_index]:
                if line.startswith('background-image:'):
                    bkgd_url = line[line.find('url(') + 4 : -1 ]
                    self._background_image(bkgd_url, slide_num,
                                           size='stretch')

            # insert text
            text = ''
            for k, line in enumerate(lines_in_slide):
                not_in_code = (not any(k in range(endpts[0] - 1, endpts[1] + 1)
                               for endpts in code_markers))
                if (k > hashlines_indices[0] and '!' not in line and
                    not_in_code):
                    text += line
                    text += '\n'
            self._insert(box='Text', text_or_url=text,
                         position='left', slide=slide_num,
                         size='small', margin=100,
                         style_attr={'fontSize': 14, 'textAlign': 'left'})

            self._color_background('#C8C8AE', slide_num)


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

    def _insert(self, box, text_or_url, position, slide=0, size='small',
                margin=0, props_attr={}, style_attr={}):
        self._add_missing_slides(slide)

        left, top, height, width = _return_specs_for_insertion(box, position,
                                                               size, margin)
        new_id = _generate_id(9)
        child = _box(box, text_or_url, left, top, height, width, new_id,
                     props_attr, style_attr)

        self['presentation']['slides'][slide]['children'].append(child)

    def _color_background(self, color, slide):
        self._add_missing_slides(slide)

        loc = self['presentation']['slides'][slide]
        loc['props']['style']['backgroundColor'] = color

    def _background_image(self, url, slide, size='stretch'):
        self._add_missing_slides(slide)

        loc = self['presentation']['slides'][slide]['props']

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
            'backgroundRepeat': 'no-repeat',
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
