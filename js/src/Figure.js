var widgets = require("@jupyter-widgets/base");
var _ = require("lodash");

window.PlotlyConfig = {MathJaxConfig: 'local'};
var Plotly = require("plotly.js/dist/plotly");
var PlotlyIndex = require("plotly.js/src/lib/index");
var semver_range = "^" + require("../package.json").version;

// Model
// =====
/**
 * A FigureModel holds a mirror copy of the state of a FigureWidget on
 * the Python side.  There is a one-to-one relationship between JavaScript
 * FigureModels and Python FigureWidgets. The JavaScript FigureModel is
 * initialized as soon as a Python FigureWidget initialized, this happens
 * even before the widget is first displayed in the Notebook
 * @type {widgets.DOMWidgetModel}
 */
var FigureModel = widgets.DOMWidgetModel.extend({

    defaults: _.extend(widgets.DOMWidgetModel.prototype.defaults(), {
        // Model metadata
        // --------------
        _model_name: "FigureModel",
        _view_name: "FigureView",
        _model_module: "plotlywidget",
        _view_module: "plotlywidget",
        _view_module_version: semver_range,
        _model_module_version: semver_range,

        // Data and Layout
        // ---------------
        // The _data and _layout properties are synchronized with the
        // Python side on initialization only.  After initialization, these
        // properties are kept in sync through the use of the _py2js_*
        // messages
        _data: [],
        _layout: {},

        // Python -> JS messages
        // ---------------------
        // Messages are implemented using trait properties. This is done so
        // that we can take advantage of ipywidget's binary serialization
        // protocol.
        //
        // Messages are sent by the Python side by assigning the message
        // contents to the appropriate _py2js_* property, and then immediately
        // setting it to None.  Messages are received by the JavaScript
        // side by registering property change callbacks in the initialize
        // methods for FigureModel and FigureView. e.g. (where this is a
        // FigureModel):
        //
        //      this.on('change:_py2js_addTraces', this.do_addTraces, this);
        //
        // Message handling methods, do_addTraces, are responsible for
        // performing the appropriate action if the message contents are
        // not null

        /**
         * @typedef {null|Object} Py2JsAddTracesMsg
         * @property {Array.<Object>} trace_data
         *  Array of traces to append to the end of the figure's current traces
         * @property {Number} trace_edit_id
         *  Edit ID to use when returning trace deltas using
         *  the _js2py_traceDeltas message.
         * @property {Number} layout_edit_id
         *  Edit ID to use when returning layout deltas using
         *  the _js2py_layoutDelta message.
         */
        _py2js_addTraces: null,

        /**
         * @typedef {null|Object} Py2JsDeleteTracesMsg
         * @property {Array.<Number>} delete_inds
         *  Array of indexes of traces to be deleted, in ascending order
         * @property {Number} trace_edit_id
         *  Edit ID to use when returning trace deltas using
         *  the _js2py_traceDeltas message.
         * @property {Number} layout_edit_id
         *  Edit ID to use when returning layout deltas using
         *  the _js2py_layoutDelta message.
         */
        _py2js_deleteTraces: null,

        /**
         * @typedef {null|Object} Py2JsMoveTracesMsg
         * @property {Array.<Number>} current_trace_inds
         *  Array of the current indexes of traces to be moved
         * @property {Array.<Number>} new_trace_inds
         *  Array of the new indexes that traces should be moved to.
         */
        _py2js_moveTraces: null,


        /**
         * @typedef {null|Object} Py2JsRestyleMsg
         * @property {Object} restyle_data
         *  Restyle data as accepted by Plotly.restyle
         * @property {null|Array.<Number>} restyle_traces
         *  Array of indexes of the traces that the resytle operation applies
         *  to, or null to apply the operation to all traces
         * @property {Number} trace_edit_id
         *  Edit ID to use when returning trace deltas using
         *  the _js2py_traceDeltas message
         * @property {Number} layout_edit_id
         *  Edit ID to use when returning layout deltas using
         *  the _js2py_layoutDelta message
         * @property {null|String} source_view_id
         *  view_id of the FigureView that triggered the original restyle
         *  event (e.g. by clicking the legend), or null if the restyle was
         *  triggered from Python
         */
        _py2js_restyle: null,

        /**
         * @typedef {null|Object} Py2JsRelayoutMsg
         * @property {Object} relayout_data
         *  Relayout data as accepted by Plotly.relayout
         * @property {Number} layout_edit_id
         *  Edit ID to use when returning layout deltas using
         *  the _js2py_layoutDelta message
         * @property {null|String} source_view_id
         *  view_id of the FigureView that triggered the original relayout
         *  event (e.g. by clicking the zoom button), or null if the
         *  relayout was triggered from Python
         */
        _py2js_relayout: null,

        /**
         * @typedef {null|Object} Py2JsUpdateMsg
         * @property {Object} style_data
         *  Style data as accepted by Plotly.update
         * @property {Object} layout_data
         *  Layout data as accepted by Plotly.update
         * @property {Array.<Number>} style_traces
         *  Array of indexes of the traces that the update operation applies
         *  to, or null to apply the operation to all traces
         * @property {Number} trace_edit_id
         *  Edit ID to use when returning trace deltas using
         *  the _js2py_traceDeltas message
         * @property {Number} layout_edit_id
         *  Edit ID to use when returning layout deltas using
         *  the _js2py_layoutDelta message
         * @property {null|String} source_view_id
         *  view_id of the FigureView that triggered the original update
         *  event (e.g. by clicking a button), or null if the update was
         *  triggered from Python
         */
        _py2js_update: null,

        /**
         * @typedef {null|Object} Py2JsAnimateMsg
         * @property {Object} style_data
         *  Style data as accepted by Plotly.animate
         * @property {Object} layout_data
         *  Layout data as accepted by Plotly.animate
         * @property {Array.<Number>} style_traces
         *  Array of indexes of the traces that the animate operation applies
         *  to, or null to apply the operation to all traces
         * @property {Object} animation_opts
         *  Animation options as accepted by Plotly.animate
         * @property {Number} trace_edit_id
         *  Edit ID to use when returning trace deltas using
         *  the _js2py_traceDeltas message
         * @property {Number} layout_edit_id
         *  Edit ID to use when returning layout deltas using
         *  the _js2py_layoutDelta message
         * @property {null|String} source_view_id
         *  view_id of the FigureView that triggered the original animate
         *  event (e.g. by clicking a button), or null if the update was
         *  triggered from Python
         */
        _py2js_animate: null,

        /**
         * @typedef {null|Object} Py2JsRemoveLayoutPropsMsg
         * @property {Array.<Array.<String|Number>>} remove_props
         *  Array of property paths to remove. Each propery path is an
         *  array of property names or array indexes that locate a property
         *  inside the _layout object
         */
        _py2js_removeLayoutProps: null,

        /**
         * @typedef {null|Object} Py2JsRemoveTracePropsMsg
         * @property {Number} remove_trace
         *  The index of the trace from which to remove properties
         * @property {Array.<Array.<String|Number>>} remove_props
         *  Array of property paths to remove. Each propery path is an
         *  array of property names or array indexes that locate a property
         *  inside the _data[remove_trace] object
         */
        _py2js_removeTraceProps: null,


        // JS -> Python messages
        // ---------------------
        // Messages are sent by the JavaScript side by assigning the
        // message contents to the appropriate _js2py_* property and then
        // calling the `touch` method on the view that triggered the
        // change. e.g. (where this is a FigureView):
        //
        //      this.model.set('_js2py_restyle', data);
        //      this.touch();
        //
        // The Python side is responsible for setting the property to None
        // after receiving the message.
        //
        // Message trigger logic is described in the corresponding
        // handle_plotly_* methods of FigureView

        /**
         * @typedef {null|Object} Js2PyRestyleMsg
         * @property {Object} style_data
         *  Style data that was passed to Plotly.restyle
         * @property {Array.<Number>} style_traces
         *  Array of indexes of the traces that the restyle operation
         *  was applied to, or null if applied to all traces
         * @property {String} source_view_id
         *  view_id of the FigureView that triggered the original restyle
         *  event (e.g. by clicking the legend)
         */
        _js2py_restyle: null,

        /**
         * @typedef {null|Object} Js2PyRelayoutMsg
         * @property {Object} relayout_data
         *  Relayout data that was passed to Plotly.relayout
         * @property {String} source_view_id
         *  view_id of the FigureView that triggered the original relayout
         *  event (e.g. by clicking the zoom button)
         */
        _js2py_relayout: null,

        /**
         * @typedef {null|Object} Js2PyUpdateMsg
         * @property {Object} style_data
         *  Style data that was passed to Plotly.update
         * @property {Object} layout_data
         *  Layout data that was passed to Plotly.update
         * @property {Array.<Number>} style_traces
         *  Array of indexes of the traces that the update operation applied
         *  to, or null if applied to all traces
         * @property {String} source_view_id
         *  view_id of the FigureView that triggered the original relayout
         *  event (e.g. by clicking the zoom button)
         */
        _js2py_update: null,

        /**
         * @typedef {null|Object} Js2PyLayoutDeltaMsg
         * @property {Object} layout_delta
         *  The layout delta object that contains all of the properties of
         *  _fullLayout that are not identical to those in the
         *  FigureModel's _layout property
         * @property {Number} layout_edit_id
         *  Edit ID of message that triggered the creation of layout delta
         */
        _js2py_layoutDelta: null,

        /**
         * @typedef {null|Object} Js2PyTraceDeltasMsg
         * @property {Array.<Object>} trace_deltas
         *  Array of trace delta objects. Each trace delta contains the
         *  trace's uid along with all of the properties of _fullData that
         *  are not identical to those in the FigureModel's _data property
         * @property {Number} trace_edit_id
         *  Edit ID of message that triggered the creation of trace deltas
         */
        _js2py_traceDeltas: null,


        /**
         * Object representing a collection of points for use in click, hover,
         * and selection events
         * @typedef {Object} Points
         * @property {Array.<Number>} trace_indexes
         *  Array of the trace index for each point
         * @property {Array.<Number>} point_indexes
         *  Array of the index of each point in its own trace
         * @property {null|Array.<Number>} xs
         *  Array of the x coordinate of each point (for cartesian trace types)
         *  or null (for non-cartesian trace types)
         * @property {null|Array.<Number>} ys
         *  Array of the y coordinate of each point (for cartesian trace types)
         *  or null (for non-cartesian trace types
         * @property {null|Array.<Number>} zs
         *  Array of the z coordinate of each point (for 3D cartesian
         *  trace types)
         *  or null (for non-3D-cartesian trace types)
         */

        /**
         * Object representing the state of the input devices during a
         * plotly event
         * @typedef {Object} InputDeviceState
         * @property {boolean} alt - true if alt key pressed,
         * false otherwise
         * @property {boolean} ctrl - true if ctrl key pressed,
         * false otherwise
         * @property {boolean} meta - true if meta key pressed,
         * false otherwise
         * @property {boolean} shift - true if shift key pressed,
         * false otherwise
         *
         * @property {boolean} button
         *  Indicates which button was pressed on the mouse to trigger the
         *  event.
         *    0: Main button pressed, usually the left button or the
         *       un-initialized state
         *    1: Auxiliary button pressed, usually the wheel button or
         *       the middle button (if present)
         *    2: Secondary button pressed, usually the right button
         *    3: Fourth button, typically the Browser Back button
         *    4: Fifth button, typically the Browser Forward button
         *
         * @property {boolean} buttons
         *  Indicates which buttons were pressed on the mouse when the event
         *  is triggered.
         *    0  : No button or un-initialized
         *    1  : Primary button (usually left)
         *    2  : Secondary button (usually right)
         *    4  : Auxilary button (usually middle or mouse wheel button)
         *    8  : 4th button (typically the "Browser Back" button)
         *    16 : 5th button (typically the "Browser Forward" button)
         *
         *  Combinations of buttons are represented by the sum of the codes
         *  above. e.g. a value of 7 indicates buttons 1 (primary),
         *  2 (secondary), and 4 (auxilary) were pressed during the event
         */

        /**
         * @typedef {Object} BoxSelectorState
         * @property {Array.<Number>} xrange
         *  Two element array containing the x-range of the box selection
         * @property {Array.<Number>} yrange
         *  Two element array containing the y-range of the box selection
         */

        /**
         * @typedef {Object} LassoSelectorState
         * @property {Array.<Number>} xs
         *  Array of the x-coordinates of the lasso selection region
         * @property {Array.<Number>} ys
         *  Array of the y-coordinates of the lasso selection region
         */

        /**
         * Object representing the state of the selection tool during a
         * plotly_select event
         * @typedef {Object} Selector
         * @property {String} type
         *  Selection type. One of: 'box', or 'lasso'
         * @property {BoxSelectorState|LassoSelectorState} selector_state
         */

        /**
         * @typedef {null|Object} Js2PyPointsCallbackMsg
         * @property {string} event_type
         *  Name of the triggering event. One of 'plotly_click',
         *  'plotly_hover', 'plotly_unhover', or 'plotly_selected'
         * @property {null|Points} points
         *  Points object for event
         * @property {null|InputDeviceState} device_state
         *  InputDeviceState object for event
         * @property {null|Selector} selector
         *  State of the selection tool for 'plotly_selected' events, null
         *  for other event types
         */
        _js2py_pointsCallback: null,

        // Message tracking
        // ----------------
        /**
         * @type {Number}
         * layout_edit_id of the last layout modification operation
         * requested by the Python side
         */
        _last_layout_edit_id: 0,

        /**
         * @type {Number}
         * trace_edit_id of the last trace modification operation
         * requested by the Python side
         */
        _last_trace_edit_id: 0
    }),

    /**
     * Initialize FigureModel. Called when the Python FigureWidget is first
     * constructed
     */
    initialize: function() {
        FigureModel.__super__.initialize.apply(this, arguments);
        console.log(["FigureModel: initialize"]);

        this.on("change:_data", this.do_data, this);
        this.on("change:_layout", this.do_layout, this);
        this.on("change:_py2js_addTraces", this.do_addTraces, this);
        this.on("change:_py2js_deleteTraces", this.do_deleteTraces, this);
        this.on("change:_py2js_moveTraces", this.do_moveTraces, this);
        this.on("change:_py2js_restyle", this.do_restyle, this);
        this.on("change:_py2js_relayout", this.do_relayout, this);
        this.on("change:_py2js_update", this.do_update, this);
        this.on("change:_py2js_animate", this.do_animate, this);
        this.on("change:_py2js_removeLayoutProps",
            this.do_removeLayoutProps, this);
        this.on("change:_py2js_removeTraceProps",
            this.do_removeTraceProps, this);
    },

    /**
     * Input a trace index specification and return an Array of trace
     * indexes where:
     *
     *  - null|undefined -> Array of all traces
     *  - Trace index as Number -> Single element array of input index
     *  - Array of trace indexes -> Input array unchanged
     *
     * @param {undefined|null|Number|Array.<Number>} trace_indexes
     * @returns {Array.<Number>}
     *  Array of trace indexes
     * @private
     */
    _normalize_trace_indexes: function (trace_indexes) {
        if (trace_indexes === null || trace_indexes === undefined) {
            var numTraces = this.get("_data").length;
            trace_indexes = _.range(numTraces);
        }
        if (!Array.isArray(trace_indexes)) {
            // Make sure idx is an array
            trace_indexes = [trace_indexes];
        }
        return trace_indexes
    },

    /**
     * Log changes to the _data trait
     *
     * This should only happed on FigureModel initialization
     */
    do_data: function () {
        console.log("Figure Model: do_data");
        var data = this.get("_data");

        if (data !== null) {
            console.log(data);
        }
    },

    /**
     * Log changes to the _layout trait
     *
     * This should only happed on FigureModel initialization
     */
    do_layout: function () {
        console.log("Figure Model: do_layout");
        var layout = this.get("_layout");

        if (layout !== null) {
            console.log(layout);
        }
    },

    /**
     * Handle addTraces message
     */
    do_addTraces: function () {
        // add trace to plot
        console.log("Figure Model: do_addTraces");

        /** @type {Py2JsAddTracesMsg} */
        var msgData = this.get("_py2js_addTraces");

        if (msgData !== null) {
            console.log(msgData);
            var currentTraces = this.get("_data");
            var newTraces = msgData.trace_data;
            _.forEach(newTraces, function (newTrace) {
                currentTraces.push(newTrace);
            })
        }
    },

    /**
     * Handle deleteTraces message
     */
    do_deleteTraces: function () {
        // remove traces from plot
        console.log("Figure Model: do_deleteTraces");

        /** @type {Py2JsDeleteTracesMsg} */
        var msgData = this.get("_py2js_deleteTraces");

        if (msgData !== null) {
            var delete_inds = msgData.delete_inds;
            var tracesData = this.get("_data");

            // Remove del inds in reverse order so indexes remain valid
            // throughout loop
            delete_inds.slice().reverse().forEach(function (del_ind) {
                tracesData.splice(del_ind, 1);
            });
        }
    },

    /**
     * Handle moveTraces message
     */
    do_moveTraces: function () {
        console.log("Figure Model: do_moveTraces");

        /** @type {Py2JsMoveTracesMsg} */
        var msgData = this.get("_py2js_moveTraces");

        console.log("do_moveTraces");

        if (msgData !== null) {
            var tracesData = this.get("_data");
            var currentInds = msgData.current_trace_inds;
            var newInds = msgData.new_trace_inds;

            performMoveTracesLike(tracesData, currentInds, newInds);
        }
    },

    /**
     * Handle restyle message
     */
    do_restyle: function () {
        console.log("FigureModel: do_restyle");

        /** @type {Py2JsRestyleMsg} */
        var msgData = this.get("_py2js_restyle");
        if (msgData !== null) {
            var restyleData = msgData.restyle_data;
            var restyleTraces = this._normalize_trace_indexes(
                msgData.restyle_traces);
            performRestyleLike(this.get("_data"), restyleData, restyleTraces);
        }
    },

    /**
     * Handle relayout message
     */
    do_relayout: function () {
        console.log("FigureModel: do_relayout");

        /** @type {Py2JsRelayoutMsg} */
        var msgData = this.get("_py2js_relayout");

        if (msgData !== null) {
            console.log(msgData);
            performRelayoutLike(this.get("_layout"), msgData.relayout_data);
            console.log(this.get("_layout"))
        }
    },

    /**
     * Handle update message
     */
    do_update: function() {
        console.log("FigureModel: do_update");

        /** @type {Py2JsUpdateMsg} */
        var msgData = this.get("_py2js_update");

        if (msgData !== null) {
            console.log(msgData);

            var style = msgData.style_data;
            var layout = msgData.layout_data;
            var styleTraces = this._normalize_trace_indexes(
                msgData.style_traces);
            performRestyleLike(this.get("_data"), style, styleTraces);
            performRelayoutLike(this.get("_layout"), layout);
        }
    },

    /**
     * Handle animate message
     */
    do_animate: function () {
        console.log("FigureModel: do_animate");

        /** @type {Py2JsAnimateMsg} */
        var msgData = this.get("_py2js_animate");
        if (msgData !== null) {
            console.log(msgData);

            var styles = msgData.style_data;
            var layout = msgData.layout_data;
            var trace_indexes = this._normalize_trace_indexes(
                msgData.style_traces);

            for (var i = 0; i < styles.length; i++) {
                var style = styles[i];
                var trace_index = trace_indexes[i];
                var trace = this.get("_data")[trace_index];
                performRelayoutLike(trace, style);
            }

            performRelayoutLike(this.get("_layout"), layout);
        }
    },

    /**
     * Handle removeLayoutProps message
     */
    do_removeLayoutProps: function () {
        console.log("FigureModel:do_removeLayoutProps");

        /** @type {Py2JsRemoveLayoutPropsMsg} */
        var msgData = this.get("_py2js_removeLayoutProps");

        if (msgData !== null) {
            console.log(this.get("_layout"));

            var keyPaths = msgData.remove_props;
            var layout = this.get("_layout");
            performRemoveProps(layout, keyPaths);

            console.log(this.get("_layout"));
        }
    },

    /**
     * Handle removeTraceProps message
     */
    do_removeTraceProps: function () {
        console.log("FigureModel:do_removeTraceProps");

        /** @type {Py2JsRemoveTracePropsMsg} */
        var msgData = this.get("_py2js_removeTraceProps");
        if (msgData !== null) {
            console.log(msgData);
            var keyPaths = msgData.remove_props;
            var traceIndex = msgData.remove_trace;
            var trace = this.get("_data")[traceIndex];

            performRemoveProps(trace, keyPaths);
        }
    }
}, {
    serializers: _.extend({
        _data: { deserialize: py2js_deserializer,
            serialize: js2py_serializer},
        _layout: { deserialize: py2js_deserializer,
            serialize: js2py_serializer},
        _py2js_addTraces: { deserialize: py2js_deserializer,
            serialize: js2py_serializer},
        _py2js_deleteTraces: { deserialize: py2js_deserializer,
            serialize: js2py_serializer},
        _py2js_moveTraces: { deserialize: py2js_deserializer,
            serialize: js2py_serializer},
        _py2js_restyle: { deserialize: py2js_deserializer,
            serialize: js2py_serializer},
        _py2js_relayout: { deserialize: py2js_deserializer,
            serialize: js2py_serializer},
        _py2js_update: { deserialize: py2js_deserializer,
            serialize: js2py_serializer},
        _py2js_animate: { deserialize: py2js_deserializer,
            serialize: js2py_serializer},
        _py2js_removeLayoutProps: { deserialize: py2js_deserializer,
            serialize: js2py_serializer},
        _py2js_removeTraceProps: { deserialize: py2js_deserializer,
            serialize: js2py_serializer},
        _js2py_restyle: { deserialize: py2js_deserializer,
            serialize: js2py_serializer},
        _js2py_relayout: { deserialize: py2js_deserializer,
            serialize: js2py_serializer},
        _js2py_update: { deserialize: py2js_deserializer,
            serialize: js2py_serializer},
        _js2py_layoutDelta: { deserialize: py2js_deserializer,
            serialize: js2py_serializer},
        _js2py_traceDeltas: { deserialize: py2js_deserializer,
            serialize: js2py_serializer},
        _js2py_pointsCallback: { deserialize: py2js_deserializer,
            serialize: js2py_serializer}
    }, widgets.DOMWidgetModel.serializers)
});

