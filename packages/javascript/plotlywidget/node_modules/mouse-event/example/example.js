var mouse = require('../mouse')

var container = document.createElement('div')
container.style['background-color'] = '#f00'
container.style.width = '400px'
container.style.height = '400px'
container.innerHTML = '<p>Buttons: 0 x:0 y:0</p>'
document.body.appendChild(container)

container.onmousemove = function(ev) {
  container.innerHTML =
    '<p>Buttons: ' + mouse.buttons(ev) + 
    ' x:' + mouse.x(ev) + 
    ' y:' + mouse.y(ev) + '</p>'
}

window.oncontextmenu = function(ev) {
  ev.stopPropagation()
  ev.preventDefault()
  return false
}