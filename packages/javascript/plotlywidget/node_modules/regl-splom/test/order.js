const regl = require('regl')({ extensions: 'oes_element_index_uint' })
const createMatrix = require('../')


// create splom instance
let splom = createMatrix(regl)

splom.update({
  data: [
    [1, 2, 3],
    [4, 6, 8]
  ],
  ranges: [
    [0, 10],
    [0, 10]
  ]
})

splom.draw()