// View
// ====
/**
 * A FigureView manages the visual presentation of a single Plotly.js
 * figure for a single notebook output cell. Each FigureView has a
 * reference to FigureModel.  Multiple views may share a single model
 * instance, as is the case when a Python FigureWidget is displayed in
 * multiple notebook output cells.
 *
 * @type {widgets.DOMWidgetView}
 */
var FigureView = widgets.DOMWidgetView.extend({

    /**
     * The perform_render method is called by processPhosphorMessage
     * after the widget's DOM element has been attached to the notebook
     * output cell. This happens after the initialize of the
     * FigureModel, and it won't happen at all if the Python FigureWidget
     * is never displayed in a notebook output cell
     */
    perform_render: function() {

        var that = this;

        // Wire up message property callbacks
        // ----------------------------------
        // Python -> JS event properties
        this.model.on("change:_py2js_addTraces",
            this.do_addTraces, this);
        this.model.on("change:_py2js_deleteTraces",
            this.do_deleteTraces, this);
        this.model.on("change:_py2js_moveTraces",
            this.do_moveTraces, this);
        this.model.on("change:_py2js_restyle",
            this.do_restyle, this);
        this.model.on("change:_py2js_relayout",
            this.do_relayout, this);
        this.model.on("change:_py2js_update",
            this.do_update, this);
        this.model.on("change:_py2js_animate",
            this.do_animate, this);

        // MathJax configuration
        // ---------------------
        if (window.MathJax) {
            MathJax.Hub.Config({SVG: {font: "STIX-Web"}});
        }

        // Get message ids
        // ---------------------
        var layout_edit_id = this.model.get("_last_layout_edit_id");
        var trace_edit_id = this.model.get("_last_trace_edit_id");

        // Set view UID
        // ------------
        this.viewID = PlotlyIndex.randstr();
        console.log("Created view with id: " + this.viewID);

        // Initialize Plotly.js figure
        // ---------------------------
        console.log("render");
        console.log(this.model.get("_data"));
        console.log(this.model.get("_layout"));

        // We must clone the model's data and layout properties so that
        // the model is not directly mutated by the Plotly.js library.
        var initialTraces = _.cloneDeep(this.model.get("_data"));
        var initialLayout = _.cloneDeep(this.model.get("_layout"));

        Plotly.newPlot(that.el, initialTraces, initialLayout).then(
            function () {

                // ### Send trace deltas ###
                // We create an array of deltas corresponding to the new
                // traces.
                that._sendTraceDeltas(trace_edit_id);

                // ### Send layout delta ###
                that._sendLayoutDelta(layout_edit_id);

                // Wire up plotly event callbacks
                that.el.on("plotly_restyle",
                    function (update) {
                        that.handle_plotly_restyle(update)
                    });
                that.el.on("plotly_relayout",
                    function (update) {
                        that.handle_plotly_relayout(update)
                    });
                that.el.on("plotly_update",
                    function (update) {
                        that.handle_plotly_update(update)
                    });
                that.el.on("plotly_click",
                    function (update) {
                        that.handle_plotly_click(update)
                    });
                that.el.on("plotly_hover",
                    function (update) {
                        that.handle_plotly_hover(update)
                    });
                that.el.on("plotly_unhover",
                    function (update) {
                        that.handle_plotly_unhover(update)
                    });
                that.el.on("plotly_selected",
                    function (update) {
                        that.handle_plotly_selected(update)
                    });
                that.el.on("plotly_doubleclick",
                    function (update) {
                        that.handle_plotly_doubleclick(update)
                    });

                // Emit event indicating that the widget has finished
                // rendering
                var event = new CustomEvent("plotlywidget-after-render",
                    { "detail": {"element": that.el, 'viewID': that.viewID}});

                // Dispatch/Trigger/Fire the event
                document.dispatchEvent(event);
            });
    },

    /**
     * Respond to phosphorjs events
     */
    processPhosphorMessage: function(msg) {
        FigureView.__super__.processPhosphorMessage.apply(this, arguments);
        var that = this;
        switch (msg.type) {
            case 'before-attach':
                // Render an initial empty figure. This establishes with
                // the page that the element will not be empty, avoiding
                // some occasions where the dynamic sizing behavior leads
                // to collapsed figure dimensions.
                var axisHidden = {
                    showgrid: false, showline: false, tickvals: []};

                Plotly.newPlot(that.el, [], {
                    xaxis: axisHidden, yaxis: axisHidden
                });

                window.addEventListener("resize", function(){
                    that.autosizeFigure();
                });
                break;
            case 'after-attach':
                // Rendering actual figure in the after-attach event allows
                // Plotly.js to size the figure to fill the available element
                this.perform_render();
                console.log([that.el._fullLayout.height, that.el._fullLayout.width]);
                break;
            case 'resize':
                this.autosizeFigure();
                break
        }
    },

    autosizeFigure: function() {
        var that = this;
        var layout = that.model.get('_layout');
        if (_.isNil(layout) ||
            _.isNil(layout.width)) {
            Plotly.Plots.resize(that.el).then(function(){
                var layout_edit_id = that.model.get(
                    "_last_layout_edit_id");
                that._sendLayoutDelta(layout_edit_id);
            });
        }
    },

    /**
     * Purge Plotly.js data structures from the notebook output display
     * element when the view is destroyed
     */
    destroy: function() {
        Plotly.purge(this.el);
    },

    /**
     * Return the figure's _fullData array merged with its data array
     *
     * The merge ensures that for any properties that el._fullData and
     * el.data have in common, we return the version from el.data
     *
     * Named colorscales are one example of why this is needed. The el.data
     * array will hold named colorscale strings (e.g. 'Viridis'), while the
     * el._fullData array will hold the actual colorscale array. e.g.
     *
     *      el.data[0].marker.colorscale == 'Viridis' but
     *      el._fullData[0].marker.colorscale = [[..., ...], ...]
     *
     * Performing the merge allows our FigureModel to retain the 'Viridis'
     * string, rather than having it overridded by the colorscale array.
     *
     */
    getFullData: function () {
        return _.mergeWith({}, this.el._fullData, this.el.data,
            fullMergeCustomizer)
    },

    /**
     * Return the figure's _fullLayout object merged with its layout object
     *
     * See getFullData documentation for discussion of why the merge is
     * necessary
     */
    getFullLayout: function () {
        return _.mergeWith({}, this.el._fullLayout, this.el.layout,
            fullMergeCustomizer);
    },

    /**
     * Build Points data structure from data supplied by the plotly_click,
     * plotly_hover, or plotly_select events
     * @param {Object} data
     * @returns {null|Points}
     */
    buildPointsObject: function (data) {

        var pointsObject;
        if (data.hasOwnProperty("points")) {
            // Most cartesian plots
            var pointObjects = data["points"];
            var numPoints = pointObjects.length;
            pointsObject = {
                "trace_indexes": new Array(numPoints),
                "point_indexes": new Array(numPoints),
                "xs": new Array(numPoints),
                "ys": new Array(numPoints)};


                for (var p = 0; p < numPoints; p++) {
                pointsObject["trace_indexes"][p] =
                    pointObjects[p]["curveNumber"];
                pointsObject["point_indexes"][p] =
                    pointObjects[p]["pointNumber"];
                pointsObject["xs"][p] =
                    pointObjects[p]["x"];
                pointsObject["ys"][p] =
                    pointObjects[p]["y"];
            }

            // Add z if present
            var hasZ = pointObjects[0] !==
                undefined && pointObjects[0].hasOwnProperty("z");
            if (hasZ) {
                pointsObject["zs"] = new Array(numPoints);
                for (p = 0; p < numPoints; p++) {
                    pointsObject["zs"][p] = pointObjects[p]["z"];
                }
            }

            return pointsObject
        } else {
            return null
        }
    },

    /**
     * Build InputDeviceState data structure from data supplied by the
     * plotly_click, plotly_hover, or plotly_select events
     * @param {Object} data
     * @returns {null|InputDeviceState}
     */
    buildInputDeviceStateObject: function (data) {
        var event = data["event"];
        if (event === undefined) {
            return null;
        } else {
            /** @type {InputDeviceState} */
            var inputDeviceState = {
                // Keyboard modifiers
                "alt": event["altKey"],
                "ctrl": event["ctrlKey"],
                "meta": event["metaKey"],
                "shift": event["shiftKey"],

                // Mouse buttons
                "button": event["button"],
                "buttons": event["buttons"]
            };
            return inputDeviceState
        }
    },

    /**
     * Build Selector data structure from data supplied by the
     * plotly_select event
     * @param data
     * @returns {null|Selector}
     */
    buildSelectorObject: function(data) {

        var selectorObject;

        if (data.hasOwnProperty("range")) {
            // Box selection
            selectorObject = {
                type: "box",
                selector_state: {
                    xrange: data["range"]["x"],
                    yrange: data["range"]["y"]
                }
            };
        } else if (data.hasOwnProperty("lassoPoints")) {
            // Lasso selection
            selectorObject = {
                type: "lasso",
                selector_state: {
                    xs: data["lassoPoints"]["x"],
                    ys: data["lassoPoints"]["y"]
                }
            };
        } else {
            selectorObject = null;
        }
        return selectorObject
    },

    /**
     * Handle ploty_restyle events emitted by the Plotly.js library
     * @param data
     */
    handle_plotly_restyle: function (data) {

        if (data === null || data === undefined) {
            // No data to report to the Python side
            return
        }

        if (data[0] && data[0].hasOwnProperty("_doNotReportToPy")) {
            // Restyle originated on the Python side
            return
        }

        // Unpack data
        var styleData = data[0];
        var styleTraces = data[1];

        // Construct restyle message to send to the Python side
        /** @type {Js2PyRestyleMsg} */
        var restyleMsg = {
            style_data: styleData,
            style_traces: styleTraces,
            source_view_id: this.viewID
        };

        // Log message
        console.log("plotly_restyle");
        console.log(restyleMsg);

        this.model.set("_js2py_restyle", restyleMsg);
        this.touch();
    },

    /**
     * Handle plotly_relayout events emitted by the Plotly.js library
     * @param data
     */
    handle_plotly_relayout: function (data) {

        if (data === null || data === undefined) {
            // No data to report to the Python side
            return
        }

        if (data.hasOwnProperty("_doNotReportToPy")) {
            // Relayout originated on the Python side
            return
        }

        /** @type {Js2PyRelayoutMsg} */
        var relayoutMsg = {
            relayout_data: data,
            source_view_id: this.viewID
        };

        // Log message
        console.log("plotly_relayout");
        console.log(relayoutMsg);

        this.model.set("_js2py_relayout", relayoutMsg);
        this.touch();
    },

    /**
     * Handle plotly_update events emitted by the Plotly.js library
     * @param data
     */
    handle_plotly_update: function (data) {

        if (data === null || data === undefined) {
            // No data to report to the Python side
            return
        }

        if (data["data"] &&
            data["data"][0].hasOwnProperty("_doNotReportToPy")) {
            // Update originated on the Python side
            return
        }

        /** @type {Js2PyUpdateMsg} */
        var updateMsg = {
            style_data: data["data"][0],
            style_traces: data["data"][1],
            layout_data: data["layout"],
            source_view_id: this.viewID
        };

        // Log message
        console.log("plotly_update");
        console.log(updateMsg);

        this.model.set("_js2py_update", updateMsg);
        this.touch();
    },

    /**
     * Handle plotly_click events emitted by the Plotly.js library
     * @param data
     */
    handle_plotly_click: function (data) {
        this._send_points_callback_message(data, "plotly_click");
    },

    /**
     * Handle plotly_hover events emitted by the Plotly.js library
     * @param data
     */
    handle_plotly_hover: function (data) {
        this._send_points_callback_message(data, "plotly_hover");
    },

    /**
     * Handle plotly_unhover events emitted by the Plotly.js library
     * @param data
     */
    handle_plotly_unhover: function (data) {
        this._send_points_callback_message(data, "plotly_unhover");
    },

    /**
     * Handle plotly_selected events emitted by the Plotly.js library
     * @param data
     */
    handle_plotly_selected: function (data) {
        this._send_points_callback_message(data, "plotly_selected");
    },

    /**
     * Build and send a points callback message to the Python side
     *
     * @param {Object} data
     *  data object as provided by the plotly_click, plotly_hover,
     *  plotly_unhover, or plotly_selected events
     * @param {String} event_type
     *  Name of the triggering event. One of 'plotly_click',
     *  'plotly_hover', 'plotly_unhover', or 'plotly_selected'
     * @private
     */
    _send_points_callback_message: function (data, event_type) {
        if (data === null || data === undefined) {
            // No data to report to the Python side
            return;
        }

        /** @type {Js2PyPointsCallbackMsg} */
        var pointsMsg = {
            event_type: event_type,
            points: this.buildPointsObject(data),
            device_state: this.buildInputDeviceStateObject(data),
            selector: this.buildSelectorObject(data)
        };

        if (pointsMsg["points"] !== null &&
            pointsMsg["points"] !== undefined) {

            this.model.set("_js2py_pointsCallback", pointsMsg);
            this.touch();
        }
    },

    /**
     * Stub for future handling of plotly_doubleclick
     * @param data
     */
    handle_plotly_doubleclick: function (data) {},


    /**
     * Handle Plotly.addTraces request
     */
    do_addTraces: function () {

        /** @type {Py2JsAddTracesMsg} */
        var msgData = this.model.get("_py2js_addTraces");

        console.log("Figure View: do_addTraces");

        if (msgData !== null) {
            console.log(msgData);

            // Save off original number of traces
            var prevNumTraces = this.el.data.length;

            var that = this;
            Plotly.addTraces(this.el, msgData.trace_data).then(function () {

                // ### Send trace deltas ###
                that._sendTraceDeltas(msgData.trace_edit_id);

                // ### Send layout delta ###
                var layout_edit_id = msgData.layout_edit_id;
                that._sendLayoutDelta(layout_edit_id);
            });
        }
    },

    /**
     * Handle Plotly.deleteTraces request
     */
    do_deleteTraces: function () {

        /** @type {Py2JsDeleteTracesMsg} */
        var msgData = this.model.get("_py2js_deleteTraces");

        console.log(["do_deleteTraces", msgData]);
        if (msgData  !== null){
            var delete_inds = msgData.delete_inds;
            var that = this;
            Plotly.deleteTraces(this.el, delete_inds).then(function () {

                // ### Send trace deltas ###
                var trace_edit_id = msgData.trace_edit_id;
                that._sendTraceDeltas(trace_edit_id);

                // ### Send layout delta ###
                var layout_edit_id = msgData.layout_edit_id;
                that._sendLayoutDelta(layout_edit_id);
            });
        }
    },

    /**
     * Handle Plotly.moveTraces request
     */
    do_moveTraces: function () {

        /** @type {Py2JsMoveTracesMsg} */
        var msgData = this.model.get("_py2js_moveTraces");
        console.log("do_moveTraces");

        if (msgData !== null){
            // Unpack message
            var currentInds = msgData.current_trace_inds;
            var newInds = msgData.new_trace_inds;

            // Check if the new trace indexes are actually different than
            // the current indexes
            var inds_equal = _.isEqual(currentInds, newInds);

            if (!inds_equal) {
                Plotly.moveTraces(this.el, currentInds, newInds)
            }
        }
    },

    /**
     * Handle Plotly.restyle request
     */
    do_restyle: function () {
        console.log("do_restyle");

        /** @type {Py2JsRestyleMsg} */
        var msgData = this.model.get("_py2js_restyle");
        console.log(msgData);
        if (msgData !== null) {
            var restyleData = msgData.restyle_data;
            var traceIndexes = this.model._normalize_trace_indexes(
                msgData.restyle_traces);

            restyleData["_doNotReportToPy"] = true;
            Plotly.restyle(this.el, restyleData, traceIndexes);

            // ### Send trace deltas ###
            // We create an array of deltas corresponding to the restyled
            // traces.
            this._sendTraceDeltas(msgData.trace_edit_id);

            // ### Send layout delta ###
            var layout_edit_id = msgData.layout_edit_id;
            this._sendLayoutDelta(layout_edit_id);
        }
    },

    /**
     * Handle Plotly.relayout request
     */
    do_relayout: function () {
        console.log("FigureView: do_relayout");

        /** @type {Py2JsRelayoutMsg} */
        var msgData = this.model.get("_py2js_relayout");
        if (msgData !== null) {
            if (msgData.source_view_id !== this.viewID) {
                var relayoutData = msgData.relayout_data;
                relayoutData["_doNotReportToPy"] = true;
                Plotly.relayout(this.el, msgData.relayout_data);
            }

            // ### Send layout delta ###
            var layout_edit_id = msgData.layout_edit_id;
            this._sendLayoutDelta(layout_edit_id);
        }
    },

    /**
     * Handle Plotly.update request
     */
    do_update: function () {
        console.log("FigureView: do_update");

        /** @type {Py2JsUpdateMsg} */
        var msgData = this.model.get("_py2js_update");

        if (msgData !== null) {
            var style = msgData.style_data || {};
            var layout = msgData.layout_data || {};
            var traceIndexes = this.model._normalize_trace_indexes(
                msgData.style_traces);

            style["_doNotReportToPy"] = true;
                Plotly.update(this.el, style, layout, traceIndexes);

            // ### Send trace deltas ###
            // We create an array of deltas corresponding to the updated
            // traces.
            this._sendTraceDeltas(msgData.trace_edit_id);

            // ### Send layout delta ###
            var layout_edit_id = msgData.layout_edit_id;
            this._sendLayoutDelta(layout_edit_id);
        }
    },

    /**
     * Handle Plotly.animate request
     */
    do_animate: function() {
        console.log("FigureView: do_animate");

        /** @type {Py2JsAnimateMsg} */
        var msgData = this.model.get("_py2js_animate");

        if (msgData !== null) {

            // Unpack params
            // var animationData = msgData[0];
            var animationOpts = msgData.animation_opts;

            var styles = msgData.style_data;
            var layout = msgData.layout_data;
            var traceIndexes = this.model._normalize_trace_indexes(
                msgData.style_traces);

            var animationData = {
                data: styles,
                layout: layout,
                traces: traceIndexes
            };

            animationData["_doNotReportToPy"] = true;
            var that = this;

            Plotly.animate(this.el, animationData, animationOpts).then(
                function () {

                    // ### Send trace deltas ###
                    // We create an array of deltas corresponding to the
                    // animated traces.
                    that._sendTraceDeltas(msgData.trace_edit_id);

                    // ### Send layout delta ###
                    var layout_edit_id = msgData.layout_edit_id;
                    that._sendLayoutDelta(layout_edit_id);
                });

        }
    },

    /**
     * Construct layout delta object and send layoutDelta message to the
     * Python side
     *
     * @param layout_edit_id
     *  Edit ID of message that triggered the creation of the layout delta
     * @private
     */
    _sendLayoutDelta: function(layout_edit_id) {
        // ### Handle layout delta ###
        var layout_delta = createDeltaObject(
            this.getFullLayout(),
            this.model.get("_layout"));

        /** @type{Js2PyLayoutDeltaMsg} */
        var layoutDeltaMsg = {
            layout_delta: layout_delta,
            layout_edit_id: layout_edit_id};

        this.model.set("_js2py_layoutDelta", layoutDeltaMsg);
        this.touch();
    },

    /**
     * Construct trace deltas array for the requested trace indexes and
     * send traceDeltas message to the Python side
     *  Array of indexes of traces for which to compute deltas
     * @param trace_edit_id
     *  Edit ID of message that triggered the creation of trace deltas
     * @private
     */
    _sendTraceDeltas: function (trace_edit_id) {

        var trace_data = this.model.get("_data");
        var traceIndexes = _.range(trace_data.length);
        var trace_deltas = new Array(traceIndexes.length);

        var fullData = this.getFullData();
        for (var i = 0; i < traceIndexes.length; i++) {
            var traceInd = traceIndexes[i];
            trace_deltas[i] = createDeltaObject(
                fullData[traceInd], trace_data[traceInd]);
        }

        /** @type{Js2PyTraceDeltasMsg} */
        var traceDeltasMsg = {
            trace_deltas: trace_deltas,
            trace_edit_id: trace_edit_id};

        console.log(["traceDeltasMsg", traceDeltasMsg]);
        this.model.set("_js2py_traceDeltas", traceDeltasMsg);
        this.touch();
    }
});

