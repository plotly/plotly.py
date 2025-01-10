import _ from "lodash-es";
import Plotly from "plotly.js";

// @ts-ignore
window.PlotlyConfig = { MathJaxConfig: "local" };

type InputDeviceState = {
  alt: any;
  ctrl: any;
  meta: any;
  shift: any;
  button: any;
  buttons: any;
};

type Js2PyLayoutDeltaMsg = {
  layout_delta: any;
  layout_edit_id: any;
};

type Js2PyMsg = {
  source_view_id: string;
};

type Js2PyPointsCallbackMsg = {
  event_type: string;
  points: Points;
  device_state: InputDeviceState;
  selector: Selector;
};

type Js2PyRelayoutMsg = Js2PyMsg & {
  relayout_data: any;
};

type Js2PyRestyleMsg = Js2PyMsg & {
  style_data: any;
  style_traces?: null | number | number[];
};

type Js2PyTraceDeltasMsg = {
  trace_deltas: any;
  trace_edit_id: any;
};

type Js2PyUpdateMsg = Js2PyMsg & {
  style_data: any;
  layout_data: any;
  style_traces?: null | number | number[];
};

type Points = {
  trace_indexes: number[];
  point_indexes: number[];
  xs: number[];
  ys: number[];
  zs?: number[];
};

type Py2JsMsg = {
  trace_edit_id?: any;
  layout_edit_id?: any;
  source_view_id?: any;
};

type Py2JsAddTracesMsg = Py2JsMsg & {
  trace_data: any;
};

type Py2JsAnimateMsg = Py2JsMsg & {
  style_data: any;
  layout_data: any;
  style_traces?: null | number | number[];
  animation_opts?: any;
};

type Py2JsDeleteTracesMsg = Py2JsMsg & {
  delete_inds: number[];
};

type Py2JsMoveTracesMsg = {
  current_trace_inds: number[];
  new_trace_inds: number[];
};

type Py2JsRestyleMsg = Py2JsMsg & {
  restyle_data: any;
  restyle_traces?: null | number | number[];
};

type Py2JsRelayoutMsg = Py2JsMsg & {
  relayout_data: any;
};

type Py2JsRemoveLayoutPropsMsg = {
  remove_props: any;
};

type Py2JsRemoveTracePropsMsg = {
  remove_props: any;
  remove_trace: any;
};

type Py2JsUpdateMsg = Py2JsMsg & {
  style_data: any;
  layout_data: any;
  style_traces?: null | number | number[];
};

type Selector = {
  type: "box" | "lasso";
  selector_state:
    | { xrange: number[]; yrange: number[] }
    | { xs: number[]; ys: number[] };
};

// Model
// =====
/**
 * A FigureModel holds a mirror copy of the state of a FigureWidget on
 * the Python side.  There is a one-to-one relationship between JavaScript
 * FigureModels and Python FigureWidgets. The JavaScript FigureModel is
 * initialized as soon as a Python FigureWidget initialized, this happens
 * even before the widget is first displayed in the Notebook
 */

type Serializer<In=any, Out=any> = {
  deserialize(value: Out): In;
  serialize(value: In): Out;
}

export class FigureModel {
  model;
  serializers: Record<string, Serializer>

  constructor(model, serializers: Record<string, Serializer>) {
    this.model = model;
    this.serializers = serializers;
  }

  get(key: string) {
    const serializer = this.serializers[key];
    const update = this.model.get(key)
    if (serializer?.deserialize) {
      return serializer.deserialize(update)
    }
    return update;
  }

  set(key: string, value: unknown) {
    let serializer = this.serializers[key];
    if (serializer?.serialize) {
      value = serializer.serialize(value)
    }
    this.model.set(key, value);
  }
  
  on(event: string, cb?: () => void) {
    this.model.on(event, cb);
  }

  save_changes() {
    this.model.save_changes();
  }

