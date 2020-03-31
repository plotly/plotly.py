import _plotly_utils.basevalidators


class YAxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="yaxis", parent_name="layout", **kwargs):
        super(YAxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "YAxis"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            anchor
                If set to an opposite-letter axis id (e.g.
                `x2`, `y`), this axis is bound to the
                corresponding opposite-letter axis. If set to
                "free", this axis' position is determined by
                `position`.
            automargin
                Determines whether long tick labels
                automatically grow the figure margins.
            autorange
                Determines whether or not the range of this
                axis is computed in relation to the input data.
                See `rangemode` for more info. If `range` is
                provided, then `autorange` is set to False.
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
                Sets the source reference on Chart Studio Cloud
                for  categoryarray .
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
            constrain
                If this axis needs to be compressed (either due
                to its own `scaleanchor` and `scaleratio` or
                those of the other axis), determines how that
                happens: by increasing the "range" (default),
                or by decreasing the "domain".
            constraintoward
                If this axis needs to be compressed (either due
                to its own `scaleanchor` and `scaleratio` or
                those of the other axis), determines which
                direction we push the originally specified plot
                area. Options are "left", "center" (default),
                and "right" for x axes, and "top", "middle"
                (default), and "bottom" for y axes.
            dividercolor
                Sets the color of the dividers Only has an
                effect on "multicategory" axes.
            dividerwidth
                Sets the width (in px) of the dividers Only has
                an effect on "multicategory" axes.
            domain
                Sets the domain of this axis (in plot
                fraction).
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
            fixedrange
                Determines whether or not this axis is zoom-
                able. If true, then zoom is disabled.
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
            layer
                Sets the layer on which this axis is displayed.
                If *above traces*, this axis is displayed above
                all the subplot's traces If *below traces*,
                this axis is displayed below all the subplot's
                traces, but above the grid lines. Useful when
                used together with scatter-like traces with
                `cliponaxis` set to False to show markers
                and/or text nodes above this axis.
            linecolor
                Sets the axis line color.
            linewidth
                Sets the width (in px) of the axis line.
            matches
                If set to another axis id (e.g. `x2`, `y`), the
                range of this axis will match the range of the
                corresponding axis in data-coordinates space.
                Moreover, matching axes share auto-range
                values, category lists and histogram auto-bins.
                Note that setting axes simultaneously in both a
                `scaleanchor` and a `matches` constraint is
                currently forbidden. Moreover, note that
                matching axes must have the same `type`.
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
            overlaying
                If set a same-letter axis id, this axis is
                overlaid on top of the corresponding same-
                letter axis, with traces and axes visible for
                both axes. If False, this axis does not overlay
                any same-letter axes. In this case, for axes
                with overlapping domains only the highest-
                numbered axis will be visible.
            position
                Sets the position of this axis in the plotting
                space (in normalized coordinates). Only has an
                effect if `anchor` is set to "free".
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
            rangebreaks
                A tuple of :class:`plotly.graph_objects.layout.
                yaxis.Rangebreak` instances or dicts with
                compatible properties
            rangebreakdefaults
                When used in a template (as layout.template.lay
                out.yaxis.rangebreakdefaults), sets the default
                property values to use for elements of
                layout.yaxis.rangebreaks
            rangemode
                If "normal", the range is computed in relation
                to the extrema of the input data. If *tozero*`,
                the range extends to 0, regardless of the input
                data If "nonnegative", the range is non-
                negative, regardless of the input data. Applies
                only to linear axes.
            scaleanchor
                If set to another axis id (e.g. `x2`, `y`), the
                range of this axis changes together with the
                range of the corresponding axis such that the
                scale of pixels per unit is in a constant
                ratio. Both axes are still zoomable, but when
                you zoom one, the other will zoom the same
                amount, keeping a fixed midpoint. `constrain`
                and `constraintoward` determine how we enforce
                the constraint. You can chain these, ie `yaxis:
                {scaleanchor: *x*}, xaxis2: {scaleanchor: *y*}`
                but you can only link axes of the same `type`.
                The linked axis can have the opposite letter
                (to constrain the aspect ratio) or the same
                letter (to match scales across subplots). Loops
                (`yaxis: {scaleanchor: *x*}, xaxis:
                {scaleanchor: *y*}` or longer) are redundant
                and the last constraint encountered will be
                ignored to avoid possible inconsistent
                constraints via `scaleratio`. Note that setting
                axes simultaneously in both a `scaleanchor` and
                a `matches` constraint is currently forbidden.
            scaleratio
                If this axis is linked to another by
                `scaleanchor`, this determines the pixel to
                unit scale ratio. For example, if this value is
                10, then every unit on this axis spans 10 times
                the number of pixels as a unit on the linked
                axis. Use this for example to create an
                elevation profile where the vertical scale is
                exaggerated a fixed amount with respect to the
                horizontal.
            separatethousands
                If "true", even 4-digit integers are separated
            showdividers
                Determines whether or not a dividers are drawn
                between the category levels of this axis. Only
                has an effect on "multicategory" axes.
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
                Determines whether or not spikes (aka
                droplines) are drawn for this axis. Note: This
                only takes affect when hovermode = closest
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
            side
                Determines whether a x (y) axis is positioned
                at the "bottom" ("left") or "top" ("right") of
                the plotting area.
            spikecolor
                Sets the spike color. If undefined, will use
                the series color
            spikedash
                Sets the dash style of lines. Set to a dash
                type string ("solid", "dot", "dash",
                "longdash", "dashdot", or "longdashdot") or a
                dash length list in px (eg "5px,10px,2px,2px").
            spikemode
                Determines the drawing mode for the spike line
                If "toaxis", the line is drawn from the data
                point to the axis the  series is plotted on. If
                "across", the line is drawn across the entire
                plot area, and supercedes "toaxis". If
                "marker", then a marker dot is drawn on the
                axis the series is plotted on
            spikesnap
                Determines whether spikelines are stuck to the
                cursor or to the closest datapoints.
            spikethickness
                Sets the width (in px) of the zero line.
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
                A tuple of :class:`plotly.graph_objects.layout.
                yaxis.Tickformatstop` instances or dicts with
                compatible properties
            tickformatstopdefaults
                When used in a template (as layout.template.lay
                out.yaxis.tickformatstopdefaults), sets the
                default property values to use for elements of
                layout.yaxis.tickformatstops
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
            tickson
                Determines where ticks and grid lines are drawn
                with respect to their corresponding tick
                labels. Only has an effect for axes of `type`
                "category" or "multicategory". When set to
                "boundaries", ticks and grid lines are drawn
                half a category to the left/bottom of labels.
            ticksuffix
                Sets a tick label suffix.
            ticktext
                Sets the text displayed at the ticks position
                via `tickvals`. Only has an effect if
                `tickmode` is set to "array". Used with
                `tickvals`.
            ticktextsrc
                Sets the source reference on Chart Studio Cloud
                for  ticktext .
            tickvals
                Sets the values at which ticks on this axis
                appear. Only has an effect if `tickmode` is set
                to "array". Used with `ticktext`.
            tickvalssrc
                Sets the source reference on Chart Studio Cloud
                for  tickvals .
            tickwidth
                Sets the tick width (in px).
            title
                :class:`plotly.graph_objects.layout.yaxis.Title
                ` instance or dict with compatible properties
            titlefont
                Deprecated: Please use layout.yaxis.title.font
                instead. Sets this axis' title font. Note that
                the title's font used to be customized by the
                now deprecated `titlefont` attribute.
            type
                Sets the axis type. By default, plotly attempts
                to determined the axis type by looking into the
                data of the traces that referenced the axis in
                question.
            uirevision
                Controls persistence of user-driven changes in
                axis `range`, `autorange`, and `title` if in
                `editable: true` configuration. Defaults to
                `layout.uirevision`.
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
    def __init__(self, plotly_name="xaxis", parent_name="layout", **kwargs):
        super(XAxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "XAxis"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            anchor
                If set to an opposite-letter axis id (e.g.
                `x2`, `y`), this axis is bound to the
                corresponding opposite-letter axis. If set to
                "free", this axis' position is determined by
                `position`.
            automargin
                Determines whether long tick labels
                automatically grow the figure margins.
            autorange
                Determines whether or not the range of this
                axis is computed in relation to the input data.
                See `rangemode` for more info. If `range` is
                provided, then `autorange` is set to False.
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
                Sets the source reference on Chart Studio Cloud
                for  categoryarray .
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
            constrain
                If this axis needs to be compressed (either due
                to its own `scaleanchor` and `scaleratio` or
                those of the other axis), determines how that
                happens: by increasing the "range" (default),
                or by decreasing the "domain".
            constraintoward
                If this axis needs to be compressed (either due
                to its own `scaleanchor` and `scaleratio` or
                those of the other axis), determines which
                direction we push the originally specified plot
                area. Options are "left", "center" (default),
                and "right" for x axes, and "top", "middle"
                (default), and "bottom" for y axes.
            dividercolor
                Sets the color of the dividers Only has an
                effect on "multicategory" axes.
            dividerwidth
                Sets the width (in px) of the dividers Only has
                an effect on "multicategory" axes.
            domain
                Sets the domain of this axis (in plot
                fraction).
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
            fixedrange
                Determines whether or not this axis is zoom-
                able. If true, then zoom is disabled.
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
            layer
                Sets the layer on which this axis is displayed.
                If *above traces*, this axis is displayed above
                all the subplot's traces If *below traces*,
                this axis is displayed below all the subplot's
                traces, but above the grid lines. Useful when
                used together with scatter-like traces with
                `cliponaxis` set to False to show markers
                and/or text nodes above this axis.
            linecolor
                Sets the axis line color.
            linewidth
                Sets the width (in px) of the axis line.
            matches
                If set to another axis id (e.g. `x2`, `y`), the
                range of this axis will match the range of the
                corresponding axis in data-coordinates space.
                Moreover, matching axes share auto-range
                values, category lists and histogram auto-bins.
                Note that setting axes simultaneously in both a
                `scaleanchor` and a `matches` constraint is
                currently forbidden. Moreover, note that
                matching axes must have the same `type`.
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
            overlaying
                If set a same-letter axis id, this axis is
                overlaid on top of the corresponding same-
                letter axis, with traces and axes visible for
                both axes. If False, this axis does not overlay
                any same-letter axes. In this case, for axes
                with overlapping domains only the highest-
                numbered axis will be visible.
            position
                Sets the position of this axis in the plotting
                space (in normalized coordinates). Only has an
                effect if `anchor` is set to "free".
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
            rangebreaks
                A tuple of :class:`plotly.graph_objects.layout.
                xaxis.Rangebreak` instances or dicts with
                compatible properties
            rangebreakdefaults
                When used in a template (as layout.template.lay
                out.xaxis.rangebreakdefaults), sets the default
                property values to use for elements of
                layout.xaxis.rangebreaks
            rangemode
                If "normal", the range is computed in relation
                to the extrema of the input data. If *tozero*`,
                the range extends to 0, regardless of the input
                data If "nonnegative", the range is non-
                negative, regardless of the input data. Applies
                only to linear axes.
            rangeselector
                :class:`plotly.graph_objects.layout.xaxis.Range
                selector` instance or dict with compatible
                properties
            rangeslider
                :class:`plotly.graph_objects.layout.xaxis.Range
                slider` instance or dict with compatible
                properties
            scaleanchor
                If set to another axis id (e.g. `x2`, `y`), the
                range of this axis changes together with the
                range of the corresponding axis such that the
                scale of pixels per unit is in a constant
                ratio. Both axes are still zoomable, but when
                you zoom one, the other will zoom the same
                amount, keeping a fixed midpoint. `constrain`
                and `constraintoward` determine how we enforce
                the constraint. You can chain these, ie `yaxis:
                {scaleanchor: *x*}, xaxis2: {scaleanchor: *y*}`
                but you can only link axes of the same `type`.
                The linked axis can have the opposite letter
                (to constrain the aspect ratio) or the same
                letter (to match scales across subplots). Loops
                (`yaxis: {scaleanchor: *x*}, xaxis:
                {scaleanchor: *y*}` or longer) are redundant
                and the last constraint encountered will be
                ignored to avoid possible inconsistent
                constraints via `scaleratio`. Note that setting
                axes simultaneously in both a `scaleanchor` and
                a `matches` constraint is currently forbidden.
            scaleratio
                If this axis is linked to another by
                `scaleanchor`, this determines the pixel to
                unit scale ratio. For example, if this value is
                10, then every unit on this axis spans 10 times
                the number of pixels as a unit on the linked
                axis. Use this for example to create an
                elevation profile where the vertical scale is
                exaggerated a fixed amount with respect to the
                horizontal.
            separatethousands
                If "true", even 4-digit integers are separated
            showdividers
                Determines whether or not a dividers are drawn
                between the category levels of this axis. Only
                has an effect on "multicategory" axes.
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
                Determines whether or not spikes (aka
                droplines) are drawn for this axis. Note: This
                only takes affect when hovermode = closest
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
            side
                Determines whether a x (y) axis is positioned
                at the "bottom" ("left") or "top" ("right") of
                the plotting area.
            spikecolor
                Sets the spike color. If undefined, will use
                the series color
            spikedash
                Sets the dash style of lines. Set to a dash
                type string ("solid", "dot", "dash",
                "longdash", "dashdot", or "longdashdot") or a
                dash length list in px (eg "5px,10px,2px,2px").
            spikemode
                Determines the drawing mode for the spike line
                If "toaxis", the line is drawn from the data
                point to the axis the  series is plotted on. If
                "across", the line is drawn across the entire
                plot area, and supercedes "toaxis". If
                "marker", then a marker dot is drawn on the
                axis the series is plotted on
            spikesnap
                Determines whether spikelines are stuck to the
                cursor or to the closest datapoints.
            spikethickness
                Sets the width (in px) of the zero line.
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
                A tuple of :class:`plotly.graph_objects.layout.
                xaxis.Tickformatstop` instances or dicts with
                compatible properties
            tickformatstopdefaults
                When used in a template (as layout.template.lay
                out.xaxis.tickformatstopdefaults), sets the
                default property values to use for elements of
                layout.xaxis.tickformatstops
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
            tickson
                Determines where ticks and grid lines are drawn
                with respect to their corresponding tick
                labels. Only has an effect for axes of `type`
                "category" or "multicategory". When set to
                "boundaries", ticks and grid lines are drawn
                half a category to the left/bottom of labels.
            ticksuffix
                Sets a tick label suffix.
            ticktext
                Sets the text displayed at the ticks position
                via `tickvals`. Only has an effect if
                `tickmode` is set to "array". Used with
                `tickvals`.
            ticktextsrc
                Sets the source reference on Chart Studio Cloud
                for  ticktext .
            tickvals
                Sets the values at which ticks on this axis
                appear. Only has an effect if `tickmode` is set
                to "array". Used with `ticktext`.
            tickvalssrc
                Sets the source reference on Chart Studio Cloud
                for  tickvals .
            tickwidth
                Sets the tick width (in px).
            title
                :class:`plotly.graph_objects.layout.xaxis.Title
                ` instance or dict with compatible properties
            titlefont
                Deprecated: Please use layout.xaxis.title.font
                instead. Sets this axis' title font. Note that
                the title's font used to be customized by the
                now deprecated `titlefont` attribute.
            type
                Sets the axis type. By default, plotly attempts
                to determined the axis type by looking into the
                data of the traces that referenced the axis in
                question.
            uirevision
                Controls persistence of user-driven changes in
                axis `range`, `autorange`, and `title` if in
                `editable: true` configuration. Defaults to
                `layout.uirevision`.
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


class WidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="width", parent_name="layout", **kwargs):
        super(WidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 10),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class WaterfallmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="waterfallmode", parent_name="layout", **kwargs):
        super(WaterfallmodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["group", "overlay"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class WaterfallgroupgapValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="waterfallgroupgap", parent_name="layout", **kwargs):
        super(WaterfallgroupgapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class WaterfallgapValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="waterfallgap", parent_name="layout", **kwargs):
        super(WaterfallgapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ViolinmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="violinmode", parent_name="layout", **kwargs):
        super(ViolinmodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["group", "overlay"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class ViolingroupgapValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="violingroupgap", parent_name="layout", **kwargs):
        super(ViolingroupgapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ViolingapValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="violingap", parent_name="layout", **kwargs):
        super(ViolingapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class UpdatemenuValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="updatemenudefaults", parent_name="layout", **kwargs
    ):
        super(UpdatemenuValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Updatemenu"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class UpdatemenusValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name="updatemenus", parent_name="layout", **kwargs):
        super(UpdatemenusValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Updatemenu"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            active
                Determines which button (by index starting from
                0) is considered active.
            bgcolor
                Sets the background color of the update menu
                buttons.
            bordercolor
                Sets the color of the border enclosing the
                update menu.
            borderwidth
                Sets the width (in px) of the border enclosing
                the update menu.
            buttons
                A tuple of :class:`plotly.graph_objects.layout.
                updatemenu.Button` instances or dicts with
                compatible properties
            buttondefaults
                When used in a template (as layout.template.lay
                out.updatemenu.buttondefaults), sets the
                default property values to use for elements of
                layout.updatemenu.buttons
            direction
                Determines the direction in which the buttons
                are laid out, whether in a dropdown menu or a
                row/column of buttons. For `left` and `up`, the
                buttons will still appear in left-to-right or
                top-to-bottom order respectively.
            font
                Sets the font of the update menu button text.
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
            pad
                Sets the padding around the buttons or dropdown
                menu.
            showactive
                Highlights active dropdown item or active
                button if true.
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
            type
                Determines whether the buttons are accessible
                via a dropdown menu or whether the buttons are
                stacked horizontally or vertically
            visible
                Determines whether or not the update menu is
                visible.
            x
                Sets the x position (in normalized coordinates)
                of the update menu.
            xanchor
                Sets the update menu's horizontal position
                anchor. This anchor binds the `x` position to
                the "left", "center" or "right" of the range
                selector.
            y
                Sets the y position (in normalized coordinates)
                of the update menu.
            yanchor
                Sets the update menu's vertical position anchor
                This anchor binds the `y` position to the
                "top", "middle" or "bottom" of the range
                selector.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class UniformtextValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="uniformtext", parent_name="layout", **kwargs):
        super(UniformtextValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Uniformtext"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            minsize
                Sets the minimum text size between traces of
                the same type.
            mode
                Determines how the font size for various text
                elements are uniformed between each trace type.
                If the computed text sizes were smaller than
                the minimum size defined by
                `uniformtext.minsize` using "hide" option hides
                the text; and using "show" option shows the
                text without further downscaling. Please note
                that if the size defined by `minsize` is
                greater than the font size defined by trace,
                then the `minsize` is used.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class UirevisionValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="uirevision", parent_name="layout", **kwargs):
        super(UirevisionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TreemapcolorwayValidator(_plotly_utils.basevalidators.ColorlistValidator):
    def __init__(self, plotly_name="treemapcolorway", parent_name="layout", **kwargs):
        super(TreemapcolorwayValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TransitionValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="transition", parent_name="layout", **kwargs):
        super(TransitionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Transition"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            duration
                The duration of the transition, in
                milliseconds. If equal to zero, updates are
                synchronous.
            easing
                The easing function used for the transition
            ordering
                Determines whether the figure's layout or
                traces smoothly transitions during updates that
                make both traces and layout change.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class TitleValidator(_plotly_utils.basevalidators.TitleValidator):
    def __init__(self, plotly_name="title", parent_name="layout", **kwargs):
        super(TitleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Title"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            font
                Sets the title font. Note that the title's font
                used to be customized by the now deprecated
                `titlefont` attribute.
            pad
                Sets the padding of the title. Each padding
                value only applies when the corresponding
                `xanchor`/`yanchor` value is set accordingly.
                E.g. for left padding to take effect, `xanchor`
                must be set to "left". The same rule applies if
                `xanchor`/`yanchor` is determined
                automatically. Padding is muted if the
                respective anchor value is "middle*/*center".
            text
                Sets the plot's title. Note that before the
                existence of `title.text`, the title's contents
                used to be defined as the `title` attribute
                itself. This behavior has been deprecated.
            x
                Sets the x position with respect to `xref` in
                normalized coordinates from 0 (left) to 1
                (right).
            xanchor
                Sets the title's horizontal alignment with
                respect to its x position. "left" means that
                the title starts at x, "right" means that the
                title ends at x and "center" means that the
                title's center is at x. "auto" divides `xref`
                by three and calculates the `xanchor` value
                automatically based on the value of `x`.
            xref
                Sets the container `x` refers to. "container"
                spans the entire `width` of the plot. "paper"
                refers to the width of the plotting area only.
            y
                Sets the y position with respect to `yref` in
                normalized coordinates from 0 (bottom) to 1
                (top). "auto" places the baseline of the title
                onto the vertical center of the top margin.
            yanchor
                Sets the title's vertical alignment with
                respect to its y position. "top" means that the
                title's cap line is at y, "bottom" means that
                the title's baseline is at y and "middle" means
                that the title's midline is at y. "auto"
                divides `yref` by three and calculates the
                `yanchor` value automatically based on the
                value of `y`.
            yref
                Sets the container `y` refers to. "container"
                spans the entire `height` of the plot. "paper"
                refers to the height of the plotting area only.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class TernaryValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="ternary", parent_name="layout", **kwargs):
        super(TernaryValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Ternary"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            aaxis
                :class:`plotly.graph_objects.layout.ternary.Aax
                is` instance or dict with compatible properties
            baxis
                :class:`plotly.graph_objects.layout.ternary.Bax
                is` instance or dict with compatible properties
            bgcolor
                Set the background color of the subplot
            caxis
                :class:`plotly.graph_objects.layout.ternary.Cax
                is` instance or dict with compatible properties
            domain
                :class:`plotly.graph_objects.layout.ternary.Dom
                ain` instance or dict with compatible
                properties
            sum
                The number each triplet should sum to, and the
                maximum range of each axis
            uirevision
                Controls persistence of user-driven changes in
                axis `min` and `title`, if not overridden in
                the individual axes. Defaults to
                `layout.uirevision`.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class TemplateValidator(_plotly_utils.basevalidators.BaseTemplateValidator):
    def __init__(self, plotly_name="template", parent_name="layout", **kwargs):
        super(TemplateValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Template"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            data
                :class:`plotly.graph_objects.layout.template.Da
                ta` instance or dict with compatible properties
            layout
                :class:`plotly.graph_objects.Layout` instance
                or dict with compatible properties
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class SunburstcolorwayValidator(_plotly_utils.basevalidators.ColorlistValidator):
    def __init__(self, plotly_name="sunburstcolorway", parent_name="layout", **kwargs):
        super(SunburstcolorwayValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SpikedistanceValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name="spikedistance", parent_name="layout", **kwargs):
        super(SpikedistanceValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            min=kwargs.pop("min", -1),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SliderValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="sliderdefaults", parent_name="layout", **kwargs):
        super(SliderValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Slider"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class SlidersValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name="sliders", parent_name="layout", **kwargs):
        super(SlidersValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Slider"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            active
                Determines which button (by index starting from
                0) is considered active.
            activebgcolor
                Sets the background color of the slider grip
                while dragging.
            bgcolor
                Sets the background color of the slider.
            bordercolor
                Sets the color of the border enclosing the
                slider.
            borderwidth
                Sets the width (in px) of the border enclosing
                the slider.
            currentvalue
                :class:`plotly.graph_objects.layout.slider.Curr
                entvalue` instance or dict with compatible
                properties
            font
                Sets the font of the slider step labels.
            len
                Sets the length of the slider This measure
                excludes the padding of both ends. That is, the
                slider's length is this length minus the
                padding on both ends.
            lenmode
                Determines whether this slider length is set in
                units of plot "fraction" or in *pixels. Use
                `len` to set the value.
            minorticklen
                Sets the length in pixels of minor step tick
                marks
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
            pad
                Set the padding of the slider component along
                each side.
            steps
                A tuple of :class:`plotly.graph_objects.layout.
                slider.Step` instances or dicts with compatible
                properties
            stepdefaults
                When used in a template (as
                layout.template.layout.slider.stepdefaults),
                sets the default property values to use for
                elements of layout.slider.steps
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
            tickcolor
                Sets the color of the border enclosing the
                slider.
            ticklen
                Sets the length in pixels of step tick marks
            tickwidth
                Sets the tick width (in px).
            transition
                :class:`plotly.graph_objects.layout.slider.Tran
                sition` instance or dict with compatible
                properties
            visible
                Determines whether or not the slider is
                visible.
            x
                Sets the x position (in normalized coordinates)
                of the slider.
            xanchor
                Sets the slider's horizontal position anchor.
                This anchor binds the `x` position to the
                "left", "center" or "right" of the range
                selector.
            y
                Sets the y position (in normalized coordinates)
                of the slider.
            yanchor
                Sets the slider's vertical position anchor This
                anchor binds the `y` position to the "top",
                "middle" or "bottom" of the range selector.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowlegendValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="showlegend", parent_name="layout", **kwargs):
        super(ShowlegendValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "legend"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShapeValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="shapedefaults", parent_name="layout", **kwargs):
        super(ShapeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Shape"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShapesValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name="shapes", parent_name="layout", **kwargs):
        super(ShapesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Shape"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            fillcolor
                Sets the color filling the shape's interior.
            layer
                Specifies whether shapes are drawn below or
                above traces.
            line
                :class:`plotly.graph_objects.layout.shape.Line`
                instance or dict with compatible properties
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
                Sets the opacity of the shape.
            path
                For `type` "path" - a valid SVG path with the
                pixel values replaced by data values in
                `xsizemode`/`ysizemode` being "scaled" and
                taken unmodified as pixels relative to
                `xanchor` and `yanchor` in case of "pixel" size
                mode. There are a few restrictions / quirks
                only absolute instructions, not relative. So
                the allowed segments are: M, L, H, V, Q, C, T,
                S, and Z arcs (A) are not allowed because
                radius rx and ry are relative. In the future we
                could consider supporting relative commands,
                but we would have to decide on how to handle
                date and log axes. Note that even as is, Q and
                C Bezier paths that are smooth on linear axes
                may not be smooth on log, and vice versa. no
                chained "polybezier" commands - specify the
                segment type for each one. On category axes,
                values are numbers scaled to the serial numbers
                of categories because using the categories
                themselves there would be no way to describe
                fractional positions On data axes: because
                space and T are both normal components of path
                strings, we can't use either to separate date
                from time parts. Therefore we'll use underscore
                for this purpose: 2015-02-21_13:45:56.789
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
            type
                Specifies the shape type to be drawn. If
                "line", a line is drawn from (`x0`,`y0`) to
                (`x1`,`y1`) with respect to the axes' sizing
                mode. If "circle", a circle is drawn from
                ((`x0`+`x1`)/2, (`y0`+`y1`)/2)) with radius
                (|(`x0`+`x1`)/2 - `x0`|, |(`y0`+`y1`)/2
                -`y0`)|) with respect to the axes' sizing mode.
                If "rect", a rectangle is drawn linking
                (`x0`,`y0`), (`x1`,`y0`), (`x1`,`y1`),
                (`x0`,`y1`), (`x0`,`y0`) with respect to the
                axes' sizing mode. If "path", draw a custom SVG
                path using `path`. with respect to the axes'
                sizing mode.
            visible
                Determines whether or not this shape is
                visible.
            x0
                Sets the shape's starting x position. See
                `type` and `xsizemode` for more info.
            x1
                Sets the shape's end x position. See `type` and
                `xsizemode` for more info.
            xanchor
                Only relevant in conjunction with `xsizemode`
                set to "pixel". Specifies the anchor point on
                the x axis to which `x0`, `x1` and x
                coordinates within `path` are relative to. E.g.
                useful to attach a pixel sized shape to a
                certain data value. No effect when `xsizemode`
                not set to "pixel".
            xref
                Sets the shape's x coordinate axis. If set to
                an x axis id (e.g. "x" or "x2"), the `x`
                position refers to an x coordinate. If set to
                "paper", the `x` position refers to the
                distance from the left side of the plotting
                area in normalized coordinates where 0 (1)
                corresponds to the left (right) side. If the
                axis `type` is "log", then you must take the
                log of your desired range. If the axis `type`
                is "date", then you must convert the date to
                unix time in milliseconds.
            xsizemode
                Sets the shapes's sizing mode along the x axis.
                If set to "scaled", `x0`, `x1` and x
                coordinates within `path` refer to data values
                on the x axis or a fraction of the plot area's
                width (`xref` set to "paper"). If set to
                "pixel", `xanchor` specifies the x position in
                terms of data or plot fraction but `x0`, `x1`
                and x coordinates within `path` are pixels
                relative to `xanchor`. This way, the shape can
                have a fixed width while maintaining a position
                relative to data or plot fraction.
            y0
                Sets the shape's starting y position. See
                `type` and `ysizemode` for more info.
            y1
                Sets the shape's end y position. See `type` and
                `ysizemode` for more info.
            yanchor
                Only relevant in conjunction with `ysizemode`
                set to "pixel". Specifies the anchor point on
                the y axis to which `y0`, `y1` and y
                coordinates within `path` are relative to. E.g.
                useful to attach a pixel sized shape to a
                certain data value. No effect when `ysizemode`
                not set to "pixel".
            yref
                Sets the annotation's y coordinate axis. If set
                to an y axis id (e.g. "y" or "y2"), the `y`
                position refers to an y coordinate If set to
                "paper", the `y` position refers to the
                distance from the bottom of the plotting area
                in normalized coordinates where 0 (1)
                corresponds to the bottom (top).
            ysizemode
                Sets the shapes's sizing mode along the y axis.
                If set to "scaled", `y0`, `y1` and y
                coordinates within `path` refer to data values
                on the y axis or a fraction of the plot area's
                height (`yref` set to "paper"). If set to
                "pixel", `yanchor` specifies the y position in
                terms of data or plot fraction but `y0`, `y1`
                and y coordinates within `path` are pixels
                relative to `yanchor`. This way, the shape can
                have a fixed height while maintaining a
                position relative to data or plot fraction.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class SeparatorsValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="separators", parent_name="layout", **kwargs):
        super(SeparatorsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SelectionrevisionValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="selectionrevision", parent_name="layout", **kwargs):
        super(SelectionrevisionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SelectdirectionValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="selectdirection", parent_name="layout", **kwargs):
        super(SelectdirectionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["h", "v", "d", "any"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class SceneValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="scene", parent_name="layout", **kwargs):
        super(SceneValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Scene"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            annotations
                A tuple of :class:`plotly.graph_objects.layout.
                scene.Annotation` instances or dicts with
                compatible properties
            annotationdefaults
                When used in a template (as layout.template.lay
                out.scene.annotationdefaults), sets the default
                property values to use for elements of
                layout.scene.annotations
            aspectmode
                If "cube", this scene's axes are drawn as a
                cube, regardless of the axes' ranges. If
                "data", this scene's axes are drawn in
                proportion with the axes' ranges. If "manual",
                this scene's axes are drawn in proportion with
                the input of "aspectratio" (the default
                behavior if "aspectratio" is provided). If
                "auto", this scene's axes are drawn using the
                results of "data" except when one axis is more
                than four times the size of the two others,
                where in that case the results of "cube" are
                used.
            aspectratio
                Sets this scene's axis aspectratio.
            bgcolor

            camera
                :class:`plotly.graph_objects.layout.scene.Camer
                a` instance or dict with compatible properties
            domain
                :class:`plotly.graph_objects.layout.scene.Domai
                n` instance or dict with compatible properties
            dragmode
                Determines the mode of drag interactions for
                this scene.
            hovermode
                Determines the mode of hover interactions for
                this scene.
            uirevision
                Controls persistence of user-driven changes in
                camera attributes. Defaults to
                `layout.uirevision`.
            xaxis
                :class:`plotly.graph_objects.layout.scene.XAxis
                ` instance or dict with compatible properties
            yaxis
                :class:`plotly.graph_objects.layout.scene.YAxis
                ` instance or dict with compatible properties
            zaxis
                :class:`plotly.graph_objects.layout.scene.ZAxis
                ` instance or dict with compatible properties
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class RadialAxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="radialaxis", parent_name="layout", **kwargs):
        super(RadialAxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "RadialAxis"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            domain
                Polar chart subplots are not supported yet.
                This key has currently no effect.
            endpadding
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots.
            orientation
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Sets the
                orientation (an angle with respect to the
                origin) of the radial axis.
            range
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Defines the start
                and end point of this radial axis.
            showline
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Determines whether
                or not the line bounding this radial axis will
                be shown on the figure.
            showticklabels
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Determines whether
                or not the radial axis ticks will feature tick
                labels.
            tickcolor
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Sets the color of
                the tick lines on this radial axis.
            ticklen
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Sets the length of
                the tick lines on this radial axis.
            tickorientation
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Sets the
                orientation (from the paper perspective) of the
                radial axis tick labels.
            ticksuffix
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Sets the length of
                the tick lines on this radial axis.
            visible
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Determines whether
                or not this axis will be visible.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class PolarValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="polar", parent_name="layout", **kwargs):
        super(PolarValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Polar"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            angularaxis
                :class:`plotly.graph_objects.layout.polar.Angul
                arAxis` instance or dict with compatible
                properties
            bargap
                Sets the gap between bars of adjacent location
                coordinates. Values are unitless, they
                represent fractions of the minimum difference
                in bar positions in the data.
            barmode
                Determines how bars at the same location
                coordinate are displayed on the graph. With
                "stack", the bars are stacked on top of one
                another With "overlay", the bars are plotted
                over one another, you might need to an
                "opacity" to see multiple bars.
            bgcolor
                Set the background color of the subplot
            domain
                :class:`plotly.graph_objects.layout.polar.Domai
                n` instance or dict with compatible properties
            gridshape
                Determines if the radial axis grid lines and
                angular axis line are drawn as "circular"
                sectors or as "linear" (polygon) sectors. Has
                an effect only when the angular axis has `type`
                "category". Note that `radialaxis.angle` is
                snapped to the angle of the closest vertex when
                `gridshape` is "circular" (so that radial axis
                scale is the same as the data scale).
            hole
                Sets the fraction of the radius to cut out of
                the polar subplot.
            radialaxis
                :class:`plotly.graph_objects.layout.polar.Radia
                lAxis` instance or dict with compatible
                properties
            sector
                Sets angular span of this polar subplot with
                two angles (in degrees). Sector are assumed to
                be spanned in the counterclockwise direction
                with 0 corresponding to rightmost limit of the
                polar subplot.
            uirevision
                Controls persistence of user-driven changes in
                axis attributes, if not overridden in the
                individual axes. Defaults to
                `layout.uirevision`.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class PlotBgcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name="plot_bgcolor", parent_name="layout", **kwargs):
        super(PlotBgcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "layoutstyle"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class PiecolorwayValidator(_plotly_utils.basevalidators.ColorlistValidator):
    def __init__(self, plotly_name="piecolorway", parent_name="layout", **kwargs):
        super(PiecolorwayValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class PaperBgcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name="paper_bgcolor", parent_name="layout", **kwargs):
        super(PaperBgcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class OrientationValidator(_plotly_utils.basevalidators.AngleValidator):
    def __init__(self, plotly_name="orientation", parent_name="layout", **kwargs):
        super(OrientationValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ModebarValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="modebar", parent_name="layout", **kwargs):
        super(ModebarValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Modebar"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            activecolor
                Sets the color of the active or hovered on
                icons in the modebar.
            bgcolor
                Sets the background color of the modebar.
            color
                Sets the color of the icons in the modebar.
            orientation
                Sets the orientation of the modebar.
            uirevision
                Controls persistence of user-driven changes
                related to the modebar, including `hovermode`,
                `dragmode`, and `showspikes` at both the root
                level and inside subplots. Defaults to
                `layout.uirevision`.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class MetasrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="metasrc", parent_name="layout", **kwargs):
        super(MetasrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class MetaValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="meta", parent_name="layout", **kwargs):
        super(MetaValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class MarginValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="margin", parent_name="layout", **kwargs):
        super(MarginValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Margin"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            autoexpand
                Turns on/off margin expansion computations.
                Legends, colorbars, updatemenus, sliders, axis
                rangeselector and rangeslider are allowed to
                push the margins by defaults.
            b
                Sets the bottom margin (in px).
            l
                Sets the left margin (in px).
            pad
                Sets the amount of padding (in px) between the
                plotting area and the axis lines
            r
                Sets the right margin (in px).
            t
                Sets the top margin (in px).
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class MapboxValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="mapbox", parent_name="layout", **kwargs):
        super(MapboxValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Mapbox"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            accesstoken
                Sets the mapbox access token to be used for
                this mapbox map. Alternatively, the mapbox
                access token can be set in the configuration
                options under `mapboxAccessToken`. Note that
                accessToken are only required when `style` (e.g
                with values : basic, streets, outdoors, light,
                dark, satellite, satellite-streets ) and/or a
                layout layer references the Mapbox server.
            bearing
                Sets the bearing angle of the map in degrees
                counter-clockwise from North (mapbox.bearing).
            center
                :class:`plotly.graph_objects.layout.mapbox.Cent
                er` instance or dict with compatible properties
            domain
                :class:`plotly.graph_objects.layout.mapbox.Doma
                in` instance or dict with compatible properties
            layers
                A tuple of :class:`plotly.graph_objects.layout.
                mapbox.Layer` instances or dicts with
                compatible properties
            layerdefaults
                When used in a template (as
                layout.template.layout.mapbox.layerdefaults),
                sets the default property values to use for
                elements of layout.mapbox.layers
            pitch
                Sets the pitch angle of the map (in degrees,
                where 0 means perpendicular to the surface of
                the map) (mapbox.pitch).
            style
                Defines the map layers that are rendered by
                default below the trace layers defined in
                `data`, which are themselves by default
                rendered below the layers defined in
                `layout.mapbox.layers`.  These layers can be
                defined either explicitly as a Mapbox Style
                object which can contain multiple layer
                definitions that load data from any public or
                private Tile Map Service (TMS or XYZ) or Web
                Map Service (WMS) or implicitly by using one of
                the built-in style objects which use WMSes
                which do not require any access tokens, or by
                using a default Mapbox style or custom Mapbox
                style URL, both of which require a Mapbox
                access token  Note that Mapbox access token can
                be set in the `accesstoken` attribute or in the
                `mapboxAccessToken` config option.  Mapbox
                Style objects are of the form described in the
                Mapbox GL JS documentation available at
                https://docs.mapbox.com/mapbox-gl-js/style-spec
                The built-in plotly.js styles objects are:
                open-street-map, white-bg, carto-positron,
                carto-darkmatter, stamen-terrain, stamen-toner,
                stamen-watercolor  The built-in Mapbox styles
                are: basic, streets, outdoors, light, dark,
                satellite, satellite-streets  Mapbox style URLs
                are of the form:
                mapbox://mapbox.mapbox-<name>-<version>
            uirevision
                Controls persistence of user-driven changes in
                the view: `center`, `zoom`, `bearing`, `pitch`.
                Defaults to `layout.uirevision`.
            zoom
                Sets the zoom level of the map (mapbox.zoom).
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class LegendValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="legend", parent_name="layout", **kwargs):
        super(LegendValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Legend"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            bgcolor
                Sets the legend background color. Defaults to
                `layout.paper_bgcolor`.
            bordercolor
                Sets the color of the border enclosing the
                legend.
            borderwidth
                Sets the width (in px) of the border enclosing
                the legend.
            font
                Sets the font used to text the legend items.
            itemclick
                Determines the behavior on legend item click.
                "toggle" toggles the visibility of the item
                clicked on the graph. "toggleothers" makes the
                clicked item the sole visible item on the
                graph. False disable legend item click
                interactions.
            itemdoubleclick
                Determines the behavior on legend item double-
                click. "toggle" toggles the visibility of the
                item clicked on the graph. "toggleothers" makes
                the clicked item the sole visible item on the
                graph. False disable legend item double-click
                interactions.
            itemsizing
                Determines if the legend items symbols scale
                with their corresponding "trace" attributes or
                remain "constant" independent of the symbol
                size on the graph.
            orientation
                Sets the orientation of the legend.
            title
                :class:`plotly.graph_objects.layout.legend.Titl
                e` instance or dict with compatible properties
            tracegroupgap
                Sets the amount of vertical space (in px)
                between legend groups.
            traceorder
                Determines the order at which the legend items
                are displayed. If "normal", the items are
                displayed top-to-bottom in the same order as
                the input data. If "reversed", the items are
                displayed in the opposite order as "normal". If
                "grouped", the items are displayed in groups
                (when a trace `legendgroup` is provided). if
                "grouped+reversed", the items are displayed in
                the opposite order as "grouped".
            uirevision
                Controls persistence of legend-driven changes
                in trace and pie label visibility. Defaults to
                `layout.uirevision`.
            valign
                Sets the vertical alignment of the symbols with
                respect to their associated text.
            x
                Sets the x position (in normalized coordinates)
                of the legend. Defaults to 1.02 for vertical
                legends and defaults to 0 for horizontal
                legends.
            xanchor
                Sets the legend's horizontal position anchor.
                This anchor binds the `x` position to the
                "left", "center" or "right" of the legend.
                Value "auto" anchors legends to the right for
                `x` values greater than or equal to 2/3,
                anchors legends to the left for `x` values less
                than or equal to 1/3 and anchors legends with
                respect to their center otherwise.
            y
                Sets the y position (in normalized coordinates)
                of the legend. Defaults to 1 for vertical
                legends, defaults to "-0.1" for horizontal
                legends on graphs w/o range sliders and
                defaults to 1.1 for horizontal legends on graph
                with one or multiple range sliders.
            yanchor
                Sets the legend's vertical position anchor This
                anchor binds the `y` position to the "top",
                "middle" or "bottom" of the legend. Value
                "auto" anchors legends at their bottom for `y`
                values less than or equal to 1/3, anchors
                legends to at their top for `y` values greater
                than or equal to 2/3 and anchors legends with
                respect to their middle otherwise.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ImageValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="imagedefaults", parent_name="layout", **kwargs):
        super(ImageValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Image"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ImagesValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name="images", parent_name="layout", **kwargs):
        super(ImagesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Image"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            layer
                Specifies whether images are drawn below or
                above traces. When `xref` and `yref` are both
                set to `paper`, image is drawn below the entire
                plot area.
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
                Sets the opacity of the image.
            sizex
                Sets the image container size horizontally. The
                image will be sized based on the `position`
                value. When `xref` is set to `paper`, units are
                sized relative to the plot width.
            sizey
                Sets the image container size vertically. The
                image will be sized based on the `position`
                value. When `yref` is set to `paper`, units are
                sized relative to the plot height.
            sizing
                Specifies which dimension of the image to
                constrain.
            source
                Specifies the URL of the image to be used. The
                URL must be accessible from the domain where
                the plot code is run, and can be either
                relative or absolute.
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
            visible
                Determines whether or not this image is
                visible.
            x
                Sets the image's x position. When `xref` is set
                to `paper`, units are sized relative to the
                plot height. See `xref` for more info
            xanchor
                Sets the anchor for the x position
            xref
                Sets the images's x coordinate axis. If set to
                a x axis id (e.g. "x" or "x2"), the `x`
                position refers to an x data coordinate If set
                to "paper", the `x` position refers to the
                distance from the left of plot in normalized
                coordinates where 0 (1) corresponds to the left
                (right).
            y
                Sets the image's y position. When `yref` is set
                to `paper`, units are sized relative to the
                plot height. See `yref` for more info
            yanchor
                Sets the anchor for the y position.
            yref
                Sets the images's y coordinate axis. If set to
                a y axis id (e.g. "y" or "y2"), the `y`
                position refers to a y data coordinate. If set
                to "paper", the `y` position refers to the
                distance from the bottom of the plot in
                normalized coordinates where 0 (1) corresponds
                to the bottom (top).
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class HovermodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="hovermode", parent_name="layout", **kwargs):
        super(HovermodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "modebar"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop(
                "values", ["x", "y", "closest", False, "x unified", "y unified"]
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class HoverlabelValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="hoverlabel", parent_name="layout", **kwargs):
        super(HoverlabelValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Hoverlabel"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            align
                Sets the horizontal alignment of the text
                content within hover label box. Has an effect
                only if the hover label text spans more two or
                more lines
            bgcolor
                Sets the background color of all hover labels
                on graph
            bordercolor
                Sets the border color of all hover labels on
                graph.
            font
                Sets the default hover label font used by all
                traces on the graph.
            namelength
                Sets the default length (in number of
                characters) of the trace name in the hover
                labels for all traces. -1 shows the whole name
                regardless of length. 0-3 shows the first 0-3
                characters, and an integer >3 will show the
                whole name if it is less than that many
                characters, but if it is longer, will truncate
                to `namelength - 3` characters and add an
                ellipsis.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class HoverdistanceValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name="hoverdistance", parent_name="layout", **kwargs):
        super(HoverdistanceValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            min=kwargs.pop("min", -1),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HidesourcesValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="hidesources", parent_name="layout", **kwargs):
        super(HidesourcesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HiddenlabelssrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="hiddenlabelssrc", parent_name="layout", **kwargs):
        super(HiddenlabelssrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HiddenlabelsValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="hiddenlabels", parent_name="layout", **kwargs):
        super(HiddenlabelsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HeightValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="height", parent_name="layout", **kwargs):
        super(HeightValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 10),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class GridValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="grid", parent_name="layout", **kwargs):
        super(GridValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Grid"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            columns
                The number of columns in the grid. If you
                provide a 2D `subplots` array, the length of
                its longest row is used as the default. If you
                give an `xaxes` array, its length is used as
                the default. But it's also possible to have a
                different length, if you want to leave a row at
                the end for non-cartesian subplots.
            domain
                :class:`plotly.graph_objects.layout.grid.Domain
                ` instance or dict with compatible properties
            pattern
                If no `subplots`, `xaxes`, or `yaxes` are given
                but we do have `rows` and `columns`, we can
                generate defaults using consecutive axis IDs,
                in two ways: "coupled" gives one x axis per
                column and one y axis per row. "independent"
                uses a new xy pair for each cell, left-to-right
                across each row then iterating rows according
                to `roworder`.
            roworder
                Is the first row the top or the bottom? Note
                that columns are always enumerated from left to
                right.
            rows
                The number of rows in the grid. If you provide
                a 2D `subplots` array or a `yaxes` array, its
                length is used as the default. But it's also
                possible to have a different length, if you
                want to leave a row at the end for non-
                cartesian subplots.
            subplots
                Used for freeform grids, where some axes may be
                shared across subplots but others are not. Each
                entry should be a cartesian subplot id, like
                "xy" or "x3y2", or "" to leave that cell empty.
                You may reuse x axes within the same column,
                and y axes within the same row. Non-cartesian
                subplots and traces that support `domain` can
                place themselves in this grid separately using
                the `gridcell` attribute.
            xaxes
                Used with `yaxes` when the x and y axes are
                shared across columns and rows. Each entry
                should be an x axis id like "x", "x2", etc., or
                "" to not put an x axis in that column. Entries
                other than "" must be unique. Ignored if
                `subplots` is present. If missing but `yaxes`
                is present, will generate consecutive IDs.
            xgap
                Horizontal space between grid cells, expressed
                as a fraction of the total width available to
                one cell. Defaults to 0.1 for coupled-axes
                grids and 0.2 for independent grids.
            xside
                Sets where the x axis labels and titles go.
                "bottom" means the very bottom of the grid.
                "bottom plot" is the lowest plot that each x
                axis is used in. "top" and "top plot" are
                similar.
            yaxes
                Used with `yaxes` when the x and y axes are
                shared across columns and rows. Each entry
                should be an y axis id like "y", "y2", etc., or
                "" to not put a y axis in that row. Entries
                other than "" must be unique. Ignored if
                `subplots` is present. If missing but `xaxes`
                is present, will generate consecutive IDs.
            ygap
                Vertical space between grid cells, expressed as
                a fraction of the total height available to one
                cell. Defaults to 0.1 for coupled-axes grids
                and 0.3 for independent grids.
            yside
                Sets where the y axis labels and titles go.
                "left" means the very left edge of the grid.
                *left plot* is the leftmost plot that each y
                axis is used in. "right" and *right plot* are
                similar.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class GeoValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="geo", parent_name="layout", **kwargs):
        super(GeoValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Geo"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            bgcolor
                Set the background color of the map
            center
                :class:`plotly.graph_objects.layout.geo.Center`
                instance or dict with compatible properties
            coastlinecolor
                Sets the coastline color.
            coastlinewidth
                Sets the coastline stroke width (in px).
            countrycolor
                Sets line color of the country boundaries.
            countrywidth
                Sets line width (in px) of the country
                boundaries.
            domain
                :class:`plotly.graph_objects.layout.geo.Domain`
                instance or dict with compatible properties
            fitbounds
                Determines if this subplot's view settings are
                auto-computed to fit trace data. On scoped
                maps, setting `fitbounds` leads to `center.lon`
                and `center.lat` getting auto-filled. On maps
                with a non-clipped projection, setting
                `fitbounds` leads to `center.lon`,
                `center.lat`, and `projection.rotation.lon`
                getting auto-filled. On maps with a clipped
                projection, setting `fitbounds` leads to
                `center.lon`, `center.lat`,
                `projection.rotation.lon`,
                `projection.rotation.lat`, `lonaxis.range` and
                `lonaxis.range` getting auto-filled. If
                "locations", only the trace's visible locations
                are considered in the `fitbounds` computations.
                If "geojson", the entire trace input `geojson`
                (if provided) is considered in the `fitbounds`
                computations, Defaults to False.
            framecolor
                Sets the color the frame.
            framewidth
                Sets the stroke width (in px) of the frame.
            lakecolor
                Sets the color of the lakes.
            landcolor
                Sets the land mass color.
            lataxis
                :class:`plotly.graph_objects.layout.geo.Lataxis
                ` instance or dict with compatible properties
            lonaxis
                :class:`plotly.graph_objects.layout.geo.Lonaxis
                ` instance or dict with compatible properties
            oceancolor
                Sets the ocean color
            projection
                :class:`plotly.graph_objects.layout.geo.Project
                ion` instance or dict with compatible
                properties
            resolution
                Sets the resolution of the base layers. The
                values have units of km/mm e.g. 110 corresponds
                to a scale ratio of 1:110,000,000.
            rivercolor
                Sets color of the rivers.
            riverwidth
                Sets the stroke width (in px) of the rivers.
            scope
                Set the scope of the map.
            showcoastlines
                Sets whether or not the coastlines are drawn.
            showcountries
                Sets whether or not country boundaries are
                drawn.
            showframe
                Sets whether or not a frame is drawn around the
                map.
            showlakes
                Sets whether or not lakes are drawn.
            showland
                Sets whether or not land masses are filled in
                color.
            showocean
                Sets whether or not oceans are filled in color.
            showrivers
                Sets whether or not rivers are drawn.
            showsubunits
                Sets whether or not boundaries of subunits
                within countries (e.g. states, provinces) are
                drawn.
            subunitcolor
                Sets the color of the subunits boundaries.
            subunitwidth
                Sets the stroke width (in px) of the subunits
                boundaries.
            uirevision
                Controls persistence of user-driven changes in
                the view (projection and center). Defaults to
                `layout.uirevision`.
            visible
                Sets the default visibility of the base layers.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class FunnelmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="funnelmode", parent_name="layout", **kwargs):
        super(FunnelmodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["stack", "group", "overlay"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class FunnelgroupgapValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="funnelgroupgap", parent_name="layout", **kwargs):
        super(FunnelgroupgapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class FunnelgapValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="funnelgap", parent_name="layout", **kwargs):
        super(FunnelgapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class FunnelareacolorwayValidator(_plotly_utils.basevalidators.ColorlistValidator):
    def __init__(
        self, plotly_name="funnelareacolorway", parent_name="layout", **kwargs
    ):
        super(FunnelareacolorwayValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class FontValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="font", parent_name="layout", **kwargs):
        super(FontValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Font"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color

            family
                HTML font family - the typeface that will be
                applied by the web browser. The web browser
                will only be able to apply a font if it is
                available on the system which it operates.
                Provide multiple font families, separated by
                commas, to indicate the preference in which to
                apply fonts if they aren't available on the
                system. The Chart Studio Cloud (at
                https://chart-studio.plotly.com or on-premise)
                generates images on a server, where only a
                select number of fonts are installed and
                supported. These include "Arial", "Balto",
                "Courier New", "Droid Sans",, "Droid Serif",
                "Droid Sans Mono", "Gravitas One", "Old
                Standard TT", "Open Sans", "Overpass", "PT Sans
                Narrow", "Raleway", "Times New Roman".
            size

""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ExtendtreemapcolorsValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="extendtreemapcolors", parent_name="layout", **kwargs
    ):
        super(ExtendtreemapcolorsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ExtendsunburstcolorsValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="extendsunburstcolors", parent_name="layout", **kwargs
    ):
        super(ExtendsunburstcolorsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ExtendpiecolorsValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="extendpiecolors", parent_name="layout", **kwargs):
        super(ExtendpiecolorsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ExtendfunnelareacolorsValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="extendfunnelareacolors", parent_name="layout", **kwargs
    ):
        super(ExtendfunnelareacolorsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class EditrevisionValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="editrevision", parent_name="layout", **kwargs):
        super(EditrevisionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class DragmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="dragmode", parent_name="layout", **kwargs):
        super(DragmodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "modebar"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop(
                "values",
                ["zoom", "pan", "select", "lasso", "orbit", "turntable", False],
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class DirectionValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="direction", parent_name="layout", **kwargs):
        super(DirectionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["clockwise", "counterclockwise"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class DatarevisionValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="datarevision", parent_name="layout", **kwargs):
        super(DatarevisionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorwayValidator(_plotly_utils.basevalidators.ColorlistValidator):
    def __init__(self, plotly_name="colorway", parent_name="layout", **kwargs):
        super(ColorwayValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorscaleValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="colorscale", parent_name="layout", **kwargs):
        super(ColorscaleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Colorscale"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            diverging
                Sets the default diverging colorscale. Note
                that `autocolorscale` must be true for this
                attribute to work.
            sequential
                Sets the default sequential colorscale for
                positive values. Note that `autocolorscale`
                must be true for this attribute to work.
            sequentialminus
                Sets the default sequential colorscale for
                negative values. Note that `autocolorscale`
                must be true for this attribute to work.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColoraxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="coloraxis", parent_name="layout", **kwargs):
        super(ColoraxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Coloraxis"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            autocolorscale
                Determines whether the colorscale is a default
                palette (`autocolorscale: true`) or the palette
                determined by `colorscale`. In case
                `colorscale` is unspecified or `autocolorscale`
                is true, the default  palette will be chosen
                according to whether numbers in the `color`
                array are all positive, all negative or mixed.
            cauto
                Determines whether or not the color domain is
                computed with respect to the input data (here
                corresponding trace color array(s)) or the
                bounds set in `cmin` and `cmax`  Defaults to
                `false` when `cmin` and `cmax` are set by the
                user.
            cmax
                Sets the upper bound of the color domain. Value
                should have the same units as corresponding
                trace color array(s) and if set, `cmin` must be
                set as well.
            cmid
                Sets the mid-point of the color domain by
                scaling `cmin` and/or `cmax` to be equidistant
                to this point. Value should have the same units
                as corresponding trace color array(s). Has no
                effect when `cauto` is `false`.
            cmin
                Sets the lower bound of the color domain. Value
                should have the same units as corresponding
                trace color array(s) and if set, `cmax` must be
                set as well.
            colorbar
                :class:`plotly.graph_objects.layout.coloraxis.C
                olorBar` instance or dict with compatible
                properties
            colorscale
                Sets the colorscale. The colorscale must be an
                array containing arrays mapping a normalized
                value to an rgb, rgba, hex, hsl, hsv, or named
                color string. At minimum, a mapping for the
                lowest (0) and highest (1) values are required.
                For example, `[[0, 'rgb(0,0,255)'], [1,
                'rgb(255,0,0)']]`. To control the bounds of the
                colorscale in color space, use`cmin` and
                `cmax`. Alternatively, `colorscale` may be a
                palette name string of the following list: Grey
                s,YlGnBu,Greens,YlOrRd,Bluered,RdBu,Reds,Blues,
                Picnic,Rainbow,Portland,Jet,Hot,Blackbody,Earth
                ,Electric,Viridis,Cividis.
            reversescale
                Reverses the color mapping if true. If true,
                `cmin` will correspond to the last color in the
                array and `cmax` will correspond to the first
                color.
            showscale
                Determines whether or not a colorbar is
                displayed for this trace.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ClickmodeValidator(_plotly_utils.basevalidators.FlaglistValidator):
    def __init__(self, plotly_name="clickmode", parent_name="layout", **kwargs):
        super(ClickmodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            extras=kwargs.pop("extras", ["none"]),
            flags=kwargs.pop("flags", ["event", "select"]),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CalendarValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="calendar", parent_name="layout", **kwargs):
        super(CalendarValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop(
                "values",
                [
                    "gregorian",
                    "chinese",
                    "coptic",
                    "discworld",
                    "ethiopian",
                    "hebrew",
                    "islamic",
                    "julian",
                    "mayan",
                    "nanakshahi",
                    "nepali",
                    "persian",
                    "jalali",
                    "taiwan",
                    "thai",
                    "ummalqura",
                ],
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class BoxmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="boxmode", parent_name="layout", **kwargs):
        super(BoxmodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["group", "overlay"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class BoxgroupgapValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="boxgroupgap", parent_name="layout", **kwargs):
        super(BoxgroupgapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class BoxgapValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="boxgap", parent_name="layout", **kwargs):
        super(BoxgapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class BarnormValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="barnorm", parent_name="layout", **kwargs):
        super(BarnormValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["", "fraction", "percent"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class BarmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="barmode", parent_name="layout", **kwargs):
        super(BarmodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["stack", "group", "overlay", "relative"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class BargroupgapValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="bargroupgap", parent_name="layout", **kwargs):
        super(BargroupgapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class BargapValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="bargap", parent_name="layout", **kwargs):
        super(BargapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class AutosizeValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="autosize", parent_name="layout", **kwargs):
        super(AutosizeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class AnnotationValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="annotationdefaults", parent_name="layout", **kwargs
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
    def __init__(self, plotly_name="annotations", parent_name="layout", **kwargs):
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
                spans two or more lines (i.e. `text` contains
                one or more <br> HTML tags) or if an explicit
                width is set to override the text width.
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
                the arrow head. If `axref` is `pixel`, a
                positive (negative)  component corresponds to
                an arrow pointing from right to left (left to
                right). If `axref` is an axis, this is an
                absolute value on that axis, like `x`, NOT a
                relative value.
            axref
                Indicates in what terms the tail of the
                annotation (ax,ay)  is specified. If `pixel`,
                `ax` is a relative offset in pixels  from `x`.
                If set to an x axis id (e.g. "x" or "x2"), `ax`
                is  specified in the same terms as that axis.
                This is useful  for trendline annotations which
                should continue to indicate  the correct trend
                when zoomed.
            ay
                Sets the y component of the arrow tail about
                the arrow head. If `ayref` is `pixel`, a
                positive (negative)  component corresponds to
                an arrow pointing from bottom to top (top to
                bottom). If `ayref` is an axis, this is an
                absolute value on that axis, like `y`, NOT a
                relative value.
            ayref
                Indicates in what terms the tail of the
                annotation (ax,ay)  is specified. If `pixel`,
                `ay` is a relative offset in pixels  from `y`.
                If set to a y axis id (e.g. "y" or "y2"), `ay`
                is  specified in the same terms as that axis.
                This is useful  for trendline annotations which
                should continue to indicate  the correct trend
                when zoomed.
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
            clicktoshow
                Makes this annotation respond to clicks on the
                plot. If you click a data point that exactly
                matches the `x` and `y` values of this
                annotation, and it is hidden (visible: false),
                it will appear. In "onoff" mode, you must click
                the same point again to make it disappear, so
                if you click multiple points, you can show
                multiple annotations. In "onout" mode, a click
                anywhere else in the plot (on another data
                point or not) will hide this annotation. If you
                need to show/hide this annotation in response
                to different `x` or `y` values, you can set
                `xclick` and/or `yclick`. This is useful for
                example to label the side of a bar. To label
                markers though, `standoff` is preferred over
                `xclick` and `yclick`.
            font
                Sets the annotation text font.
            height
                Sets an explicit height for the text box. null
                (default) lets the text set the box height.
                Taller text will be clipped.
            hoverlabel
                :class:`plotly.graph_objects.layout.annotation.
                Hoverlabel` instance or dict with compatible
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
                Sets the annotation's x position. If the axis
                `type` is "log", then you must take the log of
                your desired range. If the axis `type` is
                "date", it should be date strings, like date
                data, though Date objects and unix milliseconds
                will be accepted and converted to strings. If
                the axis `type` is "category", it should be
                numbers, using the scale where each category is
                assigned a serial number from zero in the order
                it appears.
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
            xclick
                Toggle this annotation when clicking a data
                point whose `x` value is `xclick` rather than
                the annotation's `x` value.
            xref
                Sets the annotation's x coordinate axis. If set
                to an x axis id (e.g. "x" or "x2"), the `x`
                position refers to an x coordinate If set to
                "paper", the `x` position refers to the
                distance from the left side of the plotting
                area in normalized coordinates where 0 (1)
                corresponds to the left (right) side.
            xshift
                Shifts the position of the whole annotation and
                arrow to the right (positive) or left
                (negative) by this many pixels.
            y
                Sets the annotation's y position. If the axis
                `type` is "log", then you must take the log of
                your desired range. If the axis `type` is
                "date", it should be date strings, like date
                data, though Date objects and unix milliseconds
                will be accepted and converted to strings. If
                the axis `type` is "category", it should be
                numbers, using the scale where each category is
                assigned a serial number from zero in the order
                it appears.
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
            yclick
                Toggle this annotation when clicking a data
                point whose `y` value is `yclick` rather than
                the annotation's `y` value.
            yref
                Sets the annotation's y coordinate axis. If set
                to an y axis id (e.g. "y" or "y2"), the `y`
                position refers to an y coordinate If set to
                "paper", the `y` position refers to the
                distance from the bottom of the plotting area
                in normalized coordinates where 0 (1)
                corresponds to the bottom (top).
            yshift
                Shifts the position of the whole annotation and
                arrow up (positive) or down (negative) by this
                many pixels.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class AngularAxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="angularaxis", parent_name="layout", **kwargs):
        super(AngularAxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "AngularAxis"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            domain
                Polar chart subplots are not supported yet.
                This key has currently no effect.
            endpadding
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots.
            range
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Defines the start
                and end point of this angular axis.
            showline
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Determines whether
                or not the line bounding this angular axis will
                be shown on the figure.
            showticklabels
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Determines whether
                or not the angular axis ticks will feature tick
                labels.
            tickcolor
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Sets the color of
                the tick lines on this angular axis.
            ticklen
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Sets the length of
                the tick lines on this angular axis.
            tickorientation
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Sets the
                orientation (from the paper perspective) of the
                angular axis tick labels.
            ticksuffix
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Sets the length of
                the tick lines on this angular axis.
            visible
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Determines whether
                or not this axis will be visible.
""",
            ),
            **kwargs
        )