// Serialization
/**
 * Create a mapping from numpy dtype strings to corresponding typed array
 * constructors
 */
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

function serializeTypedArray(v) {
    var numpyType;
    if (v instanceof Int8Array) {
        numpyType = 'int8';
    } else if (v instanceof Int16Array) {
        numpyType = 'int16';
    } else if (v instanceof Int32Array) {
        numpyType = 'int32';
    } else if (v instanceof Uint8Array) {
        numpyType = 'uint8';
    } else if (v instanceof Uint16Array) {
        numpyType = 'uint16';
    } else if (v instanceof Uint32Array) {
        numpyType = 'uint32';
    } else if (v instanceof Float32Array) {
        numpyType = 'float32';
    } else if (v instanceof Float64Array) {
        numpyType = 'float64';
    } else {
        // Don't understand it, return as is
        return v;
    }
    var res = {
        dtype: numpyType,
        shape: [v.length],
        value: v.buffer
    };
    return res
}

/**
 * ipywidget JavaScript -> Python serializer
 */
function js2py_serializer(v, widgetManager) {
    var res;

    if (_.isTypedArray(v)) {
        res = serializeTypedArray(v);
    } else if (Array.isArray(v)) {
        // Serialize array elements recursively
        res = new Array(v.length);
        for (var i = 0; i < v.length; i++) {
            res[i] = js2py_serializer(v[i]);
        }
    } else if (_.isPlainObject(v)) {
        // Serialize object properties recursively
        res = {};
        for (var p in v) {
            if (v.hasOwnProperty(p)) {
                res[p] = js2py_serializer(v[p]);
            }
        }
    } else if (v === undefined) {
        // Translate undefined into '_undefined_' sentinal string. The
        // Python _js_to_py deserializer will convert this into an
        // Undefined object
        res = "_undefined_";
    } else {
        // Primitive value to transfer directly
        res = v;
    }
    return res
}

