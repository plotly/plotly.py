var widgets = require('@jupyter-widgets/base');
var _ = require('lodash');
var Plotly = require('plotly.js');


// Models
// ======
var FigureModel = widgets.DOMWidgetModel.extend({

    defaults: _.extend(widgets.DOMWidgetModel.prototype.defaults(), {
        _model_name: 'FigureModel',
        _view_name: 'FigureView',
        _model_module: 'ipyplotly',
        _view_module: 'ipyplotly',

        _data: [],
        _layout: {}, // Not synced to python side

        // Message properties
        _py2js_addTraces: null,
        _py2js_deleteTraces: null,
        _py2js_moveTraces: null,
        _py2js_restyle: null,
        _py2js_relayout: null,
        _py2js_update: null,
        _py2js_animate: null,

        _py2js_removeLayoutProps: null,
        _py2js_removeStyleProps: null,

        _py2js_requestSvg: null,

        // JS -> Python
        _js2py_restyle: null,
        _js2py_relayout: null,
        _js2py_update: null,

        _js2py_layoutDelta: null,
        _js2py_tracesDelta: null,

        // callbacks
        _js2py_pointsCallback: null,

        // svg
        _js2py_svg: null,

        // message tracking
        _last_relayout_msg_id: 0,
        _last_restyle_msg_id: 0
    }),

    initialize: function() {
        FigureModel.__super__.initialize.apply(this, arguments);
        console.log(['FigureModel: initialize', this._data, this._layout]);

        this.on('change:_py2js_addTraces', this.do_addTraces, this);
        this.on('change:_py2js_deleteTraces', this.do_deleteTraces, this);
        this.on('change:_py2js_moveTraces', this.do_moveTraces, this);
        this.on("change:_py2js_restyle", this.do_restyle, this);
        this.on("change:_py2js_relayout", this.do_relayout, this);
        this.on("change:_py2js_update", this.do_update, this);
        this.on("change:_py2js_animate", this.do_animate, this);
        this.on("change:_py2js_removeLayoutProps", this.do_removeLayoutProps, this);
        this.on("change:_py2js_removeStyleProps", this.do_removeStyleProps, this);
    },

    _str_to_dict_path: function (rawKey) {

        // Split string on periods. e.g. 'foo.bar[0]' -> ['foo', 'bar[0]']
        var keyPath = rawKey.split('.');
        var regex = /(.*)\[(\d+)\]/;

        // Split out bracket indexes. e.g. ['foo', 'bar[0]'] -> ['foo', 'bar', '0']
        var keyPath2 = [];
        for (var k = 0; k < keyPath.length; k++) {
            var key = keyPath[k];
            var match = regex.exec(key);
            if (match === null) {
                keyPath2.push(key);
            } else {
                keyPath2.push(match[1]);
                keyPath2.push(match[2]);
            }
        }

        // Convert elements to ints if possible. e.g. e.g. ['foo', 'bar', '0'] -> ['foo', 'bar', 0]
        for (k = 0; k < keyPath2.length; k++) {
            key = keyPath2[k];
            var potentialInt = parseInt(key);
            if (!isNaN(potentialInt)) {
                keyPath2[k] = potentialInt;
            }
        }
        return keyPath2
    },

    normalize_trace_indexes: function (trace_indexes) {
        if (trace_indexes === null || trace_indexes === undefined) {
            var numTraces = this.get('_data').length;
            trace_indexes = Array.apply(null, new Array(numTraces)).map(function (_, i) {return i;});
        }
        if (!Array.isArray(trace_indexes)) {
            // Make sure idx is an array
            trace_indexes = [trace_indexes];
        }
        return trace_indexes
    },


    do_addTraces: function () {
        // add trace to plot
        console.log('Figure Model: do_addTraces');
        var data = this.get('_py2js_addTraces');

        if (data !== null) {
            console.log(data);
            var tracesData = this.get('_data');
            _.forEach(data, function (traceData) {
                tracesData.push(traceData);
            })
        }
    },

    do_deleteTraces: function () {
        // add trace to plot
        var data = this.get('_py2js_deleteTraces');
        console.log('Figure Model: do_deleteTraces');
        if (data !== null) {
            var delete_inds = data['delete_inds'];
            var tracesData = this.get('_data');

            // Remove del inds in reverse order so indexes remain valid throughout loop
            delete_inds.slice().reverse().forEach(function (del_ind) {
                tracesData.splice(del_ind, 1);
            });
        }
    },

    do_moveTraces: function () {
        console.log('Figure Model: do_moveTraces');

        var move_data = this.get('_py2js_moveTraces');
        console.log('do_moveTraces');

        if (move_data !== null) {
            var currentInds = move_data[0];
            var newInds = move_data[1];
            var tracesData = this.get('_data');

            // ### Remove by curr_inds in reverse order ###
            var movingTracesData = [];
            for (var ci = currentInds.length - 1; ci >= 0; ci--) {
                // Insert moving tracesData at beginning of the list
                movingTracesData.splice(0, 0, tracesData[currentInds[ci]]);
                tracesData.splice(currentInds[ci], 1);
            }

            // ### Sort newInds and movingTracesData by newInds ###
            var newIndexSortedArrays = _(newInds).zip(movingTracesData)
                .sortBy(0)
                .unzip()
                .value();

            newInds = newIndexSortedArrays[0];
            movingTracesData = newIndexSortedArrays[1];

            // ### Insert by newInds in forward order ###
            for (var ni = 0; ni < newInds.length; ni++) {
                tracesData.splice(newInds[ni], 0, movingTracesData[ni]);
            }
        }
    },

    do_restyle: function () {
        console.log('FigureModel: do_restyle');
        var data = this.get('_py2js_restyle');
        if (data !== null) {
            var style = data[0];
            var trace_indexes = this.normalize_trace_indexes(data[1]);
            this._performRestyle(style, trace_indexes)
        }
    },

    _performRestyle: function (style, trace_indexes){

        for (var rawKey in style) {
            if (!style.hasOwnProperty(rawKey)) { continue }
            var v = style[rawKey];

            if (!Array.isArray(v)) {
                v = [v]
            }

            var keyPath = this._str_to_dict_path(rawKey);

            for (var i = 0; i < trace_indexes.length; i++) {
                var trace_ind = trace_indexes[i];
                var valParent = this.get('_data')[trace_ind];

                for (var kp = 0; kp < keyPath.length-1; kp++) {
                    var keyPathEl = keyPath[kp];

                    // Extend val_parent list if needed
                    if (Array.isArray(valParent)) {
                        if (typeof keyPathEl === 'number') {
                            while (valParent.length <= keyPathEl) {
                                valParent.push(null)
                            }
                        }
                    } else { // object
                        // Initialize child if needed
                        if (valParent[keyPathEl] === undefined) {
                            if (typeof keyPath[kp + 1] === 'number') {
                                valParent[keyPathEl] = []
                            } else {
                                valParent[keyPathEl] = {}
                            }
                        }
                    }
                    valParent = valParent[keyPathEl];
                }

                var lastKey = keyPath[keyPath.length-1];
                var trace_v = v[i % v.length];

                if (trace_v === undefined) {
                    // Nothing to do
                } else if (trace_v === null){
                    if(valParent.hasOwnProperty(lastKey)) {
                        delete valParent[lastKey];
                    }
                } else {
                    if (Array.isArray(valParent) && typeof lastKey === 'number') {
                        while (valParent.length <= lastKey) {
                            // Make sure array is long enough to assign into
                            valParent.push(null)
                        }
                    }
                    valParent[lastKey] = trace_v;
                }
            }
        }
    },

    do_relayout: function () {
        console.log('FigureModel: do_relayout');
        var data = this.get('_py2js_relayout');
        if (data !== null) {
            console.log(data);
            this._performRelayout(data);
            console.log(this.get('_layout'))
        }
    },

    _performRelayout: function (relayout_data) {
        this._performRelayoutLike(relayout_data, this.get('_layout'))
    },

    _performRelayoutLike: function (relayout_data, parent_data) {
        // Perform a relayout style operation on a given parent object
        for (var rawKey in relayout_data) {
            if (!relayout_data.hasOwnProperty(rawKey)) {
                continue
            }

            var v = relayout_data[rawKey];
            var keyPath = this._str_to_dict_path(rawKey);

            var valParent = parent_data;

            for (var kp = 0; kp < keyPath.length-1; kp++) {
                var keyPathEl = keyPath[kp];

                // Extend val_parent list if needed
                if (Array.isArray(valParent)) {
                    if(typeof keyPathEl === 'number') {
                        while (valParent.length <= keyPathEl) {
                            valParent.push(null)
                        }
                    }
                } else {
                    // Initialize child if needed
                    if (valParent[keyPathEl] === undefined) {
                        if (typeof keyPath[kp + 1] === 'number') {
                            valParent[keyPathEl] = []
                        } else {
                            valParent[keyPathEl] = {}
                        }
                    }
                }
                valParent = valParent[keyPathEl];
            }

            var lastKey = keyPath[keyPath.length-1];

            if (v === undefined) {
                // Nothing to do
            } else if (v === null){
                if(valParent.hasOwnProperty(lastKey)) {
                    delete valParent[lastKey];
                }
            } else {
                if (Array.isArray(valParent) && typeof lastKey === 'number') {
                    while (valParent.length <= lastKey) {
                        // Make sure array is long enough to assign into
                        valParent.push(null)
                    }
                }
                valParent[lastKey] = v;
            }
        }
    },

    do_update: function() {
        console.log('FigureModel: do_update');
        var data = this.get('_py2js_update');
        if (data !== null) {
            console.log(data);

            var style = data[0];
            var layout = data[1];
            var trace_indexes = this.normalize_trace_indexes(data[2]);
            this._performRestyle(style, trace_indexes);
            this._performRelayout(layout);
        }
    },

    do_animate: function () {
        console.log('FigureModel: do_animate');
        var data = this.get('_py2js_animate');
        if (data !== null) {
            console.log(data);
            var animationData = data[0];

            var styles = animationData['data'];
            var layout = animationData['layout'];
            var trace_indexes = this.normalize_trace_indexes(animationData['traces']);

            for (var i = 0; i < styles.length; i++) {
                var style = styles[i];
                var trace_index = trace_indexes[i];
                var trace = this.get('_data')[trace_index];
                this._performRelayoutLike(style, trace);
            }

            this._performRelayout(layout);
        }
    },

    // ### Remove props ###
    do_removeLayoutProps: function () {
        console.log('FigureModel:do_removeLayoutProps');
        var data = this.get('_py2js_removeLayoutProps');
        if (data !== null) {
            console.log(this.get('_layout'));
            for(var i=0; i < data.length; i++) {

                var keyPath = data[i];
                var valParent = this.get('_layout');

                for (var kp = 0; kp < keyPath.length - 1; kp++) {
                    var keyPathEl = keyPath[kp];
                    if (valParent[keyPathEl] === undefined) {
                        valParent = null;
                        break
                    }
                    valParent = valParent[keyPathEl];
                }
                if (valParent !== null) {
                    var lastKey = keyPath[keyPath.length - 1];
                    if (valParent.hasOwnProperty(lastKey)) {
                        delete valParent[lastKey];
                        console.log('Removed ' + keyPath)
                    }
                }
            }
            console.log(this.get('_layout'));
        }
    },

    do_removeStyleProps: function () {
        console.log('FigureModel:do_removeStyleProps');
        var data = this.get('_py2js_removeStyleProps');
        if (data !== null) {
            console.log(data);
            var keyPaths = data[0];
            var trace_indexes = this.normalize_trace_indexes(data[1]);

            for(var k=0; k < keyPaths.length; k++) {

                var keyPath = keyPaths[k];

                for (var i = 0; i < trace_indexes.length; i++) {
                    var trace_ind = trace_indexes[i];
                    var valParent = this.get('_data')[trace_ind];

                    for (var kp = 0; kp < keyPath.length - 1; kp++) {
                        var keyPathEl = keyPath[kp];
                        if (valParent[keyPathEl] === undefined) {
                            valParent = null;
                            break
                        }
                        valParent = valParent[keyPathEl];
                    }
                    if (valParent !== null) {
                        var lastKey = keyPath[keyPath.length - 1];
                        if (valParent.hasOwnProperty(lastKey)) {
                            delete valParent[lastKey];
                            console.log('Removed ' + keyPath)
                        }
                    }
                }
            }
        }
    }
}, {
    serializers: _.extend({
        _data: { deserialize: py2js_serializer, serialize: js2py_serializer},
        _layout: { deserialize: py2js_serializer, serialize: js2py_serializer},
        _py2js_addTraces: { deserialize: py2js_serializer, serialize: js2py_serializer},
        _py2js_deleteTraces: { deserialize: py2js_serializer, serialize: js2py_serializer},
        _py2js_moveTraces: { deserialize: py2js_serializer, serialize: js2py_serializer},
        _py2js_restyle: { deserialize: py2js_serializer, serialize: js2py_serializer},
        _py2js_relayout: { deserialize: py2js_serializer, serialize: js2py_serializer},
        _py2js_update: { deserialize: py2js_serializer, serialize: js2py_serializer},
        _py2js_animate: { deserialize: py2js_serializer, serialize: js2py_serializer},
        _py2js_removeLayoutProps: { deserialize: py2js_serializer, serialize: js2py_serializer},
        _py2js_removeStyleProps: { deserialize: py2js_serializer, serialize: js2py_serializer},
        _js2py_restyle: { deserialize: py2js_serializer, serialize: js2py_serializer},
        _js2py_relayout: { deserialize: py2js_serializer, serialize: js2py_serializer},
        _js2py_update: { deserialize: py2js_serializer, serialize: js2py_serializer},
        _js2py_layoutDelta: { deserialize: py2js_serializer, serialize: js2py_serializer},
        _js2py_tracesDelta: { deserialize: py2js_serializer, serialize: js2py_serializer},
        _js2py_pointsCallback: { deserialize: py2js_serializer, serialize: js2py_serializer},
    }, widgets.DOMWidgetModel.serializers)
});

