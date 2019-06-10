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
    name: 'sv',
    dictionary: {
        'Autoscale': 'Autoskala',                                                        // components/modebar/buttons.js:148
        'Box Select': 'Välj rektangel',                                                  // components/modebar/buttons.js:112
        'Click to enter Colorscale title': 'Klicka för att ange titel på färgskala',     // plots/plots.js:326
        'Click to enter Component A title': 'Klicka för att ange titel på komponent A',  // plots/ternary/ternary.js:376
        'Click to enter Component B title': 'Klicka för att ange titel på komponent B',  // plots/ternary/ternary.js:386
        'Click to enter Component C title': 'Klicka för att ange titel på komponent C',  // plots/ternary/ternary.js:396
        'Click to enter Plot title': 'Klicka för att ange titel på diagram',             // plot_api/plot_api.js:584
        'Click to enter X axis title': 'Klicka för att ange titel på x-axel',            // plots/plots.js:324
        'Click to enter Y axis title': 'Klicka för att ange titel på y-axel',            // plots/plots.js:325
        'Click to enter radial axis title': 'Klicka för att ange titel på radiell axel', // plots/polar/polar.js:498
        'Compare data on hover': 'Jämför data när muspekaren hålls över',                // components/modebar/buttons.js:176
        'Double-click on legend to isolate one trace': 'Dubbelklicka på förklaringen för att visa endast en serie',  // components/legend/handle_click.js:89
        'Double-click to zoom back out': 'Dubbelklicka för att zooma ut igen',           // plots/cartesian/dragbox.js:1089
        'Download plot': 'Ladda ner diagram',                                            // components/modebar/buttons.js:53
        'Download plot as a png': 'Ladda ner diagram som png',                           // components/modebar/buttons.js:52
        'Edit in Chart Studio': 'Editera i Chart Studio',                                // components/modebar/buttons.js:85
        'IE only supports svg.  Changing format to svg.': 'IE stöder enbart svg. Byter format till svg.',  // components/modebar/buttons.js:63
        'Lasso Select': 'Välj lasso',                                                    // components/modebar/buttons.js:121
        'Orbital rotation': 'Orbital rotation',                                          // components/modebar/buttons.js:281
        'Pan': 'Panorera',                                                               // components/modebar/buttons.js:103
        'Produced with Plotly': 'Skapad med Plotly',                                     // components/modebar/modebar.js:304
        'Reset': 'Återställ',                                                            // components/modebar/buttons.js:433
        'Reset axes': 'Återställ axlar',                                                 // components/modebar/buttons.js:157
        'Reset camera to default': 'Återställ kamera till standard',                     // components/modebar/buttons.js:319
        'Reset camera to last save': 'Återställ kamera till senast sparad',              // components/modebar/buttons.js:327
        'Reset view': 'Återställ vy',                                                    // components/modebar/buttons.js:512
        'Reset views': 'Återställ vyer',                                                 // components/modebar/buttons.js:550
        'Show closest data on hover': 'Visa närmaste värde när muspekaren hålls över',   // components/modebar/buttons.js:166
        'Snapshot succeeded': 'Bild skapad',                                             // components/modebar/buttons.js:75
        'Sorry, there was a problem downloading your snapshot!': 'Tyvärr gick något fel vid nedladdning av bild',  // components/modebar/buttons.js:78
        'Taking snapshot - this may take a few seconds': 'Skapar bild - detta kan ta några sekunder',  // components/modebar/buttons.js:60
        'Toggle Spike Lines': 'Aktivera/Inaktivera topplinjer',                          // components/modebar/buttons.js:569
        'Toggle show closest data on hover': 'Aktivera/Inaktivera visa närmaste värde när muspekaren hålls över',                      // components/modebar/buttons.js:361
        'Turntable rotation': 'Platt rotation',                                          // components/modebar/buttons.js:290
        'Zoom': 'Zooma',                                                                 // components/modebar/buttons.js:94
        'Zoom in': 'Zooma in',                                                           // components/modebar/buttons.js:130
        'Zoom out': 'Zooma ut',                                                          // components/modebar/buttons.js:139
        'close:': 'stängning:',                                                          // traces/ohlc/calc.js:106
        'concentration:': 'koncentration:',                                              // traces/sankey/plot.js:166
        'high:': 'hög:',                                                                 // traces/ohlc/calc.js:104
        'incoming flow count:': 'inkommande flöde summering:',                           // traces/sankey/plot.js:167
        'kde:': 'kde:',                                                                  // traces/violin/calc.js:94
        'lat:': 'lat:',                                                                  // traces/scattergeo/calc.js:48
        'lon:': 'lon:',                                                                  // traces/scattergeo/calc.js:49
        'low:': 'låg:',                                                                  // traces/ohlc/calc.js:105
        'lower fence:': 'undre gräns:',                                                  // traces/box/calc.js:146
        'max:': 'max:',                                                                  // traces/box/calc.js:144
        'mean ± σ:': 'medel ± σ:',                                                       // traces/box/calc.js:145
        'mean:': 'medel:',                                                               // traces/box/calc.js:145
        'median:': 'median:',                                                            // traces/box/calc.js:140
        'min:': 'min:',                                                                  // traces/box/calc.js:141
        'new text': 'ny text',                                                           // plots/plots.js:327
        'open:': 'öppning:',                                                             // traces/ohlc/calc.js:103
        'outgoing flow count:': 'utgående flöde summering:',                             // traces/sankey/plot.js:168
        'q1:': 'q1:',                                                                    // traces/box/calc.js:142
        'q3:': 'q3:',                                                                    // traces/box/calc.js:143
        'source:': 'källa:',                                                             // traces/sankey/plot.js:164
        'target:': 'mål:',                                                               // traces/sankey/plot.js:165
        'trace': 'serie',                                                                // plots/plots.js:329
        'upper fence:': 'övre gräns:',                                                   // traces/box/calc.js:147
    },
    format: {
        days: ['Söndag', 'Måndag', 'Tisdag', 'Onsdag', 'Torsdag', 'Fredag', 'Lördag'],
        shortDays: ['Sön', 'Mån', 'Tis', 'Ons', 'Tor', 'Fre', 'Lör'],
        months: [
            'Januari', 'Februari', 'Mars', 'April', 'Maj', 'Juni',
            'Juli', 'Augusti', 'September', 'Oktober', 'November', 'December'
        ],
        shortMonths: [
            'Jan', 'Feb', 'Mar', 'Apr', 'Maj', 'Jun',
            'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec'
        ],
        date: '%Y-%m-%d'
    }
};
