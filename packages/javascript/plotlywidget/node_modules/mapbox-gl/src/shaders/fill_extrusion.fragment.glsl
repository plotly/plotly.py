varying vec4 v_color;
#pragma mapbox: define lowp float base
#pragma mapbox: define lowp float height
#pragma mapbox: define highp vec4 color

void main() {
    #pragma mapbox: initialize lowp float base
    #pragma mapbox: initialize lowp float height
    #pragma mapbox: initialize highp vec4 color

    gl_FragColor = v_color;

#ifdef OVERDRAW_INSPECTOR
    gl_FragColor = vec4(1.0);
#endif
}