var numpy_dtype_to_typedarray_type = {
    int8: Int8Array,
    int16: Int16Array,
    int32: Int32Array,
    uint8: Uint8Array,
    uint16: Uint16Array,
    uint32: Uint32Array,
    float32: Float32Array,
    float64: Float64Array
};

function js2py_serializer(v, widgetManager) {
    var res;
    if (Array.isArray(v)) {
        res = new Array(v.length);
        for (var i = 0; i < v.length; i++) {
            res[i] = js2py_serializer(v[i]);
        }
    } else if (_.isPlainObject(v)) {
        res = {};
        for (var p in v) {
            if (v.hasOwnProperty(p)) {
                res[p] = js2py_serializer(v[p]);
            }
        }
    } else if (v === undefined) {
        res = '_undefined_';
    } else {
        res = v;
    }
    return res
}

function py2js_serializer(v, widgetManager) {
    var res;
    if (Array.isArray(v)) {
        res = new Array(v.length);
        for (var i = 0; i < v.length; i++) {
            res[i] = py2js_serializer(v[i]);
        }
    } else if (_.isPlainObject(v)) {
        if (_.has(v, 'buffer') && _.has(v, 'dtype') && _.has(v, 'shape')) {
            var typedarray_type = numpy_dtype_to_typedarray_type[v.dtype];
            var typedarray = new typedarray_type(v.buffer.buffer);
            res = Array.from(typedarray);
        } else {
            res = {};
            for (var p in v) {
                if (v.hasOwnProperty(p)) {
                    res[p] = py2js_serializer(v[p]);
                }
            }
        }
    } else if (v === '_undefined_') {
        res = undefined;
    } else {
        res = v;
    }
    return res
}