/**
 * ipywidget Python -> Javascript deserializer
 */
function py2js_deserializer(v, widgetManager) {
    var res;

    if (Array.isArray(v)) {
        // Deserialize array elements recursively
        res = new Array(v.length);
        for (var i = 0; i < v.length; i++) {
            res[i] = py2js_deserializer(v[i]);
        }
    } else if (_.isPlainObject(v)) {
        if ((_.has(v, 'value') || _.has(v, 'buffer')) &&
            _.has(v, 'dtype') &&
            _.has(v, 'shape')) {
            // Deserialize special buffer/dtype/shape objects into typed arrays
            // These objects correspond to numpy arrays on the Python side
            //
            // Note plotly.py<=3.1.1 called the buffer object `buffer`
            // This was renamed `value` in 3.2 to work around a naming conflict
            // when saving widget state to a notebook.
            var typedarray_type = numpy_dtype_to_typedarray_type[v.dtype];
            var buffer = _.has(v, 'value')? v.value.buffer: v.buffer.buffer;
            res = new typedarray_type(buffer);
        } else {
            // Deserialize object properties recursively
            res = {};
            for (var p in v) {
                if (v.hasOwnProperty(p)) {
                    res[p] = py2js_deserializer(v[p]);
                }
            }
        }
    } else if (v === "_undefined_") {
        // Convert the _undefined_ sentinal into undefined
        res = undefined;
    } else {
        // Accept primitive value directly
        res = v;
    }
    return res
}

