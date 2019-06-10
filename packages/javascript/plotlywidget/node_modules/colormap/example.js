var cmap = require('.'),
    img = document.body.appendChild(document.createElement('img')),
    canvas = document.body.appendChild(document.createElement('canvas')),
    c = canvas.getContext('2d'),
    n = 48,
    colormaps = [
        'jet', 'hsv','hot','cool','spring','summer','autumn','winter','bone',
        'copper','greys','YIGnBu','greens','YIOrRd','bluered','RdBu','picnic',
        'rainbow','portland','blackbody','earth','electric',

        'viridis', 'inferno', 'magma', 'plasma', 'warm', 'cool', 'rainbow-soft',

        'bathymetry', 'cdom', 'chlorophyll', 'density', 'freesurface-blue', 'freesurface-red', 'oxygen', 'par', 'phase', 'salinity', 'temperature', 'turbidity', 'velocity-blue', 'velocity-green',

        'cubehelix'
    ];

img.width = 480;
img.onload = run;
img.src = './night.jpg'

function drawColorMaps (colormap, name, height) {
    /*
     * Build up the color ranges and add text
     */
    for (var j = 0; j < n; j++) {
        c.fillStyle = colormap[j];      // start ind at index 0
        c.fillRect(j*10, height, 10, 40);
    }
    c.fillStyle = '#262626';
    c.font = '16px Helvetica';
    c.fillText( name, n*10 + 10, height + 26);
}

function run() {
    var height, colormap;
    c.canvas.height = colormaps.length * 40 + img.height;
    c.canvas.width = 648;

    for (var i = 0; i < colormaps.length; i++) {
        height = i*40;
        colormap = cmap({
            colormap: colormaps[i],
            nshades: n,
            format: 'rgbaString'
        });
        drawColorMaps(colormap, colormaps[i], height);
    }

    /*
     * Now lets try some alpha maps overtop an image!
     */
    var ilast = i;
    c.drawImage(img, 0, i*40, 480, 240);

    // remove background img
    img.parentElement.removeChild(img);

    for (var i = 0; i < colormaps.length; i++) {
        height = (ilast + i)*40;
        colormap = cmap({
            colormap: colormaps[i],
            nshades: n,
            format: 'rgbaString',
            alpha: [0, 1]
        });
        drawColorMaps(colormap, colormaps[i] + ' with transparency', height);
    }
}
