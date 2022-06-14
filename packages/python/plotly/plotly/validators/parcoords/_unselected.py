import _plotly_utils.basevalidators


class UnselectedValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="unselected", parent_name="parcoords", **kwargs):
        super(UnselectedValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Unselected"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            The 'line' property is a dictionary of string/value 
            properties describing the unselected lines.

                Supported dict properties:

                    color
                        The 'color' property is a color and may be specified as:
                        - A hex string (e.g. '#ff0000')
                        - An rgb/rgba string (e.g. 'rgb(255,0,0)')
                        - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
                        - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
                        - A named CSS color:
                                aliceblue, antiquewhite, aqua, aquamarine, azure,
                                beige, bisque, black, blanchedalmond, blue,
                                blueviolet, brown, burlywood, cadetblue,
                                chartreuse, chocolate, coral, cornflowerblue,
                                cornsilk, crimson, cyan, darkblue, darkcyan,
                                darkgoldenrod, darkgray, darkgrey, darkgreen,
                                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                                darkorchid, darkred, darksalmon, darkseagreen,
                                darkslateblue, darkslategray, darkslategrey,
                                darkturquoise, darkviolet, deeppink, deepskyblue,
                                dimgray, dimgrey, dodgerblue, firebrick,
                                floralwhite, forestgreen, fuchsia, gainsboro,
                                ghostwhite, gold, goldenrod, gray, grey, green,
                                greenyellow, honeydew, hotpink, indianred, indigo,
                                ivory, khaki, lavender, lavenderblush, lawngreen,
                                lemonchiffon, lightblue, lightcoral, lightcyan,
                                lightgoldenrodyellow, lightgray, lightgrey,
                                lightgreen, lightpink, lightsalmon, lightseagreen,
                                lightskyblue, lightslategray, lightslategrey,
                                lightsteelblue, lightyellow, lime, limegreen,
                                linen, magenta, maroon, mediumaquamarine,
                                mediumblue, mediumorchid, mediumpurple,
                                mediumseagreen, mediumslateblue, mediumspringgreen,
                                mediumturquoise, mediumvioletred, midnightblue,
                                mintcream, mistyrose, moccasin, navajowhite, navy,
                                oldlace, olive, olivedrab, orange, orangered,
                                orchid, palegoldenrod, palegreen, paleturquoise,
                                palevioletred, papayawhip, peachpuff, peru, pink,
                                plum, powderblue, purple, red, rosybrown,
                                royalblue, rebeccapurple, saddlebrown, salmon,
                                sandybrown, seagreen, seashell, sienna, silver,
                                skyblue, slateblue, slategray, slategrey, snow,
                                springgreen, steelblue, tan, teal, thistle, tomato,
                                turquoise, violet, wheat, white, whitesmoke,
                                yellow, yellowgreen
                    opacity
                        Sets the line opacity. It is a number between 0 and 1.
                        0 is transparent. 1 is opaque.
""",
            ),
            **kwargs,
        )