/**
 * Return whether the input value is a typed array
 * @param potentialTypedArray
 *  Value to examine
 * @returns {boolean}
 */
function isTypedArray(potentialTypedArray) {
    return ArrayBuffer.isView(potentialTypedArray) &&
        !(potentialTypedArray instanceof DataView);
}

/**
 * Customizer for use with lodash's mergeWith function
 *
 * The customizer ensures that typed arrays are not converted into standard
 * arrays during the recursive merge
 *
 * See: https://lodash.com/docs/latest#mergeWith
 */
function fullMergeCustomizer(objValue, srcValue) {
    if (isTypedArray(srcValue)) {
        // Return typed arrays directly, don't recurse inside
        return srcValue
    }
}

/**
 * Reform a Plotly.relayout like operation on an input object
 *
 * @param {Object} parentObj
 *  The object that the relayout operation should be applied to
 * @param {Object} relayoutData
 *  An relayout object as accepted by Plotly.relayout
 *
 *  Examples:
 *      var d = {foo {bar [5, 10]}};
 *      performRelayoutLike(d, {'foo.bar': [0, 1]});
 *      d -> {foo: {bar: [0, 1]}}
 *
 *      var d = {foo {bar [5, 10]}};
 *      performRelayoutLike(d, {'baz': 34});
 *      d -> {foo: {bar: [5, 10]}, baz: 34}
 *
 *      var d = {foo: {bar: [5, 10]};
 *      performRelayoutLike(d, {'foo.baz[1]': 17});
 *      d -> {foo: {bar: [5, 17]}}
 *
 */
