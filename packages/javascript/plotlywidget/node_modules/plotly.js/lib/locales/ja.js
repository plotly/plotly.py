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
    name: 'ja',
    dictionary: {
        'Autoscale': '自動ズーム',                                                                         // components/modebar/buttons.js:139
        'Box Select': '矩形選択',                                                                          // components/modebar/buttons.js:103
        'Click to enter Colorscale title': '色スケールタイトルを入力するにはクリック',                     // plots/plots.js:437
        'Click to enter Component A title': 'コンポーネントAのタイトル入力するにはクリック',               // plots/ternary/ternary.js:386
        'Click to enter Component B title': 'コンポーネントBのタイトル入力するにはクリック',               // plots/ternary/ternary.js:400
        'Click to enter Component C title': 'コンポーネントCのタイトル入力するにはクリック',               // plots/ternary/ternary.js:411
        'Click to enter Plot title': 'プロットタイトルを入力するにはクリック',                             // plot_api/plot_api.js:579
        'Click to enter X axis title': 'X軸タイトルを入力するにはクリック',                                // plots/plots.js:435
        'Click to enter Y axis title': 'Y軸タイトルを入力するにはクリック',                                // plots/plots.js:436
        'Compare data on hover': 'ホバー中のデータを比較',                                                 // components/modebar/buttons.js:167
        'Double-click on legend to isolate one trace': '凡例をダブルクリックして1つのトレースを無効化します', // components/legend/handle_click.js:90
        'Double-click to zoom back out': 'ダブルクリックでズームを戻します',                               // plots/cartesian/dragbox.js:299
        'Download plot as a png': 'PNGファイルでダウンロード',                                             // components/modebar/buttons.js:52
        'Edit in Chart Studio': 'Chart Studioで編集',                                                      // components/modebar/buttons.js:76
        'IE only supports svg.  Changing format to svg.': 'IEはSVGのみサポートしています。SVGに変換します。', // components/modebar/buttons.js:60
        'Lasso Select': '投げ縄選択',                                                                      // components/modebar/buttons.js:112
        'Orbital rotation': '軌道回転',                                                                    // components/modebar/buttons.js:279
        'Pan': '拡大',                                                                                     // components/modebar/buttons.js:94
        'Produced with Plotly': 'Plotlyにより作成',                                                        // components/modebar/modebar.js:256
        'Reset': 'リセット',                                                                                // components/modebar/buttons.js:432
        'Reset axes': '軸をリセット',                                                                       // components/modebar/buttons.js:148
        'Reset camera to default': 'カメラをデフォルトに戻す',                                              // components/modebar/buttons.js:314
        'Reset camera to last save': 'カメラを最後の保存状態に戻す',                                        // components/modebar/buttons.js:322
        'Reset view': 'ビューをリセット',                                                                   // components/modebar/buttons.js:583
        'Reset views': 'ビューをリセット',                                                                  // components/modebar/buttons.js:529
        'Show closest data on hover': 'ホバー時に一番近いデータを表示',                                     // components/modebar/buttons.js:157
        'Snapshot succeeded': 'スナップショットに成功',                                                     // components/modebar/buttons.js:66
        'Sorry, there was a problem downloading your snapshot!': 'すみません、スナップショットダウンロードでエラーです!', // components/modebar/buttons.js:69
        'Taking snapshot - this may take a few seconds': 'スナップショットを撮影',                          // components/modebar/buttons.js:57
        'Zoom': 'ズーム',                                                                                   // components/modebar/buttons.js:85
        'Zoom in': '拡大',                                                                                  // components/modebar/buttons.js:121
        'Zoom out': '縮小',                                                                                 // components/modebar/buttons.js:130
        'close:': '閉じる:',                                                                                // traces/ohlc/transform.js:139
        'trace': 'トレース:',                                                                               // plots/plots.js:439
        'lat:': '緯度:',                                                                                    // traces/scattergeo/calc.js:48
        'lon:': '経度:',                                                                                    // traces/scattergeo/calc.js:49
        'q1:': '第一四分位数:',                                                                                       // traces/box/calc.js:130
        'q3:': '第三四分位数:',                                                                                       // traces/box/calc.js:131
        'source:': 'ソース:',                                                                               // traces/sankey/plot.js:140
        'target:': 'ターゲット:',                                                                            // traces/sankey/plot.js:141
        'lower fence:': 'フェンス下限:',                                                                     // traces/box/calc.js:134
        'upper fence:': 'フェンス上限:',                                                                     // traces/box/calc.js:135
        'max:': '最大:',                                                                                    // traces/box/calc.js:132
        'mean ± σ:': '平均 ± σ:',                                                                       // traces/box/calc.js:133
        'mean:': '平均:',                                                                                   // traces/box/calc.js:133
        'median:': '中央値:',                                                                               // traces/box/calc.js:128
        'min:': '最小:',                                                                                  // traces/box/calc.js:129
        'Turntable rotation': '軸回転:',                                                                    // components/modebar/buttons.js:288
        'Toggle Spike Lines': 'スパイクラインのオンオフ',                                                   // components/modebar/buttons.js:548
        'open:': '開く:',                                                                                   // traces/ohlc/transform.js:136
        'high:': '高:',                                                                                     // traces/ohlc/transform.js:137
        'low:': '低:',                                                                                      // traces/ohlc/transform.js:138
        'Toggle show closest data on hover': 'ホバー時に一番近いデータを表示のオンオフ',                          // components/modebar/buttons.js:353
        'incoming flow count:': '流入フローカウント:',                                                      // traces/sankey/plot.js:142
        'outgoing flow count:': '流出フローカウント:',                                                      // traces/sankey/plot.js:143
        'kde:': 'kde:',                                                                                     // traces/violin/calc.js:73
        'Click to enter radial axis title': '放射軸タイトルを入力するにはクリック',
        'new text': '新規テキスト'
    },
    format: {
        days: ['日曜日', '月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日'],
        shortDays: ['日', '月', '火', '水', '木', '金', '土'],
        months: [
            '1月', '2月', '3月', '4月', '5月', '6月',
            '7月', '8月', '9月', '10月', '11月', '12月'
        ],
        shortMonths: [
            '1月', '2月', '3月', '4月', '5月', '6月',
            '7月', '8月', '9月', '10月', '11月', '12月'
        ],
        date: '%Y/%m/%d'
    }
};