// Figure View
// ===========
var FigureView = widgets.DOMWidgetView.extend({

    render: function() {

        var that = this;

        // Wire up property callbacks
        // --------------------------
        // Python -> JS event properties
        this.model.on('change:_py2js_addTraces', this.do_addTraces, this);
        this.model.on('change:_py2js_deleteTraces', this.do_deleteTraces, this);
        this.model.on('change:_py2js_moveTraces', this.do_moveTraces, this);
        this.model.on('change:_py2js_restyle', this.do_restyle, this);
        this.model.on("change:_py2js_relayout", this.do_relayout, this);
        this.model.on("change:_py2js_update", this.do_update, this);
        this.model.on("change:_py2js_animate", this.do_animate, this);
        this.model.on("change:_py2js_requestSvg", this.do_requestSvg, this);

        // Increment message ids
        // ---------------------
        var relayout_msg_id = this.model.get('_last_relayout_msg_id') + 1;
        this.model.set('_last_relayout_msg_id', relayout_msg_id);
        var restyle_msg_id = this.model.get('_last_restyle_msg_id') + 1;
        this.model.set('_last_restyle_msg_id', restyle_msg_id);
        this.touch();

        // Set view UID
        // ------------
        this.viewID = randstr();
        console.log('Created view with id: ' + this.viewID);

        // Initialize figure
        // -----------------
        console.log('render');
        console.log(this.model.get('_data'));
        console.log(this.model.get('_layout'));

        // Clone traces and layout so plotly instances in the views don't mutate the model
        var initial_traces = JSON.parse(JSON.stringify(this.model.get('_data')));
        var initial_layout = JSON.parse(JSON.stringify(this.model.get('_layout')));

        Plotly.newPlot(this.el, initial_traces, initial_layout).then(function () {

            // Update layout
            var relayoutDelta = that.create_delta_object(that.model.get('_layout'), that.getFullLayout());
            relayoutDelta['_relayout_msg_id'] = relayout_msg_id;
            that.model.set('_js2py_layoutDelta', relayoutDelta);

            // Update traces
            // Loop over new traces
            var traceDeltas = new Array(initial_traces.length);
            var fullData = that.getFullData();
            for(var i=0; i < initial_traces.length; i++) {
                var fullTraceData = fullData[i];
                var traceData = initial_traces[i];
                traceDeltas[i] = that.create_delta_object(traceData, fullTraceData);
                traceDeltas[i]['_restyle_msg_id'] = restyle_msg_id;
            }

            console.log(traceDeltas);
            that.model.set('_js2py_styleDelta', traceDeltas);

            // sync any/all changes back to model
            that.touch();

            // Wire up plotly event callbacks
            that.el.on('plotly_restyle', function(update) {that.handle_plotly_restyle(update)});
            that.el.on('plotly_relayout', function(update) {that.handle_plotly_relayout(update)});
            that.el.on('plotly_update', function(update) {that.handle_plotly_update(update)});

            that.el.on('plotly_click', function(update) {that.handle_plotly_click(update)});
            that.el.on('plotly_hover', function(update) {that.handle_plotly_hover(update)});
            that.el.on('plotly_unhover', function(update) {that.handle_plotly_unhover(update)});
            that.el.on('plotly_selected', function(update) {that.handle_plotly_selected(update)});
            that.el.on('plotly_doubleclick', function(update) {that.handle_plotly_doubleclick(update)});
            that.el.on('plotly_afterplot', function(update) {that.handle_plotly_afterplot(update)});
        });
    },
    destroy: function() {
        Plotly.purge(this.el);
    },
    getFullData: function () {
        // Merge so that we use .data properties if available.
        // e.g. colorscales can be stored by name in this.el.data (Viridis) but by array in el._fullData. We want
        // the string in this case
        return _.merge(this.el._fullData, this.el.data);
    },

    getFullLayout: function () {
        return _.merge(this.el._fullLayout, this.el.layout);
    },

    buildPointsObject: function (data) {

        var pointsObject;
        if (data.hasOwnProperty('points')) {
            // Most cartesian plots
            var pointObjects = data['points'];
            var numPoints = pointObjects.length;
            pointsObject = {
                'curveNumbers': new Array(numPoints),
                'pointNumbers': new Array(numPoints),
                'xs': new Array(numPoints),
                'ys': new Array(numPoints)};


                for (var p = 0; p < numPoints; p++) {
                pointsObject['curveNumbers'][p] = pointObjects[p]['curveNumber'];
                pointsObject['pointNumbers'][p] = pointObjects[p]['pointNumber'];
                pointsObject['xs'][p] = pointObjects[p]['x'];
                pointsObject['ys'][p] = pointObjects[p]['y'];
            }

            // Add z if present
            var hasZ = pointObjects[0] !== undefined && pointObjects[0].hasOwnProperty('z');
            if (hasZ) {
                pointsObject['zs'] = new Array(numPoints);
                for (p = 0; p < numPoints; p++) {
                    pointsObject['zs'][p] = pointObjects[p]['z'];
                }
            }

            return pointsObject
        } else {
            return null
        }
    },

    buildMouseEventObject: function (data) {
        var event = data['event'];
        if (event === undefined) {
            return {}
        } else {
            var mouseEventObject = {
                // Keyboard modifiers
                'alt': event['altKey'],
                'ctrl': event['ctrlKey'],
                'meta': event['metaKey'],
                'shift': event['shiftKey'],

                // Mouse buttons
                'button': event['button'],
                // Indicates which button was pressed on the mouse to trigger the event.
                //   0: Main button pressed, usually the left button or the un-initialized state
                //   1: Auxiliary button pressed, usually the wheel button or the middle button (if present)
                //   2: Secondary button pressed, usually the right button
                //   3: Fourth button, typically the Browser Back button
                //   4: Fifth button, typically the Browser Forward button
                'buttons': event['buttons']
                // Indicates which buttons are pressed on the mouse when the event is triggered.
                //   0  : No button or un-initialized
                //   1  : Primary button (usually left)
                //   2  : Secondary button (usually right)
                //   4  : Auxilary button (usually middle or mouse wheel button)
                //   8  : 4th button (typically the "Browser Back" button)
                //   16 : 5th button (typically the "Browser Forward" button)
            };
            return mouseEventObject
        }
    },

    buildSelectorObject: function(data) {
        var selectorObject = {};

        // Test for box select
        if (data.hasOwnProperty('range')) {
            selectorObject['type'] = 'box';
            selectorObject['xrange'] = data['range']['x'];
            selectorObject['yrange'] = data['range']['y'];
        } else if (data.hasOwnProperty('lassoPoints')) {
            selectorObject['type'] = 'lasso';
            selectorObject['xs'] = data['lassoPoints']['x'];
            selectorObject['ys'] = data['lassoPoints']['y'];
        }
        return selectorObject
    },

    handle_plotly_restyle: function (data) {
        if (data !== null && data !== undefined && data[0].hasOwnProperty('_doNotReportToPy')) {
            // Restyle originated on the Python side
            return
        }

        // Work around some plotly bugs/limitations
        if (data === null || data === undefined) {

            data = new Array(this.el.data.length);

            for (var t = 0; t < this.el.data.length; t++) {
                var traceData = this.el.data[t];
                data[t] = {'uid': traceData['uid']};
                if (traceData['type'] === 'parcoords') {

                    // Parallel coordinate diagram 'constraintrange' property not provided
                    for (var d = 0; d < traceData.dimensions.length; d++) {
                        var constraintrange = traceData.dimensions[d]['constraintrange'];
                        if (constraintrange !== undefined) {
                            data[t]['dimensions[' + d + '].constraintrange'] = [constraintrange];
                        }
                    }
                }
            }
        }

        // Add viewID to style
        data[0]['_view_id'] = this.viewID;

        // Log message
        console.log("plotly_restyle");
        console.log(data);

        this.model.set('_js2py_restyle', data);
        this.touch();
    },

    handle_plotly_relayout: function (data) {
        if (data !== null && data !== undefined && data.hasOwnProperty('_doNotReportToPy')) {
            // Relayout originated on the Python side
            return
        }

        // Work around some plotly bugs/limitations

        // Sometimes (in scatterGL at least) axis range isn't wrapped in range
        if ('xaxis' in data && Array.isArray(data['xaxis'])) {
            data['xaxis'] = {'range': data['xaxis']}
        }

        if ('yaxis' in data && Array.isArray(data['yaxis'])) {
            data['yaxis'] = {'range': data['yaxis']}
        }

        // Add viewID
        data['_view_id'] = this.viewID;

        // Log message
        console.log("plotly_relayout");
        console.log(data);

        this.model.set('_js2py_relayout', data);
        this.touch();
    },

    handle_plotly_update: function (data) {
        if (data !== null && data !== undefined &&
            data['data'][0].hasOwnProperty('_doNotReportToPy')) {
            // Update originated on the Python side
            return
        }

        // Add viewID to style element
        data['data'][0]['_view_id'] = this.viewID;

        // Log message
        console.log("plotly_update");
        console.log(data);

        this.model.set('_js2py_update', data);
        this.touch();
    },

    handle_plotly_click: function (data) {
        console.log("plotly_click");

        if (data === null || data === undefined) return;

        var pyData = {
            'event_type': 'plotly_click',
            'points': this.buildPointsObject(data),
            'state': this.buildMouseEventObject(data)
        };

        if (pyData['points'] !== null) {
            console.log(data);
            console.log(pyData);
            this.model.set('_js2py_pointsCallback', pyData);
            this.touch();
        }
    },

    handle_plotly_hover: function (data) {
        console.log("plotly_hover");

        if (data === null || data === undefined) return;

        var pyData = {
            'event_type': 'plotly_hover',
            'points': this.buildPointsObject(data),
            'state': this.buildMouseEventObject(data)
        };

        if (pyData['points'] !== null && pyData['points'] !== undefined) {
            console.log(data);
            console.log(pyData);
            this.model.set('_js2py_pointsCallback', pyData);
            this.touch();
        }
    },

    handle_plotly_unhover: function (data) {
        console.log("plotly_unhover");

        if (data === null || data === undefined) return;

        var pyData = {
            'event_type': 'plotly_unhover',
            'points': this.buildPointsObject(data),
            'state': this.buildMouseEventObject(data)
        };

        if (pyData['points'] !== null) {
            console.log(data);
            console.log(pyData);
            this.model.set('_js2py_pointsCallback', pyData);
            this.touch();
        }
    },

    handle_plotly_selected: function (data) {
        console.log("plotly_selected");

        if (data === null ||
            data === undefined) return;

        var pyData = {
            'event_type': 'plotly_selected',
            'points': this.buildPointsObject(data),
            'selector': this.buildSelectorObject(data),
        };

        if (pyData['points'] !== null) {
            console.log(data);
            console.log(pyData);
            this.model.set('_js2py_pointsCallback', pyData);
            this.touch();
        }
    },

    handle_plotly_doubleclick: function (data) {
        // console.log("plotly_doubleclick");
        // console.log(data);
    },

    handle_plotly_afterplot: function (data) {
        // console.log("plotly_afterplot");
        // console.log(data);
    },

    do_addTraces: function () {
        // add trace to plot

        var data = this.model.get('_py2js_addTraces');
        console.log('Figure View: do_addTraces');

        if (data !== null) {
            console.log(data);
            var prev_num_traces = this.el.data.length;

            // console.log(data);
            var that = this;
            Plotly.addTraces(this.el, data).then(function () {
                // Loop over new traces
                var traceDeltas = new Array(data.length);
                var tracesData = that.model.get('_data');
                var fullData = that.getFullData();
                var restyle_msg_id = data[0]['_restyle_msg_id'];
                var relayout_msg_id = data[0]['_relayout_msg_id'];
                console.log('relayout_msg_id: ' + relayout_msg_id);
                for(var i=0; i < data.length; i++) {
                    var fullTraceData = fullData[i + prev_num_traces];
                    var traceData = tracesData[i + prev_num_traces];
                    traceDeltas[i] = that.create_delta_object(traceData, fullTraceData);
                    traceDeltas[i]['_restyle_msg_id'] = restyle_msg_id;
                }

                that.model.set('_js2py_styleDelta', traceDeltas);


                // Update layout
                var layoutDelta = that.create_delta_object(that.model.get('_layout'), that.getFullLayout());
                layoutDelta['_relayout_msg_id'] = relayout_msg_id;
                that.model.set('_js2py_layoutDelta', layoutDelta);
                console.log(layoutDelta);

                that.touch();
            });
        }
    },

    do_deleteTraces: function () {
        var data = this.model.get('_py2js_deleteTraces');
        console.log('do_deleteTraces');
        if (data !== null){
            var delete_inds = data['delete_inds'];
            var relayout_msg_id = data['_relayout_msg_id'];

            console.log(delete_inds);
            var that = this;
            Plotly.deleteTraces(this.el, delete_inds).then(function () {
                // Send back layout delta
                var relayoutDelta = that.create_delta_object(that.model.get('_layout'), that.getFullLayout());
                relayoutDelta['_relayout_msg_id'] = relayout_msg_id;
                that.model.set('_js2py_layoutDelta', relayoutDelta);
                that.touch();
            });
        }
    },

    do_moveTraces: function () {
        var move_data = this.model.get('_py2js_moveTraces');
        console.log('do_moveTraces');

        if (move_data !== null){
            var current_inds = move_data[0];
            var new_inds = move_data[1];

            var inds_equal = current_inds.length===new_inds.length &&
                current_inds.every(function(v,i) { return v === new_inds[i]});

            if (!inds_equal) {
                console.log(current_inds + "->" + new_inds);
                Plotly.moveTraces(this.el, current_inds, new_inds)
            }
        }
    },

    do_restyle: function () {
        console.log('do_restyle');
        var data = this.model.get('_py2js_restyle');
        console.log(data);
        if (data !== null) {
            var style = data[0];
            var trace_indexes = this.model.normalize_trace_indexes(data[1]);

            if (style['_view_id'] === this.viewID) {
                // Operation originated from this view, don't re-apply it
                console.log('Skipping restyle for view ' + this.viewID);
                return
            } else {
                console.log('Applying restyle for view ' + this.viewID)
            }

            style['_doNotReportToPy'] = true;
            Plotly.restyle(this.el, style, trace_indexes);

            // uid
            var restyle_msg_id = style['_restyle_msg_id'];

            // Send back style delta
            var traceDeltas = new Array(trace_indexes.length);
            var trace_data = this.model.get('_data');
            var fullData = this.getFullData();
            for (var i = 0; i < trace_indexes.length; i++) {
                traceDeltas[i] = this.create_delta_object(trace_data[trace_indexes[i]], fullData[trace_indexes[i]]);
                traceDeltas[i]['_restyle_msg_id'] = restyle_msg_id;
            }

            this.model.set('_js2py_styleDelta', traceDeltas);

            // Send back layout delta
            var relayout_msg_id = style['_relayout_msg_id'];
            var relayoutDelta = this.create_delta_object(this.model.get('_layout'), this.getFullLayout());
            relayoutDelta['_relayout_msg_id'] = relayout_msg_id;
            this.model.set('_js2py_layoutDelta', relayoutDelta);

            this.touch();
        }
    },

    do_relayout: function () {
        console.log('FigureView: do_relayout');
        var data = this.model.get('_py2js_relayout');
        if (data !== null) {

            if (data['_view_id'] === this.viewID) {
                // Operation originated from this view, don't re-apply it
                console.log('Skipping relayout for view ' + this.viewID)
                return
            } else {
                console.log('Applying relayout for view ' + this.viewID)
            }

            data['_doNotReportToPy'] = true;
            Plotly.relayout(this.el, data);

            var layoutDelta = this.create_delta_object(this.model.get('_layout'), this.getFullLayout());

            // Add message id
            layoutDelta['_relayout_msg_id'] = data['_relayout_msg_id'];

            console.log(layoutDelta);
            console.log(this.model.get('_layout'));
            this.model.set('_js2py_layoutDelta', layoutDelta);

            this.touch();
        }
    },

    do_update: function () {
        console.log('FigureView: do_update');
        var data = this.model.get('_py2js_update');
        if (data !== null) {
            var style = data[0];
            var layout = data[1];
            var trace_indexes = this.model.normalize_trace_indexes(data[2]);

            if (style['_view_id'] === this.viewID) {
                // Operation originated from this view, don't re-apply it
                console.log('Skipping update for view ' + this.viewID);
                return
            } else {
                console.log('Applying update for view ' + this.viewID)
            }

            style['_doNotReportToPy'] = true;
            Plotly.update(this.el, style, layout, trace_indexes);

            // Message ids
            var restyle_msg_id = style['_restyle_msg_id'];
            var relayout_msg_id = layout['_relayout_msg_id'];

            // Send back style delta
            var traceDeltas = new Array(trace_indexes.length);
            var trace_data = this.model.get('_data');
            var fullData = this.getFullData();
            for (var i = 0; i < trace_indexes.length; i++) {
                traceDeltas[i] = this.create_delta_object(trace_data[trace_indexes[i]], fullData[trace_indexes[i]]);
                traceDeltas[i]['_restyle_msg_id'] = restyle_msg_id;
            }

            this.model.set('_js2py_styleDelta', traceDeltas);

            // Send back layout delta
            var relayoutDelta = this.create_delta_object(this.model.get('_layout'), this.getFullLayout());
            relayoutDelta['_relayout_msg_id'] = relayout_msg_id;
            this.model.set('_js2py_layoutDelta', relayoutDelta);

            this.touch();
        }
    },

    do_animate: function() {
        console.log('FigureView: do_animate');
        var data = this.model.get('_py2js_animate');
        if (data !== null) {

            // Unpack params
            var animationData = data[0];
            var animationOpts = data[1];

            var styles = animationData['data'];
            var layout = animationData['layout'];
            var trace_indexes = this.model.normalize_trace_indexes(animationData['traces']);

            animationData['_doNotReportToPy'] = true;
            var that = this;
            Plotly.animate(this.el, animationData, animationOpts).then(function () {
                // Send back style delta
                var traceDeltas = new Array(trace_indexes.length);
                var trace_data = that.model.get('_data');
                var fullData = that.getFullData();
                for (var i = 0; i < trace_indexes.length; i++) {
                    var restyle_msg_id = styles[i]['_restyle_msg_id'];
                    traceDeltas[i] = that.create_delta_object(trace_data[trace_indexes[i]], fullData[trace_indexes[i]]);
                    traceDeltas[i]['_restyle_msg_id'] = restyle_msg_id;
                }

                that.model.set('_js2py_styleDelta', traceDeltas);

                // Send back layout delta
                var relayout_msg_id = layout['_relayout_msg_id'];
                var relayoutDelta = that.create_delta_object(that.model.get('_layout'), that.getFullLayout());
                relayoutDelta['_relayout_msg_id'] = relayout_msg_id;
                that.model.set('_js2py_layoutDelta', relayoutDelta);

                that.touch();
            });
        }
    },

    do_requestSvg: function() {
        console.log('FigureView: do_requestSvg');
        var req_id = this.model.get('_py2js_requestSvg');
        var that = this;
        if (req_id !== null) {
            Plotly.toImage(this.el, {format:'svg'}).then(function (svg_uri) {
                console.log([req_id, svg_uri]);

                that.send({event: 'svg', req_id: req_id, svg_uri: svg_uri});

                // that.model.set('_js2py_svg', [req_id, svg_uri]);
                // that.touch();
            });
        }
    },

    clone_fullLayout_data: function (fullLayout) {
        var fullStr = JSON.stringify(fullLayout, function(k, v) {
            if (k.length > 0 && k[0] === '_') {
                return undefined
            }
            return v
        });
        return JSON.parse(fullStr)
    },

    clone_fullData_metadata: function (fullData) {
        var fullStr = JSON.stringify(fullData, function(k, v) {
            if (k.length > 0 && k[0] === '_') {
                return undefined
            } else if (Array.isArray(v)) {
                // For performance, we don't clone arrays
                return undefined
            }
            return v
        });
        return JSON.parse(fullStr)
    },

    create_delta_object: function(data, fullData) {
        var res;
        if(Array.isArray(fullData)) {
            res = new Array(fullData.length);
        } else {
            res = {};
        }

        if (data === null || data === undefined) {
            data = {};
        }
        for (var p in fullData) {
            if (p[0] !== '_' && fullData.hasOwnProperty(p) && fullData[p] !== null) {

                var props_equal;
                if (data.hasOwnProperty(p) && Array.isArray(data[p]) && Array.isArray(fullData[p])) {
                    props_equal = JSON.stringify(data[p]) === JSON.stringify(fullData[p]);
                } else if (data.hasOwnProperty(p)) {
                    props_equal = data[p] === fullData[p];
                } else {
                    props_equal = false;
                }

                if (!props_equal || p === 'uid') {  // Let uids through
                    // property has non-null value in fullData that doesn't match the value in
                    var full_val = fullData[p];
                    if (data.hasOwnProperty(p) && typeof full_val === 'object') {
                        if(Array.isArray(full_val)) {

                            if (full_val.length > 0 && typeof(full_val[0]) === 'object') {
                                // We have an object array
                                res[p] = new Array(full_val.length);
                                for (var i = 0; i < full_val.length; i++) {
                                    if (!Array.isArray(data[p]) || data[p].length <= i) {
                                        res[p][i] = full_val[i]
                                    } else {
                                        res[p][i] = this.create_delta_object(data[p][i], full_val[i]);
                                    }
                                }
                            } else {
                                // We have a primitive array
                                res[p] = full_val;
                            }
                        } else { // object
                            var full_obj = this.create_delta_object(data[p], full_val);
                            if (Object.keys(full_obj).length > 0) {
                                // new object is not empty
                                res[p] = full_obj;
                            }
                        }
                    } else if (typeof full_val === 'object' && !Array.isArray(full_val)) {
                        res[p] = this.create_delta_object({}, full_val);

                    } else if (full_val !== undefined) {
                        res[p] = full_val;
                    }
                }
            }
        }
        return res
    }
});

// Copied from Plotly src/lib/index.js (How can we call it?)
// random string generator
function randstr(existing, bits, base) {
    /*
     * Include number of bits, the base of the string you want
     * and an optional array of existing strings to avoid.
     */
    if(!base) base = 16;
    if(bits === undefined) bits = 24;
    if(bits <= 0) return '0';

    var digits = Math.log(Math.pow(2, bits)) / Math.log(base),
        res = '',
        i,
        b,
        x;

    for(i = 2; digits === Infinity; i *= 2) {
        digits = Math.log(Math.pow(2, bits / i)) / Math.log(base) * i;
    }

    var rem = digits - Math.floor(digits);

    for(i = 0; i < Math.floor(digits); i++) {
        x = Math.floor(Math.random() * base).toString(base);
        res = x + res;
    }

    if(rem) {
        b = Math.pow(base, rem);
        x = Math.floor(Math.random() * b).toString(base);
        res = x + res;
    }

    var parsed = parseInt(res, base);
    if((existing && (existing.indexOf(res) > -1)) ||
         (parsed !== Infinity && parsed >= Math.pow(2, bits))) {
        return randstr(existing, bits, base);
    }
    else return res;
};

module.exports = {
    FigureView : FigureView,
    FigureModel: FigureModel,
};