  defaults() {
    return {

      // Data and Layout
      // ---------------
      // The _widget_data and _widget_layout properties are synchronized with the
      // Python side on initialization only.  After initialization, these
      // properties are kept in sync through the use of the _py2js_*
      // messages
      _widget_data: [],
      _widget_layout: {},
      _config: {},

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
       *  inside the _widget_layout object
       */
      _py2js_removeLayoutProps: null,

      /**
       * @typedef {null|Object} Py2JsRemoveTracePropsMsg
       * @property {Number} remove_trace
       *  The index of the trace from which to remove properties
       * @property {Array.<Array.<String|Number>>} remove_props
       *  Array of property paths to remove. Each propery path is an
       *  array of property names or array indexes that locate a property
       *  inside the _widget_data[remove_trace] object
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
       *  FigureModel's _widget_layout property
       * @property {Number} layout_edit_id
       *  Edit ID of message that triggered the creation of layout delta
       */
      _js2py_layoutDelta: null,

      /**
       * @typedef {null|Object} Js2PyTraceDeltasMsg
       * @property {Array.<Object>} trace_deltas
       *  Array of trace delta objects. Each trace delta contains the
       *  trace's uid along with all of the properties of _fullData that
       *  are not identical to those in the FigureModel's _widget_data property
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
      _last_trace_edit_id: 0,
    };
  }

  /**
   * Initialize FigureModel. Called when the Python FigureWidget is first
   * constructed
   */
  initialize() {
    this.model.on("change:_widget_data", () => this.do_data());
    this.model.on("change:_widget_layout", () => this.do_layout());
    this.model.on("change:_py2js_addTraces", () => this.do_addTraces());
    this.model.on("change:_py2js_deleteTraces", () => this.do_deleteTraces());
    this.model.on("change:_py2js_moveTraces", () => this.do_moveTraces());
    this.model.on("change:_py2js_restyle", () => this.do_restyle());
    this.model.on("change:_py2js_relayout", () => this.do_relayout());
    this.model.on("change:_py2js_update", () => this.do_update());
    this.model.on("change:_py2js_animate", () => this.do_animate());
    this.model.on("change:_py2js_removeLayoutProps", () => this.do_removeLayoutProps());
    this.model.on("change:_py2js_removeTraceProps", () => this.do_removeTraceProps());
  }

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
  _normalize_trace_indexes(trace_indexes?: null | number | number[]): number[] {
    if (trace_indexes === null || trace_indexes === undefined) {
      var numTraces = this.model.get("_widget_data").length;
      trace_indexes = _.range(numTraces);
    }
    if (!Array.isArray(trace_indexes)) {
      // Make sure idx is an array
      trace_indexes = [trace_indexes];
    }
    return trace_indexes;
  }

  /**
   * Log changes to the _widget_data trait
   *
   * This should only happed on FigureModel initialization
   */
  do_data() {}

  /**
   * Log changes to the _widget_layout trait
   *
   * This should only happed on FigureModel initialization
   */
  do_layout() {}

  /**
   * Handle addTraces message
   */
  do_addTraces() {
    // add trace to plot
    /** @type {Py2JsAddTracesMsg} */
    var msgData: Py2JsAddTracesMsg = this.model.get("_py2js_addTraces");

    if (msgData !== null) {
      var currentTraces = this.model.get("_widget_data");
      var newTraces = msgData.trace_data;
      _.forEach(newTraces, function (newTrace) {
        currentTraces.push(newTrace);
      });
    }
  }

  /**
   * Handle deleteTraces message
   */
  do_deleteTraces() {
    // remove traces from plot

    /** @type {Py2JsDeleteTracesMsg} */
    var msgData: Py2JsDeleteTracesMsg = this.model.get("_py2js_deleteTraces");

    if (msgData !== null) {
      var delete_inds = msgData.delete_inds;
      var tracesData = this.model.get("_widget_data");

      // Remove del inds in reverse order so indexes remain valid
      // throughout loop
      delete_inds
        .slice()
        .reverse()
        .forEach(function (del_ind) {
          tracesData.splice(del_ind, 1);
        });
    }
  }

  /**
   * Handle moveTraces message
   */
  do_moveTraces() {
    /** @type {Py2JsMoveTracesMsg} */
    var msgData: Py2JsMoveTracesMsg = this.model.get("_py2js_moveTraces");

    if (msgData !== null) {
      var tracesData = this.model.get("_widget_data");
      var currentInds = msgData.current_trace_inds;
      var newInds = msgData.new_trace_inds;

      performMoveTracesLike(tracesData, currentInds, newInds);
    }
  }

  /**
   * Handle restyle message
   */
  do_restyle() {
    /** @type {Py2JsRestyleMsg} */
    var msgData: Py2JsRestyleMsg = this.model.get("_py2js_restyle");
    if (msgData !== null) {
      var restyleData = msgData.restyle_data;
      var restyleTraces = this._normalize_trace_indexes(msgData.restyle_traces);
      performRestyleLike(this.model.get("_widget_data"), restyleData, restyleTraces);
    }
  }

  /**
   * Handle relayout message
   */
  do_relayout() {
    /** @type {Py2JsRelayoutMsg} */
    var msgData: Py2JsRelayoutMsg = this.model.get("_py2js_relayout");

    if (msgData !== null) {
      performRelayoutLike(this.model.get("_widget_layout"), msgData.relayout_data);
    }
  }

  /**
   * Handle update message
   */
  do_update() {
    /** @type {Py2JsUpdateMsg} */
    var msgData: Py2JsUpdateMsg = this.model.get("_py2js_update");

    if (msgData !== null) {
      var style = msgData.style_data;
      var layout = msgData.layout_data;
      var styleTraces = this._normalize_trace_indexes(msgData.style_traces);
      performRestyleLike(this.model.get("_widget_data"), style, styleTraces);
      performRelayoutLike(this.model.get("_widget_layout"), layout);
    }
  }

  /**
   * Handle animate message
   */
  do_animate() {
    /** @type {Py2JsAnimateMsg} */
    var msgData: Py2JsAnimateMsg = this.model.get("_py2js_animate");
    if (msgData !== null) {
      var styles = msgData.style_data;
      var layout = msgData.layout_data;
      var trace_indexes = this._normalize_trace_indexes(msgData.style_traces);

      for (var i = 0; i < styles.length; i++) {
        var style = styles[i];
        var trace_index = trace_indexes[i];
        var trace = this.model.get("_widget_data")[trace_index];
        performRelayoutLike(trace, style);
      }

      performRelayoutLike(this.model.get("_widget_layout"), layout);
    }
  }

  /**
   * Handle removeLayoutProps message
   */
  do_removeLayoutProps() {
    /** @type {Py2JsRemoveLayoutPropsMsg} */
    var msgData: Py2JsRemoveLayoutPropsMsg = this.model.get(
      "_py2js_removeLayoutProps"
    );

    if (msgData !== null) {
      var keyPaths = msgData.remove_props;
      var layout = this.model.get("_widget_layout");
      performRemoveProps(layout, keyPaths);
    }
  }

  /**
   * Handle removeTraceProps message
   */
  do_removeTraceProps() {
    /** @type {Py2JsRemoveTracePropsMsg} */
    var msgData: Py2JsRemoveTracePropsMsg = this.model.get("_py2js_removeTraceProps");
    if (msgData !== null) {
      var keyPaths = msgData.remove_props;
      var traceIndex = msgData.remove_trace;
      var trace = this.model.get("_widget_data")[traceIndex];

      performRemoveProps(trace, keyPaths);
    }
  }
}

const serializers: Record<string, Serializer> = {
  _widget_data: {
    deserialize: py2js_deserializer,
    serialize: js2py_serializer,
  },
  _widget_layout: {
    deserialize: py2js_deserializer,
    serialize: js2py_serializer,
  },
  _py2js_addTraces: {
    deserialize: py2js_deserializer,
    serialize: js2py_serializer,
  },
  _py2js_deleteTraces: {
    deserialize: py2js_deserializer,
    serialize: js2py_serializer,
  },
  _py2js_moveTraces: {
    deserialize: py2js_deserializer,
    serialize: js2py_serializer,
  },
  _py2js_restyle: {
    deserialize: py2js_deserializer,
    serialize: js2py_serializer,
  },
  _py2js_relayout: {
    deserialize: py2js_deserializer,
    serialize: js2py_serializer,
  },
  _py2js_update: {
    deserialize: py2js_deserializer,
    serialize: js2py_serializer,
  },
  _py2js_animate: {
    deserialize: py2js_deserializer,
    serialize: js2py_serializer,
  },
  _py2js_removeLayoutProps: {
    deserialize: py2js_deserializer,
    serialize: js2py_serializer,
  },
  _py2js_removeTraceProps: {
    deserialize: py2js_deserializer,
    serialize: js2py_serializer,
  },
  _js2py_restyle: {
    deserialize: py2js_deserializer,
    serialize: js2py_serializer,
  },
  _js2py_relayout: {
    deserialize: py2js_deserializer,
    serialize: js2py_serializer,
  },
  _js2py_update: {
    deserialize: py2js_deserializer,
    serialize: js2py_serializer,
  },
  _js2py_layoutDelta: {
    deserialize: py2js_deserializer,
    serialize: js2py_serializer,
  },
  _js2py_traceDeltas: {
    deserialize: py2js_deserializer,
    serialize: js2py_serializer,
  },
  _js2py_pointsCallback: {
    deserialize: py2js_deserializer,
    serialize: js2py_serializer,
  },
};

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
export class FigureView {
  viewID: string;
  resizeEventListener: () => void;

  model: FigureModel;
  el: HTMLElement;

  constructor(model: FigureModel, el: HTMLElement) {
    this.model = model;
    this.el = el;
  }

  /**
   * The perform_render method is called by processLuminoMessage
   * after the widget's DOM element has been attached to the notebook
   * output cell. This happens after the initialize of the
   * FigureModel, and it won't happen at all if the Python FigureWidget
   * is never displayed in a notebook output cell
   */
  perform_render() {
    var that = this;

    // Wire up message property callbacks
    // ----------------------------------
    // Python -> JS event properties
    this.model.on("change:_py2js_addTraces", () => this.do_addTraces());
    this.model.on("change:_py2js_deleteTraces", () => this.do_deleteTraces());
    this.model.on("change:_py2js_moveTraces", () => this.do_moveTraces());
    this.model.on("change:_py2js_restyle", () => this.do_restyle());
    this.model.on("change:_py2js_relayout", () => this.do_relayout());
    this.model.on("change:_py2js_update", () => this.do_update());
    this.model.on("change:_py2js_animate", () => this.do_animate());

    // MathJax v2 configuration
    // ---------------------
    (window as any)?.MathJax?.Hub?.Config?.({ SVG: { font: "STIX-Web" } });

    // Get message ids
    // ---------------------
    var layout_edit_id = this.model.get("_last_layout_edit_id");
    var trace_edit_id = this.model.get("_last_trace_edit_id");

    // Set view UID
    // ------------
    this.viewID = randstr();

    // Initialize Plotly.js figure
    // ---------------------------
    // We must clone the model's data and layout properties so that
    // the model is not directly mutated by the Plotly.js library.
    var initialTraces = _.cloneDeep(this.model.get("_widget_data"));
    var initialLayout = _.cloneDeep(this.model.get("_widget_layout"));
    if (!initialLayout.height) {
      initialLayout.height = 360;
    }
    var config = this.model.get("_config");
    config.editSelection = false;

    Plotly.newPlot(that.el, initialTraces, initialLayout, config).then(
      function () {
        // ### Send trace deltas ###
        // We create an array of deltas corresponding to the new
        // traces.
        that._sendTraceDeltas(trace_edit_id);

        // ### Send layout delta ###
        that._sendLayoutDelta(layout_edit_id);

        // Wire up plotly event callbacks
        (<Plotly.PlotlyHTMLElement>that.el).on("plotly_restyle", function (update: any) {
          that.handle_plotly_restyle(update);
        });
        (<Plotly.PlotlyHTMLElement>that.el).on("plotly_relayout", function (update: any) {
          that.handle_plotly_relayout(update);
        });
        (<Plotly.PlotlyHTMLElement>that.el).on("plotly_update", function (update: any) {
          that.handle_plotly_update(update);
        });
        (<Plotly.PlotlyHTMLElement>that.el).on("plotly_click", function (update: any) {
          that.handle_plotly_click(update);
        });
        (<Plotly.PlotlyHTMLElement>that.el).on("plotly_hover", function (update: any) {
          that.handle_plotly_hover(update);
        });
        (<Plotly.PlotlyHTMLElement>that.el).on("plotly_unhover", function (update: any) {
          that.handle_plotly_unhover(update);
        });
        (<Plotly.PlotlyHTMLElement>that.el).on("plotly_selected", function (update: any) {
          that.handle_plotly_selected(update);
        });
        (<Plotly.PlotlyHTMLElement>that.el).on("plotly_deselect", function (update: any) {
          that.handle_plotly_deselect(update);
        });
        (<Plotly.PlotlyHTMLElement>that.el).on("plotly_doubleclick", function (update: any) {
          that.handle_plotly_doubleclick(update);
        });

        // Emit event indicating that the widget has finished
        // rendering
        var event = new CustomEvent("plotlywidget-after-render", {
          detail: { element: that.el, viewID: that.viewID },
        });

        // Dispatch/Trigger/Fire the event
        document.dispatchEvent(event);
      }
    );
  }

  /**
   * Respond to Lumino events
   */
  _processLuminoMessage(msg: any, _super: any) {
    _super.apply(this, arguments);
    var that = this;
    switch (msg.type) {
      case "before-attach":
        // Render an initial empty figure. This establishes with
        // the page that the element will not be empty, avoiding
        // some occasions where the dynamic sizing behavior leads
        // to collapsed figure dimensions.
        var axisHidden = {
          showgrid: false,
          showline: false,
          tickvals: [] as any[],
        };

        Plotly.newPlot(that.el, [], {
          xaxis: axisHidden,
          yaxis: axisHidden,
        });
        this.resizeEventListener = () => {
          this.autosizeFigure();
        }
        window.addEventListener("resize", this.resizeEventListener);
        break;
      case "after-attach":
        // Rendering actual figure in the after-attach event allows
        // Plotly.js to size the figure to fill the available element
        this.perform_render();
        break;
      case "after-show":
      case "resize":
        this.autosizeFigure();
        break;
    }
  }

  autosizeFigure() {
    var that = this;
    var layout = that.model.get("_widget_layout");
    if (_.isNil(layout) || _.isNil(layout.width)) {
      // @ts-ignore
      Plotly.Plots.resize(that.el).then(function () {
        var layout_edit_id = that.model.get("_last_layout_edit_id");
        that._sendLayoutDelta(layout_edit_id);
      });
    }
  }

  /**
   * Purge Plotly.js data structures from the notebook output display
   * element when the view is destroyed
   */
  remove() {
    Plotly.purge(this.el);
    window.removeEventListener("resize", this.resizeEventListener);
  }

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
  getFullData() {
    return _.mergeWith(
      {},
      (<Plotly.PlotlyHTMLElement>this.el)._fullData,
      (<Plotly.PlotlyHTMLElement>this.el).data,
      fullMergeCustomizer
    );
  }

  /**
   * Return the figure's _fullLayout object merged with its layout object
   *
   * See getFullData documentation for discussion of why the merge is
   * necessary
   */
  getFullLayout() {
    return _.mergeWith(
      {},
      (<Plotly.PlotlyHTMLElement>this.el)._fullLayout,
      (<Plotly.PlotlyHTMLElement>this.el).layout,
      fullMergeCustomizer
    );
  }

  /**
   * Build Points data structure from data supplied by the plotly_click,
   * plotly_hover, or plotly_select events
   * @param {Object} data
   * @returns {null|Points}
   */
  buildPointsObject(data: any): null | Points {
    var pointsObject: Points;
    if (data.hasOwnProperty("points")) {
      // Most cartesian plots
      var pointObjects = data["points"];
      var numPoints = pointObjects.length;

      var hasNestedPointObjects = true;
      for (let i = 0; i < numPoints; i++) {
        hasNestedPointObjects =
          hasNestedPointObjects &&
          pointObjects[i].hasOwnProperty("pointNumbers");
        if (!hasNestedPointObjects) break;
      }
      var numPointNumbers = numPoints;
      if (hasNestedPointObjects) {
        numPointNumbers = 0;
        for (let i = 0; i < numPoints; i++) {
          numPointNumbers += pointObjects[i]["pointNumbers"].length;
        }
      }
      pointsObject = {
        trace_indexes: new Array(numPointNumbers),
        point_indexes: new Array(numPointNumbers),
        xs: new Array(numPointNumbers),
        ys: new Array(numPointNumbers),
      };

      if (hasNestedPointObjects) {
        var flatPointIndex = 0;
        for (var p = 0; p < numPoints; p++) {
          for (
            let i = 0;
            i < pointObjects[p]["pointNumbers"].length;
            i++, flatPointIndex++
          ) {
            pointsObject["point_indexes"][flatPointIndex] =
              pointObjects[p]["pointNumbers"][i];
            // also add xs, ys and traces so that the array doesn't get truncated later
            pointsObject["xs"][flatPointIndex] = pointObjects[p]["x"];
            pointsObject["ys"][flatPointIndex] = pointObjects[p]["y"];
            pointsObject["trace_indexes"][flatPointIndex] =
              pointObjects[p]["curveNumber"];
          }
        }

        let single_trace = true;
        for (let i = 1; i < numPointNumbers; i++) {
          single_trace = single_trace && (pointsObject["trace_indexes"][i - 1] === pointsObject["trace_indexes"][i])
          if (!single_trace) break;
        }
        if (single_trace) {
          pointsObject["point_indexes"].sort((function (a, b) {
            return a - b
          }))
        }

      } else {
        for (var p = 0; p < numPoints; p++) {
          pointsObject["trace_indexes"][p] = pointObjects[p]["curveNumber"];
          pointsObject["point_indexes"][p] = pointObjects[p]["pointNumber"];
          pointsObject["xs"][p] = pointObjects[p]["x"];
          pointsObject["ys"][p] = pointObjects[p]["y"];
        }
      }

      // Add z if present
      var hasZ =
        pointObjects[0] !== undefined && pointObjects[0].hasOwnProperty("z");
      if (hasZ) {
        pointsObject["zs"] = new Array(numPoints);
        for (p = 0; p < numPoints; p++) {
          pointsObject["zs"][p] = pointObjects[p]["z"];
        }
      }

      return pointsObject;
    } else {
      return null;
    }
  }

  /**
   * Build InputDeviceState data structure from data supplied by the
   * plotly_click, plotly_hover, or plotly_select events
   * @param {Object} data
   * @returns {null|InputDeviceState}
   */
  buildInputDeviceStateObject(data: any): null | InputDeviceState {
    var event = data["event"];
    if (event === undefined) {
      return null;
    } else {
      /** @type {InputDeviceState} */
      var inputDeviceState: InputDeviceState = {
        // Keyboard modifiers
        alt: event["altKey"],
        ctrl: event["ctrlKey"],
        meta: event["metaKey"],
        shift: event["shiftKey"],

        // Mouse buttons
        button: event["button"],
        buttons: event["buttons"],
      };
      return inputDeviceState;
    }
  }

  /**
   * Build Selector data structure from data supplied by the
   * plotly_select event
   * @param data
   * @returns {null|Selector}
   */
  buildSelectorObject(data: any): null | Selector {
    var selectorObject: Selector;

    if (data.hasOwnProperty("range")) {
      // Box selection
      selectorObject = {
        type: "box",
        selector_state: {
          xrange: data["range"]["x"],
          yrange: data["range"]["y"],
        },
      };
    } else if (data.hasOwnProperty("lassoPoints")) {
      // Lasso selection
      selectorObject = {
        type: "lasso",
        selector_state: {
          xs: data["lassoPoints"]["x"],
          ys: data["lassoPoints"]["y"],
        },
      };
    } else {
      selectorObject = null;
    }
    return selectorObject;
  }

  /**
   * Handle ploty_restyle events emitted by the Plotly.js library
   * @param data
   */
  handle_plotly_restyle(data: any) {
    if (data === null || data === undefined) {
      // No data to report to the Python side
      return;
    }

    if (data[0] && data[0].hasOwnProperty("_doNotReportToPy")) {
      // Restyle originated on the Python side
      return;
    }

    // Unpack data
    var styleData = data[0];
    var styleTraces = data[1];

    // Construct restyle message to send to the Python side
    /** @type {Js2PyRestyleMsg} */
    var restyleMsg: Js2PyRestyleMsg = {
      style_data: styleData,
      style_traces: styleTraces,
      source_view_id: this.viewID,
    };

    this.model.set("_js2py_restyle", restyleMsg);
    this.touch();
  }

  touch() {
    this.model.save_changes();
  }

  /**
   * Handle plotly_relayout events emitted by the Plotly.js library
   * @param data
   */
  handle_plotly_relayout(data: any) {
    if (data === null || data === undefined) {
      // No data to report to the Python side
      return;
    }

    if (data.hasOwnProperty("_doNotReportToPy")) {
      // Relayout originated on the Python side
      return;
    }

    /** @type {Js2PyRelayoutMsg} */
    var relayoutMsg: Js2PyRelayoutMsg = {
      relayout_data: data,
      source_view_id: this.viewID,
    };

    this.model.set("_js2py_relayout", relayoutMsg);
    this.touch();
  }

  /**
   * Handle plotly_update events emitted by the Plotly.js library
   * @param data
   */
  handle_plotly_update(data: any) {
    if (data === null || data === undefined) {
      // No data to report to the Python side
      return;
    }

    if (data["data"] && data["data"][0].hasOwnProperty("_doNotReportToPy")) {
      // Update originated on the Python side
      return;
    }

    /** @type {Js2PyUpdateMsg} */
    var updateMsg: Js2PyUpdateMsg = {
      style_data: data["data"][0],
      style_traces: data["data"][1],
      layout_data: data["layout"],
      source_view_id: this.viewID,
    };

    // Log message
    this.model.set("_js2py_update", updateMsg);
    this.touch();
  }

  /**
   * Handle plotly_click events emitted by the Plotly.js library
   * @param data
   */
  handle_plotly_click(data: any) {
    this._send_points_callback_message(data, "plotly_click");
  }

  /**
   * Handle plotly_hover events emitted by the Plotly.js library
   * @param data
   */
  handle_plotly_hover(data: any) {
    this._send_points_callback_message(data, "plotly_hover");
  }

  /**
   * Handle plotly_unhover events emitted by the Plotly.js library
   * @param data
   */
  handle_plotly_unhover(data: any) {
    this._send_points_callback_message(data, "plotly_unhover");
  }

  /**
   * Handle plotly_selected events emitted by the Plotly.js library
   * @param data
   */
  handle_plotly_selected(data: any) {
    this._send_points_callback_message(data, "plotly_selected");
  }

  /**
   * Handle plotly_deselect events emitted by the Plotly.js library
   * @param data
   */
  handle_plotly_deselect(data: any) {
    data = {
      points: [],
    };
    this._send_points_callback_message(data, "plotly_deselect");
  }

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
  _send_points_callback_message(data: any, event_type: string) {
    if (data === null || data === undefined) {
      // No data to report to the Python side
      return;
    }

    /** @type {Js2PyPointsCallbackMsg} */
    var pointsMsg: Js2PyPointsCallbackMsg = {
      event_type: event_type,
      points: this.buildPointsObject(data),
      device_state: this.buildInputDeviceStateObject(data),
      selector: this.buildSelectorObject(data),
    };

    if (pointsMsg["points"] !== null && pointsMsg["points"] !== undefined) {
      this.model.set("_js2py_pointsCallback", pointsMsg);
      this.touch();
    }
  }

  /**
   * Stub for future handling of plotly_doubleclick
   * @param data
   */
  handle_plotly_doubleclick(data: any) {}

  /**
   * Handle Plotly.addTraces request
   */
  do_addTraces() {
    /** @type {Py2JsAddTracesMsg} */
    var msgData: Py2JsAddTracesMsg = this.model.get("_py2js_addTraces");

    if (msgData !== null) {
      var that = this;
      Plotly.addTraces(this.el, msgData.trace_data).then(function () {
        // ### Send trace deltas ###
        that._sendTraceDeltas(msgData.trace_edit_id);

        // ### Send layout delta ###
        var layout_edit_id = msgData.layout_edit_id;
        that._sendLayoutDelta(layout_edit_id);
      });
    }
  }

  /**
   * Handle Plotly.deleteTraces request
   */
  do_deleteTraces() {
    /** @type {Py2JsDeleteTracesMsg} */
    var msgData: Py2JsDeleteTracesMsg = this.model.get("_py2js_deleteTraces");

    if (msgData !== null) {
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
  }

  /**
   * Handle Plotly.moveTraces request
   */
  do_moveTraces() {
    /** @type {Py2JsMoveTracesMsg} */
    var msgData: Py2JsMoveTracesMsg = this.model.get("_py2js_moveTraces");

    if (msgData !== null) {
      // Unpack message
      var currentInds = msgData.current_trace_inds;
      var newInds = msgData.new_trace_inds;

      // Check if the new trace indexes are actually different than
      // the current indexes
      var inds_equal = _.isEqual(currentInds, newInds);

      if (!inds_equal) {
        Plotly.moveTraces(this.el, currentInds, newInds);
      }
    }
  }

  /**
   * Handle Plotly.restyle request
   */
  do_restyle() {
    /** @type {Py2JsRestyleMsg} */
    var msgData: Py2JsRestyleMsg = this.model.get("_py2js_restyle");
    if (msgData !== null) {
      var restyleData = msgData.restyle_data;
      var traceIndexes = (this.model as FigureModel)._normalize_trace_indexes(
        msgData.restyle_traces
      );

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
  }

  /**
   * Handle Plotly.relayout request
   */
  do_relayout() {
    /** @type {Py2JsRelayoutMsg} */
    var msgData: Py2JsRelayoutMsg = this.model.get("_py2js_relayout");
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
  }

  /**
   * Handle Plotly.update request
   */
  do_update() {
    /** @type {Py2JsUpdateMsg} */
    var msgData: Py2JsUpdateMsg = this.model.get("_py2js_update");

    if (msgData !== null) {
      var style = msgData.style_data || {};
      var layout = msgData.layout_data || {};
      var traceIndexes = (this.model as FigureModel)._normalize_trace_indexes(
        msgData.style_traces
      );

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
  }

  /**
   * Handle Plotly.animate request
   */
  do_animate() {
    /** @type {Py2JsAnimateMsg} */
    var msgData: Py2JsAnimateMsg = this.model.get("_py2js_animate");

    if (msgData !== null) {
      // Unpack params
      // var animationData = msgData[0];
      var animationOpts = msgData.animation_opts;

      var styles = msgData.style_data;
      var layout = msgData.layout_data;
      var traceIndexes = (this.model as FigureModel)._normalize_trace_indexes(
        msgData.style_traces
      );

      var animationData: any = {
        data: styles,
        layout: layout,
        traces: traceIndexes,
      };

      animationData["_doNotReportToPy"] = true;
      var that = this;

      // @ts-ignore
      Plotly.animate(this.el, animationData, animationOpts).then(function () {
        // ### Send trace deltas ###
        // We create an array of deltas corresponding to the
        // animated traces.
        that._sendTraceDeltas(msgData.trace_edit_id);

        // ### Send layout delta ###
        var layout_edit_id = msgData.layout_edit_id;
        that._sendLayoutDelta(layout_edit_id);
      });
    }
  }

  /**
   * Construct layout delta object and send layoutDelta message to the
   * Python side
   *
   * @param layout_edit_id
   *  Edit ID of message that triggered the creation of the layout delta
   * @private
   */
  _sendLayoutDelta(layout_edit_id: any) {
    // ### Handle layout delta ###
    var layout_delta = createDeltaObject(
      this.getFullLayout(),
      this.model.get("_widget_layout")
    );

    /** @type{Js2PyLayoutDeltaMsg} */
    var layoutDeltaMsg: Js2PyLayoutDeltaMsg = {
      layout_delta: layout_delta,
      layout_edit_id: layout_edit_id,
    };

    this.model.set("_js2py_widget_layoutDelta", layoutDeltaMsg);
    this.touch();
  }

  /**
   * Construct trace deltas array for the requested trace indexes and
   * send traceDeltas message to the Python side
   *  Array of indexes of traces for which to compute deltas
   * @param trace_edit_id
   *  Edit ID of message that triggered the creation of trace deltas
   * @private
   */
  _sendTraceDeltas(trace_edit_id: any) {
    var trace_data = this.model.get("_widget_data");
    var traceIndexes = _.range(trace_data.length);
    var trace_deltas = new Array(traceIndexes.length);

    var fullData = this.getFullData();
    for (var i = 0; i < traceIndexes.length; i++) {
      var traceInd = traceIndexes[i];
      trace_deltas[i] = createDeltaObject(
        fullData[traceInd],
        trace_data[traceInd]
      );
    }

    /** @type{Js2PyTraceDeltasMsg} */
    var traceDeltasMsg: Js2PyTraceDeltasMsg = {
      trace_deltas: trace_deltas,
      trace_edit_id: trace_edit_id,
    };

    this.model.set("_js2py_traceDeltas", traceDeltasMsg);
    this.touch();
  }
}

// Serialization
/**
 * Create a mapping from numpy dtype strings to corresponding typed array
 * constructors
 */
const numpy_dtype_to_typedarray_type = {
  int8: Int8Array,
  int16: Int16Array,
  int32: Int32Array,
  uint8: Uint8Array,
  uint16: Uint16Array,
  uint32: Uint32Array,
  float32: Float32Array,
  float64: Float64Array,
};

function serializeTypedArray(v: ArrayConstructor) {
  var numpyType;
  if (v instanceof Int8Array) {
    numpyType = "int8";
  } else if (v instanceof Int16Array) {
    numpyType = "int16";
  } else if (v instanceof Int32Array) {
    numpyType = "int32";
  } else if (v instanceof Uint8Array) {
    numpyType = "uint8";
  } else if (v instanceof Uint16Array) {
    numpyType = "uint16";
  } else if (v instanceof Uint32Array) {
    numpyType = "uint32";
  } else if (v instanceof Float32Array) {
    numpyType = "float32";
  } else if (v instanceof Float64Array) {
    numpyType = "float64";
  } else {
    // Don't understand it, return as is
    return v;
  }
  var res = {
    dtype: numpyType,
    shape: [v.length],
    value: v.buffer,
  };
  return res;
}

/**
 * ipywidget JavaScript -> Python serializer
 */
function js2py_serializer(v: any, widgetManager?: any) {
  var res: any;

  if (_.isTypedArray(v)) {
    res = serializeTypedArray(v);
  } else if (Array.isArray(v)) {
    // Serialize array elements recursively
    res = new Array(v.length);
    for (var i = 0; i < v.length; i++) {
      res[i] = js2py_serializer(v[i]);
    }
  } else if (_.isObject(v)) {
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
  return res;
}

/**
 * ipywidget Python -> Javascript deserializer
 */
function py2js_deserializer(v: any, widgetManager?: any) {
  var res: any;

  if (Array.isArray(v)) {
    // Deserialize array elements recursively
    res = new Array(v.length);
    for (var i = 0; i < v.length; i++) {
      res[i] = py2js_deserializer(v[i]);
    }
  } else if (_.isObject(v)) {
    if (
      (_.has(v, "value") || _.has(v, "buffer")) &&
      _.has(v, "dtype") &&
      _.has(v, "shape")
    ) {
      // Deserialize special buffer/dtype/shape objects into typed arrays
      // These objects correspond to numpy arrays on the Python side
      //
      // Note plotly.py<=3.1.1 called the buffer object `buffer`
      // This was renamed `value` in 3.2 to work around a naming conflict
      // when saving widget state to a notebook.
      // @ts-ignore
      var typedarray_type = numpy_dtype_to_typedarray_type[v.dtype];
      var buffer = _.has(v, "value") ? v.value.buffer : v.buffer.buffer;
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
  return res;
}

/**
 * Return whether the input value is a typed array
 * @param potentialTypedArray
 *  Value to examine
 * @returns {boolean}
 */
function isTypedArray(potentialTypedArray: any): boolean {
  return (
    ArrayBuffer.isView(potentialTypedArray) &&
    !(potentialTypedArray instanceof DataView)
  );
}

/**
 * Customizer for use with lodash's mergeWith function
 *
 * The customizer ensures that typed arrays are not converted into standard
 * arrays during the recursive merge
 *
 * See: https://lodash.com/docs/latest#mergeWith
 */
function fullMergeCustomizer(objValue: any, srcValue: any, key: string) {
  if (key[0] === "_") {
    // Don't recurse into private properties
    return null;
  } else if (isTypedArray(srcValue)) {
    // Return typed arrays directly, don't recurse inside
    return srcValue;
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
function performRelayoutLike(parentObj: any, relayoutData: any) {
  // Perform a relayout style operation on a given parent object
  for (var rawKey in relayoutData) {
    if (!relayoutData.hasOwnProperty(rawKey)) {
      continue;
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
function performRestyleLike(
  parentArray: any[],
  restyleData: any,
  restyleTraces: number[]
) {
  // Loop over the properties of restyleData
  for (var rawKey in restyleData) {
    if (!restyleData.hasOwnProperty(rawKey)) {
      continue;
    }

    // Extract value for property and normalize into a value list
    var valArray = restyleData[rawKey];
    if (!Array.isArray(valArray)) {
      valArray = [valArray];
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
      } else if (singleVal !== undefined) {
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
function performMoveTracesLike(
  parentArray: any[],
  currentInds: number[],
  newInds: number[]
) {
  // ### Remove by currentInds in reverse order ###
  var movingTracesData: any[] = [];
  for (var ci = currentInds.length - 1; ci >= 0; ci--) {
    // Insert moving parentArray at beginning of the list
    movingTracesData.splice(0, 0, parentArray[currentInds[ci]]);
    parentArray.splice(currentInds[ci], 1);
  }

  // ### Sort newInds and movingTracesData by newInds ###
  var newIndexSortedArrays = _(newInds)
    .zip(movingTracesData)
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
function performRemoveProps(
  parentObj: object,
  keyPaths: Array<Array<number | string>>
) {
  for (var i = 0; i < keyPaths.length; i++) {
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
function createDeltaObject(fullObj: any, removeObj: any) {
  // Initialize result as object or array
  var res: any;
  if (Array.isArray(fullObj)) {
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
    if (
      p[0] !== "_" && // Don't consider private properties
      fullObj.hasOwnProperty(p) && // Exclude parent properties
      fullObj[p] !== null // Exclude cases where fullObj doesn't
      // have the property
    ) {
      // Compute object equality
      var props_equal;
      props_equal = _.isEqual(fullObj[p], removeObj[p]);

      // Perform recursive comparison if props are not equal
      if (!props_equal || p === "uid") {
        // Let uids through

        // property has non-null value in fullObj that doesn't
        // match the value in removeObj
        var fullVal = fullObj[p];
        if (removeObj.hasOwnProperty(p) && typeof fullVal === "object") {
          // Recurse over object properties
          if (Array.isArray(fullVal)) {
            if (fullVal.length > 0 && typeof fullVal[0] === "object") {
              // We have an object array
              res[p] = new Array(fullVal.length);
              for (var i = 0; i < fullVal.length; i++) {
                if (!Array.isArray(removeObj[p]) || removeObj[p].length <= i) {
                  res[p][i] = fullVal[i];
                } else {
                  res[p][i] = createDeltaObject(fullVal[i], removeObj[p][i]);
                }
              }
            } else {
              // We have a primitive array or typed array
              res[p] = fullVal;
            }
          } else {
            // object
            var full_obj = createDeltaObject(fullVal, removeObj[p]);
            if (Object.keys(full_obj).length > 0) {
              // new object is not empty
              res[p] = full_obj;
            }
          }
        } else if (typeof fullVal === "object" && !Array.isArray(fullVal)) {
          // Return 'clone' of fullVal
          // We don't use a standard clone method so that we keep
          // the special case handling of this method
          res[p] = createDeltaObject(fullVal, {});
        } else if (fullVal !== undefined && typeof fullVal !== "function") {
          // No recursion necessary, Just keep value from fullObj.
          // But skip values with function type
          res[p] = fullVal;
        }
      }
    }
  }
  return res;
}

function randstr(
  existing?: { [k: string]: any },
  bits?: number,
  base?: number,
  _recursion?: number
): string {
  if (!base) base = 16;
  if (bits === undefined) bits = 24;
  if (bits <= 0) return "0";

  var digits = Math.log(Math.pow(2, bits)) / Math.log(base);
  var res = "";
  var i, b, x;

  for (i = 2; digits === Infinity; i *= 2) {
    digits = (Math.log(Math.pow(2, bits / i)) / Math.log(base)) * i;
  }

  var rem = digits - Math.floor(digits);

  for (i = 0; i < Math.floor(digits); i++) {
    x = Math.floor(Math.random() * base).toString(base);
    res = x + res;
  }

  if (rem) {
    b = Math.pow(base, rem);
    x = Math.floor(Math.random() * b).toString(base);
    res = x + res;
  }

  var parsed = parseInt(res, base);
  if (
    (existing && existing[res]) ||
    (parsed !== Infinity && parsed >= Math.pow(2, bits))
  ) {
    if (_recursion > 10) {
      console.warn("randstr failed uniqueness");
      return res;
    }
    return randstr(existing, bits, base, (_recursion || 0) + 1);
  } else return res;
}

export default () => {
  let model;
  return {
    /** @type {import('anywidget/types').Initialize<Model>} */
    initialize(ctx) {
      model = new FigureModel(ctx.model, serializers);
      model.initialize();
    },
    /** @type {import('anywidget/types').Render<Model>} */
    render({ el }) {
      const view = new FigureView(model, el);
      view.perform_render()
      return () => view.remove();
    }
  }
}
