import { Token } from '@phosphor/coreutils';
import { WidgetModel, WidgetView } from './widget';
/**
 * A runtime interface token for a widget registry.
 */
export declare const IJupyterWidgetRegistry: Token<IJupyterWidgetRegistry>;
/**
 * A registry of Jupyter Widgets.
 *
 * This is used by widget managers that support an external registry.
 */
export interface IJupyterWidgetRegistry {
    /**
     * Register a widget module.
     */
    registerWidget(data: IWidgetRegistryData): void;
}
export declare type ExportMap = {
    [key: string]: typeof WidgetModel | typeof WidgetView;
};
export declare type ExportData = ExportMap | Promise<ExportMap> | (() => ExportMap) | (() => Promise<ExportMap>);
export interface IWidgetRegistryData {
    /**
     * The widget module name.
     */
    name: string;
    /**
     * The widget module version.
     */
    version: string;
    /**
     * A map of object names to widget classes provided by the module, or a
     * promise to such a map, or a function returning the same.
     */
    exports: ExportData;
}
