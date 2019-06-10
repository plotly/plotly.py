# plotly.js changelog

For more context information, please read through the
[release notes](https://github.com/plotly/plotly.js/releases).

To see all merged commits on the master branch that will be part of the next plotly.js release, go to:

https://github.com/plotly/plotly.js/compare/vX.Y.Z...master

where X.Y.Z is the semver of most recent plotly.js release.


## [1.48.1] -- 2019-05-30

### Fixed
- Fix single-sample-point `histogram2d` traces with set bins settings [#3922]
- Fix bingroup attributes for `histogram2dcontour` traces [#3922]
- Fix hover label content on empty `histogram2d` bins [#3922]


## [1.48.0] -- 2019-05-28

### Added
- Add `funnel` traces [#3817, #3911]
- Add `funnelarea` traces [#3876, #3912]
- Add support for shared color axes via `coloraxis` attributes
  in the layout [#3803, #3786, #3901, #3916]
- Add support for sorting categorical cartesian axes by value [#3864]
- Add `bingroup` to `histogram`, `histogram2d` and `histogram2dcontour` to group
  traces to have compatible auto-bin values [#3845]
- Add legend `itemclick` and `itemdoubleclick` attributes to set or disable
  the legend item click and double-click behavior [#3862]
- Add `insidetextanchor` attribute for `bar` and `waterfall` traces [#3817]
- Add `textangele` attribute for `bar` and `waterfall` traces [#3817]
- Add `textinfo` to `waterfall` traces [#3790]
- Add support for side-by-side `scatter3d` `marker` and `line` colorbars [#3803]
- Add `meta` attribute to traces to complement `layout.meta` [#3865]
- Emit `plotly_relayouting` during drag motion on subplots [#3888]
- Add Swedish locale (`sv`) [#3821]

### Changed
- Use `sane-topojson@v3.0.1` (backed by Natural Earth v4.1.0 shapefiles)
  to generate geographic features in `geo` subplots. Most notably, the Russia/Ukraine
  border has been updated [#3856]
- Draw `box` and `violin` points as legend item when other parts have opacity `0` [#3846]
- Draw `marker.line` for bars with no-span [#3848]
- Do not make request for topojson files when drawing geo subplot
  without geographic features [#3856]

### Fixed
- Fix `categoryarray` ordering for `heatmap` and `contour` traces [#3827]
- Fix `heatmap` brick positioning for non-overlapping categories [#3827]
- Fix `Plotly.update` calls that resulted in removal of modebar buttons [#3825]
- Fix auto-range for one-sided `violin` with set `width` [#3842]
- Fix hover label placement for one-sided `violin` with set `width` [#3842]
- Fix `scattergl` mode ordering in/out of selections [#3810]
- Fix `scattergl` unselected styling in/out of select/lasso dragmode [#3810]
- Fix `automargin` edge cases where draw code can be stuck in infinite loops [#3811]
- Fix `locationmode: 'USA-states'` on world scope under `50m` resolution [#3856]
- Fix reset view interactions on geo subplots following `geo.scope` updates [#3856]
- Fix `Plotly.animate`  on graphs with multiple subplot types [#3860]
- Fix `filter` transforms that result in empty coordinate arrays [#3766]
- Fix handling of `0` number in `pie` and `sunburst` text and hover [#3847]
- Fix `sunburst`  text in sectors centered around theta=180 [#3907]
- Fix handling of number `0` in `sunburst` ids/parents [#3903]
- Fix selection range event data on category axes [#3869]
- Fix `contour` with heatmap coloring rendering after graph resize [#3803]
- Fix `histogram2d` hover label content for trace with bins spanning multiple `y` sample values [#3890]
- Fix `parcoords` rendering of first value when it is part of own `constraintrange` [#3915]
- Fix rgba colorscale fallback for `parcoords` traces [#3917]
- Fix de-selected style of error bar on `bar` traces [#3644]
- Fix hover labels rendering for some zoomed-in `violin` traces [#3889]
- Fix `mesh3d` `vertexcolor` attribute description [#3688]


## [1.47.4] -- 2019-04-25

### Fixed
- Fix graphs with `sankey` and cartesian subplots [#3802]
- Fix selection of `bar` traces on subplot with a range slider [#3806]


## [1.47.3] -- 2019-04-18

### Fixed
- Fix MathJax rendering in Firefox [#3783]
- Fix `waterfall` hover under `hovermode: 'closest'` [#3778]
- Fix `waterfall` `connector.line.width` updates [#3789]
- Fix `waterfall` positioning on date axes [#3791]
- Fix `waterfall` default connector line color [#3788]
- Fix `hoverlabel.align` behavior for centered hover labels [#3781]


## [1.47.2] -- 2019-04-15

### Fixed
- Fix bar `'auto'` and `'inside'` `textposition` rendering on log size axes [#3762, #3773]
- Fix matching axes autorange algorithm for date axes [#3772]
- Fix SVG gradient rendering (colorbar and marker gradient) when `<base>` is present on page [#3765]


## [1.47.1] -- 2019-04-10

### Fixed
- Fix console errors during selections (bug introduced in 1.47.0) [#3755]


## [1.47.0] -- 2019-04-09

### Added
- New `volume` gl3d trace type [#3488]
- Implement node grouping via box and lasso selections for `sankey` traces [#3712, #3750]
- Implement `hovermode: 'x'`  for `sankey` traces,
  allowing users to compare links in a flow on hover [#3730]
- Add way for `Plotly.toImage` and `Plotly.downloadImage` to export images
  with current graph width/height by passing width/height option as `null` [#3746]
- Add legend attribute `itemsizing` with value `'constant'` making legend item symbol sizing
  independent of the sizing of their corresponding trace item [#3732]
- Add `hoverlabel.align` with value `'left'`, `'right'` and `'auto'` to set the horizontal
  alignment of the text content within hover labels [#3753]
- Add `contour.start`, `contour.end` and `contour.size` attribute to `surface` traces [#3469]
- Add `isosurface` and `volume` to the `gl3d` bundle [#3488]

### Changed
- Allow re-plot during drag interactions [#3716]
- Use high-precision in `scattergl` error bars shader [#3739]

### Fixed
- Fix implementation of geo `lonaxis` and `lataxis` attribute `tick0` [#3706]
- Fix `scrollZoom: false` configuration on mapbox subplots [#3745]
- Fix rendering of alpha channel in `mesh3d` traces [#3744]
- Fix `hoverlabel.namelength: 0` case [#3734]
- Fix implementation of `hoverlabel.namelength` for `pie`, `sankey`, `sunburst` and
  the gl3d traces [#3734]
- Fix `waterfall` rendering when transforms filter out all
  increasing or decreasing bars [#3720]
- Fix clip-path attributes for pages with parenthesis in their `<base>` URL [#3725]


## [1.46.1] -- 2019-04-02

### Fixed
- Fix `bar` traces that set `textfont` but don't have `text`
  (bug introduced in 1.46.0) [#3715]
- Fix hover text formatting in `waterfall` traces [#3711]
- Fix `surface` and `mesh3d` color scales with more than 256 items [#3702]


## [1.46.0] -- 2019-04-01

### Added
- New `waterfall` trace type [#3531, #3708]
- New `sunburst` trace type [#3594]
- Add attributes `node.x` and `node.y` to `sankey` traces [#3583]
- Implement `connectgaps` on `surface` traces [#3638]
- Implement `hovertemplate` for `box` and `violin` points [#3685]

### Changed
- Display hover labels above modebar, ensuring that the hover labels
  are always visible within the graph div [#3589, #3678]

### Fixed
- Fix horizontal legend item wrapping by pushing overflowed items to newline [#3628]
- Fix erroneous gap for histogram under relative `barmode` [#3652]
- Fix position of overlapping grouped bars within trace [#3680]
- Fix `violin` `bandwidth` logic for traces with identical values in sample [#3626]
- Fix `violin` trace `scalegroup` description [#3687]
- Fix stacked scatter for groupby traces [#3692]
- Fix outside text on empty items in `bar` traces under `textposition: 'outside'` [#3701]
- Fix `pie` un-hover event emission after updates [#3662, 3690]
- Fix `scatter` line decimation algo for filled trace with far-away data points [#3696]
- Fix `heatmap` and `contour` computation for traces with category coordinates containing `0` [#3691]
- Fix zoom interactions on gl3d subplots using an orthographic projection [#3601]
- Fix miscellaneous gl3d camera on-initialization bugs [#3585]
- Fix `surface` contour line rendering in some Firefox versions [#3670]
- Fix rendering of marker points and gl3d subplots on date axes (or with coordinates close to 64K floating limits)
  for WebGL-based traces on some iOS devices [#3666, #3672, #3674, #3676]
- Fix center-aligned hover labels positioning [#3681]


## [1.45.3] -- 2019-03-19

### Fixed
- Fix legend click dispatch on legend item symbols (bug introduced in 1.44.0) [#3635]
- Fix overlapping of "very close" hover labels [#3645]
- Fix `hovermode` default logic for stacked `scatter` traces [#3646]
- Fix `glPixelRatio` handling in `surface` contour lines [#3641]
- Fix `gl2d` subplot zoombox appearance (bug introduced in 1.32.0) [#3647]
- Fix axis label updates on `gl2d` subplots on scroll (bug introduced in 1.32.0) [#3647]
- Fix `dragmode` relayout calls on `gl2d` subplots [#3647]
- Improve info about `<extra>` in `hovertemplate` description [#3623]


## [1.45.2] -- 2019-03-07

### Fixed
- Fix webpack builds that include `sankey` by upgrading d3-sankey-circular to 0.33.0 (bug introduced in 1.45.0) [#3611]

## [1.45.1] -- 2019-03-05

### Fixed
- Fix axis automargin pushes for rotated tick labels [#3605]
- Fix automargin logic on (very) small graphs [#3605]
- Fix locales support in `hovertemplate` strings [#3586]
- Fix gl3d reset camera buttons for scenes with orthographic projection [#3597]
- Fix typed array support for `parcoords` dimensions values and `line.color` [#3598]
- Fix `cone` rendering on some older browsers [#3591]
- Fix `lightposition` behavior for `cone` traces [#3591]
- Fix `lightposition` behavior for `streamtube` trace [#3593]
- Remove unused files from `gl-cone3d` dependency [#3591]
- Remove unused files from `gl-streamtube3d` dependency [#3593]


## [1.45.0] -- 2019-02-26

### Added
- Add support for circular networks in `sankey` traces [#3406, #3535, #3564]
- Add matching axes behavior to cartesian axes via new axis attribute and
  new splom attribute dimensions attribute `matches` [#3506, #3565]
- Add attributes `alignmentgroup` and `offsetgroup` to `bar`, `histogram`, `box`
  and `violin` traces to make cross-trace positioning easier [#3529]
- Add support for orthographic projections in gl3d subplots via new attribute
  `scene.camera.projection.type` [#3550]
- Add `cmid` and `zmid` colorscale attributes to pick the middle of the color
  range during the auto-colorscale computations [#3549]
- Add support for `sankey` grouping via new attribute `groups` [#3556]
- Add support for `sankey` concentration `colorscales` [#3501]
- Add support for `hovertemplate` for all `gl3d` traces, `contour`,
  `heatmap`, `histogram*`, `parcats`, `scattercarpet` and `splom` traces [#3530]
- Add `hovertext` attribute to all traces that support hover 'text',
  for consistency with traces that already have an `hovertext` attribute [#3553]
- Add support for layout `meta` templating in trace `name`,
  `rangeselector`, `updatemenus` and `sliders` labels as well as
  within `hovertemplate` [#3548]
- Add support for `opacity` to `isosurface` traces [#3545]
- Add `mapbox.layers` attributes: `minzoom`, `maxzoom`, `line.dash` and `symbol.placement` [#3399]

### Changed
- More consistency pass down WebGL pixel ratio to gl3d renderers,
  this leads to better axis line and error bar rendering on some hardwares [#3573]
- Performance boost for `isosurface` trace generation [#3521]
- Export template string regex of `Lib` [#3548]
- Do no cluster points in  `scattergl` trace with less than 1e5 data pts,
  this fixes reported "missing data points" scenarios [#3578]

### Fixed
- Fix selection outline clearing during cartesian axis-range relayout calls
  (bug introduced in 1.42.0) [#3577]
- Fix modebar interactions on graphs with `scatter3d` traces with
  marker colorscales (bug introduced in 1.44.0) [#3554]
- Fix axis `automargin` for superimposed subplots (bug introduced in 1.44.3) [#3566]
- Fix polar angular tick labels placement [#3538]
- Fix `scattergl` updates after selections for trace with on-graph text [#3575]
- Fix `responsive: true` config option for graph with WebGL traces [#3500]
- Fix `modebar.bgcolor` for vertical modebars with wrapped buttons [#3500]
- Fix `ohlc` and `candlestick` auto-range computations [#3544]


## [1.44.4] -- 2019-02-12

### Fixed
- Fix `Plotly.react` used with `uirevision` when removing traces [#3527]
- Fix `scattergl` update calls that change the number of on-graph text elements [#3536]
- Fix annotations SVG errors on trace-less subplots [#3534]
- Fix `ohlc` and `candlestick` hover on blank coordinates (bug introduced in 1.43.2) [#3537]


## [1.44.3] -- 2019-02-06

### Fixed
- Fix axis `automargin` push offset which resulted in clipped
  tick labels in some scenarios [#3510]
- Fix handling of alpha channel in marker, line and error bar `rgba`
  coloring in `scatter3d` traces [#3496]
- Fix subplots with multiple `carpet` traces each with a `scattercarpet`
  trace on top of them [#3512]
- Fix MathJax placement in ternary `aaxis` titles [#3513]


## [1.44.2] -- 2019-02-04

### Fixed
- Fix vertical modebars in IE11 [@3491]
- Fix `hovertemplate` for traces with blank `name` [#3480]
- Fix 3D grid lines and tick labels colored by rgba color
  with full transparency [#3494]
- Fix white highlights rendering problems for `mesh3d` trace on
  some devices (bug introduced in 1.44.0) [#3483]
- Fix `fill.color` description for `table` traces [#3481]


## [1.44.1] -- 2019-01-24

### Fixed
- Fix `mesh3d` rendering on (some) mobile devices (bug introduced in 1.44.0) [#3463]
- Fix scene camera update when changing to `turntable` mode when `up.z` is zero
  (bug introduced in 1.43.0) [#3465, #3475]
- Fix `react` when cartesian axis `scaleanchor` patterns change [#3461]
- Fix "days" entries in polish (`pl`) locales [#3464]
- Remove inner function declarations in our `vectorize-text` that caused
  bundling errors for some (bug introduced in 1.43.0) [#3474]


## [1.44.0] -- 2019-01-22

### Added
- Add `isosurface` gl3d trace type [#3438]
- Add support for transitions from `Plotly.react` via new layout
 `transition` attribute [#3217]
- Add `meta` layout attribute, intended for making references
  to strings in text templates [#3439]
- Add support for `line.color` colorbars for `scatter3d` traces [#3384]
- Add support for `hovertemplate` on `scatterpolar`, `scatterpolargl`,
  `scatterternary`, `barpolar`, `choropleth`, `scattergeo` and
  `scattermapbox` trace [#3398, #3436]
- Add `width` attribute to `box` and `violin` traces [#3234]
- Add support for `<sup>`, `<sup>`, `<b>`, `<i>` and `<em>` pseudo-html
  tags in extra (aka trace "name") hover labels [#3443]
- Add support for div id as 1st arg to `Plotly.makeTemplate` [#3375]
- Add `config` option in plot-schema JSON output [#3376]

### Changed
- Config option `scrollZoom` is now a flaglist (instead of a boolean),
  each flag corresponding to subplot types where scroll is to be enabled [#3422]
- Use `glslify@7.0.0` across all our dependencies [#3421]

### Fixed
- Fix `error_(x|y|z)` color attribute inheritance [#3408]
- Fix `scrollZoom: false` config behavior for `geo`, `gl3d` and `mapbox` subplots [#3422]
- Fix cartesian scroll zoom when `responsive` config option is turned on [#3424]
- Fix cartesian scroll zoom when the page where the graph is embedded is scrollable [#3424]
- Fix `box` / `violin` autorange edge cases [#3234]
- Fix `box` / `violin` points hover labels on numeric positions [#3441, #3458]
- Fix `box` / `violin` grouping algorithm for subplots with as many distinct positions
  as the number of traces [#3445]
- Fix bar autorange calculations for trace with `base` above zero [#3452]
- Fix bar + errorbar autorange calculations [#3452]
- Fix `lightposition` behavior for `mesh3d` traces [#3415]
- Fix legend `valign` behavior for `pie` traces [#3435]
- Fix wrapped horizontal legends height edge cases [#3446]
- Fix hover label alignment for hover labels with multi-line extra (aka trace "name") labels [#3443]
- Fix cartesian axis domain lower limit [#3404]
- Fix dynamic imports of `lib/` trace modules [#3448]
- Fix `scl` and `reversescl` backward-compatible logic [#3423]
- Fix range slider `borderwidth` attribute description [#3453]


## [1.43.2] -- 2019-01-08

First 2019 release.

### Fixed
- Fix `uirevision` behavior for `gl3d`, `geo` and `mapbox` subplots [#3394]
- Fix `reversescale` behavior for `surface`, `mesh3d` and `streamtube`
  traces (bug introduced in 1.43.0) [#3418]
- Fix modebar hover styling (bug introduced in 1.43.0) [#3397]
- Fix horizontal `box` / `violin` hover label misalignment under
  `hovermode:'closest'` [#3401]
- Fix `ohlc` and `candlestick` hover for traces with empty items [#3366]
- Fix `surface` trace `visible` logic [#3365]
- Fix `mesh3d` trace `visible` logic [#3369]


## [1.43.1] -- 2018-12-21

### Fixed
- Fix z-axis auto-type for cartesian + gl3d graphs (bug introduced in 1.43.0) [#3360]
- Fix `multicategory` axis coordinate sorting [#3362]
- Fix `multicategory` y-axes clearance [#3354]
- Fix contour label clipPath segments for reversed axes [#3352]
- Fix axis autorange on double-click on graph `fixedrange:true` [#3351]


## [1.43.0] -- 2018-12-19

### Added
- Add `hovertemplate` attribute to `scatter`, `scattergl`, `bar`, `histogram`,
  `pie` and `sankey` traces [#3126, #3265, #3284]
- Add `layout.title` placement attributes `x`, `y`, `xref`, `yref`,
  `xanchor`, `yanchor` and `pad` [#3276]
- Add support for `<br>`, `<sup>`, and `<sub>` pseudo-html in `scatter3d` and `gl3d`
  scene text [#3207]
- Add `multicategory` axis type, allowing for "multi-level" categorical axis labels
  and category dividers with axis attributes: `showdividers`,
  `dividercolor` and `diverwidth` [#3254, #3300, #3326]
- Add cartesian axis attribute `tickson` with value '`boundaries`' to
  place categorical ticks on the category boundaries [#3254, #3275]
- Add `uirevision` attributes to control the persistence of user-driven changes
  on the graph [#3236]
- Add `legend.valign` to set the vertical alignment of the legend symbols
  with respect to their associated text labels [#3263]
- Implement `arrayOk` `textposition` for `scatter3d` traces [#3200]
- Add layout attributes `colorscale.sequential`, `colorscale.sequentialminus` and
 `colorscale.diverging` to set graph-wide colorscale defaults [#3274]
- Add `dragmode: false` to disable all drag interactions on cartesian subplots [#3170]
- Add `plotly.js-locales` npm packages that includes all official locales modules [#3223]
- Add `watermark` config option to permanently show Plotly's logo
  in the mode bar (set to false by default) [#3280]
- Add Finnish locale (`fi`) [#3325]

### Changed
- Remove "Edit in Chart Studio" button by default [#3307]
- `title` attributes linked to strings are now deprecated. Please use
  `title.text` instead to fill in your title text [#3276]
- `title*` attributes are new deprecated. They moved to `title.*`. For
  example, `colorbar.titleside` is now `colorbar.title.side` [#3276]
- No longer mutate `colorscale` values into user data [#3341]
- No longer mutate `zmin`/`zmax`, `cmin`/`cmax` values into user data [#3341]

### Fixed
- Fix `react` when updates trigger a new set of auto-margins [#3323]
- Fix `scattergl` coloring when more than 255 marker colors are present [#3328, #3334]
- More `scattergl` IE11 fixes [#3333, #3335]
- Multiple `surface` rendering fixes [#3281]
- Correctly default `scene.dragmode` to `'orbit'` when camera up vector is
  tilted [#3256]
- Fix hover on `scatter3d` traces with `opacity: 1` on Ubuntu [#3301]
- Fix console error _Uncaught ax.dtick error: NaN_ in gl3d subplots [#3233]
- Fix histogram hover event triggers when hovering from bar to bar [#3345]
- Fix graphs with empty and non-empty histogram traces [#3343]
- Fix contour labels on reversed axes [#3279]
- Fix `autocolorscale` toggling [#3341]
- Fix template support for `marker.colorscale` [#3341]
- Fix `scatter3D` trace with `mode: 'lines+markers'` with line color array error [#3341]
- Do not add `<base>` href to SVG clip paths during toImage [#3272]
- Fix table scrolling that leaked into window scope [#3327]
- Fix fills on segment-less marker-less traces [#3282]
- Fix rangesliders on reversed-range axes [#3304]
- Fix rangesliders on `side: 'top'`x-axes [#3329]
- Fix typed array support for `ohlc` and `candlestick` traces [#3342]
- Fix `restyle` with `impliedEdits` on trace with `groupby` transforms [#3236]
- Fix `editable: true` drag on `marker` colorbars [#3236]


## [1.42.5] -- 2018-11-08

### Fixed
- Fix `scattergl` / `scatterpolargl` with `mode: lines` and
  more than 1e5 pts (bug introduced in 1.42.0) [#3228]


## [1.42.4] -- 2018-11-07

### Fixed
- Remove rendering artifacts from `table` orca PDF exports [#3220]


## [1.42.3] -- 2018-11-06

### Fixed
- Fix `histogram` binning for typed array inputs (bug introduced in 1.42.0) [#3211]
- Fix textfont color `restyle` calls for `pie` traces [#3214]
- Fix textfont color `editType` for `bar` traces [#3214]
- Fix array `hoverinfo` support for `ohlc` and `candelestick` [#3213]
- Correctly list `parcats` hoverinfo attributes which does not support array inputs [#3213]


## [1.42.2] -- 2018-11-01

### Fixed
- Fix runaway loops for `scattergl` lines and fill traces
  (bug introduced in 1.42.0) [#3199]
- Fix size and alignment vertical modebar [#3193]
- Fix legend item rendering for traces with typed array marker
  settings [#3192]


## [1.42.1] -- 2018-10-31

### Fixed
- Fix IE regression introduced in 1.42.0 [#3187]
- Fix `parcats` text-shadowing on dark `plot_bgcolor` [#3191]
- Fix `scatter3d` text alignment [#3180]
- Fix `hoverinfo` flags in attribute descriptions [#3158]
- No longer coerce unused `hoverlabel` attribute in `parcoods` [#3158]
- No longer coerce `transforms` attributes in traces that don't support them [#3158]


## [1.42.0] -- 2018-10-29

### Added
- Add `parcats` (aka parallel categories) trace type [#2963, #3072]
- Add new gl3d tick and title auto-rotation algorithm that limits text
  overlaps [#3084, #3104, #3131]
- Add support for reversed-range axes on gl3d subplots [#3141]
- Add modebar layout style attributes: `orientation`, `bgcolor`, `color`
  and `activecolor` [#3068, #3091]
- Add `title`, `titleposition` and `titlefont` attributes to `pie` traces [#2987]
- Add `hoverlabel.split` attribute to `ohlc` and `candlestick` traces to split
  hover labels into multiple pieces [#2959]
- Add support for `line.shape` values 'hv', 'vh', 'hvh' and 'vhv'
  in `scattergl` traces [#3087]
- Add handler for `PlotlyConfig.MathJaxConfig: 'local'` to override our default
  MathJax behavior which modifies the global MathJax config on load [#2994]
- Add support for graph div as first argument for `Plotly.makeTemplate`
  and `Plotly.validateTemplate` [#3111, #3118]
- Implement trace, node and link hoverinfo for `sankey` traces [#3096, #3150]
- Implement per-sector textfont settings in `pie` traces [#3130]

## Changed
- Use new Plotly logo in "Produced with Plotly" modebar button [#3068]
- Improve `histogram` autobin algorithm: allow partial bin specification,
  deprecate `autobin(x|y)` attributes, force stacked/grouped histograms to match size
  and have compatible `start` value [#3044]
- Count distinct values for category and date axis auto-type, which
  improves the detection of "NaN" string values in numerical data [#3070]
- Improve bar and pie textfont color inheritance [#3130]
- Improve `splom` first-render, axis range relayout and marker restyle
  performance [#3057, #3161]
- Make `splom` `xaxes` and `yaxes` list always have same length as the trace
  `dimensions` regardless of their partial visiblities [#3057]
- Improve axis `overlaying` documentation [#3082]

### Fixed
- Fix `gl3d` subplots on tablets [#3088]
- Fix responsive behavior under flexbox and grid CSS [#3056, #3090, #3122]
- Fix relayout calls turning back `autosize` on [#3120]
- Fix MathJax rendering (for recent versions of MathJax) [#2994]
- Fix `scattergl` update on graphs with fractional computed dimensions [#3132]
- Fix `scattergl` symbols in MS Edge [#2750]
- Fix `scattergl` selections on overlaying axes [#3067]
- Fix `scattergl` `tozero` fills with bad values [#3087, #3168]
- Fix `scattergl` fill layer ordering [#3087]
- Fix `scattergl` lines on reversed-range axes [#3078]
- Fix axis auto-type routine for boolean data [#3070]
- Fix `splom` axis placement when the diagonal is missing [#3057]
- Fix line `restyle` calls on `parcoords` traces [#3178]
- Fix `parcoods` rendering after `hovermode` relayout calls [#3123]
- Fix WebGL warnings for `scatter3d` traces with blank text items [#3171, #3177]
- Fix WebGL warnings for `scatter3d` trace with empty lines [#3174]
- Fix rendering of `scatter3d` lines for certain scene angles [#3163]
- Fix handling of large pad values in `sankey` traces [#3143]
- Fix `scatterpolargl`  to `scatterpolar` toggling [#3098]
- Fix `scatterpolargl` axis-autorange padding [#3098]
- Fix `bar` text position for traces with set `base` [#3156]
- Fix `bar` support for typed arrays for `width` and `offset` attributes [#3169]
- Fix aggregate transforms with bad group values [#3093]
- Fix transforms operating on auto-invisible traces [#3139]
- Fix templating for polar and carpet axes [#3092, #3095]
- Ignore invalid trace indices in restyle and update [#3114]
- Fix grid style `relayout` calls on graph with large `splom` traces [#3067]
- Fix logging on some old browsers [#3137]
- Remove erroneous warning `WARN: unrecognized full object value` when
  relayouting array containers [#3053]


## [1.41.3] -- 2018-09-25

### Fixed
- Fix handling of hover `text` in `barpolar` traces [#3040]
- Fix `scatterpolar[gl]` `text` placement in hover label [#3040]
- Fix `pie` trace support for individual stroke width values [#3030]
- Fix handling of CSS `max-width` and `max-height` in auto-size routine [#3033]
- Rotate hover labels when `hovermode: 'y'` and a single trace produces multiple
  labels [#3043]
- Rotate hover labels when `hovermode: 'closest'` and multiple labels are
  generated including one from an horizontal trace [#3043]
- Fix hover label coloring on white bgcolor [#3048]
- Do not coerce nor validate `polar?.bar*` attributes on
  subplots w/o visible `barpolar` traces [#3023]
- Fix legacy polar attribute descriptions [#3023]


## [1.41.2] -- 2018-09-19

### Fixed
- Fix two-sided zoombox -> double-click -> one-sided zoombox behavior [#3028]


## [1.41.1] -- 2018-09-18

### Fixed
- Bring back hover labels on "touch" hover (bug introduced in 1.29.0) [#2997]
- Fix MathJax rendering in legends [#3018]
- Fix fill and layering for multiple stack-groups and unstacked `scatter` traces [#3005]
- Fix removal of `scatter` traces with set `stackgroup` [#3005]
- Fix stacked area gap insertion edge case [#3017]
- Fix zeroline logic for `splom`-generated axes [#3015]
- Fix `error_x` and `error_y` on `scatter3d` w/o `error_z` [#3011]
- Fix `scatter3d` error bars on log axes [#2992]
- Fix `Plotly.react` when updating geo axis `dtick` [#3016]
- Fix `polar.hole=1` case [#3021]
- Fix handling of `polar.sector` that span more than 360 degrees [#3021]


## [1.41.0] -- 2018-09-12

### Added
- Enable selection by clicking on points via new layout attribute `clickmode`
  and flag `'select'` [#2944]
- Add stacked area charts via new attributes `stackgroup` and `stackgaps` in
  `scatter` traces [#2960]
- Add `barpolar` traces - which replace and augment `area` traces [#2954]
- Add `polar.hole` to punch hole at the middle of polar subplot offsetting the
  start of the radial range [#2977, #2996]
- Add an 'inner' radial axis drag box on polar subplots [#2977]
- Add `{responsive: true}` plot config option [#2974]
- Emit `plotly_webglcontextlost` event on WebGL context lost [#2986]
- Support all numbered HTML entities (decimal and hex) in text elements [#2932]
- Add Welsh (`cy`) locale [#2945]

### Changed
- Attribute meta information is now stripped be stripped out of bundles (made
  with bundlers that support browserify transforms) by default [#1584]
- Draw polar axis ticks above polar axis lines [#2977]
- Improve ordering of trace hover labels for matching positions [#2960]
- Speed polar subplot radial drag interactions [#2954]
- Improve pseudo-html conversion performance [#2932]
- Bump `regl-splom` requirement to `^1.0.4` [#2956]
- Bump `glslify` requirement to `^6.3.1` [#2990]
- Use `gl-text` instead of `@etpinard/gl-text` [#2956]

### Fixed
- Fix `scatter` ordering in inner SVG `<g>` on some restyle calls [#2978]
- Fix cartesian axis autorange edge cases [#2960]
- Fix double-decoding of some HTML entities in text nodes [#2927]
- Fix `scattergl` line traces rendered after non-line traces [#2990]
- Fix legend positioning on graphs with very large margins [#2983]
- Fix rendering of ternary subplots fix with `showticklabels: false` [#2993]
- Fix show/hide updates of tick and tick labels on ternary subplots [#2993]
- Fix handling of multi-selections in ternary subplots [#2944]
- Fix `sankey` hover under `hovermode: false` [#2949]
- Fix `sankey` positioning for non-default `domain.x` values [#2984]
- Fix `type: 'date'` polar radial axes [#2954]
- Fix send-to-cloud modebar buttons on graphs with typed arrays [#2995]
- Fix handling of custom transforms that make their own data arrays in
  `Plotly.react`[#2973]
- Fix missing violin and colorbar attributes in `gd._fullData` [#2850]


## [1.40.1] -- 2018-08-22

### Changed
- Bump `browserify` to `v16` [#2923]
- Bump `glslify` to `v6.2.1` [#2923]
- Use `color-normlize@1.3.0` throughout code base [#2923]

### Fixed
- Fix logic for hiding zero lines when they conflict with axis lines [#2936]
- Fix `exponentformat` values `'e'` and `'E'` on log axes [#2921]
- Fix dynamic layer ordering of `heatmap` and `carpet` traces [#2917]
- Fix `Plotly.downloadImage` when using graph id or figure object
  as first argument [#2931]
- Fix regl-based rendering when WebGL buffer dimensions don't match canvas
  dimensions [#2939]

## [1.40.0] -- 2018-08-16

### Added
- Allow `contour`, `contourcarpet` and `histogram2dcontour` to have
  corresponding legend items using `showlegend` [#2891, #2914]
- Add `scatterpolar` and `scatterpolargl` attributes `r0`, `dr`, `theta0` and
  `dtheta` [#2895]
- Add layout attributes `piecolorway` and `extendpiecolors`
  for more control over `pie` colors [#2870]
- Add splom attribute `dimensions[i].axis.type` to easily override axis type
  in splom-generated axes [#2899]
- Add support for on-graph text in `scatterpolargl` traces [#2895]

### Changed
- Use `derequire` browserify plugin to make bundling distributed npm package
  with browserify possible [#2905]
- Speed up cartesian axis autorange edits (and thus double-click interactions) [#2823]
- Do not clear WebGL context when `scattergl` graph has no `visible:true`
  traces, which speeds up e.g. legend interactions [#2860]
- Compute data extremes per trace, which improves performance in some cases [#2860]
- Use `<linearGradient>` to render filled colorbars [#2910, #2914]
- Rename trace module `setPositions` methods `crossTraceCalc` [#2868]
- Use `regl@1.3.7` [#2863]

### Fixed
- Fix scalar `marker.size` bounds in legend items [#2840]
- Fix positioning of legend symbols for traces with fills [#2891]
- Fix `scattergl` select -> double-click -> pan behavior [#2815]
- Fix `scattergl` marker for IE11 [#2863]
- Fix inheritance of explicit `pie` colors by later traces [#2870]
- Fix layer ordering on graphs with multiple `contour` traces with heatmap
  coloring [#2891]
- Fix layer ordering on `visible` toggling for `contour`-like traces [#2891]
- Fix cases where colorbars would be drawn over its bounds [#2910]
- Fix `tickwidth` edits on `ohlc` traces [#2823]
- Fix labels on splom-generated axes with categorical data [#2899]
- Fix handling of splom dimensions on axes of conflicting types [#2899]
- Fix `splom` trace `visible` edits [#2860]
- Fix `splom` select -> double-click -> pan behavior [#2899]
- Fix `scatterpolargl` behavior during angular and radial drag interactions [#2888]
- Fix handling of auto date ticks below our 100 microseconds limit [#2912]
- Fix `scatter3d` attributes which had incorrectly labeled `textposition`
  and `textfont.family` as `arrayOk` and contained unimplemented `line.showscale`
  and `line.colorbar` [#2879]
- Fix `scattergl` and `scatterpolargl` attribute declarations for `hoveron` [#2895]


## [1.39.4] -- 2018-08-02

### Fixed
- Fix tenths of milliseconds handling in old numeric date data
  (bug introduced in 1.21.0) [#2847]
- Fix `yaxis` overlaying `yaxis2` layouts
  (bug introduced in 1.39.3) [#2857]


## [1.39.3] -- 2018-07-25

### Fixed
- Fix overlaying subplot configuration relayouts [#2831]
- Fix trace toggling from position-editable horizontal legends [#2829]
- Fix `[un]selected.marker.opacity` settings on `scattergeo` traces [#2827]
- Fix selections on some Robinson projections [#2827]


## [1.39.2] -- 2018-07-16

### Fixed
- Fix scattergl selection after resize relayouts [#2801]
- Fix scattergl layout replot edits [#2793]
- Fix cartesian axis range animations (bug introduced in 1.37.0) [#2788]
- Fix contour labels that require thousands suffixes [#2806]
- Fix 'legendonly' legend items link to array `marker.symbol` [#2816]
- Fix handling of duplicate points under `line.simplify` [#2814]
- Fix transform removal via `Plotly.react` [#2805]
- Fix out-of-subplot scroll zoom on some geo projection types [#2811]
- Fix hover label in RTL pages [#2790]
- Reduce minified bundle back to their 1.39.0 sizes [#2792]


## [1.39.1] -- 2018-07-09

### Fixed
- Fix mapbox subplots in our minified bundles (bug introduced in 1.39.0) [#2789]
- Fix box and violin traces inner parts removal (bug introduced in 1.37.0) [#2785]


## [1.39.0] -- 2018-07-05

### Added
- Add distributed npm packages for the main plotly.js bundle and all our partial
  bundles for easy installation and bundling [#2670]
- Add template machinery along with helpers methods `Plotly.makeTemplate` and
  `Plotly.validateTemplate` [#2764]
- Add 3D `streamtube` traces [#2658]
- Add support for on-graph text in `scattergl` traces [#2737, #2783]
- Add `gridshape` attribute to polar subplots with values `'circular'` (the
  default) and `'linear'` (to draw polygon grids) [#2739]
- Add `'range'` and `'change'` `aggregate` transform functions [#2764]
- Add `visible` attribute to `rangeselector` and `updatemenu` buttons,  slider
  steps and `mapbox` layout layers as well as `tickformatstops` items [#2761]
- Add support for colorbar linked to `marker.color` values for `splom`,
  `scatterpolar` and `scatterpolargl` traces [#2681]
- Revamp icon settings in custom mode bar buttons, allowing users to specify
  their own dimensions and SVG transforms [#2762]
- Add `plotlyServerURL` config option [#2760]
- Added no-WebGL warnings for graphs with `scattergl`, `scatterpolargl`, `splom`
  and `parcoords` traces [#2697]

### Changed
- `plotly_afterplot` is now emitted after all edit types [#2773]
- Trace `uid` is no longer mutated into user trace objects [#2681]
- No longer add `marker.line` in `scattermapbox` fullData [#2766]
- Use `regl@1.3.6` [#2694]
- Use `mapbox-gl@0.45.0` [#2709]

### Fixed
- Fix `Plotly.react`'s handling of changing auto-margins [#2681]
- Make plotting/updating WebGL-based traces fail gracefully when WebGL isn't
  supported [#2697]
- Fix mapbox layout layer updates [#2734]
- Fix mapbox event inconsistencies [#2766]
- Correctly emit `plotly_relayout` at end of scroll on mapbox subplots [#2709]
- Fix `scatter3d` scalar `hovertext` handling [#2698]
- Fix line decimation for segments crossing the viewport [#2705]
- Fix `surface` trace contours when first level has length zero [#2712]
- Fix `contour(x|y|z).highlight` partial settings [#2712]
- Fix old date timezone precision in Chrome 67+ [#2747]
- Fix `Plotly.validate` for attribute with trailing numbers (e.g. `x0`, `y1`) [#2761]
- Fix x-only zoom moves when `xaxis.fixedrange: true`[#2776]
- Fix colorbar edits for `parcoords` and `histogram` traces [#2681]
- Fix bandwidth for single-value violins [#2775]
- Sanitize `margin` after 'autosize' relayouts [#2758]
- Make `Plots.resize` work when `layout` attribute is gone from graph div [#2710]
- Fix `colorscale` attribute descriptions [#2658]


## [1.38.3] -- 2018-06-11

### Fixed
- Fix `cone` axis padding when under `sizemode: 'absolute'` [#2715]
- Fix `cone` scaling on irregular grids [#2715]
- Fix `cone` `sizemode: 'absolute'` scaling and attribute description [#2715]
- Improve `cone` hover picking [#2715]
- Fix exception during histogram cross-trace computation [#2724]
- Fix handling of custom transforms that make their own data arrays [#2714]


## [1.38.2] -- 2018-06-04

### Fixed
- Fix bar text removal (bug introduced in 1.36.0) [#2689]
- Fix handling number `0` in hover labels and on-graph text [#2682]


## [1.38.1] -- 2018-05-29

### Fixed
- Fix transforms on `scattergl` traces [#2677]
- Fix `marker.line.width` scaling in `scattergl` traces [#2677]
- Fix `[un]selected.marker.size` scaling in `scattergl` traces [#2677]
- Create two not three WebGL contexts for scattergl/splom graphs
  (bug introduced 1.36.0) [#2656]
- Fix `z` updates of interpolated values on heatmap and contour traces with gaps [#2657]
- Fix select/pan double-click behavior when relayout from one another
  (bug introduced in 1.36.0) [#2668]
- Fix shift selection behavior after pan/scroll
  (bug introduced in 1.36.0) [#2676]


## [1.38.0] -- 2018-05-23

### Added

- Add 3D `cone` traces to visualize vector fields [#2641, #2647]
- Add ability to interactively change length and rotate line shapes [#2594]
- Add `toImageButtonOptions` config object to override to-image mode bar button
  options [#2607]
- Add Brazilian Portuguese (`pt-br`) locale [#2622]
- Add Italian (`it`) locale [#2632]

### Changed
- Improve cartesian scroll and pan (mostly) performance for graphs with
  many marker or/and text nodes [#2623]
- Improve `splom` first render and axis-range relayout performance [#2628]
- Improve multi-axis axis-range relayout performance by updating minimal set of
  axes instead of all axes [#2628]
- Use "grab" cursor to denote when annotations and shapes are draggable [#2594]
- Ignore zero and negative link values in `sankey` traces [#2629]
- Ignore unused and malformed links `sankey` traces without logging [#2629]

### Fixed
- Fix `scattergl` error bar computations when input value are numeric strings [#2620]
- Fix `scattergl` error bar computations for `x0`/`dx` and `y0`/`dy` coordinates [#2620]
- Fix `violin` kde span edge cases [#2650]
- Make `sankey` traces accept numeric strings [#2629]
- Fix axis range edits under axis constraints [#2620]
- Fix "sloppy click" event emission during cartesian zoom [#2649]
- Fix layout `grid` validation which lead to exceptions [#2638]
- Fix `parcoords` rendering in old Safari version [#2612]
- Link to https://get.webgl.org instead of http version in no WebGL message [#2617]


## [1.37.1] -- 2018-05-02

### Fixed
- Fix `Plotly.react` when adding/removing traces (bug introduced in 1.37.0) [#2603]


## [1.37.0] -- 2018-05-01

### Added
- Add `plotly_legendclick` and `plotly_legenddoubleclick` events [#2581]
- Add Swahili (`sw`) locale [#2526]

### Changed
- Improve cartesian trace update and removal by using more d3-iomatic patterns.
  This results in some performance improvements during redraws [#2574]
- Our internal `Lib.nestedProperty` no longer prunes empty containers in
  `gd.data`, `gd.layout`, `gd._fullData` and `gd._fulllayout`.
  We made this change to clean up some of the `Plotly.react` internals.
  This also lead to a slight performance boost [#2577]

### Fixed
- Fix `Plotly.react`'s handling of transformed traces [#2577]
- Fix Safari support for `scattergl` and `splom` traces [#2593]
- Fix `scattergl` point clustering edge cases [#2593]
- Fix `scattergl` selection after double-click on graphs
  with more than 1e5 points [#2593]
- Fix artificial number of lines limit in `scattergl` traces [#2568]
- Fix typed array support in color array in `scattergl` traces [#2596]
- Fix typed array support for `splom` traces [#2596]
- Make `scatter` and `scattercarpet` coexist on same subplot [#2574]
- Fix incorrect fallback border color for axis common hover labels [#2557]
- Fix handling of blank editable legend items [#2587]
- Fix spikelines positioning in Firefox [#2590]
- Fix `Plotly.react` modebar updates when the locale changes [#2592]
- Fix `scatter` selection performance regression (dating back to 1.32.0) [#2583]
- Fix `plotly_beforeplot` and `plotly_beforehover` event handlers when attached
  with `gd.once` [#2581]


## [1.36.1] -- 2018-04-18

### Fixed
- Fix `scattergl` in dist and CDN bundles
  (due to `browser-pack-flat` discrepancy introduced in 1.36.0)
  by removing `browser-pack-flat` from our bundling pipeline [#2572]


## [1.36.0] -- 2018-04-17

### Added
- Add `splom` (aka scatter plot matrix) traces [#2505]
- Add multi-selection and click-to-select on `parcoords` axes [#2415]
- Add selection and improve legend items for `ohlc` and `candlestick` [#2561]
- Add 'fixed size' layout shapes through new shape attributes
  `xsizemode`, `ysizemode`, `xanchor`  and `yanchor` [#2532]
- Add layout attribute `selectdirection` to restrict select-box direction [#2506]
- Add support for selections on graphs with range sliders [#2561]
- Add support for ragged `table` inputs [#2511]
- Add Czech (`cs`) locale [#2483]
- Add Japanese (`ja`) locale [#2558]

### Changed
- Multiple performance improvements for cartesian subplots, most noticeable
  on graphs with many cartesian subplots [#2474, #2487, #2527]
- Use new `gl-mesh3d` version that attempts to make lighting results less
  hardware-dependent [#2365]
- New and improved point-clustering algorithm for `scattergl` [#2499]
- Improved `regl-line2d` component [#2556]

### Fixed
- Fix memory leak in `parcoords` traces [#2415]
- Fix `scattergl` `selectedpoints` clearance under select/lasso drag modes [#2492]
- Fix `scattergl` horizontal lines rendering [#2564]
- Fix `scattergl` unselected marker opacity for array marker opacity traces [#2503]
- Fix `scattergl` hover over data gaps [#2499]
- Fix `ohlc` on category axes [#2561]
- Fix inconsistencies in `ohlc` and `candlestick` event data [#2561]
- Fix hover `text` for `candlestick` traces [#2561]
- Fix `scattermapbox` selections for traces with data gaps [#2513]
- Fix `table` border cases that got previously cut off [#2511]
- Fix `box` traces with one jittered outlier [#2530]
- Fix `cliponfalse: false` on reversed axes [#2533]
- Fix buggy `plot_bgcolor` rendering when updating axis `overlaying` attribute [#2516]
- Fix buggy `Plotly.react` behavior for `carpet`, `contourcarpet`, `scattercarpet`,
  `table` and x/y/z column `heatmap` traces [#2525]
- Fix buggy `Plotly.react` behavior for `ohlc` and `candlestick` traces [#2561]
- Fix ordered categories on graphs with `visible: false` traces [#2489]
- Fix ordered categories in multi-subplot graphs [#2489]
- Fix inconsistencies when ordering number and numeric string categories [#2489]
- Fix format `days` in English locale [#2490]
- Handle HTML links with encoded URIs correctly in svg text labels [#2471]


## [1.35.2] -- 2018-03-09

### Fixed
- Ping `mapbox-gl` to `0.44.1` so that users on fresh
  `npm install` do not get the wrong mapbox-gl version message [#2467]
- Fix swapping between `scatter` and `scatter3d` traces and other
  potential problems caused by incorrect axis constraints resetting [#2465]


## [1.35.1] -- 2018-03-08

### Fixed
- Fix `scatterpolar` in dist and CDN bundles
  (due to `browser-pack-flat` discrepancy introduced in 1.35.0) [#2458]
- Fix removing and adding scatter(gl) as not the first module [#2455]
- Ensure we don't draw ticks if there are none to draw [#2454]


## [1.35.0] -- 2018-03-07

### Added
- Add `automargin` attribute to cartesian axes which auto-expands margins
  when ticks, tick labels and/or axis titles do not fit on the graph [#2243]
- Add support for typed arrays as data array inputs [#2388]
- Add layout `grids` attribute for easy subplot generation [#2399]
- Implement `cliponaxis: false` for bar text [#2378]
- Add opposite axis attributes for range slider to control y axis range behavior [#2364]
- Generalize `hoverdistance` and `spikedistance` for area-like objects [#2379]
- Bring `scattergl` auto-range logic to par with SVG `scatter` [#2404]
- Add selected/unselected marker color size support to `scattermapbox` traces [#2361]

### Changed
- Remove all circular dependencies in our `src/` directory [#2429]
- Build our CDN bundles with `browser-pack-flat` browserify plugin [#2447]
- Bump `mapbox-gl` to `v0.44.0` [#2361]
- Bump `glslify` to `v6.1.1` [#2377]
- Stop relinking `customdata`, `ids` and any matching objects
  in `gd._fullLayout` during `Plots.supplyDefaults` [#2375]

### Fixed
- Fix buggy auto-range / auto-margin interaction
  leading to axis range inconsistencies on redraws
  (this bug was mostly noticeable on graphs with legends) [#2437]
- Bring back `scattergl` lines under select/lasso `dragmode`
  (bug introduced in `1.33.0`) [#2377]
- Fix `scattergl` visible toggling for graphs with multiple traces
  with different modes (bug introduced in `1.33.0`) [#2442]
- Bring back `spikelines` for traces other than `scatter`
  (bug introduced in `1.33.0`) [#2379]
- Fix `Plotly.Fx.hover` acting on multiple subplots
  (bug introduced in `1.32.0`) [#2379]
- Fix range slider with stacked y axes positioning
  (bug introduced in `1.32.0`) [#2451]
- Fix `scattergl` color clustering [#2377]
- Fix `Plotly.restyle` for `scattergl` `fill` [#2377]
- Fix multi-line y-axis label positioning [#2424]
- Fix centered hover labels edge cases [#2440, #2445]
- Fix hover labels in bar groups in compare mode [#2414]
- Fix axes and axis lines removal [#2416]
- Fix auto-sizing in `Plotly.react` [#2437]
- Fix error bars for `Plotly.react` and uneven data arrays [#2360]
- Fix edits for date-string referenced annotations [#2368]
- Fix `z` hover labels with exponents [#2422]
- Fix yet another histogram edge case [#2413]
- Fix fall back for contour labels when there's only one contour [#2411]
- Fix `scatterpolar` category angular period calculations [#2449]
- Clear select outlines on mapbox zoomstart [#2361]
- Fix legend click to causes legend scroll bug [#2426]


## [1.34.0] -- 2018-02-12

### Added
- Add `Plotly.react`, a new do-it-all API method that creates and update graphs
  using the same API signature [#2341]
- Add constraint-type contours to `contour` traces [#2270]
- Add `notched` and `notchwidth` attributes to `box` traces [#2305]
- Add localization machinery to auto-formatted date axis ticks [#2261]
- Add support for `text` in `mesh3d` traces [#2327]
- Add support for scalar `text` in `surface` traces [#2327]
- Make mode bar for graphs with multiple subplot types more usable [#2339]
- Add `npm@5` package-lock file [#2323]

### Changed
- All of gl-vis dependencies now use `gl-shader@4.2.1` [#2293, #2306]
- All our dependencies and source now use `glslify@6.1.0` [#2326]

### Fixed
- Prevent page scroll on mobile device on `gl2d` and `gl3d` subplots [#2296]
- Fix multi-marker `scattergl` selection errors (bug introduced in `1.33.0`) [#2295]
- Fix `Plotly.addTraces` in `scattergl` selection call backs (bug introduced in `1.33.0`) [#2298]
- Fix trace `opacity` restyle for `scattergl` traces (bug introduced in `1.33.0`) [#2299]
- Fix `scattergl` handling of `selectedpoints` across multiple traces [#2311]
- Fix `scattergl` horizontal and vertical line rendering [#2340]
- Fix restyle for scalar `hoverinfo` for `scatter3d`, `surface` and `mesh3d` traces [#2327]
- Fix `table` when content-less cells and headers are supplied [#2314]
- Fix `Plotly.animate` for attribute nested in `dimensions` containers [#2324]
- Fix `hoverformat` on `visible: false` cartesian axes (bug introduced in `1.33.0`) [#2329]
- Fix handling of double negative translate transform values [#2339]
- Fix compare `hovermode` fallback for non-cartesian subplot types [#2339]
- Fix animation error messages when overriding and ignoring frames updates [#2313]


## [1.33.1] -- 2018-01-24

### Fixed

- Fix selection on `scattergl` plots with >20k points [#2266]
- Update Spanish localization with new strings [#2268]
- Fix test_dashboard overly rigid restriction so parcoods works there [#2273]
- Make `layout.colorway` compatible with `sankey` traces [#2277]
- Fix click events on `fixedrange` subplots [#2279]
- Remove ghost fill when trace data is emptied out [#2280]
- Fix resizing of new `scattergl` plots [#2283]
- Fix positioning of carpet axis titles for `cheaterslope` edge cases [#2285]
- Fix coloring and hover info for heatmaps and contour maps with nonuniform bins [#2288]


## [1.33.0] -- 2018-01-18

### Added
- Completely rewritten `scattergl` trace type using `regl` [#2258]
- Completely rewritten polar chart renderer accompanied by new
  `scatterpolar` and `scatterpolargl` trace types [#2200]
- Add the ability to draw layout images and layout shapes on subplot
  with `scattergl` traces [#2258]
- Add `fill` capabilities to `scattergl` traces [#2258]
- Add `spikedistance`, `hoverdistance` and `skipsnap` for more customizable
  spikes and hover behavior on cartesian subplots [#2247]
- Add official Spanish translation (locale `es`) [#2249]
- Add official French translation (locale `fr`) [#2252]
- Add locale machinery to annotation _new text_ placeholder [#2257]

### Changed
- Old polar trace types (`scatter` with `(r,t)` coordinates,
  `bar` with `(r,t)` coordinates and `area`) are now deprecated.

### Fixed

- Fix `gl2d` tick label on pan interaction regression [#2258]
- Fix `candlestick` hover label regression (bug introduced in v1.32.0) [#2264]
- Fix several `gl2d` axis related bugs with new regl-based `scattergl` [#2258]
  See full list under the On-par gl2d milestone https://github.com/plotly/plotly.js/milestone/3
- Fix several polar bugs with `scatterpolar` [#2200].
  See full list under the On-par polar milestone https://github.com/plotly/plotly.js/milestone/2
- Fix `scattergl` marker.colorscale handling [#2258]
- Fix ternary relayout calls involving axis tick styles and titles [#2200]
- Fix decimal and thousands settings in `de` locale [#2246]
- Make scroll handler _passive_, removing those annoying console warnings [#2251]


## [1.32.0] -- 2018-01-11

### Added

- Add localization machinery including an official German translation (locale `de`) [#2195, #2207, #2210, #2232, #2217]
- Add `violin` trace type [#2116]
- Add `selected` and `unselected` attribute containers to customize selection states [#2135]
- Add support for multi-selections [#2140]
- Add layout `colorway` to custom the trace-to-trace color sequence [#2156]
- Add `tickformatstops` to set tick format per cartesian axis range [#1965]
- Add hover labels and selections to box points [#2094]
- Histogram events & bin hover label improvements [#2113]
- Add support for aggregation in `pie` traces [#2117]
- Add annotations `startarrowhead`, `arrowside`, `startarrowsize` and `startstandoff` attributes [#2164]
- Add `zhoverformat` to format `z` values in `heatmap`, `contour` and 2d histogram traces [#2106, #2127]
- Add `marker.opacity` to bar traces [#2163]
- Add `Cividis` colorscale [#2178]
- Implement transform inverse mapping [#2126, #2162]

### Changed

- Selections are now persistent [#2135]
- Make subplot initialization and removal more robust and consistent [#2227]
- Share WebGL context between `gl2d` and `parcoords` subplots [#2159, #2238]
- Rename _Save and edit plot in cloud_ mode bar button _Edit in Chart Studio_ [#2183]
- Minify bundles using `minify-stream` instead of UglifyJS2 [#2187]
- Update header for new year 2018 [#2231]
- Remove `type="text/javascript"` from `<script>` tags present in our docs and test utilities [#2217]

### Fixed

- Fix right-click handling [#2241]
- Miscellaneous fixes for `table` traces [#2107, #2182]
- Fix horizontal legend items alignment edge case [#2149]
- Fix shape and updatemenu layering [#2121]
- Fix bar with error bar with set `ids` edge case [#2169]
- Fix `cliponaxis: false` for non linear cartesian axes [#2177]
- Fix heatmap non-uniform brick gaps problem [#2213]
- Fix choropleth selection when `visible: false` trace are present on graph [#2099, #2109]
- Fix yet another contour drawing bug [#2091]
- Clean up pie event data [#2117]
- Fix scatter + bar hover edge cases [#2218]
- Allow hover labels to extend to edges of graph area [#2215]
- Harden location-to-feature against non-string country names for geo subplot [#2122]
- Remove obsolete `smith` attribute from plot schema [#2093]
- Fix colorbar class name [#2139]
- Make `Plotly.Plots.resize` accept graph ids (as well as graph divs) [#2212]


## [1.31.2] -- 2017-10-23

### Fixed
- Fix multiple `table` restyle bugs [#2107]
- Fix selection work when `visible: false` choropleth traces are present [#2099, #2109]
- Fix (another) contour generation bug [#2091]


## [1.31.1] -- 2017-10-16

### Fixed
- Fix IE and Edge SVG `toImage` support [#2068]
- Return empty set during selections of `visible: false` traces [#2081]
- Fix scroll glitch in `table` traces [#2064]
- Fix handling of 1D header values in `table` [#2072]
- Fix `table` line style defaults [#2074]
- Do not attempt to start drag on right-click [#2087]
- Phase out `alignment-baseline` attributes in SVG text nodes [#2076]
- Listen to document events on drag instead of relying on
  cover-slip node [#2075]


## [1.31.0] -- 2017-10-05

### Added
- Add `table` trace type [#2030]
- Add `geo.center` making geo views fully reproducible using layout attributes [#2030]
- Add lasso and select-box drag modes to `scattergeo` and `choropleth` traces
  [#2030]
- Add lasso and select-box drag modes to `bar` and `histogram` traces [#2045]
- Add `scale` option to `Plotly.toImage` and `Plotly.downloadImage` [#1979]
- Add `plot-schema.json` to `dist/`[#1999]

### Changed
- Throttle lasso and select-box events for smoother behavior [#2040]
- Harmonize gl3d and gl2d zoom speed with cartesian behavior [#2041]

### Fixed
- Fix numerous `restyle` and `relayout` bugs [#1999]
- Fix handling of extreme off-plot data points in scatter lines [#2060]
- Fix `hoverinfo` array support for `scattergeo`, `choropleth`,
  `scatterternary` and `scattermapbox` traces [#2055]
- Fix `Plotly.plot` MathJax promise chain resolution [#1991]
- Fix legend double-click trace isolation behavior for graphs with
  `visible: false` traces [#2019]
- Fix legend visibility toggling for traces with `groupby` transforms [#2019]
- Fix single-bin histogram edge case [#2028]
- Fix autorange for bar with base zero [#2050]
- Fix annotations arrow rendering when graph div is off the DOM [#2046]
- Fix hover for graphs with `scattergeo` markers outside 'usa' scope [#2030]
- Fix handling of cross anti-meridian geo `lonaxis` ranges [#2030]
- Fix miter limit for lines on geo subplots [#2030]
- Fix `marker.opacity` handling for `scattergeo` bubbles [#2030]
- Fix layout animation of secondary axes [#1999]
- Fix `sankey` hover text placement for empty `link.label` items [#2016]
- Fix `sankey` rendering of nodes with very small values [#2017, #2021]
- Fix `sankey` hover label positioning on pages that style the
  'svg-container' div node [#2027]
- Fix aggregation transforms restyle calls [#2031]


## [1.30.1] -- 2017-09-06

### Fixed
- Fix shapes on overlaid axes [#1975]
- Correctly clear cartesian axis titles on full axis updates [#1981]
- Make cartesian hover spikes work when no tick labels are present [#1980]

## [1.30.0] -- 2017-08-21

### Added
- Add aggregate transform [#1924]
- Add `constraintext` attribute for bar traces [#1931]
- Add axis `layer` attribute to ternary axes [#1952]
- Add cross-trace matching auto-binning logic to histogram traces [#1944]
- Add `data/layout/config` api to `Plotly.toImage` to generate a static
  graph without having to render an interactive graph first [#1939]
- Add `nameformat` attribute to `groupby` transforms to set pattern by which
  grouped traces are named [#1919]

### Fixed
- Fix hover label exponents [#1932, #1949]
- Fix scatter fill with isolated endpoints [#1933]
- Fix parcoords axis tick scale when `ticktext` is unordered [#1945]
- Fix sankey with 4 multi-links or more [#1934]
- Fix exponent labels beyond SI prefixes [#1930]
- Fix image generation for marker gradient legend items [#1928]
- Fix parcoords image generation when multiple parcoords graphs
  are present on page [#1947]
- Ignore bare closing tags in pseudo-html string inputs [#1926]


## [1.29.3] -- 2017-07-27

### Fixed
- Fix `groupby` / `filter` interactions when filter includes `target` data
  [#1892]


## [1.29.2] -- 2017-07-26

### Fixed
- Add fallback for `ArrayBuffer.isView` fixing gl2d and gl3d rendering
  in environments that don't support it (e.g. RStudio) [#1915]


## [1.29.1] -- 2017-07-25

### Fixed
- Fix axis line rendering when `showticklabels` is false
  (bug introduced in 1.29.0) [#1910]
- Fix histogram auto bin restyle [#1901]
- Fix colorbar edge case that caused infinite loops [#1906]


## [1.29.0] -- 2017-07-19

### Added
- Add touch interactions to cartesian, gl2d and ternary subplots including for
  select and lasso drag modes [#1804, #1890]
- Add support for contour line labels in `contour` and `contourcarpet` traces
  [#1815]
- Add support for select and lasso drag modes on `scattermapbox` traces [#1836]
- Add double click interactions to mapbox subplots [#1883]
- Add reset view and toggle hover mode bar buttons to mapbox subplots [#1883]
- Add support for array `marker.opacity` settings in `scattermapbox` traces
  [#1836]
- Add `namelength` layout and trace attribute to control the trace name's
  visible length in hover labels [#1822]
- Add `cliponaxis` attribute to `scatter` and `scatterternary` traces to allow
  markers and text nodes to be displayed above their subplot's axes [#1861]
- Add axis `layer` attribute with `'above traces'` and `'below traces'` values
  [#1871]
- Add granular `editable` configuration options [#1895]
- Expanded traces generated by transforms now have unique colors [#1830]

### Fixed
- Fix axis line width, length, and positioning for coupled subplots [#1854]
- Fix alignment of cartesian tick labels [#1854]
- Fix rendering and updates of overlaying axis lines [#1855]
- Fix hover for 2D traces with custom colorbar `tickvals` [#1891]
- Fix hover and event data for `heatmapgl` and `contourgl` traces [#1884]
- Fix event data for `pie` and `sankey` traces [#1896]
- Fix drag mode `'pan'`in IE and Edge [#1871]
- Fix bar, error bar and box point scaling on scroll zoom [#1897]
- Fix shading issue in `surface` trace in iOS [#1868]
- Fix lasso and select drag modes for `scatterternary` traces [#1831]
- Fix cases of intersecting `contour` lines on log axes [#1856]
- Safer construction of `popup` click handler [#1888]
- Fix animation of annotations, shapes and images [#1315]
- Fix histogram bin computation when more than 5000 bins are needed [#1887]
- Fix tick label rendering when more than 1000 labels are present [#1898]
- Fix handling of empty `transforms` item [#1829]


## [1.28.3] -- 2017-06-26

### Fixed
- Fix deselect on double-clicking for gl2d traces [#1811]
- Fix `Plotly.purge` for gl2d and gl3d subplots
  (bug introduced in 1.28.0, leading to memory leaks) [#1821]
- Fix hover labels for `ohlc` and `candlestick` traces
  (bug introduced in 1.28.0) [#1808]
- Fix event data for `scattergeo` traces [#1819]
- Fix support of HTML entity number in pseudo-html inputs [#1820]


## [1.28.2] -- 2017-06-21

### Fixed
- Fix IE rendering error (`node.children` doesn't work on SVG nodes in IE) [#1803]


## [1.28.1] -- 2017-06-20

### Fixed
- Fix `scattergl` selected points. Points do not disappear after zoom any more
  in fast mode [#1800]


## [1.28.0] -- 2017-06-19

### Added
- Allow constraints by domain on cartesian axes using new axis attributes:
  `contrain: 'domain'` and `contraintoward` [#1767]
- Add gl3d annotations [#1638, #1786]
- Add support for lasso and select `dragmode` on `scattergl` traces [#1657]
- Add 48 new `scattergl` marker symbols (for total of 56) [#1781]
- Add array support for `hoverinfo` [#1761]
- Add animation support for `fillcolor` attribute [#1722]
- Add `colorscale` attributes to `mesh3d` traces [#1719]
- Add support for target and popup attributes pseudo-html text links [#1726]
- Add per-`direction` updatemenu dropdown arrows [#1792]
- Add `execute` attribute to sliders and updatemenus to skip method calls while
  still triggering associated events [#1700]
- Add `skip` value to the `method` attribute for sliders and updatemenus which
  acts as a no-op [#1699]

### Changed
- Include values of all array attributes in hover/click/select event data
  including `ids` and `customdata` [#1770]
- Make gl2d axis tick labels on-par with SVG versions [#1766]
- Build SVG text nodes directly instead of using `DOMParser` [#1783]
- Rework transform style into array syntax [#1794]
- Recompute hover on click to increase click robustness [#1646]
- Miscellaneous performance improvements including improved bounding box caching
  and adding a few short-circuit [#1772, #1792]

### Fixed
- Fix pan/zoom for layout component linked to `category` axes [#1748, #1791]
- Fix non-`linear` gl3d axis range settings [#1730]
- Fix `ohlc` and `candlestick` when open value equals close value [#1655]
- Fix annotations positioning when MathJax symbols are present [#1788]
- Fix array values in event data for transformed traces [#1717, #1727, #1737]
- Fix relayout event data for gl3d camera interactions [#1732]
- Fix scatter markers and text nodes linked to `ids` ordering on updates [#1709]
- Fix `Plotly.validate` for dynamic enumerated attribute
  (e.g. axis `anchor`, `overlaying`) [#1769]
- Fix pseudo-html handling in sliders, updatemenus, range-sliders,
  range-selectors and carpet traces [#1792]
- Fix annotation bounding box and arrow heads in IE [#1782]
- Fix svg exports in IE for graphs with multiple clip paths [#1740]
- Fix `sankey` positioning in IE [#1723, #1731, #1729, #1735]
- Fix relative links in IE [#1715]
- Suppress render warning in gl3d graphs with error bars [#1718]


## [1.27.1] -- 2017-05-17

### Fixed
- Fix text box positioning on scrolled windows (bug introduced in 1.27.0) [#1683, #1690]
- Fix styling over links in annotation text [#1681]
- Fix `mesh3d` with `vertexcolor` coloring [#1686]
- Fix `sort` transform with set `categoryarray` [#1689]
- Fix `scatter` text node data join [#1672]
- Fix `plot` promise resolution in graphs with layout images in IE11 [#1691]

## [1.27.0] -- 2017-05-10

### Added
- Sankey diagram with new trace type `sankey` [#1591, #1664]
- Add `hoverlabel` trace and layout attributes to customize hover label colors
  and fonts [#1582]
- Add `marker.gradient` attributes for `scatter`, `scattergeo`, `scatterternary`
  and `scattercarpet` traces [#1620]
- Add `sort` transform [#1609]
- Add `preservegaps` `filter` transform attribute [#1589]
- Add `!=` (not equal) `filter` transform operation [#1589]
- Add `labelfont`, `tickfont` and `rangefont` attributes for `parcoords` traces
  [#1624]
- Pass DOM mouse event on `plotly_clickannotations` events [#1652]

### Changed
- Performance optimization for range sliders and Drawing cache [#1585]

### Fixed
- Fix `scattergl` marker symbol positioning (bug introduced in 1.25.0) [#1633]
- Fix gl2d zoom where two clicks would trigger a zoom box (bug introduced 1.26.0) [#1632]
- Fix legend double click handler for `carpet` traces [#1636]
- Fix `restyle` for `scattercarpet` for style attributes with array support [#1641]
- Fix `restyle` for array layout components when more than 10 items are present
  [#1639]
- Fix select-box and lasso selections so that they don't include bad-data items
  [#1656]
- Fix `restyle` for contour `zmin` and `zmax` [#1653]
- Fix `scatter` text node transitions [#1616, #1626]


## [1.26.1] -- 2017-04-21

### Fixed
- Fix `pie` fill opacity [#1615]
- Fix `contour.value` declaration for `contourcarpet` trace [#1612]


## [1.26.0] -- 2017-04-18

### Added
- Carpets plots with new trace types: `carpet`, `scattercarpet` and
  `contourcarpet` [#1595, #1596]
- Axis constraints with new cartesian and gl2d axis attributes `scaleanchor` and
  `scaleratio` [#1522]
- Annotations `width`, `height`, `valign` and `xshift` and `yshift` attributes
  [#1551, #1590]
- Hover text over annotations with `hovertext` and `hoverlabel` attributes
  [#1573, #1590]
- Add `hovertext` attribute to trace types that can show `text` values on graph
  to allow setting hover text independently [#1523]
- Add `spikes` interactions functionality to cartesian subplots [#1461]
- Pass mouse DOM mouse event during `plotly_click`, `plotly_hover` and
  `plotly_unhover` [#1505]
- Add `visible` attribute to cartesian and gl3d axes to easily make them
  disappear [#1595, #1599]
- Make `deleteFrames(gd)` delete all frames [#1531]

### Changed
- Lock down `gl-plot3d` and `matrix-camera-controller` dependencies to include
  latest memory management improvements [#1570]
- Performance improvements for `category` axes [#1544]
- Skip overhead for `showLink` config option is false [#1557]
- Optimize scatter trace sorting on updates [#1555]
- Lock down `gl-scatter2d-sdf` dependency to `1.3.4` while waiting for bug fix
  there [#1572]

### Fixed
- Fix bar sizes of traces with (x,y) `NaN` items [#1519]
- Fix handling of `NaN` items in array-ok attributes for `scattergeo` and
  `scattermapbox` traces [#1538, #1564]
- Fix hover label position for `bar` traces with set `width` [#1527]
- Fix `restyle` for attribute containers [#1536]
- Fix `restyle` exception for `scattergl` traces with no `y` data [#1567]
- Fix animation of text nodes that contain `<br>`s [#1602]
- Fix `toImage` for mapbox subplots when access token is set in the config
  options [#1598]
- Emit `plotly_hover` on `pie` traces when `hoverinfo: 'none'` [#1505]
- Pass trace info during `plotly_click` on `pie` traces [#1505]
- Pass through the wheel event if the scrollbar is at the very top or bottom
  [#1588]


## [1.25.2] -- 2017-03-31

### Fixed
- rm `const` token from dist bundles that depend on `big-rat`,
  see https://github.com/rat-nest/big-rat/pull/4 for more details.


## [1.25.1] -- 2017-03-28

### Fixed
- Fix `restyle` for `scattergl` traces with array `marker.size` (bug introduced
  in `1.25.0`) [#1521]
- Fix `relayout` for `histogram2dcontour` traces [#1520]
- Do not unnecessary mutate `parcoords` full trace objects when computing
  line color and colorscale [#1509, #1508]
- Do not unnecessary coerce trace opacity in `parcoords` traces [#1506]


## [1.25.0] -- 2017-03-20

### Added
- Double click handler on legend items to isolate 1 traces / group on graph
  [#1432]

### Changed
- Use signed distance fields (SDF) method to render heterogeneous `scattergl`
  traces improving performance [#1398]
- Improve first-render performance in `scattergl` traces by only creating
  visible objects [#1444]
- Use `color-rgba` instead of `tinycolor2` to convert plotly color definitions to
  WebGL buffers improving performance for gl3d and gl2d traces [#1443]
- Bump `uglify-js` minifier to version `2.8.12` [#1450]

### Fixed
- Fix 3D trace ordering on visibility toggle [#1466]
- Fix gl2d trace ordering on visibility toggle [#1444]
- Fix autorange routine for bar traces [#1475]
- Fix shapes and images referencing a missing subplot [#1481]
- Ensure array attributes can be restyled in all situations [#1488]
- Fix XYZ-column-to-2D-z convert routine for columns containing nulls [#1491]
- Fix range slider display when anchored to log axes [#1472]
- Make sure all trace types can be deleted from range sliders [#1472]
- Let the `parcoords` object tree be garbage collected on `restyle` [#1479]
- Bring back support for histogram colorscales (bug introduced in `1.21.3`)
  [#1500]
- Support all axis types for clicktoshow annotations [#1497]
- Fix 3D margin relayout calls (bug introduced in `1.24.1`) [#1494]
- Fix `relayout` when trying to update empty axis containers (bug introduced in
  `1.24.0`) [#1494]


## [1.24.2] -- 2017-03-10

### Fixed
- Fix removal of last annotation or shape [#1451]
- Fix shape and image clip path removal [#1453]
- Fix overdrawing of data-referenced images [#1453]
- Make handling of `layer: 'below'` shape more robust [#1453]
- Allow multiple `parcoords` dimensions with the same label [#1457]


## [1.24.1] -- 2017-03-07

### Fixed
- Ensure that calling restyle or relayout in a `plotly_unhover` handler does not
  result in an infinite loop (bug introduced in 1.24.0) [#1448]
- Ensure autorange routine is bypassed when axis range is set (bug introduced in
  1.24.0) [#1425]
- Fix annotations dragging in editable mode (bug introduced in 1.22.0) [#1441]
- Show correct curve number in gl2d hover data [#1427]
- Clear parcoords canvas specially if no panel exist [#1440]
- Fix parcoords to render last block increment [#1447]
- Axis refs in hover data are not plagued by circular references [#1431]


## [1.24.0] -- 2017-02-27

### Added
- Add `parcoords` trace type (parallel coordinate plots) [#1256]
- Add support for multiple range sliders [#1355]
- Add `'aitoff'` and `'sinusoidal'` geo projection types [#1422]
- Implement `scene.dragmode: false` to disable drag interaction on 3D subplots
  [#1377]
- Add `showAxisDragHandles` and `showAxisRangeEntryBoxes` configuration options
  [#1389]
- Add `customdata` attribute to scatter traces to add custom data to scatter SVG
  nodes [#1379]

### Changed
- Consistent handling of array containers during `relayout` [#1403]
- Improve hover for `choropleth` traces [#1401]
- Make range slider handles and mask crispier [#1409]
- Bump `country-regex` dependency to `1.1.0` [#1392]

### Fixed
- Fix 3D on iOS devices [#1411]
- Fix `surface` trace opacity scaling [#1415]
- Fix hover data in animations [#1274]
- Fix annotations edit when dragging from one axis to another [#1403]
- Fix 3D hover labels for date axes [#1414]
- Deleting cartesian subplots now clear their corresponding axis titles [#1393]
- Fix hover for xyz column `heatmap` trace `'text'` [#1417]
- Fix `scattermapbox` lines with trailing gaps [#1421]
- Make `restyle`, `relayout` and `update` not mutate input update objects [#1376]
- Fix race condition in gl2d `toImage` [#1388]
- Fix handling of `Virgin Islands` country name [#1392]
- Fix `Plotly.validate` for `colorscale` attributes [#1420]


## [1.23.2] -- 2017-02-15

### Changed
- Bower installs now fetch un-minified `dist/plotly.js` bundle [#1373]
- Add package to packagist repository [#1375]


## [1.23.1] -- 2017-02-13

### Fixed
- Fix `relayout` for `scene.camera` values [#1364]
- Fix scaling on axis corner drag interactions for `bar` traces [#1370]
- Allow `bar` and `histogram` traces to coexist on same subplot [#1365]
- Fix `bar` position computations when placeholder traces are present [#1310]
- Fix auto-axis-type routine for data-less `candelestick`traces [#1359]


## [1.23.0] -- 2017-02-06

### Added
- Add scrollbox to long dropdown updatemenus [#1214]

### Fixed
- Multiple IE9 fixes [#1332]
- Ensure that `plotly_afterplot` is fired before `Plotly.plot` promise is
  resolved [#1342]
- Fix exception when dragging graphs with empty text labels [#1336]
- Fix exception when creating empty `ohlc` and `candlestick` traces [#1348]
- Fix `editable: true` legend items logic for `ohlc` and `candlestick` traces [#1349]
- Fix restyle for contour traces in cases where autocontour is defaulted to true
  [#1338]
- Fix edge case in axis label tick assignments [#1324]
- Fix vanishing titles text in `editable: true` [#1351]
- Fix 3D thumbnail image generation [#1327]


## [1.22.0] -- 2017-01-19

### Added
- Add `cumulative` histogram attributes to generate Cumulative Distribution
  Functions [#1189]
- Add `standoff` attribute for annotations to move the arrowhead away from the
  point it's marking [#1265]
- Add `clicktoshow`, `xclick` and `yclick` attributes for annotations to
  show/hide annotations on click [#1265]
- Support data-referenced annotation in gl2d subplots [#1301, #1319]
- Honor `fixedrange: false` in y-axes anchored to xaxis with range slider
  [#1261]
- Add fallbacks for IE9 so that all cartesian traces can render without any
  polyfill [#1297, #1299]

### Changed
- Adapt plot schema output for plotly.py 2.0 [#1292]
- Bump `mouse-change` dep to `^1.4.0` [#1305]
- Improve performance in `visible` toggling for `scattergl` [#1300]

### Fixed
- Fix XSS vulnerability in trace name on hover [#1307]
- Fix ternary and geo subplot with `visible: false` first trace [#1291]
- Fix opacity for `mode: 'lines'` items in legend [#1204]
- Fix legend items style for bar trace with marker arrays [#1289]
- Fix range slider svg / pdf and eps image exports [#1306]
- Fix scattergl `visible: false` traces with empty data arrays [#1300]
- Fix a few contour trace edge cases [#1309]
- Updatemenus buttons now render above sliders [#1302]
- Add fallback for categorical histogram on linear axes [#1284]
- Allow style fields in sub and sup text [#1288]


## [1.21.3] -- 2017-01-05

### Fixed
- Fix zoom behavior on transformed traces [#1257]
- Compute axis auto-range after transform operation [#1260]
- Fix contour trace blowing up on zoom [#591]
- Fix `scattermapbox` and `scattergeo` handling of blank strings `text` [#1283]
- Lock `mouse-change@1.3.0` fixing 3D hover labels on fresh `npm install`
  [#1281]


## [1.21.2] -- 2016-12-14

### Fixed
- Fix handling of calendar in `filter` transforms where distinct calendars can
  now be set for both the `target` and `value` [#1253]
- Make `Plotly.addFrames` skip over non-plain-objects inputs [#1254]
- Make `Plots.graphJson` aware of `frames` [#1255]


## [1.21.1] -- 2016-12-14

### Fixed
- Fix `ms2datetime` routine for Chinese calendar [#1252]
- Fix `tickformat` for world calendars [#1252]


## [1.21.0] -- 2016-12-12

### Added
- Bar labels via `text` and `textposition` [#1159]
- Add support for 16 non-gregorian calendars for date inputs and display [#1220,
  #1230, #1237]
- Add support for ISO-8601 timestamps [#1194]
- Extend histogram bin auto-shifting algorithm to date axes [#1201]
- Trace type `heatmapgl` is now included in the main plotly.js bundle [#1197]

### Changed
- Linearize date coordinates using UTC rather than local milliseconds [#1194]

### Fixed
- Fix wrongly computed date positions around daylight savings time [#1194]
- Fix erroneous traces in multi-subplot layout containing fill-to scatter
  traces (and plotly.py violin plots) [#1198]
- Fix clip path URL on pages with query hashes [#1203]
- Ensure that numeric frame name are handle correctly [#1236]
- Fallback for manual manipulation of slider/frames [#1233]


## [1.20.5] -- 2016-11-23

### Fixed
- Fix 1.20.0 regression in handling numerical strings including commas and spaces
  [#1185]
- Fix 1.20.0 regression involving date histograms [#1186]
- Fix numerous  tickvals` and `ticktext` edge cases [#1191]


## [1.20.4] -- 2016-11-21

### Fixed
- Fix metaKeys field `PlotSchema.get()` output

## [1.20.3] -- 2016-11-21

### Fixed
- Remove infinite loop when plotting 1-pt `scattergl` traces [#1168]
- Fix updatemenu bug where the wrong button was set to active [#1176]
- Fix `addTraces` when called with existing traces as input [#1175]


## [1.20.2] -- 2016-11-17

### Fixed
- Fix hover labels in stacked bar charts [#1163]
- Fix mode bar zoom buttons on date axes [#1162]


## [1.20.1] -- 2016-11-16

### Fixed
- Fix annotation positioning on categorical axes [#1155]


## [1.20.0] -- 2016-11-15

### Added
- Allow date string inputs for axis ranges, `tick0`, `dtick`, annotation / image
  positions, histogram bins [#1078, #1150]
- Add special `dtick` values for log axes [#1078]
- Add `visible` attribute to annotations, shapes and images items [#1110]
- Expose events on slider start/change/end [#1126]
- Expose event on updatemenu button click [#1128]
- Allow custom transform module to have supply layout default handler [#1122]

### Changed
- Increase `scattergl` precision [#1114]
- Use `topojson-client` to convert topojson to geojson [#1147]

### Fixed
- Fix hover labels for multi-trace `scattergl` graphs (bug introduced in
  `1.18.0`) [#1148]
- Fix date format on hover on full hour [#1078]
- Fix bar labels for non-zero `base` values [#1142]
- Scatter colorscale now yield correct colors when cmin and cmax ashow re equal
  [#1112]
- Fix `filter` transform for categorical `target` arrays with range operations
  [#1120]
- Make sure frames with `null` values clear array containers [#1118]
- Fix animations involving trace `opacity` [#1146]
- Fix fallback for non-animatable trace modules (bug introduced in `1.18.1`)
  [#1141]
- Fix race condition in animation resolution when coupled with `relayout`
  [#1108]
- Enforce casting requested frame names to strings [#1124]
- `Plotly.animte` no longer breaks when passing `null` frames [#1121]
- `Plotly.PlotSchema.get` now correctly list rangeslider and rangeselector under
  `xaxis` only [#1144]
- `Plotly.relayout` correctly updates arbitrary layout attributes [#1133]


## [1.19.2] -- 2016-11-02

### Fixed
- Fix hover label positioning on bar traces [#1107]


## [1.19.1] -- 2016-10-27

### Fixed
- Fix dist bundles [#1094]


## [1.19.0] -- 2016-10-27

**Unpublished on npm and CDN** due to broken dist bundles.

### Added
- Add two-argument `Plotly.plot` call signature [#1014]
- Add two-way binding functionality to updatemenus and sliders [#1016]
- Add `width`, `base` and `offset` attribute to bar trace [#1075]
- Add `fromcurrent` and `direction` animation options [#1087]
- Add ability to filter by arbitrary array [#1062]

### Changed
- Rename `filtersrc` filter transform attribute `target` (with
  backward-compatible map) [#1062]
- Bump `sane-topojson` requirement to 2.0.0. New topojson dist files fix
  the Michigan state border [#1077]
- scattergl now handles higher resolution dates [#1033]
- Improve error messages in `Plotly.animate` [#1088]

### Fixed
- `Plotly.newPlot` now respect user-defined layout `height` and `width` [#537]
- Fix dendrogram cartesian axis layers [#1063]
- Fix RGBA colorscale handler for contour [#1090]
- Fix gl2d axis title positioning [#1067]
- Fix gl2d multi-line axis tick labels display [#1087]
- Fix performance deficit of scattergl trace type with date coordinates [#1021]
- Fix ohlc trace offset computation [#1066]
- Fix ohlc and candlestick default trace names [#1073]
- Make `Plotly.animate` work with frames container array containers (e.g
  annotations) [#1081]
- Make `restyle` and `relayout` consistently remove items in array containers
  when called with value argument `null` [#1086]


## [1.18.1] -- 2016-10-18

### Fixed
- Fix cartesian subplot resize [#1049]
- Fix cartesian interactivity after click [#1049]
- Fix `scattergeo` traces with not-found country names [#1046]
- Honor `'name'` hoverinfo flag in `ohlc` traces [#1050]
- Fix animation merging for frames including array containers [#1041. #1048]
- Fix `requestAnimationFrame` polyfill for script-tag imports [#1039]


## [1.18.0] -- 2016-10-13

### Added
- Add `ohlc` and `candlestick` trace types [#1020]
- Add slider layout component [#986, #1029]
- Add filter and groupby transforms [#936, #978]
- Add support for all cartesian trace types and subplot configuration in
  range slider range plots [#946, #1017]
- Add update menus `'buttons'` type, `direction` and `showactive` options [#974]
- Add `pad` attributes to update menus for more intuitive positioning [#989]
- Add `plotly_hover`, `plotly_click` and `plotly_unhover` event emitters
  on gl2d subplot [#994]
- Make `'text'` mode  scatter traces animatable [#1011]
- Add picking for `'line'` mode scattergeo traces [#1004]
- Add support for `fill: 'toself'` in scattergeo traces [#1004]

### Changed
- Allow null / undefined frames in `Plotly.addFrames`[#1013]

### Fixed
- Allow range sliders to properly relayout [#962]
- Fix handling of `NaN` gaps in range slider range plots [#946, #1017]
- Properly skip over `NaN`s in scattergeo data arrays [#1004]
- Fix handling graph div with style `visibility: inherit` [#990]
- Fix `Plotly.update` for updates that require a full data + layout replot [#971]
- Let update menus use `Plotly.update` method value [#972]
- Fix tickfont relayout call on 3D subplot [#982]


## [1.17.3] -- 2016-09-21

### Fixed
- Fix scatter text node translations on range relayout [#956]
- Fix `Plotly.restyle` for scatter trace `mode` [#956]
- Fix color mapping discontinuity in `surface` trace with circular colorscale
  [#959]
- Fix `Plotly.redraw` when scatter traces are added to the graph [#947]
- Fix double click side-effects in gl2d plots [#958]
- Emit event animatingframe frame during animations [#953]


## [1.17.2] -- 2016-09-12

### Fixed
- 3D colored axis backgrounds and axis labels are rendered again (bug introduced
  in 1.17.0) [#931]


## [1.17.1] -- 2016-09-09

### Fixed
- Restyling `visible` to `false` on all scatter traces present on a graph
  is now working again (bug introduced in 1.17.0) [#920]
- Relayouting `paper_bgcolor` now properly propagate to legend
  and updatemenu `bgcolor [#921]
- Mapbox plot routine no longer make request to public Mapbox server
  when linked to a Mapbox Atlas instance [#919]


## [1.17.0] -- 2016-09-07

### Added
- Add support for animations for scatter trace [#802]
- Add frames and animate API -> `Plotly.animate`, `Plotly.addFrames` and
  `Plotly.deleteFrames` [#802]
- Add `Plotly.update` method which can perform data and layout update in one
  call [#875]
- Add `pointcloud` gl2d trace type [#850, #869]
- Add `xgap` and `ygap` to heatmap traces to define space between heatmap bricks
  [#868]
- Add `separatethousands` axis attribute which determines whether four-digit
  numbers are separated or not [#848]
- Add `'skip'` value to trace `hoverinfo` corresponding to traces transparent to
  the hover picking routine [#851]
- Add support for trace opacity in `toself` filled trace [#896]
- Add global transform config option [#852]
- Add `requestAnimationFrame` to `dist/`[#904]

### Changed
- Explicitly skip undefined props on `restyle` and `relayout` [#844]
- Removed a few circular dependency patterns [#833, #837, #845, #878]

### Fixed
- Fix legend trace toggle background attributes on restyle [#909]
- Make 'yanchor' default be its intended value of `'top'` [#894]
- Fix box plot jitter algorithm when IQR = 0 [#915]
- Fix box plot jitter algorithm when data range is 0 [#915]
- Fix mapbox event firing duplicates [#901]
- Fix mapbox visible false traces handling on first draw [#900]
- Avoid draw buffer to display buffer copy in gl2d plots [#843]
- Do not extend data array on event emission [#842, #866]
- Make `Plotly.redraw` throw an error when called on non plotly graph div [#907]
- Make `plotly.min.js` work when injected in Require.js environment [#914]


## [1.16.3] -- 2016-08-23

### Fixed
- Fix SVG exports for graphs with layout images [#846]
- Properly handles duplicate categories in non-default `categoryorder` [#863]
- Fix range selector position logic for overlaying axes [#873]
- Autorange is now properly computed for heatmapgl and contourgl traces [#855,
  #874]
- Trace toggling via legend preserves axis ranges in gl2d plots [#855, #874]
- Bump `mapbox-gl` dependency to 0.22.0 [#867]


## [1.16.2] -- 2016-08-09

### Fixed
- Fix decoding for the supported HTML entities (bug introduced in 1.16.0) [#835]
- Fix layout images position on subplots [#831]
- Fix a few cartesian autorange edge cases [#813]


## [1.16.1] -- 2016-08-05

### Changed
- Drop support for plotting in child windows which broke `Plotly.plot` in
  some numerous browsers (e.g. FF46, FF47, FF48) [#829]


## [1.16.0] -- 2016-08-04

### Added
- Add `updatemenus` (aka dropdowns) layout components [#770]
- Trace type `scattermapbox` is now part of the main bundle [#816]
- Add support for `plot` in child windows [#764, #806]
- Horizontal legends with many items are now wrapped into multiple lines [#786]
- Active color of range selector button is now configurable via `activecolor`
  [#796]
- Add support for mapbox style JSON [#795]

### Changed
- Promise queue is cleared on `restyle` and `relayout` instead of in
  the `plot` catch handler (which ate up user-defined catch handlers as of
  1.15.0) [#776, #789]
- Improve performance in `convertToSVG` step [#791, #804]

### Fixed
- Skip over non-container arrays in relink private key step (performance bug
  introduced in 1.15.0) [#817]
- Categorical heatmap traces with insufficient brick are now functional again
  (bug introduced in 1.14.0) [#783, #812]
- Fix `Plotly.validate` for info and container array attributes [#814, #819]
- Range selector buttons can now be deleted via `relayout` [#793]


## [1.15.0] -- 2016-07-25

### Added
- Add `Plotly.validate` method [#697]
- Add support for transforms plugins modules [#499]
- Some partial bundles are now distributed  in `dist/` [#740]
- Mapbox access token can now be set in `layout.mapbox` [#729]
- Undo/Redo queue length is now configurable via configuration option
  `queueLength` [#737]

### Changed
- Improve performance in gl2d request animation frame loop [#731]
- Improve `Lib.extendDeep` performance for primitive arrays [#732]
- Improve potential XSS input in `text` fields [#736]
- Improve scaling on scroll zoom for scatter lines and markers [#761, #762]

### Fixed
- `toImage` pixel output for gl2d graphs are now scaled properly [#735]
- `scattermapbox` marker size and color arrays are now correctly converted when
  they include repeated values [#747]
- Fix scatter3d marker line color inheritance [#754]
- `text` fields can now support link with query params `=` and `&` [#736]
- Fix Chrome 50 bug where tester svg blocked other DOM nodes [#745]


## [1.14.2] -- 2016-07-11

### Fixed
- `Plotly.newPlot` correctly clears all present WebGL contexts [#724]
- Bar traces with `layout.bargap` 0 and unset `marker.line.width` are functional
  again (bug introduced in 1.3.0) [#709]
- Stacked bar traces now correctly set the first bar position when leading gaps
  are present (bug introduced in 1.11.0) [#716]
- Bar traces with `layout.barmode` relative now correctly compute the bar sum of
  the first position when positive and negative values are present [#723]
- Event `plotly_relayout` is emitted upon pan / zoom on a mapbox subplot [#727]
- Lasso and select box drag modes now work with fixed ranged axes [#728]
- gl2d trace objects are purged when their parent scenes are destroyed [#724]


## [1.14.1] -- 2016-06-28

### Fixed
- Fix colorscale restyle calls on heatmap traces (bug introduced in 1.14.0)
  [#694]
- Hover after zoom / pan is now functional again in ternary plots (bug
  introduced in 1.14.0) [#688]
- Fix mapbox layer relayout starting from invisible layer [#693]
- Hover labels when `hoveron: 'fills'` are now constrained to the viewports
  [#688]
- Fix `surface` countours description [#696]
- Fix `mapbox.layers.line` description [#690]


## [1.14.0] -- 2016-06-22

### Added
- Attribute `line.color` in `scatter3d` traces now support color scales [#617]
- Annotations tail positions can now be set in data coordinates via the new
  `axref` and `ayref` attributes [#610]
- Attribute `hoveron` is added for `scatter` and `scatterternary` traces which
  adds the option to show hover labels about fill regions (instead of simply of
  about data points) [#673]
- Layout shapes can now be moved and resized (except for 'path' shapes) in
  editable contexts [#660]

### Changed
- Numerous additions and changes where made to the mapbox layout layers
  attributes (introduced in 1.13.0). Namely, `circle` and `symbol` layer type
  where added. Note that some style attributes have been renamed to match the
  mapbox-gl API more closely. [#681]

### Fixed
- Off-screen heatmap traces are properly deleted (bug introduced in 1.5.1)
  [#655]
- Hover labels for multi-heatmap subplot is functional again (bug introduced in
  1.4.0) [#655]
- Heatmap x/y brick generation is now functional for 0 and 1 item columns [#651]
- Multiple layout images can now shared the same image source [#672]
- Updating legend border and bgcolor attribute now works via `Plotly.relayout`
  [#652]
- Dragmode 'select' and 'lasso' no longer throw exception when selecting
  `legendonly` traces [#644]
- Ternary plots now respect the `staticPlot` config option [#645]
- Descriptions for axes `nticks` and contour traces `ncountours`now properly
  describe their behavior [#662]


## [1.13.0] -- 2016-06-13

### Added
- Beta version of the `scattermapbox` trace type - which allows users to create
  `mapbox-gl` maps using the plotly.js API. Note that `scattermapbox` is only
  available through custom bundling in this release [#626]
- Configurable log levels. All plotly.js logging is now turned off by default.
  Use `Plotly.setPlotConfig({ logging: /* 1 or 2 */ })` to (1) display warnings
  only or (2) all logs [#590]
- Thorough `mesh3d` attribute descriptions [#593]

### Changed
- Generalize hover picking routine (to make more easily re-usable for other plot
  types) [#575, #631]

### Fixed
- Fix `Plotly.toImage` and `Plotly.downloadImage` bug specific to Chrome 51 on
  OSX [#604]
- Fix `Plotly.downloadImage` for `svg` types [#604]
- Fix `scattergl` opacity and connectgaps for `'lines'` mode [#589]
- Make legend scroll bar keep its position after redraws [#584]
- Properly handle axis-reference shapes on overlaid axes [#612]
- Fix `Plotly.relayout` calls for `layout.images` in `{ astr: val }` notation
  [#624]
- Bring back correct default value for `lightposition` in surface traces (bug
  introduced in 1.12.0) [#571]
- Fix typos in contours descriptions in contour traces [#583]
- Fix typos in `axis.ticktext` description [#607]
- Fix ambiguities in histogram `nbin` descriptions [#623]


## [1.12.0] -- 2016-05-26

### Added
- Light positions, face normal epsilon and vertex normal epsilon are now
  configurable in `mesh3d` traces [#556]
- Light position is now configurable in `surface` traces [#556]
- `surface` and `mesh3d` lighting attributes are now accompanied with
  comprehensive descriptions. [#556]

### Changed
- Plot modules are now allowed to have their own `toSVG` method for
  subplot-specific to-svg logic [#554]

### Fixed
- gl2d plots are now functional in `core-js` environments (e.g. in babel es6
  presets) [#569]
- gl2d replot calls from a blank plot are now functional [#570]
- SVG graph config argument `scrollZoom` is now again functional (bug introduced
  in v1.10.0) [#564]
- `layout.separators` is now honored in pie text labels [#547]
- Heatmap `zsmooth` value `'fast'` is now functional for arbitrary layout widths
  [#548]
- Range sliders now respond to all axis range relayout calls [#568]


## [1.11.0] -- 2016-05-17

### Added
- Add top-level methods `Plotly.toImage` to convert a plotly graph to an image
  data URL (svg, png, jpg, and webp are supported) and `Plotly.downloadImage` to
  download a plotly graph as an image [#446]
- Add the ability to add arbitrary images loaded from a url to a plot's layout
  [#525]
- Add the option of making legend span horizontally [#535]
- Add `connectgaps` attribute to `scattergl` traces [#449]
- Add new 'relative' bar mode which stacks on top of one another with negative
  values below the axis, positive values above [#517]
- Add support for the 'winkel tripel' projection in geo subplots [#492]
- Event `plotly_relayout` is now emitted on gl2d subplot drag/pan/zoom
  interactions [#466]
- Add support for fill coloring in `contourgl` traces [#522, #543]

### Changed
- Cartesian on-hover routine is now uses a 50ms interval between search calls
  instead of 100ms for smoother displaying hover labels [#514]
- [Internal change] fullLayout `_has` fields are replaced by a `_has` method
  which checks if a particular plot type is present on a graph [#491]

### Fixed
- Bar widths of traces with null coordinates are now correctly computed [#542]
- Error bar spans on bar traces with null coordinates are now correctly computed
  [#542]
- All promises spawn in `Plotly.plot` are now guaranteed to be resolved before
  the final resolve [#521]
- Restyling `scatterternary` data attributes is now working [#540]
- Error bar of 0 length in log axes are not included in hover labels (instead of
  showing `NaN`s) [#533]


## [1.10.2] -- 2016-05-05

### Fixed
- Subplot and range slider clip paths are now functional in AngularJS [#509]
- `relayout` call involving axis `categoryorder` and `categoryarray` are now
  working [#510]
- Annotation drag interactions in `editable: true` mode are now functional (bug
  introduced in 1.10.0)[#505]
- Improved attribute description for shape `xref` and `yref` [#506]


## [1.10.1] -- 2016-05-02

### Fixed
- Resizing a graph (e.g. via `Plotly.relayout` or Plotly.Plots.resize)
  properly updates the plot area clip paths (bug introduced in 1.10.0) [#490]
- `Plotly.Snapshot.toSVG` is now functional again in IE11 and old version of
  Chrome and FF (bug introduced in 1.10.0) [#489]
- Hover labels of superimposed traces when 'hovermode' is set to 'closest' are
  properly displayed (bug introduced in 1.10.0) [#495]
- Surface contour highlights are toggleable [#459]
- Surface contour highlights style attributes are lower cased [#459]
- Zoom overlay are drawn over shapes [#448]
- Legend are draggable in `editable: true` contexts (bug introduced in 1.6.0)
  [#487]
- Legend scroll box are drawn outside the legend [#478]


## [1.10.0] -- 2016-04-12

### Added
- Beta version of two new 2D WebGL trace types: `heatmapgl` and `contourgl`
  [#427, #434]
- Two new `scatter` line `fill` modes: `'toself'` and `'tonext'` [#462]
- Fills for `scatterternary` traces are now supported [#462]
- Configurable axis category ordering with `categoryorder` and an optional
  `categoryarray` axis attributes [#419]
- Configurable shapes layer position with shape attribute `layer` [#439]
- Configurable range slider range (so that the initial xaxis range can differ
  from the range slider range) [#473]

### Changed
- Nested SVG elements in SVG image exports are removed, making the to-image mode
  bar button work in RStudio and SVG export compatible with Adobe Illustrator
  [#415, #454, #442]
- Use `country-regex` npm package instead of hard-coded file of ISO-3 code to
  country regular expressions [#461]

### Fixed
- Legend positioning does not break on negative `x` and `y` settings (bug
  introduced in 1.6.0) [#417]
- Shapes are properly deleted when clearing all of them at once (bug introduced
  in 1.9.0) [#465]
- Promise are return after first render in gl3d and gl2d plots [#421]
- Click and hover events are properly triggered when trace `hoverinfo` is set to
  `'none'` [#438]
- `plotly_unhover` events is now properly triggered on geo trace types [#429]
- `plotly_relayout` event is now properly triggered on gl3d set camera [#458]
- RGBA colors are now supported in `scatter` and `bar` custom color scales
  [#422]
- Range slider is now functional with `x0`/`dx` data [#441]
- Range slider is now compatible with mode bar axis range buttons and double
  click [#471]


## [1.9.0] -- 2016-04-12

### Added
- Ternary plots with support for scatter traces (trace type `scatterternary`) [#390]

### Fixed
- Toggling the visibility of `scatter3d` traces with `surfaceaxis` now works [#405]
- `scatter3d` traces with `surfaceaxis` turned now feature real 3D opacity [#408]
- `plotly_unhover` is now properly triggered over `pie` traces [#407]
- Better grammar in `scatter` attribute descriptions [#406]


## [1.8.0] -- 2016-04-04

### Added
- Range slider functionality for scatter traces [#336, #368, #377]
- Range selector functionality for cartesian and gl2d plot types [#373]
- Support for connectgaps in scatter3d traces [#361]

### Fixed
- gl2d toImage mode bar button is now again functional (bug introduced in 1.7.0) [#369]
- IE / Edge handling of getComputedTextLength is now functional [#376]
- improved marker color attribute description [#366]


## [1.7.1] -- 2016-03-30

### Fixed
- Legend dimensions are correctly updated (bug introduced in 1.7.0) [#365]
- Friction between cartesian double-click and drag interactions is reduced [#355]
- Ultra-zoomed svg line paths are correctly computed [#353]
- Initial axis ranges are no longer reset on data-updating restyle calls [#351]
- Events now work in jQuery no-conflict scopes (bug introduced in 1.7.0) [#352]


## [1.7.0] -- 2016-03-22

### Added
- Custom surface color functionality (for 4D plotting) is added to surface traces [#347]
- Top-level `Plotly.purge` method (which returns the graph div in its
  pre-Plotly.plot state) is added [#300]
- Support for custom hover labels on multiple subplots in `Plotly.Fx.hover` is
  added [#301]

### Fixed
- Error bars node ordering now respect the trace ordering [#343]
- Geo traces nodes now update properly on streaming plot calls [#324]
- jQuery check in event module is made more robust [#328]


## [1.6.3] -- 2016-03-07

### Fixed
-  Argument parsing for vertex and face colors of mesh3d traces is now
   functional [#287]


## [1.6.2] -- 2016-03-03

### Fixed
- SVG overflow property is now properly set for IE11 [#305, #306]
- Hover labels associated with `text` arrays with falsy values are properly
  skipped over [#310]
- Snapshot routines now strip browser-only user-select style attributes [#311]


## [1.6.1] -- 2016-03-01

### Fixed
- Legend scroll bars are no longer invalid SVG elements (bug introduced in 1.6.0) [#304]
- Colorscale YlGnBu and YlOrRd are now properly identified [#295]


## [1.6.0] -- 2016-02-29

### Added
- SVG cartesian, 3D, geographic maps and pie charts can now coexist on the same
  graph [#246, #258, #289]
- Legends with long item lists are now scrollable (instead of being cropped)
  [#243]
- Event `plotly_deselect` is now emitted after double-clicking in `select` and
  `lasso` drag modes.
- Event `plotly_doubleclick` is now emitted after double-clicking on SVG cartesian
  graphs in `zoom` and `pan` drag modes.
- Layout attributes `dragmode` and `hovermode` can now be set individually in
  each scene [#258]
- `Plotly.Plots.resize` now returns a promise. [#253, #262]

### Fixed

- `Plotly.deleteTraces` now properly deletes the last trace of a cartesian
  subplot [#289]
- `Plotly.deleteTraces` now works on heatmap, contour, pie, surface, mesh3d and
  geo trace types [#289]
- `Plotly.deleteTraces` now properly delete color bars associated with deleted
  traces
- Clearing cartesian axes via `relayout` no longer results in an uncaught error
  [#289]
- Events `plotly_hover`, `plotly_unhover` and `plotly_click` are properly
  emitted on 3D graphs [#240]
- Null and undefined categories are properly skipped over [#286]
- Hover labels on 3D graphs are now properly hidden when `hovermode` is set to
  false [#258]
- Multi-scene 3D graphs now set their camera position via their own scene
  attributes [#258]
- Toggling `hovermode` on 3D graphs no longer resets the scene domain [#258]
- Resetting the camera position on scenes where the `camera` attribute was
  supplied no longer results in an uncaught error [#258]
- Axis attributes `hoverformat`, `tickprefix`, `ticksuffix` are honored even
  when `showticklabels` is set to false [#267]
- Config option `doubleClick` set to `'reset'` now properly handles auto-ranged
  axes [#285]


## [1.5.2] -- 2016-02-10

### Fixed
- Fix geo trace visibility toggling (bug introduced in 1.5.1) [#245]


## [1.5.1] -- 2016-02-01

### Fixed
- Scattergeo and choropleth now correctly fire hover and click events [#215]
- Heatmap and contour traces are redrawn in the correct order [#194]
- Early returns in `Plotly.plot` now correctly return Promise rejections [#226]
- Soon to be deprecated `SVGElement.offsetParent` calls are removed [#222]
- Geo zoom in button is now correctly titled `Zoom in` [#219]
- All attribute description are correctly stripped from the dist files (bug
  introduced in 1.5.0) [#223]
- Insecure dev dependencies `ecstatic` and `uglify-js` are bumped [#225]
- Outdated karma-browserify dev dependency is bumped [#229]


## [1.5.0] -- 2016-01-22

### Added
- Modularize the library (first iteration). Trace types can be required in
  one-by-one to make custom plotly.js bundles of lesser size. [#180, #187, #193, #202]

### Changed
- Remove json assets from the js source files (to better support Webpack bundling) [#183]
- Update d3, tinycolor2, topojson dependencies [#195]
- Improve `'colorscale'` attribute description [#186]

### Fixed
- Fix pan mode drag delay [#188]
- Make `Plotly.deleteTrace` handle big-indices-array properly [#203]


## [1.4.1] -- 2016-01-11

### Fixed
- Click events work properly after being broken in 1.4.0 [#174]


## [1.4.0] -- 2016-01-11

### Added
- Lasso and rectangular selection interactions for scatter-marker and scatter-text traces [#154, #169]
- Un-gitignore css and svg font built files, removing post-install step and
  dependency on node-sass [#164]

### Changed
- Clean up Pie, Box and Choropleth trace module [#158, #159, #165]

### Fixed
- Surface traces correctly handle `zmin` and `zmax` attributes [#153]
- Pie trace correctly trigger hover events [#150]


## [1.3.1] -- 2016-01-04

### Fixed
- Fix `Plotly.addTraces` for gl3d and gl2d trace types [#140]


## [1.3.0] -- 2015-12-21

### Added
- Trigger click event on pie charts [#111]
- Add attribute descriptions for mesh3d trace type [#115]

### Changed
- [Internal] Trace module have now a 1-to-1 correspondence with trace type [#124]
- [Internal] Remove circularize import in colorbar and colorscale module [#136]

### Fixed
- Fixed zeroline behavior in gl3d plots [#112]
- Axis `tickangle` consistently used degrees in both svg and gl plots [#131]
- `Plotly.newPlot` destroy mode bar before plotting new one [#125]
- `Plotly.newPlot` removes all event listeners from graph div [#117]
- Fixed attribute description for scatter3d marker opacity [#114]


## [1.2.1] -- 2015-12-14

### Changed
- Improve XSS check in anchor href [#100]

### Fixed
- Fix Fifefox 42 to-image failures [#104]
- Fix error bar with type 'sqrt' logic making them visible without
  specifying the 'value' field [#91]
- Fix cartesian zoom/drag cover attributes for Firefox 31 [#92]


## [1.2.0] -- 2015-12-07

### Added
- All `Plotly.____` methods now return a promise, and pass the graph-div as an argument [#77]
- `package.json` now has `webpack` field so plotly.js can be used by webpack users [#68]
- Add support for rgba colours in pie-charts [#63]

### Changed
- Optimized by calling window.getComputedStyle only once [#81]
- Improved npm install process for topojson file resolve [#48]

### Fixed
- Fixed geo-plot promises [#52]
- Typo fixed in `No DOM element` error message [#64]
- Fix hover labels with hoverinfo 'text' [#70]
- Fix scaling for gl3d error bars [#74]


## [1.1.1] -- 2015-12-01

### Fixed
- Fix `displayModeBar` plot config logic [#57]
- Fix length-1 bins count as ascending in `Lib.findBin` [#47]
- Fix jasmine test runner on windows [#46]


## [1.1.0] -- 2015-11-25

### Added
- Add three plot config options: `modeBarButtonsToRemove`,
  `modeBarButtonsToAdd` and `modeBarButtons` which combine
  to add the ability to remove specific mode bar buttons add
  custom mode bar buttons and fully customize the mode bar.

### Fixed
- Fix installation from npm3 [#12]
- Fix UMD in plotly.js dist files [#18]
- Fix for blank elements in a text array [#31]

## [1.0.0] -- 2015-11-17

First fully open source release.

### Added
- Add 2D WebGL plot engine

### Changed
- Save to cloud is now done via a modebar button by default,
  the `'Edit chart'` link is still available through the
  `'showLink'` plot config.
- Better double-click notifier CSS

### Fixed
- Fix `Plotly.newPlot` 3D and geo bug.
- Fix `plotly_click` event bug in latest Chrome and Firefox.

### Known limitations
- Different plot types cannot be mixed in subplots.
- 2D WebGL has no image test support.
- Click and hover events are not hooked for gl3d, geo and gl2d
  plot types.
- Polar chart are under-developed.
