/**
 * @module color-space/hsp
 */
'use strict'

var rgb = require('./rgb'),
  Pr = 0.299,
  Pg = 0.587,
  Pb = 0.114;

module.exports = {
  name: 'hsp',
  min: [0, 0, 0],
  max: [360, 100, 255],
  channel: ['hue', 'saturation', 'perceived_brightness'],
  alias: ['HSP'],

  rgb: function (hsp) {
    var h = hsp[0]/360.0,
      s = hsp[1]/100.0,
      p = hsp[2],
      r, g, b, part,
      minOverMax = 1.0 - s;

    if (minOverMax > 0.0) {
      if (h < 1.0 / 6.0) { //  R>G>B
        h = 6.0 * (h - 0.0 / 6.0);
        part = 1.0 + h * (1.0 / minOverMax - 1.0);
        b = p / Math.sqrt(Pr / minOverMax / minOverMax + Pg * part * part + Pb);
        r = (b) / minOverMax;
        g = (b) + h * ((r) - (b));
      } else if (h < 2.0 / 6.0) { //  G>R>B
        h = 6.0 * (-h + 2.0 / 6.0);
        part = 1.0 + h * (1.0 / minOverMax - 1.0);
        b = p / Math.sqrt(Pg / minOverMax / minOverMax + Pr * part * part + Pb);
        g = (b) / minOverMax;
        r = (b) + h * ((g) - (b));
      } else if (h < 3.0 / 6.0) { //  G>B>R
        h = 6.0 * (h - 2.0 / 6.0);
        part = 1.0 + h * (1.0 / minOverMax - 1.0);
        r = p / Math.sqrt(Pg / minOverMax / minOverMax + Pb * part * part + Pr);
        g = (r) / minOverMax;
        b = (r) + h * ((g) - (r));
      } else if (h < 4.0 / 6.0) { //  B>G>R
        h = 6.0 * (-h + 4.0 / 6.0);
        part = 1.0 + h * (1.0 / minOverMax - 1.0);
        r = p / Math.sqrt(Pb / minOverMax / minOverMax + Pg * part * part + Pr);
        b = (r) / minOverMax;
        g = (r) + h * ((b) - (r));
      } else if (h < 5.0 / 6.0) { //  B>R>G
        h = 6.0 * (h - 4.0 / 6.0);
        part = 1.0 + h * (1.0 / minOverMax - 1.0);
        g = p / Math.sqrt(Pb / minOverMax / minOverMax + Pr * part * part + Pg);
        b = (g) / minOverMax;
        r = (g) + h * ((b) - (g));
      } else { //  R>B>G
        h = 6.0 * (-h + 6.0 / 6.0);
        part = 1.0 + h * (1.0 / minOverMax - 1.0);
        g = p / Math.sqrt(Pr / minOverMax / minOverMax + Pb * part * part + Pg);
        r = (g) / minOverMax;
        b = (g) + h * ((r) - (g));
      }
    } else {
      if (h < 1.0 / 6.0) { //  R>G>B
        h = 6.0 * (h - 0.0 / 6.0);
        r = Math.sqrt(p * p / (Pr + Pg * h * h));
        g = (r) * h;
        b = 0.0;
      } else if (h < 2.0 / 6.0) { //  G>R>B
        h = 6.0 * (-h + 2.0 / 6.0);
        g = Math.sqrt(p * p / (Pg + Pr * h * h));
        r = (g) * h;
        b = 0.0;
      } else if (h < 3.0 / 6.0) { //  G>B>R
        h = 6.0 * (h - 2.0 / 6.0);
        g = Math.sqrt(p * p / (Pg + Pb * h * h));
        b = (g) * h;
        r = 0.0;
      } else if (h < 4.0 / 6.0) { //  B>G>R
        h = 6.0 * (-h + 4.0 / 6.0);
        b = Math.sqrt(p * p / (Pb + Pg * h * h));
        g = (b) * h;
        r = 0.0;
      } else if (h < 5.0 / 6.0) { //  B>R>G
        h = 6.0 * (h - 4.0 / 6.0);
        b = Math.sqrt(p * p / (Pb + Pr * h * h));
        r = (b) * h;
        g = 0.0;
      } else { //  R>B>G
        h = 6.0 * (-h + 6.0 / 6.0);
        r = Math.sqrt(p * p / (Pr + Pb * h * h));
        b = (r) * h;
        g = 0.0;
      }
    }

	return [Math.round(r), Math.round(g), Math.round(b)];
  }

  
};


//append rgb
rgb.hsp = function (rgb) {
  var r = parseInt(rgb[0], 10),
    g = parseInt(rgb[1], 10),
    b = parseInt(rgb[2], 10),
    h, s, p;

  //  Calculate the Perceived brightness
  p = Math.sqrt(r * r * Pr + g * g * Pg + b * b * Pb);

  //  Calculate the Hue and Saturation
  if (r === g && r === b) {
    h = 0.0;
    s = 0.0;
  } else {    
    //  R is largest
    if (r >= g && r >= b) {
      if (b >= g) {
        h = 6.0 / 6.0 - 1.0 / 6.0 * (b - g) / (r - g);
        s = 1.0 - g / r;
      } else {
        h = 0.0 / 6.0 + 1.0 / 6.0 * (g - b) / (r - b);
        s = 1.0 - b / r;
      }
    }

    // G is largest
    if (g >= r && g >= b) {
      if (r >= b) {
        h = 2.0 / 6.0 - 1.0 / 6.0 * (r - b) / (g - b);
        s = 1 - b / g;
      } else {
        h = 2.0 / 6.0 + 1.0 / 6.0 * (b - r) / (g - r);
        s = 1.0 - r / g;
      }
    }

    // B is largest
    if (b >= r && b >= g) {
      if (g >= r) {
        h = 4.0 / 6.0 - 1.0 / 6.0 * (g - r) / (b - r);
        s = 1.0 - r / b;
      } else {
        h = 4.0 / 6.0 + 1.0 / 6.0 * (r - g) / (b - g);
        s = 1.0 - g / b;
      }
    }
  }
    
  return [Math.round(h*360.0), s*100.0, Math.round(p)];
};