function performRelayoutLike(parentObj, relayoutData) {
    // Perform a relayout style operation on a given parent object
    for (var rawKey in relayoutData) {
        if (!relayoutData.hasOwnProperty(rawKey)) {
            continue
        }

        // Extract value for this key
        var relayoutVal = relayoutData[rawKey];

        // Set property value
        if (relayoutVal === null) {
            _.unset(parentObj, rawKey);
        } else {
            _.set(parentObj, rawKey, relayoutVal);
        }
    }
}

/**
 * Perform a Plotly.restyle like operation on an input object array
 *
 * @param {Array.<Object>} parentArray
 *  The object that the restyle operation should be applied to
 * @param {Object} restyleData
 *  A restyle object as accepted by Plotly.restyle
 * @param {Array.<Number>} restyleTraces
 *  Array of indexes of the traces that the resytle operation applies to
 *
 *  Examples:
 *      var d = [{foo: {bar: 1}}, {}, {}]
 *      performRestyleLike(d, {'foo.bar': 2}, [0])
 *      d -> [{foo: {bar: 2}}, {}, {}]
 *
 *      var d = [{foo: {bar: 1}}, {}, {}]
 *      performRestyleLike(d, {'foo.bar': 2}, [0, 1, 2])
 *      d -> [{foo: {bar: 2}}, {foo: {bar: 2}}, {foo: {bar: 2}}]
 *
 *      var d = [{foo: {bar: 1}}, {}, {}]
 *      performRestyleLike(d, {'foo.bar': [2, 3, 4]}, [0, 1, 2])
 *      d -> [{foo: {bar: 2}}, {foo: {bar: 3}}, {foo: {bar: 4}}]
 *
 */
