import _plotly_utils.basevalidators


class ZAxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="zaxis", parent_name="layout.scene", **kwargs):
        super(ZAxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "ZAxis"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            autorange
                Determines whether or not the range of this
                axis is computed in relation to the input data.
                See `rangemode` for more info. If `range` is
                provided, then `autorange` is set to False.
            backgroundcolor
                Sets the background color of this axis' wall.
            calendar
                Sets the calendar system to use for `range` and
                `tick0` if this is a date axis. This does not
                set the calendar for interpreting data on this
                axis, that's specified in the trace or via the
                global `layout.calendar`
            categoryarray
                Sets the order in which categories on this axis
                appear. Only has an effect if `categoryorder`
                is set to "array". Used with `categoryorder`.
            categoryarraysrc
                Sets the source reference on plot.ly for
                categoryarray .
            categoryorder
                Specifies the ordering logic for the case of
                categorical variables. By default, plotly uses
                "trace", which specifies the order that is
                present in the data supplied. Set
                `categoryorder` to *category ascending* or
                *category descending* if order should be
                determined by the alphanumerical order of the
                category names. Set `categoryorder` to "array"
                to derive the ordering from the attribute
                `categoryarray`. If a category is not found in
                the `categoryarray` array, the sorting behavior
                for that attribute will be identical to the
                "trace" mode. The unspecified categories will
                follow the categories in `categoryarray`. Set
                `categoryorder` to *total ascending* or *total
                descending* if order should be determined by
                the numerical order of the values. Similarly,
                the order can be determined by the min, max,
                sum, mean or median of all the values.
            color
                Sets default for all colors associated with
                this axis all at once: line, font, tick, and
                grid colors. Grid color is lightened by
                blending this with the plot background
                Individual pieces can override this.
            dtick
                Sets the step in-between ticks on this axis.
                Use with `tick0`. Must be a positive number, or
                special strings available to "log" and "date"
                axes. If the axis `type` is "log", then ticks
                are set every 10^(n*dtick) where n is the tick
                number. For example, to set a tick mark at 1,
                10, 100, 1000, ... set dtick to 1. To set tick
                marks at 1, 100, 10000, ... set dtick to 2. To
                set tick marks at 1, 5, 25, 125, 625, 3125, ...
                set dtick to log_10(5), or 0.69897000433. "log"
                has several special values; "L<f>", where `f`
                is a positive number, gives ticks linearly
                spaced in value (but not position). For example
                `tick0` = 0.1, `dtick` = "L0.5" will put ticks
                at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10
                plus small digits between, use "D1" (all
                digits) or "D2" (only 2 and 5). `tick0` is
                ignored for "D1" and "D2". If the axis `type`
                is "date", then you must convert the time to
                milliseconds. For example, to set the interval
                between ticks to one day, set `dtick` to
                86400000.0. "date" also has special values
                "M<n>" gives ticks spaced by a number of
                months. `n` must be a positive integer. To set
                ticks on the 15th of every third month, set
                `tick0` to "2000-01-15" and `dtick` to "M3". To
                set ticks every 4 years, set `dtick` to "M48"
            exponentformat
                Determines a formatting rule for the tick
                exponents. For example, consider the number
                1,000,000,000. If "none", it appears as
                1,000,000,000. If "e", 1e+9. If "E", 1E+9. If
                "power", 1x10^9 (with 9 in a super script). If
                "SI", 1G. If "B", 1B.
            gridcolor
                Sets the color of the grid lines.
            gridwidth
                Sets the width (in px) of the grid lines.
            hoverformat
                Sets the hover text formatting rule using d3
                formatting mini-languages which are very
                similar to those in Python. For numbers, see:
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                And for dates see:
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                We add one item to d3's date formatter: "%{n}f"
                for fractional seconds with n digits. For
                example, *2016-10-13 09:15:23.456* with
                tickformat "%H~%M~%S.%2f" would display
                "09~15~23.46"
            linecolor
                Sets the axis line color.
            linewidth
                Sets the width (in px) of the axis line.
            mirror
                Determines if the axis lines or/and ticks are
                mirrored to the opposite side of the plotting
                area. If True, the axis lines are mirrored. If
                "ticks", the axis lines and ticks are mirrored.
                If False, mirroring is disable. If "all", axis
                lines are mirrored on all shared-axes subplots.
                If "allticks", axis lines and ticks are
                mirrored on all shared-axes subplots.
            nticks
                Specifies the maximum number of ticks for the
                particular axis. The actual number of ticks
                will be chosen automatically to be less than or
                equal to `nticks`. Has an effect only if
                `tickmode` is set to "auto".
            range
                Sets the range of this axis. If the axis `type`
                is "log", then you must take the log of your
                desired range (e.g. to set the range from 1 to
                100, set the range from 0 to 2). If the axis
                `type` is "date", it should be date strings,
                like date data, though Date objects and unix
                milliseconds will be accepted and converted to
                strings. If the axis `type` is "category", it
                should be numbers, using the scale where each
                category is assigned a serial number from zero
                in the order it appears.
            rangemode
                If "normal", the range is computed in relation
                to the extrema of the input data. If *tozero*`,
                the range extends to 0, regardless of the input
                data If "nonnegative", the range is non-
                negative, regardless of the input data. Applies
                only to linear axes.
            separatethousands
                If "true", even 4-digit integers are separated
            showaxeslabels
                Sets whether or not this axis is labeled
            showbackground
                Sets whether or not this axis' wall has a
                background color.
            showexponent
                If "all", all exponents are shown besides their
                significands. If "first", only the exponent of
                the first tick is shown. If "last", only the
                exponent of the last tick is shown. If "none",
                no exponents appear.
            showgrid
                Determines whether or not grid lines are drawn.
                If True, the grid lines are drawn at every tick
                mark.
            showline
                Determines whether or not a line bounding this
                axis is drawn.
            showspikes
                Sets whether or not spikes starting from data
                points to this axis' wall are shown on hover.
            showticklabels
                Determines whether or not the tick labels are
                drawn.
            showtickprefix
                If "all", all tick labels are displayed with a
                prefix. If "first", only the first tick is
                displayed with a prefix. If "last", only the
                last tick is displayed with a suffix. If
                "none", tick prefixes are hidden.
            showticksuffix
                Same as `showtickprefix` but for tick suffixes.
            spikecolor
                Sets the color of the spikes.
            spikesides
                Sets whether or not spikes extending from the
                projection data points to this axis' wall
                boundaries are shown on hover.
            spikethickness
                Sets the thickness (in px) of the spikes.
            tick0
                Sets the placement of the first tick on this
                axis. Use with `dtick`. If the axis `type` is
                "log", then you must take the log of your
                starting tick (e.g. to set the starting tick to
                100, set the `tick0` to 2) except when
                `dtick`=*L<f>* (see `dtick` for more info). If
                the axis `type` is "date", it should be a date
                string, like date data. If the axis `type` is
                "category", it should be a number, using the
                scale where each category is assigned a serial
                number from zero in the order it appears.
            tickangle
                Sets the angle of the tick labels with respect
                to the horizontal. For example, a `tickangle`
                of -90 draws the tick labels vertically.
            tickcolor
                Sets the tick color.
            tickfont
                Sets the tick font.
            tickformat
                Sets the tick label formatting rule using d3
                formatting mini-languages which are very
                similar to those in Python. For numbers, see:
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                And for dates see:
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                We add one item to d3's date formatter: "%{n}f"
                for fractional seconds with n digits. For
                example, *2016-10-13 09:15:23.456* with
                tickformat "%H~%M~%S.%2f" would display
                "09~15~23.46"
            tickformatstops
                A tuple of plotly.graph_objects.layout.scene.za
                xis.Tickformatstop instances or dicts with
                compatible properties
            tickformatstopdefaults
                When used in a template (as layout.template.lay
                out.scene.zaxis.tickformatstopdefaults), sets
                the default property values to use for elements
                of layout.scene.zaxis.tickformatstops
            ticklen
                Sets the tick length (in px).
            tickmode
                Sets the tick mode for this axis. If "auto",
                the number of ticks is set via `nticks`. If
                "linear", the placement of the ticks is
                determined by a starting position `tick0` and a
                tick step `dtick` ("linear" is the default
                value if `tick0` and `dtick` are provided). If
                "array", the placement of the ticks is set via
                `tickvals` and the tick text is `ticktext`.
                ("array" is the default value if `tickvals` is
                provided).
            tickprefix
                Sets a tick label prefix.
            ticks
                Determines whether ticks are drawn or not. If
                "", this axis' ticks are not drawn. If
                "outside" ("inside"), this axis' are drawn
                outside (inside) the axis lines.
            ticksuffix
                Sets a tick label suffix.
            ticktext
                Sets the text displayed at the ticks position
                via `tickvals`. Only has an effect if
                `tickmode` is set to "array". Used with
                `tickvals`.
            ticktextsrc
                Sets the source reference on plot.ly for
                ticktext .
            tickvals
                Sets the values at which ticks on this axis
                appear. Only has an effect if `tickmode` is set
                to "array". Used with `ticktext`.
            tickvalssrc
                Sets the source reference on plot.ly for
                tickvals .
            tickwidth
                Sets the tick width (in px).
            title
                plotly.graph_objects.layout.scene.zaxis.Title
                instance or dict with compatible properties
            titlefont
                Deprecated: Please use
                layout.scene.zaxis.title.font instead. Sets
                this axis' title font. Note that the title's
                font used to be customized by the now
                deprecated `titlefont` attribute.
            type
                Sets the axis type. By default, plotly attempts
                to determined the axis type by looking into the
                data of the traces that referenced the axis in
                question.
            visible
                A single toggle to hide the axis while
                preserving interaction like dragging. Default
                is true when a cheater plot is present on the
                axis, otherwise false
            zeroline
                Determines whether or not a line is drawn at
                along the 0 value of this axis. If True, the
                zero line is drawn on top of the grid lines.
            zerolinecolor
                Sets the line color of the zero line.
            zerolinewidth
                Sets the width (in px) of the zero line.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class YAxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="yaxis", parent_name="layout.scene", **kwargs):
        super(YAxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "YAxis"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            autorange
                Determines whether or not the range of this
                axis is computed in relation to the input data.
                See `rangemode` for more info. If `range` is
                provided, then `autorange` is set to False.
            backgroundcolor
                Sets the background color of this axis' wall.
            calendar
                Sets the calendar system to use for `range` and
                `tick0` if this is a date axis. This does not
                set the calendar for interpreting data on this
                axis, that's specified in the trace or via the
                global `layout.calendar`
            categoryarray
                Sets the order in which categories on this axis
                appear. Only has an effect if `categoryorder`
                is set to "array". Used with `categoryorder`.
            categoryarraysrc
                Sets the source reference on plot.ly for
                categoryarray .
            categoryorder
                Specifies the ordering logic for the case of
                categorical variables. By default, plotly uses
                "trace", which specifies the order that is
                present in the data supplied. Set
                `categoryorder` to *category ascending* or
                *category descending* if order should be
                determined by the alphanumerical order of the
                category names. Set `categoryorder` to "array"
                to derive the ordering from the attribute
                `categoryarray`. If a category is not found in
                the `categoryarray` array, the sorting behavior
                for that attribute will be identical to the
                "trace" mode. The unspecified categories will
                follow the categories in `categoryarray`. Set
                `categoryorder` to *total ascending* or *total
                descending* if order should be determined by
                the numerical order of the values. Similarly,
                the order can be determined by the min, max,
                sum, mean or median of all the values.
            color
                Sets default for all colors associated with
                this axis all at once: line, font, tick, and
                grid colors. Grid color is lightened by
                blending this with the plot background
                Individual pieces can override this.
            dtick
                Sets the step in-between ticks on this axis.
                Use with `tick0`. Must be a positive number, or
                special strings available to "log" and "date"
                axes. If the axis `type` is "log", then ticks
                are set every 10^(n*dtick) where n is the tick
                number. For example, to set a tick mark at 1,
                10, 100, 1000, ... set dtick to 1. To set tick
                marks at 1, 100, 10000, ... set dtick to 2. To
                set tick marks at 1, 5, 25, 125, 625, 3125, ...
                set dtick to log_10(5), or 0.69897000433. "log"
                has several special values; "L<f>", where `f`
                is a positive number, gives ticks linearly
                spaced in value (but not position). For example
                `tick0` = 0.1, `dtick` = "L0.5" will put ticks
                at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10
                plus small digits between, use "D1" (all
                digits) or "D2" (only 2 and 5). `tick0` is
                ignored for "D1" and "D2". If the axis `type`
                is "date", then you must convert the time to
                milliseconds. For example, to set the interval
                between ticks to one day, set `dtick` to
                86400000.0. "date" also has special values
                "M<n>" gives ticks spaced by a number of
                months. `n` must be a positive integer. To set
                ticks on the 15th of every third month, set
                `tick0` to "2000-01-15" and `dtick` to "M3". To
                set ticks every 4 years, set `dtick` to "M48"
            exponentformat
                Determines a formatting rule for the tick
                exponents. For example, consider the number
                1,000,000,000. If "none", it appears as
                1,000,000,000. If "e", 1e+9. If "E", 1E+9. If
                "power", 1x10^9 (with 9 in a super script). If
                "SI", 1G. If "B", 1B.
            gridcolor
                Sets the color of the grid lines.
            gridwidth
                Sets the width (in px) of the grid lines.
            hoverformat
                Sets the hover text formatting rule using d3
                formatting mini-languages which are very
                similar to those in Python. For numbers, see:
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                And for dates see:
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                We add one item to d3's date formatter: "%{n}f"
                for fractional seconds with n digits. For
                example, *2016-10-13 09:15:23.456* with
                tickformat "%H~%M~%S.%2f" would display
                "09~15~23.46"
            linecolor
                Sets the axis line color.
            linewidth
                Sets the width (in px) of the axis line.
            mirror
                Determines if the axis lines or/and ticks are
                mirrored to the opposite side of the plotting
                area. If True, the axis lines are mirrored. If
                "ticks", the axis lines and ticks are mirrored.
                If False, mirroring is disable. If "all", axis
                lines are mirrored on all shared-axes subplots.
                If "allticks", axis lines and ticks are
                mirrored on all shared-axes subplots.
            nticks
                Specifies the maximum number of ticks for the
                particular axis. The actual number of ticks
                will be chosen automatically to be less than or
                equal to `nticks`. Has an effect only if
                `tickmode` is set to "auto".
            range
                Sets the range of this axis. If the axis `type`
                is "log", then you must take the log of your
                desired range (e.g. to set the range from 1 to
                100, set the range from 0 to 2). If the axis
                `type` is "date", it should be date strings,
                like date data, though Date objects and unix
                milliseconds will be accepted and converted to
                strings. If the axis `type` is "category", it
                should be numbers, using the scale where each
                category is assigned a serial number from zero
                in the order it appears.
            rangemode
                If "normal", the range is computed in relation
                to the extrema of the input data. If *tozero*`,
                the range extends to 0, regardless of the input
                data If "nonnegative", the range is non-
                negative, regardless of the input data. Applies
                only to linear axes.
            separatethousands
                If "true", even 4-digit integers are separated
            showaxeslabels
                Sets whether or not this axis is labeled
            showbackground
                Sets whether or not this axis' wall has a
                background color.
            showexponent
                If "all", all exponents are shown besides their
                significands. If "first", only the exponent of
                the first tick is shown. If "last", only the
                exponent of the last tick is shown. If "none",
                no exponents appear.
            showgrid
                Determines whether or not grid lines are drawn.
                If True, the grid lines are drawn at every tick
                mark.
            showline
                Determines whether or not a line bounding this
                axis is drawn.
            showspikes
                Sets whether or not spikes starting from data
                points to this axis' wall are shown on hover.
            showticklabels
                Determines whether or not the tick labels are
                drawn.
            showtickprefix
                If "all", all tick labels are displayed with a
                prefix. If "first", only the first tick is
                displayed with a prefix. If "last", only the
                last tick is displayed with a suffix. If
                "none", tick prefixes are hidden.
            showticksuffix
                Same as `showtickprefix` but for tick suffixes.
            spikecolor
                Sets the color of the spikes.
            spikesides
                Sets whether or not spikes extending from the
                projection data points to this axis' wall
                boundaries are shown on hover.
            spikethickness
                Sets the thickness (in px) of the spikes.
            tick0
                Sets the placement of the first tick on this
                axis. Use with `dtick`. If the axis `type` is
                "log", then you must take the log of your
                starting tick (e.g. to set the starting tick to
                100, set the `tick0` to 2) except when
                `dtick`=*L<f>* (see `dtick` for more info). If
                the axis `type` is "date", it should be a date
                string, like date data. If the axis `type` is
                "category", it should be a number, using the
                scale where each category is assigned a serial
                number from zero in the order it appears.
            tickangle
                Sets the angle of the tick labels with respect
                to the horizontal. For example, a `tickangle`
                of -90 draws the tick labels vertically.
            tickcolor
                Sets the tick color.
            tickfont
                Sets the tick font.
            tickformat
                Sets the tick label formatting rule using d3
                formatting mini-languages which are very
                similar to those in Python. For numbers, see:
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                And for dates see:
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                We add one item to d3's date formatter: "%{n}f"
                for fractional seconds with n digits. For
                example, *2016-10-13 09:15:23.456* with
                tickformat "%H~%M~%S.%2f" would display
                "09~15~23.46"
            tickformatstops
                A tuple of plotly.graph_objects.layout.scene.ya
                xis.Tickformatstop instances or dicts with
                compatible properties
            tickformatstopdefaults
                When used in a template (as layout.template.lay
                out.scene.yaxis.tickformatstopdefaults), sets
                the default property values to use for elements
                of layout.scene.yaxis.tickformatstops
            ticklen
                Sets the tick length (in px).
            tickmode
                Sets the tick mode for this axis. If "auto",
                the number of ticks is set via `nticks`. If
                "linear", the placement of the ticks is
                determined by a starting position `tick0` and a
                tick step `dtick` ("linear" is the default
                value if `tick0` and `dtick` are provided). If
                "array", the placement of the ticks is set via
                `tickvals` and the tick text is `ticktext`.
                ("array" is the default value if `tickvals` is
                provided).
            tickprefix
                Sets a tick label prefix.
            ticks
                Determines whether ticks are drawn or not. If
                "", this axis' ticks are not drawn. If
                "outside" ("inside"), this axis' are drawn
                outside (inside) the axis lines.
            ticksuffix
                Sets a tick label suffix.
            ticktext
                Sets the text displayed at the ticks position
                via `tickvals`. Only has an effect if
                `tickmode` is set to "array". Used with
                `tickvals`.
            ticktextsrc
                Sets the source reference on plot.ly for
                ticktext .
            tickvals
                Sets the values at which ticks on this axis
                appear. Only has an effect if `tickmode` is set
                to "array". Used with `ticktext`.
            tickvalssrc
                Sets the source reference on plot.ly for
                tickvals .
            tickwidth
                Sets the tick width (in px).
            title
                plotly.graph_objects.layout.scene.yaxis.Title
                instance or dict with compatible properties
            titlefont
                Deprecated: Please use
                layout.scene.yaxis.title.font instead. Sets
                this axis' title font. Note that the title's
                font used to be customized by the now
                deprecated `titlefont` attribute.
            type
                Sets the axis type. By default, plotly attempts
                to determined the axis type by looking into the
                data of the traces that referenced the axis in
                question.
            visible
                A single toggle to hide the axis while
                preserving interaction like dragging. Default
                is true when a cheater plot is present on the
                axis, otherwise false
            zeroline
                Determines whether or not a line is drawn at
                along the 0 value of this axis. If True, the
                zero line is drawn on top of the grid lines.
            zerolinecolor
                Sets the line color of the zero line.
            zerolinewidth
                Sets the width (in px) of the zero line.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class XAxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="xaxis", parent_name="layout.scene", **kwargs):
        super(XAxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "XAxis"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            autorange
                Determines whether or not the range of this
                axis is computed in relation to the input data.
                See `rangemode` for more info. If `range` is
                provided, then `autorange` is set to False.
            backgroundcolor
                Sets the background color of this axis' wall.
            calendar
                Sets the calendar system to use for `range` and
                `tick0` if this is a date axis. This does not
                set the calendar for interpreting data on this
                axis, that's specified in the trace or via the
                global `layout.calendar`
            categoryarray
                Sets the order in which categories on this axis
                appear. Only has an effect if `categoryorder`
                is set to "array". Used with `categoryorder`.
            categoryarraysrc
                Sets the source reference on plot.ly for
                categoryarray .
            categoryorder
                Specifies the ordering logic for the case of
                categorical variables. By default, plotly uses
                "trace", which specifies the order that is
                present in the data supplied. Set
                `categoryorder` to *category ascending* or
                *category descending* if order should be
                determined by the alphanumerical order of the
                category names. Set `categoryorder` to "array"
                to derive the ordering from the attribute
                `categoryarray`. If a category is not found in
                the `categoryarray` array, the sorting behavior
                for that attribute will be identical to the
                "trace" mode. The unspecified categories will
                follow the categories in `categoryarray`. Set
                `categoryorder` to *total ascending* or *total
                descending* if order should be determined by
                the numerical order of the values. Similarly,
                the order can be determined by the min, max,
                sum, mean or median of all the values.
            color
                Sets default for all colors associated with
                this axis all at once: line, font, tick, and
                grid colors. Grid color is lightened by
                blending this with the plot background
                Individual pieces can override this.
            dtick
                Sets the step in-between ticks on this axis.
                Use with `tick0`. Must be a positive number, or
                special strings available to "log" and "date"
                axes. If the axis `type` is "log", then ticks
                are set every 10^(n*dtick) where n is the tick
                number. For example, to set a tick mark at 1,
                10, 100, 1000, ... set dtick to 1. To set tick
                marks at 1, 100, 10000, ... set dtick to 2. To
                set tick marks at 1, 5, 25, 125, 625, 3125, ...
                set dtick to log_10(5), or 0.69897000433. "log"
                has several special values; "L<f>", where `f`
                is a positive number, gives ticks linearly
                spaced in value (but not position). For example
                `tick0` = 0.1, `dtick` = "L0.5" will put ticks
                at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10
                plus small digits between, use "D1" (all
                digits) or "D2" (only 2 and 5). `tick0` is
                ignored for "D1" and "D2". If the axis `type`
                is "date", then you must convert the time to
                milliseconds. For example, to set the interval
                between ticks to one day, set `dtick` to
                86400000.0. "date" also has special values
                "M<n>" gives ticks spaced by a number of
                months. `n` must be a positive integer. To set
                ticks on the 15th of every third month, set
                `tick0` to "2000-01-15" and `dtick` to "M3". To
                set ticks every 4 years, set `dtick` to "M48"
            exponentformat
                Determines a formatting rule for the tick
                exponents. For example, consider the number
                1,000,000,000. If "none", it appears as
                1,000,000,000. If "e", 1e+9. If "E", 1E+9. If
                "power", 1x10^9 (with 9 in a super script). If
                "SI", 1G. If "B", 1B.
            gridcolor
                Sets the color of the grid lines.
            gridwidth
                Sets the width (in px) of the grid lines.
            hoverformat
                Sets the hover text formatting rule using d3
                formatting mini-languages which are very
                similar to those in Python. For numbers, see:
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                And for dates see:
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                We add one item to d3's date formatter: "%{n}f"
                for fractional seconds with n digits. For
                example, *2016-10-13 09:15:23.456* with
                tickformat "%H~%M~%S.%2f" would display
                "09~15~23.46"
            linecolor
                Sets the axis line color.
            linewidth
                Sets the width (in px) of the axis line.
            mirror
                Determines if the axis lines or/and ticks are
                mirrored to the opposite side of the plotting
                area. If True, the axis lines are mirrored. If
                "ticks", the axis lines and ticks are mirrored.
                If False, mirroring is disable. If "all", axis
                lines are mirrored on all shared-axes subplots.
                If "allticks", axis lines and ticks are
                mirrored on all shared-axes subplots.
            nticks
                Specifies the maximum number of ticks for the
                particular axis. The actual number of ticks
                will be chosen automatically to be less than or
                equal to `nticks`. Has an effect only if
                `tickmode` is set to "auto".
            range
                Sets the range of this axis. If the axis `type`
                is "log", then you must take the log of your
                desired range (e.g. to set the range from 1 to
                100, set the range from 0 to 2). If the axis
                `type` is "date", it should be date strings,
                like date data, though Date objects and unix
                milliseconds will be accepted and converted to
                strings. If the axis `type` is "category", it
                should be numbers, using the scale where each
                category is assigned a serial number from zero
                in the order it appears.
            rangemode
                If "normal", the range is computed in relation
                to the extrema of the input data. If *tozero*`,
                the range extends to 0, regardless of the input
                data If "nonnegative", the range is non-
                negative, regardless of the input data. Applies
                only to linear axes.
            separatethousands
                If "true", even 4-digit integers are separated
            showaxeslabels
                Sets whether or not this axis is labeled
            showbackground
                Sets whether or not this axis' wall has a
                background color.
            showexponent
                If "all", all exponents are shown besides their
                significands. If "first", only the exponent of
                the first tick is shown. If "last", only the
                exponent of the last tick is shown. If "none",
                no exponents appear.
            showgrid
                Determines whether or not grid lines are drawn.
                If True, the grid lines are drawn at every tick
                mark.
            showline
                Determines whether or not a line bounding this
                axis is drawn.
            showspikes
                Sets whether or not spikes starting from data
                points to this axis' wall are shown on hover.
            showticklabels
                Determines whether or not the tick labels are
                drawn.
            showtickprefix
                If "all", all tick labels are displayed with a
                prefix. If "first", only the first tick is
                displayed with a prefix. If "last", only the
                last tick is displayed with a suffix. If
                "none", tick prefixes are hidden.
            showticksuffix
                Same as `showtickprefix` but for tick suffixes.
            spikecolor
                Sets the color of the spikes.
            spikesides
                Sets whether or not spikes extending from the
                projection data points to this axis' wall
                boundaries are shown on hover.
            spikethickness
                Sets the thickness (in px) of the spikes.
            tick0
                Sets the placement of the first tick on this
                axis. Use with `dtick`. If the axis `type` is
                "log", then you must take the log of your
                starting tick (e.g. to set the starting tick to
                100, set the `tick0` to 2) except when
                `dtick`=*L<f>* (see `dtick` for more info). If
                the axis `type` is "date", it should be a date
                string, like date data. If the axis `type` is
                "category", it should be a number, using the
                scale where each category is assigned a serial
                number from zero in the order it appears.
            tickangle
                Sets the angle of the tick labels with respect
                to the horizontal. For example, a `tickangle`
                of -90 draws the tick labels vertically.
            tickcolor
                Sets the tick color.
            tickfont
                Sets the tick font.
            tickformat
                Sets the tick label formatting rule using d3
                formatting mini-languages which are very
                similar to those in Python. For numbers, see:
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                And for dates see:
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                We add one item to d3's date formatter: "%{n}f"
                for fractional seconds with n digits. For
                example, *2016-10-13 09:15:23.456* with
                tickformat "%H~%M~%S.%2f" would display
                "09~15~23.46"
            tickformatstops
                A tuple of plotly.graph_objects.layout.scene.xa
                xis.Tickformatstop instances or dicts with
                compatible properties
            tickformatstopdefaults
                When used in a template (as layout.template.lay
                out.scene.xaxis.tickformatstopdefaults), sets
                the default property values to use for elements
                of layout.scene.xaxis.tickformatstops
            ticklen
                Sets the tick length (in px).
            tickmode
                Sets the tick mode for this axis. If "auto",
                the number of ticks is set via `nticks`. If
                "linear", the placement of the ticks is
                determined by a starting position `tick0` and a
                tick step `dtick` ("linear" is the default
                value if `tick0` and `dtick` are provided). If
                "array", the placement of the ticks is set via
                `tickvals` and the tick text is `ticktext`.
                ("array" is the default value if `tickvals` is
                provided).
            tickprefix
                Sets a tick label prefix.
            ticks
                Determines whether ticks are drawn or not. If
                "", this axis' ticks are not drawn. If
                "outside" ("inside"), this axis' are drawn
                outside (inside) the axis lines.
            ticksuffix
                Sets a tick label suffix.
            ticktext
                Sets the text displayed at the ticks position
                via `tickvals`. Only has an effect if
                `tickmode` is set to "array". Used with
                `tickvals`.
            ticktextsrc
                Sets the source reference on plot.ly for
                ticktext .
            tickvals
                Sets the values at which ticks on this axis
                appear. Only has an effect if `tickmode` is set
                to "array". Used with `ticktext`.
            tickvalssrc
                Sets the source reference on plot.ly for
                tickvals .
            tickwidth
                Sets the tick width (in px).
            title
                plotly.graph_objects.layout.scene.xaxis.Title
                instance or dict with compatible properties
            titlefont
                Deprecated: Please use
                layout.scene.xaxis.title.font instead. Sets
                this axis' title font. Note that the title's
                font used to be customized by the now
                deprecated `titlefont` attribute.
            type
                Sets the axis type. By default, plotly attempts
                to determined the axis type by looking into the
                data of the traces that referenced the axis in
                question.
            visible
                A single toggle to hide the axis while
                preserving interaction like dragging. Default
                is true when a cheater plot is present on the
                axis, otherwise false
            zeroline
                Determines whether or not a line is drawn at
                along the 0 value of this axis. If True, the
                zero line is drawn on top of the grid lines.
            zerolinecolor
                Sets the line color of the zero line.
            zerolinewidth
                Sets the width (in px) of the zero line.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class UirevisionValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="uirevision", parent_name="layout.scene", **kwargs):
        super(UirevisionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HovermodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="hovermode", parent_name="layout.scene", **kwargs):
        super(HovermodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "modebar"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["closest", False]),
            **kwargs
        )


import _plotly_utils.basevalidators


class DragmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="dragmode", parent_name="layout.scene", **kwargs):
        super(DragmodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["orbit", "turntable", "zoom", "pan", False]),
            **kwargs
        )


import _plotly_utils.basevalidators


class DomainValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="domain", parent_name="layout.scene", **kwargs):
        super(DomainValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Domain"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            column
                If there is a layout grid, use the domain for
                this column in the grid for this scene subplot
                .
            row
                If there is a layout grid, use the domain for
                this row in the grid for this scene subplot .
            x
                Sets the horizontal domain of this scene
                subplot (in plot fraction).
            y
                Sets the vertical domain of this scene subplot
                (in plot fraction).
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class CameraValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="camera", parent_name="layout.scene", **kwargs):
        super(CameraValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Camera"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            center
                Sets the (x,y,z) components of the 'center'
                camera vector This vector determines the
                translation (x,y,z) space about the center of
                this scene. By default, there is no such
                translation.
            eye
                Sets the (x,y,z) components of the 'eye' camera
                vector. This vector determines the view point
                about the origin of this scene.
            projection
                plotly.graph_objects.layout.scene.camera.Projec
                tion instance or dict with compatible
                properties
            up
                Sets the (x,y,z) components of the 'up' camera
                vector. This vector determines the up direction
                of this scene with respect to the page. The
                default is *{x: 0, y: 0, z: 1}* which means
                that the z axis points up.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class BgcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name="bgcolor", parent_name="layout.scene", **kwargs):
        super(BgcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class AspectratioValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="aspectratio", parent_name="layout.scene", **kwargs):
        super(AspectratioValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Aspectratio"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            x

            y

            z

""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class AspectmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="aspectmode", parent_name="layout.scene", **kwargs):
        super(AspectmodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {}),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["auto", "cube", "data", "manual"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class AnnotationValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="annotationdefaults", parent_name="layout.scene", **kwargs
    ):
        super(AnnotationValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Annotation"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class AnnotationsValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name="annotations", parent_name="layout.scene", **kwargs):
        super(AnnotationsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Annotation"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            align
                Sets the horizontal alignment of the `text`
                within the box. Has an effect only if `text`
                spans more two or more lines (i.e. `text`
                contains one or more <br> HTML tags) or if an
                explicit width is set to override the text
                width.
            arrowcolor
                Sets the color of the annotation arrow.
            arrowhead
                Sets the end annotation arrow head style.
            arrowside
                Sets the annotation arrow head position.
            arrowsize
                Sets the size of the end annotation arrow head,
                relative to `arrowwidth`. A value of 1
                (default) gives a head about 3x as wide as the
                line.
            arrowwidth
                Sets the width (in px) of annotation arrow
                line.
            ax
                Sets the x component of the arrow tail about
                the arrow head (in pixels).
            ay
                Sets the y component of the arrow tail about
                the arrow head (in pixels).
            bgcolor
                Sets the background color of the annotation.
            bordercolor
                Sets the color of the border enclosing the
                annotation `text`.
            borderpad
                Sets the padding (in px) between the `text` and
                the enclosing border.
            borderwidth
                Sets the width (in px) of the border enclosing
                the annotation `text`.
            captureevents
                Determines whether the annotation text box
                captures mouse move and click events, or allows
                those events to pass through to data points in
                the plot that may be behind the annotation. By
                default `captureevents` is False unless
                `hovertext` is provided. If you use the event
                `plotly_clickannotation` without `hovertext`
                you must explicitly enable `captureevents`.
            font
                Sets the annotation text font.
            height
                Sets an explicit height for the text box. null
                (default) lets the text set the box height.
                Taller text will be clipped.
            hoverlabel
                plotly.graph_objects.layout.scene.annotation.Ho
                verlabel instance or dict with compatible
                properties
            hovertext
                Sets text to appear when hovering over this
                annotation. If omitted or blank, no hover label
                will appear.
            name
                When used in a template, named items are
                created in the output figure in addition to any
                items the figure already has in this array. You
                can modify these items in the output figure by
                making your own item with `templateitemname`
                matching this `name` alongside your
                modifications (including `visible: false` or
                `enabled: false` to hide it). Has no effect
                outside of a template.
            opacity
                Sets the opacity of the annotation (text +
                arrow).
            showarrow
                Determines whether or not the annotation is
                drawn with an arrow. If True, `text` is placed
                near the arrow's tail. If False, `text` lines
                up with the `x` and `y` provided.
            standoff
                Sets a distance, in pixels, to move the end
                arrowhead away from the position it is pointing
                at, for example to point at the edge of a
                marker independent of zoom. Note that this
                shortens the arrow from the `ax` / `ay` vector,
                in contrast to `xshift` / `yshift` which moves
                everything by this amount.
            startarrowhead
                Sets the start annotation arrow head style.
            startarrowsize
                Sets the size of the start annotation arrow
                head, relative to `arrowwidth`. A value of 1
                (default) gives a head about 3x as wide as the
                line.
            startstandoff
                Sets a distance, in pixels, to move the start
                arrowhead away from the position it is pointing
                at, for example to point at the edge of a
                marker independent of zoom. Note that this
                shortens the arrow from the `ax` / `ay` vector,
                in contrast to `xshift` / `yshift` which moves
                everything by this amount.
            templateitemname
                Used to refer to a named item in this array in
                the template. Named items from the template
                will be created even without a matching item in
                the input figure, but you can modify one by
                making an item with `templateitemname` matching
                its `name`, alongside your modifications
                (including `visible: false` or `enabled: false`
                to hide it). If there is no template or no
                matching item, this item will be hidden unless
                you explicitly show it with `visible: true`.
            text
                Sets the text associated with this annotation.
                Plotly uses a subset of HTML tags to do things
                like newline (<br>), bold (<b></b>), italics
                (<i></i>), hyperlinks (<a href='...'></a>).
                Tags <em>, <sup>, <sub> <span> are also
                supported.
            textangle
                Sets the angle at which the `text` is drawn
                with respect to the horizontal.
            valign
                Sets the vertical alignment of the `text`
                within the box. Has an effect only if an
                explicit height is set to override the text
                height.
            visible
                Determines whether or not this annotation is
                visible.
            width
                Sets an explicit width for the text box. null
                (default) lets the text set the box width.
                Wider text will be clipped. There is no
                automatic wrapping; use <br> to start a new
                line.
            x
                Sets the annotation's x position.
            xanchor
                Sets the text box's horizontal position anchor
                This anchor binds the `x` position to the
                "left", "center" or "right" of the annotation.
                For example, if `x` is set to 1, `xref` to
                "paper" and `xanchor` to "right" then the
                right-most portion of the annotation lines up
                with the right-most edge of the plotting area.
                If "auto", the anchor is equivalent to "center"
                for data-referenced annotations or if there is
                an arrow, whereas for paper-referenced with no
                arrow, the anchor picked corresponds to the
                closest side.
            xshift
                Shifts the position of the whole annotation and
                arrow to the right (positive) or left
                (negative) by this many pixels.
            y
                Sets the annotation's y position.
            yanchor
                Sets the text box's vertical position anchor
                This anchor binds the `y` position to the
                "top", "middle" or "bottom" of the annotation.
                For example, if `y` is set to 1, `yref` to
                "paper" and `yanchor` to "top" then the top-
                most portion of the annotation lines up with
                the top-most edge of the plotting area. If
                "auto", the anchor is equivalent to "middle"
                for data-referenced annotations or if there is
                an arrow, whereas for paper-referenced with no
                arrow, the anchor picked corresponds to the
                closest side.
            yshift
                Shifts the position of the whole annotation and
                arrow up (positive) or down (negative) by this
                many pixels.
            z
                Sets the annotation's z position.
""",
            ),
            **kwargs
        )
