"use strict"

var vectorizeText = require("vectorize-text")

module.exports = getGlyph

var GLYPH_CACHE = {}

function getGlyph(symbol, font, pixelRatio) {
  var fontCache = GLYPH_CACHE[font]
  if(!fontCache) {
    fontCache = GLYPH_CACHE[font] = {}
  }
  if(symbol in fontCache) {
    return fontCache[symbol]
  }

  var config = {
    textAlign: "center",
    textBaseline: "middle",
    lineHeight: 1.0,
    font: font,
    lineSpacing: 1.25,
    styletags: {
      breaklines:true,
      bolds: true,
      italics: true,
      subscripts:true,
      superscripts:true
    }
  }

  //Get line and triangle meshes for glyph
  config.triangles = true
  var triSymbol = vectorizeText(symbol, config)
  config.triangles = false
  var lineSymbol = vectorizeText(symbol, config)

  var i, j

  if(pixelRatio && pixelRatio !== 1) {
    for(i = 0; i < triSymbol.positions.length; ++i){
      for(j = 0; j < triSymbol.positions[i].length; ++j){
        triSymbol.positions[i][j] /= pixelRatio;
      }
    }

    for(i = 0; i < lineSymbol.positions.length; ++i){
      for(j = 0; j < lineSymbol.positions[i].length; ++j){
        lineSymbol.positions[i][j] /= pixelRatio;
      }
    }
  }

  //Calculate bounding box
  var bounds = [[Infinity,Infinity], [-Infinity,-Infinity]]
  var n = lineSymbol.positions.length
  for(i = 0; i < n; ++i) {
    var p = lineSymbol.positions[i]
    for(j=0; j<2; ++j) {
      bounds[0][j] = Math.min(bounds[0][j], p[j])
      bounds[1][j] = Math.max(bounds[1][j], p[j])
    }
  }

  //Save cached symbol
  return fontCache[symbol] = [triSymbol, lineSymbol, bounds]
}