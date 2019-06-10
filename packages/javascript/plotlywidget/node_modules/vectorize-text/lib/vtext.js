module.exports = vectorizeText
module.exports.processPixels = processPixels

var surfaceNets = require('surface-nets')
var ndarray = require('ndarray')
var simplify = require('simplify-planar-graph')
var cleanPSLG = require('clean-pslg')
var cdt2d = require('cdt2d')
var toPolygonCrappy = require('planar-graph-to-polyline')

var TAG_bold = "b"
var CHR_bold = 'b|'

var TAG_italic = "i"
var CHR_italic = 'i|'

var TAG_super = "sup"
var CHR_super0 = '+'
var CHR_super = '+1'

var TAG_sub = "sub"
var CHR_sub0 = '-'
var CHR_sub = '-1'

function parseTag(tag, TAG_CHR, str, map) {

  var opnTag =  "<"  + tag + ">"
  var clsTag =  "</" + tag + ">"

  var nOPN = opnTag.length
  var nCLS = clsTag.length

  var isRecursive = (TAG_CHR[0] === CHR_super0) ||
                    (TAG_CHR[0] === CHR_sub0);

  var a = 0
  var b = -nCLS
  while (a > -1) {
    a = str.indexOf(opnTag, a)
    if(a === -1) break

    b = str.indexOf(clsTag, a + nOPN)
    if(b === -1) break

    if(b <= a) break

    for(var i = a; i < b + nCLS; ++i){
      if((i < a + nOPN) || (i >= b)) {
        map[i] = null
        str = str.substr(0, i) + " " + str.substr(i + 1)
      } else {
        if(map[i] !== null) {
          var pos = map[i].indexOf(TAG_CHR[0])
          if(pos === -1) {
            map[i] += TAG_CHR
          } else { // i.e. to handle multiple sub/super-scripts
            if(isRecursive) {
              // i.e to increase the sub/sup number
              map[i] = map[i].substr(0, pos + 1) + (1 + parseInt(map[i][pos + 1])) + map[i].substr(pos + 2)
            }
          }
        }
      }
    }

    var start = a + nOPN
    var remainingStr = str.substr(start, b - start)

    var c = remainingStr.indexOf(opnTag)
    if(c !== -1) a = c
    else a = b + nCLS
  }

  return map
}

function transformPositions(positions, options, size) {
  var align = options.textAlign || "start"
  var baseline = options.textBaseline || "alphabetic"

  var lo = [1<<30, 1<<30]
  var hi = [0,0]
  var n = positions.length
  for(var i=0; i<n; ++i) {
    var p = positions[i]
    for(var j=0; j<2; ++j) {
      lo[j] = Math.min(lo[j], p[j])|0
      hi[j] = Math.max(hi[j], p[j])|0
    }
  }

  var xShift = 0
  switch(align) {
    case "center":
      xShift = -0.5 * (lo[0] + hi[0])
    break

    case "right":
    case "end":
      xShift = -hi[0]
    break

    case "left":
    case "start":
      xShift = -lo[0]
    break

    default:
      throw new Error("vectorize-text: Unrecognized textAlign: '" + align + "'")
  }

  var yShift = 0
  switch(baseline) {
    case "hanging":
    case "top":
      yShift = -lo[1]
    break

    case "middle":
      yShift = -0.5 * (lo[1] + hi[1])
    break

    case "alphabetic":
    case "ideographic":
      yShift = -3 * size
    break

    case "bottom":
      yShift = -hi[1]
    break

    default:
      throw new Error("vectorize-text: Unrecoginized textBaseline: '" + baseline + "'")
  }

  var scale = 1.0 / size
  if("lineHeight" in options) {
    scale *= +options.lineHeight
  } else if("width" in options) {
    scale = options.width / (hi[0] - lo[0])
  } else if("height" in options) {
    scale = options.height / (hi[1] - lo[1])
  }

  return positions.map(function(p) {
    return [ scale * (p[0] + xShift), scale * (p[1] + yShift) ]
  })
}

