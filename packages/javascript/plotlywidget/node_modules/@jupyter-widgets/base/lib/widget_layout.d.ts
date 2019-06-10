import { WidgetModel, WidgetView } from './widget';
export declare class LayoutModel extends WidgetModel {
    defaults(): any;
}
export declare class LayoutView extends WidgetView {
    /**
     * Public constructor
     */
    initialize(parameters: any): void;
    /**
     * Register a CSS trait that is known by the model
     * @param trait
     */
    registerTrait(trait: string): void;
    /**
     * Get the the name of the css property from the trait name
     * @param  model attribute name
     * @return css property name
     */
    css_name(trait: string): string;
    /**
     * Handles when a trait value changes
     */
    handleChange(trait: string, value: any): void;
    /**
     * Remove the styling from the parent view.
     */
    unlayout(): void;
    private _traitNames;
}
