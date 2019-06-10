"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = Object.setPrototypeOf ||
        ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
        function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
var domutils_1 = require("@phosphor/domutils");
var messaging_1 = require("@phosphor/messaging");
var signaling_1 = require("@phosphor/signaling");
var boxlayout_1 = require("./boxlayout");
var stackedpanel_1 = require("./stackedpanel");
var tabbar_1 = require("./tabbar");
var widget_1 = require("./widget");
/**
 * A widget which combines a `TabBar` and a `StackedPanel`.
 *
 * #### Notes
 * This is a simple panel which handles the common case of a tab bar
 * placed next to a content area. The selected tab controls the widget
 * which is shown in the content area.
 *
 * For use cases which require more control than is provided by this
 * panel, the `TabBar` widget may be used independently.
 */
var TabPanel = (function (_super) {
    __extends(TabPanel, _super);
    /**
     * Construct a new tab panel.
     *
     * @param options - The options for initializing the tab panel.
     */
    function TabPanel(options) {
        if (options === void 0) { options = {}; }
        var _this = _super.call(this) || this;
        _this._currentChanged = new signaling_1.Signal(_this);
        _this.addClass('p-TabPanel');
        // Create the tab bar and stacked panel.
        _this.tabBar = new tabbar_1.TabBar(options);
        _this.tabBar.addClass('p-TabPanel-tabBar');
        _this.stackedPanel = new stackedpanel_1.StackedPanel();
        _this.stackedPanel.addClass('p-TabPanel-stackedPanel');
        // Connect the tab bar signal handlers.
        _this.tabBar.tabMoved.connect(_this._onTabMoved, _this);
        _this.tabBar.currentChanged.connect(_this._onCurrentChanged, _this);
        _this.tabBar.tabCloseRequested.connect(_this._onTabCloseRequested, _this);
        _this.tabBar.tabActivateRequested.connect(_this._onTabActivateRequested, _this);
        // Connect the stacked panel signal handlers.
        _this.stackedPanel.widgetRemoved.connect(_this._onWidgetRemoved, _this);
        // Get the data related to the placement.
        _this._tabPlacement = options.tabPlacement || 'top';
        var direction = Private.directionFromPlacement(_this._tabPlacement);
        var orientation = Private.orientationFromPlacement(_this._tabPlacement);
        // Configure the tab bar for the placement.
        _this.tabBar.orientation = orientation;
        _this.tabBar.dataset['placement'] = _this._tabPlacement;
        // Create the box layout.
        var layout = new boxlayout_1.BoxLayout({ direction: direction, spacing: 0 });
        // Set the stretch factors for the child widgets.
        boxlayout_1.BoxLayout.setStretch(_this.tabBar, 0);
        boxlayout_1.BoxLayout.setStretch(_this.stackedPanel, 1);
        // Add the child widgets to the layout.
        layout.addWidget(_this.tabBar);
        layout.addWidget(_this.stackedPanel);
        // Install the layout on the tab panel.
        _this.layout = layout;
        return _this;
    }
    Object.defineProperty(TabPanel.prototype, "currentChanged", {
        /**
         * A signal emitted when the current tab is changed.
         *
         * #### Notes
         * This signal is emitted when the currently selected tab is changed
         * either through user or programmatic interaction.
         *
         * Notably, this signal is not emitted when the index of the current
         * tab changes due to tabs being inserted, removed, or moved. It is
         * only emitted when the actual current tab node is changed.
         */
        get: function () {
            return this._currentChanged;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(TabPanel.prototype, "currentIndex", {
        /**
         * Get the index of the currently selected tab.
         *
         * #### Notes
         * This will be `-1` if no tab is selected.
         */
        get: function () {
            return this.tabBar.currentIndex;
        },
        /**
         * Set the index of the currently selected tab.
         *
         * #### Notes
         * If the index is out of range, it will be set to `-1`.
         */
        set: function (value) {
            this.tabBar.currentIndex = value;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(TabPanel.prototype, "currentWidget", {
        /**
         * Get the currently selected widget.
         *
         * #### Notes
         * This will be `null` if there is no selected tab.
         */
        get: function () {
            var title = this.tabBar.currentTitle;
            return title ? title.owner : null;
        },
        /**
         * Set the currently selected widget.
         *
         * #### Notes
         * If the widget is not in the panel, it will be set to `null`.
         */
        set: function (value) {
            this.tabBar.currentTitle = value ? value.title : null;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(TabPanel.prototype, "tabsMovable", {
        /**
         * Get the whether the tabs are movable by the user.
         *
         * #### Notes
         * Tabs can always be moved programmatically.
         */
        get: function () {
            return this.tabBar.tabsMovable;
        },
        /**
         * Set the whether the tabs are movable by the user.
         *
         * #### Notes
         * Tabs can always be moved programmatically.
         */
        set: function (value) {
            this.tabBar.tabsMovable = value;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(TabPanel.prototype, "tabPlacement", {
        /**
         * Get the tab placement for the tab panel.
         *
         * #### Notes
         * This controls the position of the tab bar relative to the content.
         */
        get: function () {
            return this._tabPlacement;
        },
        /**
         * Set the tab placement for the tab panel.
         *
         * #### Notes
         * This controls the position of the tab bar relative to the content.
         */
        set: function (value) {
            // Bail if the placement does not change.
            if (this._tabPlacement === value) {
                return;
            }
            // Update the internal value.
            this._tabPlacement = value;
            // Get the values related to the placement.
            var direction = Private.directionFromPlacement(value);
            var orientation = Private.orientationFromPlacement(value);
            // Configure the tab bar for the placement.
            this.tabBar.orientation = orientation;
            this.tabBar.dataset['placement'] = value;
            // Update the layout direction.
            this.layout.direction = direction;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(TabPanel.prototype, "widgets", {
        /**
         * A read-only array of the widgets in the panel.
         */
        get: function () {
            return this.stackedPanel.widgets;
        },
        enumerable: true,
        configurable: true
    });
    /**
     * Add a widget to the end of the tab panel.
     *
     * @param widget - The widget to add to the tab panel.
     *
     * #### Notes
     * If the widget is already contained in the panel, it will be moved.
     *
     * The widget's `title` is used to populate the tab.
     */
    TabPanel.prototype.addWidget = function (widget) {
        this.insertWidget(this.widgets.length, widget);
    };
    /**
     * Insert a widget into the tab panel at a specified index.
     *
     * @param index - The index at which to insert the widget.
     *
     * @param widget - The widget to insert into to the tab panel.
     *
     * #### Notes
     * If the widget is already contained in the panel, it will be moved.
     *
     * The widget's `title` is used to populate the tab.
     */
    TabPanel.prototype.insertWidget = function (index, widget) {
        if (widget !== this.currentWidget) {
            widget.hide();
        }
        this.stackedPanel.insertWidget(index, widget);
        this.tabBar.insertTab(index, widget.title);
    };
    /**
     * Handle the `currentChanged` signal from the tab bar.
     */
    TabPanel.prototype._onCurrentChanged = function (sender, args) {
        // Extract the previous and current title from the args.
        var previousIndex = args.previousIndex, previousTitle = args.previousTitle, currentIndex = args.currentIndex, currentTitle = args.currentTitle;
        // Extract the widgets from the titles.
        var previousWidget = previousTitle ? previousTitle.owner : null;
        var currentWidget = currentTitle ? currentTitle.owner : null;
        // Hide the previous widget.
        if (previousWidget) {
            previousWidget.hide();
        }
        // Show the current widget.
        if (currentWidget) {
            currentWidget.show();
        }
        // Emit the `currentChanged` signal for the tab panel.
        this._currentChanged.emit({
            previousIndex: previousIndex, previousWidget: previousWidget, currentIndex: currentIndex, currentWidget: currentWidget
        });
        // Flush the message loop on IE and Edge to prevent flicker.
        if (domutils_1.Platform.IS_EDGE || domutils_1.Platform.IS_IE) {
            messaging_1.MessageLoop.flush();
        }
    };
    /**
     * Handle the `tabActivateRequested` signal from the tab bar.
     */
    TabPanel.prototype._onTabActivateRequested = function (sender, args) {
        args.title.owner.activate();
    };
    /**
     * Handle the `tabCloseRequested` signal from the tab bar.
     */
    TabPanel.prototype._onTabCloseRequested = function (sender, args) {
        args.title.owner.close();
    };
    /**
     * Handle the `tabMoved` signal from the tab bar.
     */
    TabPanel.prototype._onTabMoved = function (sender, args) {
        this.stackedPanel.insertWidget(args.toIndex, args.title.owner);
    };
    /**
     * Handle the `widgetRemoved` signal from the stacked panel.
     */
    TabPanel.prototype._onWidgetRemoved = function (sender, widget) {
        this.tabBar.removeTab(widget.title);
    };
    return TabPanel;
}(widget_1.Widget));
exports.TabPanel = TabPanel;
/**
 * The namespace for the module implementation details.
 */
var Private;
(function (Private) {
    /**
     * Convert a tab placement to tab bar orientation.
     */
    function orientationFromPlacement(plc) {
        return placementToOrientationMap[plc];
    }
    Private.orientationFromPlacement = orientationFromPlacement;
    /**
     * Convert a tab placement to a box layout direction.
     */
    function directionFromPlacement(plc) {
        return placementToDirectionMap[plc];
    }
    Private.directionFromPlacement = directionFromPlacement;
    /**
     * A mapping of tab placement to tab bar orientation.
     */
    var placementToOrientationMap = {
        'top': 'horizontal',
        'left': 'vertical',
        'right': 'vertical',
        'bottom': 'horizontal'
    };
    /**
     * A mapping of tab placement to box layout direction.
     */
    var placementToDirectionMap = {
        'top': 'top-to-bottom',
        'left': 'left-to-right',
        'right': 'right-to-left',
        'bottom': 'bottom-to-top'
    };
})(Private || (Private = {}));