function getPixels(canvas, context, rawString, fontSize, lineSpacing, styletags) {

  rawString = rawString.replace(/\n/g, '') // don't accept \n in the input

  if(styletags.breaklines === true) {
    rawString = rawString.replace(/\<br\>/g, '\n') // replace <br> tags with \n in the string
  } else {
    rawString = rawString.replace(/\<br\>/g, ' ') // don't accept <br> tags in the input and replace with space in this case
  }

  var activeStyle = ""
  var map = []
  for(j = 0; j < rawString.length; ++j) {
    map[j] = activeStyle
  }

  if(styletags.bolds === true) map = parseTag(TAG_bold, CHR_bold, rawString, map)
  if(styletags.italics === true) map = parseTag(TAG_italic, CHR_italic, rawString, map)
  if(styletags.superscripts === true) map = parseTag(TAG_super, CHR_super, rawString, map)
  if(styletags.subscripts === true) map = parseTag(TAG_sub, CHR_sub, rawString, map)

  var allStyles = []
  var plainText = ""
  for(j = 0; j < rawString.length; ++j) {
    if(map[j] !== null) {
      plainText += rawString[j]
      allStyles.push(map[j])
    }
  }

  var allTexts = plainText.split('\n')

  var numberOfLines = allTexts.length
  var lineHeight = Math.round(lineSpacing * fontSize)
  var offsetX = fontSize
  var offsetY = fontSize * 2
  var maxWidth = 0
  var minHeight = numberOfLines * lineHeight + offsetY

  if(canvas.height < minHeight) {
    canvas.height = minHeight
  }

  context.fillStyle = "#000"
  context.fillRect(0, 0, canvas.width, canvas.height)

  context.fillStyle = "#fff"
  var i, j, xPos, yPos, zPos
  var nDone = 0

  var buffer = ""
  function writeBuffer() {
    if(buffer !== "") {
      var delta = context.measureText(buffer).width

      context.fillText(buffer, offsetX + xPos, offsetY + yPos)
      xPos += delta
    }
  }

  function getTextFontSize() {
    return "" + Math.round(zPos) + "px ";
  }

  function changeStyle(oldStyle, newStyle) {
    var ctxFont = "" + context.font;

    if(styletags.subscripts === true) {
      var oldIndex_Sub = oldStyle.indexOf(CHR_sub0);
      var newIndex_Sub = newStyle.indexOf(CHR_sub0);

      var oldSub = (oldIndex_Sub > -1) ? parseInt(oldStyle[1 + oldIndex_Sub]) : 0;
      var newSub = (newIndex_Sub > -1) ? parseInt(newStyle[1 + newIndex_Sub]) : 0;

      if(oldSub !== newSub) {
        ctxFont = ctxFont.replace(getTextFontSize(), "?px ")
        zPos *= Math.pow(0.75, (newSub - oldSub))
        ctxFont = ctxFont.replace("?px ", getTextFontSize())
      }
      yPos += 0.25 * lineHeight * (newSub - oldSub);
    }

    if(styletags.superscripts === true) {
      var oldIndex_Super = oldStyle.indexOf(CHR_super0);
      var newIndex_Super = newStyle.indexOf(CHR_super0);

      var oldSuper = (oldIndex_Super > -1) ? parseInt(oldStyle[1 + oldIndex_Super]) : 0;
      var newSuper = (newIndex_Super > -1) ? parseInt(newStyle[1 + newIndex_Super]) : 0;

      if(oldSuper !== newSuper) {
        ctxFont = ctxFont.replace(getTextFontSize(), "?px ")
        zPos *= Math.pow(0.75, (newSuper - oldSuper))
        ctxFont = ctxFont.replace("?px ", getTextFontSize())
      }
      yPos -= 0.25 * lineHeight * (newSuper - oldSuper);
    }

    if(styletags.bolds === true) {
      var wasBold = (oldStyle.indexOf(CHR_bold) > -1)
      var is_Bold = (newStyle.indexOf(CHR_bold) > -1)

      if(!wasBold && is_Bold) {
        if(wasItalic) {
          ctxFont = ctxFont.replace("italic ", "italic bold ")
        } else {
          ctxFont = "bold " + ctxFont
        }
      }
      if(wasBold && !is_Bold) {
        ctxFont = ctxFont.replace("bold ", '')
      }
    }

    if(styletags.italics === true) {
      var wasItalic = (oldStyle.indexOf(CHR_italic) > -1)
      var is_Italic = (newStyle.indexOf(CHR_italic) > -1)

      if(!wasItalic && is_Italic) {
        ctxFont = "italic " + ctxFont
      }
      if(wasItalic && !is_Italic) {
        ctxFont = ctxFont.replace("italic ", '')
      }
    }
    context.font = ctxFont
  }

  for(i = 0; i < numberOfLines; ++i) {
    var txt = allTexts[i] + '\n'
    xPos = 0
    yPos = i * lineHeight
    zPos = fontSize

    buffer = ""
    
    for(j = 0; j < txt.length; ++j) {
      var style = (j + nDone < allStyles.length) ? allStyles[j + nDone] : allStyles[allStyles.length - 1]
      if(activeStyle === style) {
        buffer += txt[j]
      } else {
        writeBuffer()
        buffer = txt[j]

        if(style !== undefined) {
          changeStyle(activeStyle, style)
          activeStyle = style
        }
      }
    }
    writeBuffer()

    nDone += txt.length

    var width = Math.round(xPos + 2 * offsetX) | 0
    if(maxWidth < width) maxWidth = width
  }

  //Cut pixels from image
  var xCut = maxWidth
  var yCut = offsetY + lineHeight * numberOfLines
  var pixels = ndarray(context.getImageData(0, 0, xCut, yCut).data, [yCut, xCut, 4])
  return pixels.pick(-1, -1, 0).transpose(1, 0)
}