function performRestyleLike(parentArray, restyleData, restyleTraces) {
    // Loop over the properties of restyleData
    for (var rawKey in restyleData) {
        if (!restyleData.hasOwnProperty(rawKey)) { continue }

        // Extract value for property and normalize into a value list
        var valArray = restyleData[rawKey];
        if (!Array.isArray(valArray)) {
            valArray = [valArray]
        }

        // Loop over the indexes of the traces being restyled
        for (var i = 0; i < restyleTraces.length; i++) {

            // Get trace object
            var traceInd = restyleTraces[i];
            var trace = parentArray[traceInd];

            // Extract value for this trace
            var singleVal = valArray[i % valArray.length];

            // Set property value
            if (singleVal === null) {
                _.unset(trace, rawKey);
            } else if (singleVal !== undefined){
                _.set(trace, rawKey, singleVal);
            }
        }
    }
}

/**
 * Perform a Plotly.moveTraces like operation on an input object array
 * @param parentArray
 *  The object that the moveTraces operation should be applied to
 * @param currentInds
 *  Array of the current indexes of traces to be moved
 * @param newInds
 *  Array of the new indexes that traces selected by currentInds should be
 *  moved to.
 *
 *  Examples:
 *      var d = [{foo: 0}, {foo: 1}, {foo: 2}]
 *      performMoveTracesLike(d, [0, 1], [2, 0])
 *      d -> [{foo: 1}, {foo: 2}, {foo: 0}]
 *
 *      var d = [{foo: 0}, {foo: 1}, {foo: 2}]
 *      performMoveTracesLike(d, [0, 2], [1, 2])
 *      d -> [{foo: 1}, {foo: 0}, {foo: 2}]
 */
