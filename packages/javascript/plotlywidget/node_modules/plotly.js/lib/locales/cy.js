/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

module.exports = {
    moduleType: 'locale',
    name: 'cy',
    dictionary: {
        'Autoscale': 'Graddfa awtomatig', // components / modebar / buttons.js: 150
        'Box Select': 'Dewiswch â blwch', // components / modebar / buttons.js: 114
        'Click to enter Colorscale title': 'Cliciwch i nodi teitl Graddfa Liw', // plots / plots.js: 327
        'Click to enter Component A title': 'Cliciwch i nodi teitl Cydran A', // plots / ternary / ternary.js: 390
        'Click to enter Component B title': 'Cliciwch i nodi teitl Cydran B', // plots / ternary / ternary.js: 405
        'Click to enter Plot title': 'Cliciwch i nodi teitl y Plot', // plot_api / plot_api.js: 513
        'Click to enter Component C title': 'Cliciwch i nodi teitl Cydran C', // plot / ternary / ternary.js: 416
        'Click to enter X axis title': 'Cliciwch i nodi teitl echelin X', // plots.js: 325
        'Click to enter Y axis title': 'Cliciwch i nodi teitl echelin Y', // plots / plots.js: 326
        'Click to enter radial axis title': 'Cliciwch i nodi teitl echelin reiddiol', // plots / polar / polar.js: 408
        'Compare data on hover': 'Cymharwch ddata wrth hofran', // components / modebar / buttons.js: 178
        'Double-click on legend to isolate one trace': 'Dwbl-gliciwch ar yr allwedd i neilltuo un llinell', // components / legend / handle_click.js: 89
        'Double-click to zoom back out': 'Dwbl-gliciwch i chwyddo\'n ôl', // plots / cartesian / dragbox.js: 1011
        'Download plot': 'Lawrlwythwch blot', // components / modebar / buttons.js: 55
        'Download plot as a png': 'Lawrlwythwch y plot fel png', // components / modebar / buttons.js: 54
        'Edit in Chart Studio': 'Golygu yn Chart Studio', // components / modebar / buttons.js: 87
        'IE only supports svg. Changing format to svg.': 'Dim ond svg mae IE yn ei gefnogi. Newid fformat i svg.', // components / modebar / buttons.js: 65
        'Lasso Select': 'Dewiswch â lasŵ', // components / modebar / buttons.js: 123
        'Orbital rotation': 'Cylchdroi orbital', // components / modebar / buttons.js: 287
        'Pan': 'Pan', // components / modebar / buttons.js: 105
        'Produced with Plotly': 'Cynhyrchwyd gyda Plotly', // components / modebar / modebar.js: 272
        'Reset': 'Ailosod', // components / modebar / buttons.js: 443
        'Reset axes': 'Ailosod echelinau', // components / modebar / buttons.js: 159
        'Reset camera to default': 'Ailosod camera i\'r rhagosodiad', // components / modebar / buttons.js: 325
        'Reset camera to last save': 'Ailosod camera i\'r cadw diwethaf', // components / modebar / buttons.js: 333
        'Reset view': 'Ailosodwch y golwg', // components / modebar / buttons.js: 592
        'Reset views': 'Ailosod olygfeydd', // components / modebar / buttons.js: 540
        'Show closest data on hover': 'Dangos y data agosaf wrth hofran', // components / modebar / buttons.js: 168
        'Snapshot succeeded': 'Llwyddodd y Ciplun', // components / modebar / buttons.js: 77
        'Sorry, there was a problem downloading your snapshot!': 'Mae\'n ddrwg gennym, roedd problem wrth lawrlwytho eich ciplun!', // components / modebar / buttons.js: 80
        'Taking snapshot - this may take a few seconds': 'Tynnu ciplun - gallai hyn gymryd ychydig o eiliadau', // components / modebar / buttons.js: 62
        'Toggle Spike Lines': 'Toglo llinellau pigog', // components / modebar / buttons.js: 559
        'Toggle show closest data on hover': 'Toglo dangos y data agosaf wrth hofran', // components / modebar / buttons.js: 364
        'Turntable rotation': 'Cylchdroi trofwrdd', // components / modebar / buttons.js: 296
        'Zoom': 'Chwyddo', // components / modebar / buttons.js: 96
        'Zoom in': 'Closio', // components / modebar / buttons.js
        'Zoom out': 'Cilio', // components / modebar / buttons.js: 141
        'close:': 'cau:',  // traces / ohlc / calc.js: 104
        'high:': 'uchel:', // traces/ ohlc / calc.js: 102
        'incoming flow count:': 'cyfrif llif sy\'n dod i mewn:', // traces / sankey / plot.js: 142
        'kde:': 'kde:', // traces / violin / calc.js: 69
        'lat:': 'lledred:', // traces / scattergeo / calc.js: 48
        'lon:': 'hydred', // traces / scattergeo / calc.js: 49
        'low:': 'isel:', // traces / ohlc / calc.js: 103
        'lower fence:': 'ffens isaf:', // traces / box / calc.js: 140
        'max:': 'uchafbwynt:', // traces / box / calc.js: 138
        'mean ± σ:': 'cymedr ± σ:', // traces / box / calc.js: 139
        'mean:': 'cymedr:', // traces / box / calc.js: 139
        'median:': 'canolrif:', // traces / box / calc.js: 134
        'min:': 'isafbwynt:', // traces / box / calc.js: 135
        'new text': 'testun newydd', // plots / plots.js: 328
        'open:': 'agor:', // traces / ohlc / calc.js: 101
        'outgoing flow count:': 'cyfrif llif sy\'n mynd allan:', // traces / sankey / plot.js: 143
        'q1:': 'q1:',   // traces / box / calc.js: 136
        'q3:': 'q3:',   // traces / box / calc.js: 137
        'source:': 'ffynhonnell:', // traces / sankey / plot.js: 140
        'target:': 'targed:', // traces / sankey / plot.js: 141
        'trace': 'olin', // plots / plots.js: 330
        'upper fence:': 'ffens uchaf:' // traces / box / calc.js: 141
    },
    format: {
        days: ['Dydd Sul', 'Dydd Llun', 'Dydd Mawrth', 'Dydd Mercher', 'Dydd Iau', 'Dydd Gwener', 'Dydd Sadwrn'],
        shortDays: ['Sul', 'Llun', 'Maw', 'Mer', 'Iau', 'Gwen', 'Sad'],
        months: [
            'Ionawr', 'Chwefror', 'Mawrth', 'Ebrill', 'Mai', 'Mehefin',
            'Gorffennaf', 'Awst', 'Medi', 'Hydref', 'Tachwedd', 'Rhagfyr'
        ],
        shortMonths: [
            'Ion', 'Chw', 'Maw', 'Ebr', 'Mai', 'Meh',
            'Gor', 'Awst', 'Medi', 'Hyd', 'Tach', 'Rhag'
        ],
        date: '%d/%m/%Y'
    }
};
