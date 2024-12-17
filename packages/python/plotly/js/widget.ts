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

type Js2PyPointsCallbackMsg = {
  event_type: string;
  points: Points;
  device_state: InputDeviceState;
  selector: Selector;
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

type Py2JsAnimateMsg = Py2JsMsg & {
  style_data: any;
  layout_data: any;
  style_traces?: null | number | number[];
  animation_opts?: any;
};

type Selector = {
  type: "box" | "lasso";
  selector_state:
    | { xrange: number[]; yrange: number[] }
    | { xs: number[]; ys: number[] };
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
  resizeEventListener: () => void;

  model;
  el: HTMLElement;

  constructor(model, el: HTMLElement) {
    this.model = model;
    this.el = el;

    model.on('change:_widget_layout', () => { 
        this.render();
    });
    model.on('change:_widget_data', () => {
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
    this.model.on("change:_py2js_animate", () => this.do_animate());

    // MathJax v2 configuration
    // ---------------------
    (window as any)?.MathJax?.Hub?.Config?.({ SVG: { font: "STIX-Web" } });

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
      this.model.save_changes();
    }
  }

  /**
   * Stub for future handling of plotly_doubleclick
   * @param data
   */
  handle_plotly_doubleclick(data: any) {}

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
   * Handle Plotly.animate request
   */
  do_animate() {
    /** @type {Py2JsAnimateMsg} */
    var msgData: Py2JsAnimateMsg = this.model.get("_py2js_animate");

    console.log('do_animate', msgData)
    if (msgData !== null) {
      // Unpack params
      // var animationData = msgData[0];
      var animationOpts = msgData.animation_opts;

      var styles = msgData.style_data;
      var layout = msgData.layout_data;

      var animationData: any = {
        data: styles,
        layout: layout,
        traces: this._normalize_trace_indexes(msgData.style_traces),
      };

      animationData["_doNotReportToPy"] = true;
      // @ts-ignore
      Plotly.animate(this.el, animationData, animationOpts);
    }
  }
}

function render ({ el, model }) {
    const view = new FigureView(model, el);
    view.render()
    return () => view.remove();
}

export default { render }