function performMoveTracesLike(parentArray, currentInds, newInds) {

    // ### Remove by currentInds in reverse order ###
    var movingTracesData = [];
    for (var ci = currentInds.length - 1; ci >= 0; ci--) {
        // Insert moving parentArray at beginning of the list
        movingTracesData.splice(0, 0, parentArray[currentInds[ci]]);
        parentArray.splice(currentInds[ci], 1);
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
        parentArray.splice(newInds[ni], 0, movingTracesData[ni]);
    }
}

/**
 * Remove nested properties from a parent object
 * @param {Object} parentObj
 *  Parent object from which properties or nested properties should be removed
 * @param {Array.<Array.<Number|String>>} keyPaths
 *  Array of key paths for properties that should be removed. Each key path
 *  is an array of properties names or array indexes that reference a
 *  property to be removed
 *
 *  Examples:
 *      var d = {foo: [{bar: 0}, {bar: 1}], baz: 32}
 *      performRemoveProps(d, ['baz'])
 *      d -> {foo: [{bar: 0}, {bar: 1}]}
 *
 *      var d = {foo: [{bar: 0}, {bar: 1}], baz: 32}
 *      performRemoveProps(d, ['foo[1].bar', 'baz'])
 *      d -> {foo: [{bar: 0}, {}]}
 *
 */
function performRemoveProps(parentObj, keyPaths) {

    for(var i=0; i < keyPaths.length; i++) {
        var keyPath = keyPaths[i];
        _.unset(parentObj, keyPath);
    }
}


/**
 * Return object that contains all properties in fullObj that are not
 * identical to the corresponding properties in removeObj
 *
 * Properties of fullObj and removeObj may be objects or arrays of objects
 *
 * Returned object is a deep clone of the properties of the input objects
 *
 * @param {Object} fullObj
 * @param {Object} removeObj
 *
 *  Examples:
 *      var fullD = {foo: [{bar: 0}, {bar: 1}], baz: 32}
 *      var removeD = {baz: 32}
 *      createDeltaObject(fullD, removeD)
 *          -> {foo: [{bar: 0}, {bar: 1}]}
 *
 *      var fullD = {foo: [{bar: 0}, {bar: 1}], baz: 32}
 *      var removeD = {baz: 45}
 *      createDeltaObject(fullD, removeD)
 *          -> {foo: [{bar: 0}, {bar: 1}], baz: 32}
 *
 *      var fullD = {foo: [{bar: 0}, {bar: 1}], baz: 32}
 *      var removeD = {foo: [{bar: 0}, {bar: 1}]}
 *      createDeltaObject(fullD, removeD)
 *          -> {baz: 32}
 *
 */
function createDeltaObject(fullObj, removeObj) {

    // Initialize result as object or array
    var res;
    if(Array.isArray(fullObj)) {
        res = new Array(fullObj.length);
    } else {
        res = {};
    }

    // Initialize removeObj to empty object if not specified
    if (removeObj === null || removeObj === undefined) {
        removeObj = {};
    }

    // Iterate over object properties or array indices
    for (var p in fullObj) {
        if (p[0] !== "_" &&  // Don't consider private properties
            fullObj.hasOwnProperty(p) &&  // Exclude parent properties
            fullObj[p] !== null  // Exclude cases where fullObj doesn't
                                 // have the property
        ) {
            // Compute object equality
            var props_equal;
            props_equal = _.isEqual(fullObj[p], removeObj[p]);

            // Perform recursive comparison if props are not equal
            if (!props_equal || p === "uid") {  // Let uids through

                // property has non-null value in fullObj that doesn't
                // match the value in removeObj
                var fullVal = fullObj[p];
                if (removeObj.hasOwnProperty(p) &&
                    typeof fullVal === "object") {
                    // Recurse over object properties
                    if(Array.isArray(fullVal)) {

                        if (fullVal.length > 0 &&
                            typeof(fullVal[0]) === "object") {
                            // We have an object array
                            res[p] = new Array(fullVal.length);
                            for (var i = 0; i < fullVal.length; i++) {
                                if (!Array.isArray(removeObj[p]) ||
                                    removeObj[p].length <= i) {

                                    res[p][i] = fullVal[i]
                                } else {
                                    res[p][i] = createDeltaObject(fullVal[i],
                                        removeObj[p][i]);
                                }
                            }
                        } else {
                            // We have a primitive array or typed array
                            res[p] = fullVal;
                        }
                    } else { // object
                        var full_obj = createDeltaObject(fullVal,
                            removeObj[p]);
                        if (Object.keys(full_obj).length > 0) {
                            // new object is not empty
                            res[p] = full_obj;
                        }
                    }
                } else if (typeof fullVal === "object" &&
                    !Array.isArray(fullVal)) {
                    // Return 'clone' of fullVal
                    // We don't use a standard clone method so that we keep
                    // the special case handling of this method
                    res[p] = createDeltaObject(fullVal, {});

                } else if (fullVal !== undefined &&
                    typeof fullVal !== 'function') {
                    // No recursion necessary, Just keep value from fullObj.
                    // But skip values with function type
                    res[p] = fullVal;
                }
            }
        }
    }
    return res
}

module.exports = {
    FigureView : FigureView,
    FigureModel: FigureModel
};
