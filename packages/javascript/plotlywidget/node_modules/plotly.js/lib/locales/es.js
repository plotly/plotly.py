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
    name: 'es',
    dictionary: {
        'Autoscale': 'Autoescalar',                                   // components/modebar/buttons.js:139
        'Box Select': 'Seleccionar Caja',                             // components/modebar/buttons.js:103
        'Click to enter Colorscale title': 'Introducir el título de la Escala de Color', // plots/plots.js:303
        'Click to enter Component A title': 'Introducir el título del Componente A', // plots/ternary/ternary.js:392
        'Click to enter Component B title': 'Introducir el título del Componente B', // plots/ternary/ternary.js:406
        'Click to enter Component C title': 'Introducir el título del Componente C', // plots/ternary/ternary.js:417
        'Click to enter Plot title': 'Introducir el título de la Gráfica', // plot_api/plot_api.js:579
        'Click to enter X axis title': 'Introducir el título del eje X', // plots/plots.js:301
        'Click to enter Y axis title': 'Introducir el título del eje Y', // plots/plots.js:302
        'Click to enter radial axis title': 'Introducir el título del eje radial',
        'Compare data on hover': 'Comparar datos al pasar por encima', // components/modebar/buttons.js:167
        'Double-click on legend to isolate one trace': 'Haga doble-clic en la leyenda para aislar una traza', // components/legend/handle_click.js:90
        'Double-click to zoom back out': 'Haga doble-clic para restaurar la escala', // plots/cartesian/dragbox.js:335
        'Download plot as a png': 'Descargar gráfica como png',       // components/modebar/buttons.js:52
        'Edit in Chart Studio': 'Editar en Chart Studio',             // components/modebar/buttons.js:76
        'IE only supports svg.  Changing format to svg.': 'IE solo soporta svg. Cambiando formato a svg.', // components/modebar/buttons.js:60
        'Lasso Select': 'Seleccionar con lazo',                       // components/modebar/buttons.js:112
        'Orbital rotation': 'Rotación esférica',                      // components/modebar/buttons.js:279
        'Pan': 'Modo Panorámica',                                     // components/modebar/buttons.js:94
        'Produced with Plotly': 'Hecho con Plotly',                   // components/modebar/modebar.js:256
        'Reset': 'Reiniciar',                                         // components/modebar/buttons.js:431
        'Reset axes': 'Reiniciar ejes',                               // components/modebar/buttons.js:148
        'Reset camera to default': 'Restaurar cámara predeterminada', // components/modebar/buttons.js:313
        'Reset camera to last save': 'Restaurar anterior cámara',     // components/modebar/buttons.js:321
        'Reset view': 'Restaurar vista',                              // components/modebar/buttons.js:582
        'Reset views': 'Restaurar vistas',                            // components/modebar/buttons.js:528
        'Show closest data on hover': 'Mostrar el dato más cercano al pasar por encima', // components/modebar/buttons.js:157
        'Snapshot succeeded': 'La captura de la instantánea finalizó correctamente', // components/modebar/buttons.js:66
        'Sorry, there was a problem downloading your snapshot!': '¡La descarga de la instantánea falló!', // components/modebar/buttons.js:69
        'Taking snapshot - this may take a few seconds': 'Capturando una instantánea - podría tardar unos segundos', // components/modebar/buttons.js:57
        'Toggle Spike Lines': 'Mostrar/Ocultar Guías',                // components/modebar/buttons.js:547
        'Toggle show closest data on hover': 'Activar/Desactivar mostrar el dato más cercano al pasar por encima', // components/modebar/buttons.js:352
        'Turntable rotation': 'Rotación plana',                       // components/modebar/buttons.js:288
        'Zoom': 'Modo Ampliar/Reducir',                               // components/modebar/buttons.js:85
        'Zoom in': 'Ampliar',                                         // components/modebar/buttons.js:121
        'Zoom out': 'Reducir',                                        // components/modebar/buttons.js:130
        'close:': 'cierre:',                                          // traces/ohlc/transform.js:139
        'high:': 'alza:',                                             // traces/ohlc/transform.js:137
        'incoming flow count:': 'flujo de entrada:',                  // traces/sankey/plot.js:142
        'kde:': 'edp:',                                               // traces/violin/calc.js:73
        'lat:': 'lat:',                                               // traces/scattergeo/calc.js:48
        'lon:': 'lon:',                                               // traces/scattergeo/calc.js:49
        'low:': 'baja:',                                              // traces/ohlc/transform.js:138
        'lower fence:': 'límite inferior:',                           // traces/box/calc.js:134
        'max:': 'máx:',                                               // traces/box/calc.js:132
        'mean ± σ:': 'media ± σ:',                                    // traces/box/calc.js:133
        'mean:': 'media:',                                            // traces/box/calc.js:133
        'median:': 'mediana:',                                        // traces/box/calc.js:128
        'min:': 'mín:',                                               // traces/box/calc.js:129
        'new text': 'nuevo texto',
        'open:': 'apertura:',                                         // traces/ohlc/transform.js:136
        'outgoing flow count:': 'flujo de salida:',                   // traces/sankey/plot.js:143
        'q1:': 'q1:',                                                 // traces/box/calc.js:130
        'q3:': 'q3:',                                                 // traces/box/calc.js:131
        'source:': 'fuente:',                                         // traces/sankey/plot.js:140
        'target:': 'destino:',                                        // traces/sankey/plot.js:141
        'trace': 'traza',                                             // plots/plots.js:305
        'upper fence:': 'límite superior:'                            // traces/box/calc.js:135
    },
    format: {
        days: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
        shortDays: ['Dom', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'],
        months: [
            'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
            'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
        ],
        shortMonths: [
            'Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun',
            'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'
        ],
        date: '%d/%m/%Y',
        decimal: ',',
        thousands: ' '
    }
};
