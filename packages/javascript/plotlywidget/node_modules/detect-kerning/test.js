'use strict'

let kerning = require('./')
let a = require('assert')
let r = require('round-to')

let table = {
	'A”': -146,
	'W.': -144,
	'P,': -139,
	'L”': -135,
	'VA': -123,
	'F.': -110,
	'YA': -104,
	'Te': -98,
	'AV': -97,
	'Vr': -86,
	'PA': -85,
	'm”': -82,
	'a”': -79,
	'FA': -78,
	'UA': -78,
	'w.': -73,
	'Yt': -72,
	'LT': -64,
	'r,': -63,
	'Xv': -54,
	'Ku': -46,
	'D,': -40,
	'D”': -36,
	'OA': -36,
	'Hv': -33,
	'T:': -32,
	'DY': -30,
	'c”': -25,
	'my': -23,
	'Ru': -21,
	'aj': -19,
	'bv': -16,
	'Sp': -14,
	'ro': -13,
	'SR': -12,
	'lp': -12,
	'ot': -11,
	'tt': -10,
	'am': -9,
	'fe': -9,
	'vo': -8,
	'xc': -8,
	'yo': -8,
	'Ix': -6,
	'e,': -6,
	'st': -5,
	'he': -4,
	'Fw': -3,
	'us': -3,
	'Ak': +3,
	'la': +3,
	'Oj': +5,
	'il': +5,
	'CO': +7,
	'bc': +9,
	'Xf': +10,
	'fr': +10,
	'F”': +12,
	'wb': +12,
	'YW': +13,
	'So': +14,
	'Co': +15,
	'VT': +16,
	'cv': +16,
	'Dv': +17,
	'OC': +18,
	'Bc': +20,
	'RX': +20,
	'T”': +22,
	'gy': +24,
	'r:': +24,
	'XA': +25,
	'ry': +29,
	'w;': +31,
	'f?': +76,
	'f”': 121
}

console.time(1)
let minionTable = kerning(['Minion Pro', 'sans-serif'])
console.timeEnd(1)
console.log(Object.keys(minionTable))

for (let pair in table) {
	if (minionTable[pair]) a.equal(table[pair], r(minionTable[pair], 2), 'Pair: `'+ pair + '`')
}
