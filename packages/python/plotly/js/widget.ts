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

// type Py2JsAnimateMsg = Py2JsMsg & {
//   style_data: any;
//   layout_data: any;
//   style_traces?: null | number | number[];
//   animation_opts?: any;
// };

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
      // The _data and _widget_layout properties are synchronized with the
      // Python side on initialization only.  After initialization, these
      // properties are kept in sync through the use of the _py2js_*
      // messages
      _data: [],
      _widget_layout: {},
      _config: {},

      // Python -> JS messages
      // ---------------------
      // Messages are implemented using trait properties. This is done so
      // this we can take advantage of ipywidget's binary serialization
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
       * @typedef {null|Object} Py2JsAnimateMsg
       * @property {Object} style_data
       *  Style data as accepted by Plotly.animate
       * @property {Object} layout_data
       *  Layout data as accepted by Plotly.animate
       * @property {Array.<Number>} style_traces
       *  Array of indexes of the traces this the animate operation applies
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
       *  view_id of the FigureView this triggered the original animate
       *  event (e.g. by clicking a button), or null if the update was
       *  triggered from Python
       */
    //   _py2js_animate: null,

      /**
       * @typedef {null|Object} Py2JsRemoveTracePropsMsg
       * @property {Number} remove_trace
       *  The index of the trace from which to remove properties
       * @property {Array.<Array.<String|Number>>} remove_props
       *  Array of property paths to remove. Each propery path is an
       *  array of property names or array indexes this locate a property
       *  inside the _data[remove_trace] object
       */
      _py2js_removeTraceProps: null,

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

    };
  }

  /**
   * Initialize FigureModel. Called when the Python FigureWidget is first
   * constructed
   */
  initialize() {
    this.model.on("change:_data", () => this.do_data());
    this.model.on("change:_widget_layout", () => this.do_layout());
    // this.model.on("change:_py2js_animate", () => this.do_animate());
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
      var numTraces = this.model.get("_data").length;
      trace_indexes = _.range(numTraces);
    }
    if (!Array.isArray(trace_indexes)) {
      // Make sure idx is an array
      trace_indexes = [trace_indexes];
    }
    return trace_indexes;
  }

  /**
   * Log changes to the _data trait
   *
   * This should only happed on FigureModel initialization
   */
  do_data() {}

  /**
   * Log changes to the _widget_layout trait
   *
   * This should only happed on FigureModel initialization
   */
  do_layout() {
    console.log("layout changed");
  }

  /**
   * Handle addTraces message
   */
  do_addTraces() {
    // add trace to plot
    /** @type {Py2JsAddTracesMsg} */
    var msgData: Py2JsAddTracesMsg = this.model.get("_py2js_addTraces");

    if (msgData !== null) {
      var currentTraces = this.model.get("_data");
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
      var tracesData = this.model.get("_data");

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
   * Handle animate message
   */
//   do_animate() {
//     /** @type {Py2JsAnimateMsg} */
//     var msgData: Py2JsAnimateMsg = this.model.get("_py2js_animate");
//     if (msgData !== null) {
//       var styles = msgData.style_data;
//       var layout = msgData.layout_data;
//       var trace_indexes = this._normalize_trace_indexes(msgData.style_traces);

//       for (var i = 0; i < styles.length; i++) {
//         var style = styles[i];
//         var trace_index = trace_indexes[i];
//         var trace = this.model.get("_data")[trace_index];
//       }

//     }
//   }
}

const serializers: Record<string, Serializer> = {
  _data: {
    deserialize: py2js_deserializer,
    serialize: js2py_serializer,
  },
  _widget_layout: {
    deserialize: py2js_deserializer,
    serialize: js2py_serializer,
  },
//   _py2js_animate: {
//     deserialize: py2js_deserializer,
//     serialize: js2py_serializer,
//   },
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

    model.on('change:_widget_layout', () => { 
        this.render();
    });
    model.on('change:_data', () => {
        this.render();
    });
  }

  /**
   * The perform_render method is called by processLuminoMessage
   * after the widget's DOM element has been attached to the notebook
   * output cell. This happens after the initialize of the
   * FigureModel, and it won't happen at all if the Python FigureWidget
   * is never displayed in a notebook output cell
   */
  render() {
    // Wire up message property callbacks
    // ----------------------------------
    // Python -> JS event properties
    // this.model.on("change:_py2js_animate", () => this.do_animate());

    // MathJax v2 configuration
    // ---------------------
    console.log('rerendering');
    (window as any)?.MathJax?.Hub?.Config?.({ SVG: { font: "STIX-Web" } });

    // Set view UID
    // ------------
    this.viewID = randstr();

    // Initialize Plotly.js figure
    // ---------------------------
    // We must clone the model's data and layout properties so that
    // the model is not directly mutated by the Plotly.js library.
    var initialTraces = _.cloneDeep(this.model.get("_data"));
    var initialLayout = _.cloneDeep(this.model.get("_widget_layout"));
    if (!initialLayout.height) {
      initialLayout.height = 360;
    }
    var config = this.model.get("_config");
    config.editSelection = false;

    const that = this;
    const handlePlotlyEvents = () => {
        // Wire up plotly event callbacks
        (<Plotly.PlotlyHTMLElement>this.el).on("plotly_click", function (update: any) {
            that.handle_plotly_click(update);
        });
        (<Plotly.PlotlyHTMLElement>this.el).on("plotly_hover", function (update: any) {
            that.handle_plotly_hover(update);
        });
        (<Plotly.PlotlyHTMLElement>this.el).on("plotly_unhover", function (update: any) {
            that.handle_plotly_unhover(update);
        });
        (<Plotly.PlotlyHTMLElement>this.el).on("plotly_selected", function (update: any) {
            that.handle_plotly_selected(update);
        });
        (<Plotly.PlotlyHTMLElement>this.el).on("plotly_deselect", function () {
            that.handle_plotly_deselect({});
        });
        (<Plotly.PlotlyHTMLElement>this.el).on("plotly_doubleclick", function () {
            that.handle_plotly_doubleclick({});
        });
    
        // Emit event indicating this the widget has finished
        // rendering
        var event = new CustomEvent("plotlywidget-after-render", {
            detail: { element: this.el, viewID: this.viewID },
        });
    
        // Dispatch/Trigger/Fire the event
        document.dispatchEvent(event);
      }
    

    Plotly
        .react(this.el, initialTraces, initialLayout, config)
        .then(handlePlotlyEvents)
  }

  /**
    * Handle Plotly.js events
  */

  autosizeFigure() {
    var layout = this.model.get("_widget_layout");
    if (_.isNil(layout) || _.isNil(layout.width)) {
      Plotly.Plots.resize(this.el);
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
      Plotly.addTraces(this.el, msgData.trace_data);
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
      Plotly.deleteTraces(this.el, delete_inds);
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
    }
  }


  /**
   * Handle Plotly.animate request
   */
//   do_animate() {
//     /** @type {Py2JsAnimateMsg} */
//     var msgData: Py2JsAnimateMsg = this.model.get("_py2js_animate");

//     if (msgData !== null) {
//       // Unpack params
//       // var animationData = msgData[0];
//       var animationOpts = msgData.animation_opts;

//       var styles = msgData.style_data;
//       var layout = msgData.layout_data;
//       var traceIndexes = (this.model as FigureModel)._normalize_trace_indexes(
//         msgData.style_traces
//       );

//       var animationData: any = {
//         data: styles,
//         layout: layout,
//         traces: traceIndexes,
//       };

//       animationData["_doNotReportToPy"] = true;
//       // @ts-ignore
//       Plotly.animate(this.el, animationData, animationOpts);
//     }
//   }
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

function render ({ el, model }) {
    console.log('rendering', model.get('_data'), model.get('_widget_layout'));
    const view = new FigureView(model, el);
    view.render()
    return () => view.remove();
}

export default { render }