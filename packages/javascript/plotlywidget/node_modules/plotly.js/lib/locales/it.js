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
    name: 'it',
    dictionary: {
        'Autoscale': 'Scala automaticamente',                                                               // components/modebar/buttons.js:139
        'Box Select': 'Selezione box',                                                                    // components/modebar/buttons.js:103
        'Click to enter Colorscale title': 'Clicca per inserire un titolo alla scala di colori',                     // plots/plots.js:437
        'Click to enter Component A title': 'Clicca per inserire un titolo al componente A',            // plots/ternary/ternary.js:386
        'Click to enter Component B title': 'Clicca per inserire un titolo al componente B',            // plots/ternary/ternary.js:400
        'Click to enter Component C title': 'Clicca per inserire un titolo al componente C',            // plots/ternary/ternary.js:411
        'Click to enter Plot title': 'Clicca per inserire un titolo al grafico',                        // plot_api/plot_api.js:579
        'Click to enter X axis title': 'Clicca per inserire un titolo all\'asse X',                      // plots/plots.js:435
        'Click to enter Y axis title': 'Clicca per inserire un titolo all\'asse Y',                      // plots/plots.js:436
        'Click to enter radial axis title': 'Clicca per inserire un titolo per l\' asse radiale',                      // plots/plots.js:436
        'Compare data on hover': 'Paragona i dati al passaggio del mouse',                            // components/modebar/buttons.js:167
        'Double-click on legend to isolate one trace': 'Doppio click per isolare i dati di una traccia',  // components/legend/handle_click.js:90
        'Double-click to zoom back out': 'Doppio click per tornare allo zoom iniziale',                                  // plots/cartesian/dragbox.js:299
        'Download plot as a png': 'Scarica il grafico come immagine png',                                                       // components/modebar/buttons.js:52
        'Edit in Chart Studio': 'Modifica in Chart Studio',                                               // components/modebar/buttons.js:76
        'IE only supports svg.  Changing format to svg.': 'IE supporta solo svg.  Modifica formato in svg.', // components/modebar/buttons.js:60
        'Lasso Select': 'Selezione lazo',                                                                     // components/modebar/buttons.js:112
        'Orbital rotation': 'Rotazione orbitale',                                                              // components/modebar/buttons.js:279
        'Pan': 'Sposta',                                                                               // components/modebar/buttons.js:94
        'Produced with Plotly': 'Creato con Plotly',                                                      // components/modebar/modebar.js:256
        'Reset': 'Reset',                                                                            // components/modebar/buttons.js:432
        'Reset axes': 'Resetta gli assi',                                                                // components/modebar/buttons.js:148
        'Reset camera to default': 'Reimposta la camera ai valori predefiniti',                                      // components/modebar/buttons.js:314
        'Reset camera to last save': 'Reimposta la camera all\' ultimo salvataggio',                          // components/modebar/buttons.js:322
        'Reset view': 'Reimposta la vista',                                                               // components/modebar/buttons.js:583
        'Reset views': 'Reimposta le viste',                                                            // components/modebar/buttons.js:529
        'Show closest data on hover': 'Mostra i dati più vicini al passaggio del mouse',                                // components/modebar/buttons.js:157
        'Snapshot succeeded': 'Screenshot creato con successo',                                                       // components/modebar/buttons.js:66
        'Sorry, there was a problem downloading your snapshot!': 'Si è verificato un errore durante la creazione dello screenshot', // components/modebar/buttons.js:69
        'Taking snapshot - this may take a few seconds': 'Creazione screenshot - potrebbe richiedere qualche secondo', // components/modebar/buttons.js:57
        'Zoom': 'Zoom',                                                                                     // components/modebar/buttons.js:85
        'Zoom in': 'Ingrandisci',                                                                          // components/modebar/buttons.js:121
        'Zoom out': 'Rimpicciolisci',                                                                         // components/modebar/buttons.js:130
        'close:': 'chiudi:',                                                                               // traces/ohlc/transform.js:139
        'trace': 'traccia',                                                                               // plots/plots.js:439
        'lat:': 'lat.:',                                                                                    // traces/scattergeo/calc.js:48
        'lon:': 'lon.:',                                                                                    // traces/scattergeo/calc.js:49
        'q1:': 'q1:',                                                                                        // traces/box/calc.js:130
        'q3:': 'q3:',                                                                                        // traces/box/calc.js:131
        'source:': 'sorgente:',                                                                               // traces/sankey/plot.js:140
        'target:': 'target:',                                                                                 // traces/sankey/plot.js:141
        'max:': 'max.:',                                                                                    // traces/box/calc.js:132
        'mean ± σ:': 'media ± σ:',                                                                     // traces/box/calc.js:133
        'mean:': 'media:',                                                                             // traces/box/calc.js:133
        'median:': 'mediana:',                                                                               // traces/box/calc.js:128
        'min:': 'min.:',                                                                                    // traces/box/calc.js:129
        'new text:': 'Nuovo testo:',                                                                                    // plots/plots.js:327
        'upper fence:': 'limite superiore:',                                                                                    // traces/box/calc.js:129
        'lower fence:': 'limite inferiore:',                                                                                    // traces/box/calc.js:129
        'Turntable rotation': 'Rotazione piattaforma',                                                          // components/modebar/buttons.js:288
        'Toggle Spike Lines': 'Abilita linee di identificazione',                                   // components/modebar/buttons.js:548
        'open:': 'apri:',                                                                              // traces/ohlc/transform.js:136
        'high:': 'alto:',                                                                             // traces/ohlc/transform.js:137
        'kde:': 'kde:',                                                                              // traces/violin/calc.js:73
        'low:': 'basso:',                                                                              // traces/ohlc/transform.js:138
        'incoming flow count:': 'Flusso in entrata:',                                                // traces/sankey/plot.js:142
        'outgoing flow count:': 'Flusso in uscita:',                                                // traces/sankey/plot.js:143
        'Toggle show closest data on hover': 'Abilita mostra i dati più vicini al passaggio del mouse',                   // components/modebar/buttons.js:353
    },
    format: {
        days: [
            'Domenica', 'Lunedì', 'Martedì', 'Mercoledì',
            'Giovedì', 'Venerdì', 'Sabato'
        ],
        shortDays: ['Dom', 'Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab'],
        months: [
            'Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno',
            'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre'
        ],
        shortMonths: [
            'Gen', 'Feb', 'Mar', 'Apr', 'Mag', 'Giu',
            'Lug', 'Ago', 'Set', 'Ott', 'Nov', 'Dic'
        ],
        date: '%d/%m/%Y'
    }
};