function getContour(pixels, doSimplify) {
  var contour = surfaceNets(pixels, 128)
  if(doSimplify) {
    return simplify(contour.cells, contour.positions, 0.25)
  }
  return {
    edges: contour.cells,
    positions: contour.positions
  }
}

function processPixelsImpl(pixels, options, size, simplify) {
  //Extract contour
  var contour = getContour(pixels, simplify)

  //Apply warp to positions
  var positions = transformPositions(contour.positions, options, size)
  var edges     = contour.edges
  var flip = "ccw" === options.orientation

  //Clean up the PSLG, resolve self intersections, etc.
  cleanPSLG(positions, edges)

  //If triangulate flag passed, triangulate the result
  if(options.polygons || options.polygon || options.polyline) {
    var result = toPolygonCrappy(edges, positions)
    var nresult = new Array(result.length)
    for(var i=0; i<result.length; ++i) {
      var loops = result[i]
      var nloops = new Array(loops.length)
      for(var j=0; j<loops.length; ++j) {
        var loop = loops[j]
        var nloop = new Array(loop.length)
        for(var k=0; k<loop.length; ++k) {
          nloop[k] = positions[loop[k]].slice()
        }
        if(flip) {
          nloop.reverse()
        }
        nloops[j] = nloop
      }
      nresult[i] = nloops
    }
    return nresult
  } else if(options.triangles || options.triangulate || options.triangle) {
    return {
      cells: cdt2d(positions, edges, {
        delaunay: false,
        exterior: false,
        interior: true
      }),
      positions: positions
    }
  } else {
    return {
      edges:     edges,
      positions: positions
    }
  }
}

function processPixels(pixels, options, size) {
  try {
    return processPixelsImpl(pixels, options, size, true)
  } catch(e) {}
  try {
    return processPixelsImpl(pixels, options, size, false)
  } catch(e) {}
  if(options.polygons || options.polyline || options.polygon) {
    return []
  }
  if(options.triangles || options.triangulate || options.triangle) {
    return {
      cells: [],
      positions: []
    }
  }
  return {
    edges: [],
    positions: []
  }
}

function vectorizeText(str, canvas, context, options) {
  var size = 64
  var lineSpacing = 1.25
  var styletags = {
    breaklines: false,
    bolds: false,
    italics: false,
    subscripts: false,
    superscripts: false
  }

  if(options) {

    if(options.size &&
       options.size > 0) size =
       options.size

    if(options.lineSpacing &&
       options.lineSpacing > 0) lineSpacing =
       options.lineSpacing

    if(options.styletags &&
       options.styletags.breaklines) styletags.breaklines =
       options.styletags.breaklines ? true : false

    if(options.styletags &&
       options.styletags.bolds) styletags.bolds =
       options.styletags.bolds ? true : false

    if(options.styletags &&
       options.styletags.italics) styletags.italics =
       options.styletags.italics ? true : false

    if(options.styletags &&
       options.styletags.subscripts) styletags.subscripts =
       options.styletags.subscripts ? true : false

    if(options.styletags &&
       options.styletags.superscripts) styletags.superscripts =
       options.styletags.superscripts ? true : false
  }

  context.font = [
    options.fontStyle,
    options.fontVariant,
    options.fontWeight,
    size + "px",
    options.font
  ].filter(function(d) {return d}).join(" ")
  context.textAlign = "start"
  context.textBaseline = "alphabetic"
  context.direction = "ltr"

  var pixels = getPixels(canvas, context, str, size, lineSpacing, styletags)

  return processPixels(pixels, options, size)
}
