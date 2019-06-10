const regl = require('regl')({ extensions: 'oes_element_index_uint' })
const createMatrix = require('../')

let splom = createMatrix(regl)

splom.update({
  data: [
    [0, 1, 2, 3, 4, 5, 10],
    [0, 1, 2, 3, 4, 5, 10],
    [0, 1, 2, 3, 4, 5, 10]
  ],
  ranges: [
    [0, 10],
    [0, 10],
    [0, 10]
  ],
  domain: [
    [0, 0, 0.333, 0.333],
    [0.3333, 0.3333, 0.66666, 0.66666],
    [0.66666, 0.66666, 1, 1]
  ],
  // domain: [
  //   [0, 0, 0.5, null],
  //   [0.5, 0, 1, 0.5],
  //   [null, 0.5, 1, 1]
  // ],
  adjustDomain: true,
  diagonal: false,
  lower: false
})

splom.draw()

splom.destroy()




// adjust domain when only half is visible
// if (!trace.diagonal && (!trace.upper || !trace.lower) && trace.adjust) {
//   let shift = 1 / trace.domain.length
//   if (trace.upper) {
//     trace.domain.forEach((d, i) => {
//       d[1] = (d[1] - shift) / (1 - shift)
//       d[3] = (d[3] - shift) / (1 - shift)
//       d[0] = (d[0]) / (1 - shift)
//       d[2] = (d[2]) / (1 - shift)
//     })
//   }
//   else if (trace.lower) {
//     trace.domain.forEach((d, i) => {
//       d[1] = (d[1]) / (1 - shift)
//       d[3] = (d[3]) / (1 - shift)
//       d[0] = (d[0] - shift) / (1 - shift)
//       d[2] = (d[2] - shift) / (1 - shift)
//     })
//   }
// }
