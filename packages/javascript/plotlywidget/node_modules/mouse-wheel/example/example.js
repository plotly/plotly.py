'use strict'

var totalX = (window.innerWidth/2)|0, totalY = (window.innerHeight/2)|0

var box = document.createElement('div')
box.style.position = 'absolute'
box.style.width = '20px'
box.style.height = '20px'
box.style.left = totalX + 'px'
box.style.top = totalY + 'px'
box.style['background-color'] = '#f00'
box.style['z-index'] = 10
document.body.appendChild(box)

var infoLog = document.createElement('div')
infoLog.innerHTML = 'Scroll to move box'
document.body.appendChild(infoLog)

require('../wheel')(function(dx, dy) {
  totalX -= dx
  totalY -= dy
  box.style.left = totalX + 'px'
  box.style.top = totalY + 'px'
  infoLog.innerHTML = 
    '<p>Scroll:' + dx + ',' + dy + ' - ' + 
    totalX + ',' + totalY + '</p>'
}, true)