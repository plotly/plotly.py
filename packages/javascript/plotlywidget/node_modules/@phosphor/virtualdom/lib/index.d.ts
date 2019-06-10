/**
 * The names of the supported HTML5 DOM element attributes.
 *
 * This list is not all-encompassing, rather it attempts to define the
 * attribute names which are relevant for use in a virtual DOM context.
 * If a standardized or widely supported name is missing, please open
 * an issue to have it added.
 *
 * The attribute names were collected from the following sources:
 *   - https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes
 *   - https://www.w3.org/TR/html5/index.html#attributes-1
 *   - https://html.spec.whatwg.org/multipage/indices.html#attributes-3
 */
export declare type ElementAttrNames = ('abbr' | 'accept' | 'accept-charset' | 'accesskey' | 'action' | 'allowfullscreen' | 'alt' | 'autocomplete' | 'autofocus' | 'autoplay' | 'autosave' | 'checked' | 'cite' | 'cols' | 'colspan' | 'contenteditable' | 'controls' | 'coords' | 'crossorigin' | 'data' | 'datetime' | 'default' | 'dir' | 'dirname' | 'disabled' | 'download' | 'draggable' | 'dropzone' | 'enctype' | 'form' | 'formaction' | 'formenctype' | 'formmethod' | 'formnovalidate' | 'formtarget' | 'headers' | 'height' | 'hidden' | 'high' | 'href' | 'hreflang' | 'id' | 'inputmode' | 'integrity' | 'ismap' | 'kind' | 'label' | 'lang' | 'list' | 'loop' | 'low' | 'max' | 'maxlength' | 'media' | 'mediagroup' | 'method' | 'min' | 'minlength' | 'multiple' | 'muted' | 'name' | 'novalidate' | 'optimum' | 'pattern' | 'placeholder' | 'poster' | 'preload' | 'readonly' | 'rel' | 'required' | 'reversed' | 'rows' | 'rowspan' | 'sandbox' | 'scope' | 'selected' | 'shape' | 'size' | 'sizes' | 'span' | 'spellcheck' | 'src' | 'srcdoc' | 'srclang' | 'srcset' | 'start' | 'step' | 'tabindex' | 'target' | 'title' | 'type' | 'typemustmatch' | 'usemap' | 'value' | 'width' | 'wrap');
/**
 * The names of the supported HTML5 CSS property names.
 *
 * If a standardized or widely supported name is missing, please open
 * an issue to have it added.
 *
 * The property names were collected from the following sources:
 *   - TypeScript's `lib.dom.d.ts` file
 */
export declare type CSSPropertyNames = ('alignContent' | 'alignItems' | 'alignSelf' | 'alignmentBaseline' | 'animation' | 'animationDelay' | 'animationDirection' | 'animationDuration' | 'animationFillMode' | 'animationIterationCount' | 'animationName' | 'animationPlayState' | 'animationTimingFunction' | 'backfaceVisibility' | 'background' | 'backgroundAttachment' | 'backgroundClip' | 'backgroundColor' | 'backgroundImage' | 'backgroundOrigin' | 'backgroundPosition' | 'backgroundPositionX' | 'backgroundPositionY' | 'backgroundRepeat' | 'backgroundSize' | 'baselineShift' | 'border' | 'borderBottom' | 'borderBottomColor' | 'borderBottomLeftRadius' | 'borderBottomRightRadius' | 'borderBottomStyle' | 'borderBottomWidth' | 'borderCollapse' | 'borderColor' | 'borderImage' | 'borderImageOutset' | 'borderImageRepeat' | 'borderImageSlice' | 'borderImageSource' | 'borderImageWidth' | 'borderLeft' | 'borderLeftColor' | 'borderLeftStyle' | 'borderLeftWidth' | 'borderRadius' | 'borderRight' | 'borderRightColor' | 'borderRightStyle' | 'borderRightWidth' | 'borderSpacing' | 'borderStyle' | 'borderTop' | 'borderTopColor' | 'borderTopLeftRadius' | 'borderTopRightRadius' | 'borderTopStyle' | 'borderTopWidth' | 'borderWidth' | 'bottom' | 'boxShadow' | 'boxSizing' | 'breakAfter' | 'breakBefore' | 'breakInside' | 'captionSide' | 'clear' | 'clip' | 'clipPath' | 'clipRule' | 'color' | 'colorInterpolationFilters' | 'columnCount' | 'columnFill' | 'columnGap' | 'columnRule' | 'columnRuleColor' | 'columnRuleStyle' | 'columnRuleWidth' | 'columnSpan' | 'columnWidth' | 'columns' | 'content' | 'counterIncrement' | 'counterReset' | 'cssFloat' | 'cssText' | 'cursor' | 'direction' | 'display' | 'dominantBaseline' | 'emptyCells' | 'enableBackground' | 'fill' | 'fillOpacity' | 'fillRule' | 'filter' | 'flex' | 'flexBasis' | 'flexDirection' | 'flexFlow' | 'flexGrow' | 'flexShrink' | 'flexWrap' | 'floodColor' | 'floodOpacity' | 'font' | 'fontFamily' | 'fontFeatureSettings' | 'fontSize' | 'fontSizeAdjust' | 'fontStretch' | 'fontStyle' | 'fontVariant' | 'fontWeight' | 'glyphOrientationHorizontal' | 'glyphOrientationVertical' | 'height' | 'imeMode' | 'justifyContent' | 'kerning' | 'left' | 'letterSpacing' | 'lightingColor' | 'lineHeight' | 'listStyle' | 'listStyleImage' | 'listStylePosition' | 'listStyleType' | 'margin' | 'marginBottom' | 'marginLeft' | 'marginRight' | 'marginTop' | 'marker' | 'markerEnd' | 'markerMid' | 'markerStart' | 'mask' | 'maxHeight' | 'maxWidth' | 'minHeight' | 'minWidth' | 'msContentZoomChaining' | 'msContentZoomLimit' | 'msContentZoomLimitMax' | 'msContentZoomLimitMin' | 'msContentZoomSnap' | 'msContentZoomSnapPoints' | 'msContentZoomSnapType' | 'msContentZooming' | 'msFlowFrom' | 'msFlowInto' | 'msFontFeatureSettings' | 'msGridColumn' | 'msGridColumnAlign' | 'msGridColumnSpan' | 'msGridColumns' | 'msGridRow' | 'msGridRowAlign' | 'msGridRowSpan' | 'msGridRows' | 'msHighContrastAdjust' | 'msHyphenateLimitChars' | 'msHyphenateLimitLines' | 'msHyphenateLimitZone' | 'msHyphens' | 'msImeAlign' | 'msOverflowStyle' | 'msScrollChaining' | 'msScrollLimit' | 'msScrollLimitXMax' | 'msScrollLimitXMin' | 'msScrollLimitYMax' | 'msScrollLimitYMin' | 'msScrollRails' | 'msScrollSnapPointsX' | 'msScrollSnapPointsY' | 'msScrollSnapType' | 'msScrollSnapX' | 'msScrollSnapY' | 'msScrollTranslation' | 'msTextCombineHorizontal' | 'msTextSizeAdjust' | 'msTouchAction' | 'msTouchSelect' | 'msUserSelect' | 'msWrapFlow' | 'msWrapMargin' | 'msWrapThrough' | 'opacity' | 'order' | 'orphans' | 'outline' | 'outlineColor' | 'outlineStyle' | 'outlineWidth' | 'overflow' | 'overflowX' | 'overflowY' | 'padding' | 'paddingBottom' | 'paddingLeft' | 'paddingRight' | 'paddingTop' | 'pageBreakAfter' | 'pageBreakBefore' | 'pageBreakInside' | 'perspective' | 'perspectiveOrigin' | 'pointerEvents' | 'position' | 'quotes' | 'resize' | 'right' | 'rubyAlign' | 'rubyOverhang' | 'rubyPosition' | 'stopColor' | 'stopOpacity' | 'stroke' | 'strokeDasharray' | 'strokeDashoffset' | 'strokeLinecap' | 'strokeLinejoin' | 'strokeMiterlimit' | 'strokeOpacity' | 'strokeWidth' | 'tableLayout' | 'textAlign' | 'textAlignLast' | 'textAnchor' | 'textDecoration' | 'textIndent' | 'textJustify' | 'textKashida' | 'textKashidaSpace' | 'textOverflow' | 'textShadow' | 'textTransform' | 'textUnderlinePosition' | 'top' | 'touchAction' | 'transform' | 'transformOrigin' | 'transformStyle' | 'transition' | 'transitionDelay' | 'transitionDuration' | 'transitionProperty' | 'transitionTimingFunction' | 'unicodeBidi' | 'verticalAlign' | 'visibility' | 'webkitAlignContent' | 'webkitAlignItems' | 'webkitAlignSelf' | 'webkitAnimation' | 'webkitAnimationDelay' | 'webkitAnimationDirection' | 'webkitAnimationDuration' | 'webkitAnimationFillMode' | 'webkitAnimationIterationCount' | 'webkitAnimationName' | 'webkitAnimationPlayState' | 'webkitAnimationTimingFunction' | 'webkitAppearance' | 'webkitBackfaceVisibility' | 'webkitBackgroundClip' | 'webkitBackgroundOrigin' | 'webkitBackgroundSize' | 'webkitBorderBottomLeftRadius' | 'webkitBorderBottomRightRadius' | 'webkitBorderImage' | 'webkitBorderRadius' | 'webkitBorderTopLeftRadius' | 'webkitBorderTopRightRadius' | 'webkitBoxAlign' | 'webkitBoxDirection' | 'webkitBoxFlex' | 'webkitBoxOrdinalGroup' | 'webkitBoxOrient' | 'webkitBoxPack' | 'webkitBoxSizing' | 'webkitColumnBreakAfter' | 'webkitColumnBreakBefore' | 'webkitColumnBreakInside' | 'webkitColumnCount' | 'webkitColumnGap' | 'webkitColumnRule' | 'webkitColumnRuleColor' | 'webkitColumnRuleStyle' | 'webkitColumnRuleWidth' | 'webkitColumnSpan' | 'webkitColumnWidth' | 'webkitColumns' | 'webkitFilter' | 'webkitFlex' | 'webkitFlexBasis' | 'webkitFlexDirection' | 'webkitFlexFlow' | 'webkitFlexGrow' | 'webkitFlexShrink' | 'webkitFlexWrap' | 'webkitJustifyContent' | 'webkitOrder' | 'webkitPerspective' | 'webkitPerspectiveOrigin' | 'webkitTapHighlightColor' | 'webkitTextFillColor' | 'webkitTextSizeAdjust' | 'webkitTransform' | 'webkitTransformOrigin' | 'webkitTransformStyle' | 'webkitTransition' | 'webkitTransitionDelay' | 'webkitTransitionDuration' | 'webkitTransitionProperty' | 'webkitTransitionTimingFunction' | 'webkitUserModify' | 'webkitUserSelect' | 'webkitWritingMode' | 'whiteSpace' | 'widows' | 'width' | 'wordBreak' | 'wordSpacing' | 'wordWrap' | 'writingMode' | 'zIndex' | 'zoom');
/**
 * A mapping of inline event name to event object type.
 *
 * This mapping is used to create the event listener properties for
 * the virtual DOM element attributes object. If a standardized or
 * widely supported name is missing, please open an issue to have it
 * added.
 *
 * The event names were collected from the following sources:
 *   - TypeScript's `lib.dom.d.ts` file
 *   - https://www.w3.org/TR/html5/index.html#attributes-1
 *   - https://html.spec.whatwg.org/multipage/webappapis.html#idl-definitions
 */
export declare type ElementEventMap = {
    onabort: UIEvent;
    onauxclick: MouseEvent;
    onblur: FocusEvent;
    oncanplay: Event;
    oncanplaythrough: Event;
    onchange: Event;
    onclick: MouseEvent;
    oncontextmenu: PointerEvent;
    oncopy: ClipboardEvent;
    oncuechange: Event;
    oncut: ClipboardEvent;
    ondblclick: MouseEvent;
    ondrag: DragEvent;
    ondragend: DragEvent;
    ondragenter: DragEvent;
    ondragexit: DragEvent;
    ondragleave: DragEvent;
    ondragover: DragEvent;
    ondragstart: DragEvent;
    ondrop: DragEvent;
    ondurationchange: Event;
    onemptied: Event;
    onended: MediaStreamErrorEvent;
    onerror: ErrorEvent;
    onfocus: FocusEvent;
    oninput: Event;
    oninvalid: Event;
    onkeydown: KeyboardEvent;
    onkeypress: KeyboardEvent;
    onkeyup: KeyboardEvent;
    onload: Event;
    onloadeddata: Event;
    onloadedmetadata: Event;
    onloadend: Event;
    onloadstart: Event;
    onmousedown: MouseEvent;
    onmouseenter: MouseEvent;
    onmouseleave: MouseEvent;
    onmousemove: MouseEvent;
    onmouseout: MouseEvent;
    onmouseover: MouseEvent;
    onmouseup: MouseEvent;
    onmousewheel: WheelEvent;
    onpaste: ClipboardEvent;
    onpause: Event;
    onplay: Event;
    onplaying: Event;
    onpointercancel: PointerEvent;
    onpointerdown: PointerEvent;
    onpointerenter: PointerEvent;
    onpointerleave: PointerEvent;
    onpointermove: PointerEvent;
    onpointerout: PointerEvent;
    onpointerover: PointerEvent;
    onpointerup: PointerEvent;
    onprogress: ProgressEvent;
    onratechange: Event;
    onreset: Event;
    onscroll: UIEvent;
    onseeked: Event;
    onseeking: Event;
    onselect: UIEvent;
    onselectstart: Event;
    onstalled: Event;
    onsubmit: Event;
    onsuspend: Event;
    ontimeupdate: Event;
    onvolumechange: Event;
    onwaiting: Event;
};
/**
 * An object which represents a dataset for a virtual DOM element.
 *
 * The names of the dataset properties will be automatically prefixed
 * with `data-` before being added to the node, e.g. `{ thing: '12' }`
 * will be rendered as `data-thing='12'` in the DOM element.
 *
 * Dataset property names should not contain spaces.
 */
export declare type ElementDataset = {
    readonly [name: string]: string;
};
/**
 * The inline style for for a virtual DOM element.
 *
 * Style attributes use the JS camel-cased property names instead of
 * the CSS hyphenated names for performance and security.
 */
export declare type ElementInlineStyle = {
    readonly [T in CSSPropertyNames]?: string;
};
/**
 * The base attributes for a virtual element node.
 *
 * These are the attributes which are applied to a real DOM element via
 * `element.setAttribute()`. The supported attribute names are defined
 * by the `ElementAttrNames` type.
 *
 * Node attributes are specified using the lower-case HTML name instead
 * of the camel-case JS name due to browser inconsistencies in handling
 * the JS versions.
 */
export declare type ElementBaseAttrs = {
    readonly [T in ElementAttrNames]?: string;
};
/**
 * The inline event listener attributes for a virtual element node.
 *
 * The supported listeners are defined by the `ElementEventMap` type.
 */
export declare type ElementEventAttrs = {
    readonly [T in keyof ElementEventMap]?: (this: HTMLElement, event: ElementEventMap[T]) => any;
};
/**
 * The special-cased attributes for a virtual element node.
 */
export declare type ElementSpecialAttrs = {
    /**
     * The key id for the virtual element node.
     *
     * If a node is given a key id, the generated DOM node will not be
     * recreated during a rendering update if it only moves among its
     * siblings in the render tree.
     *
     * In general, reordering child nodes will cause the nodes to be
     * completely re-rendered. Keys allow this to be optimized away.
     *
     * If a key is provided, it must be unique among sibling nodes.
     */
    readonly key?: string;
    /**
     * The JS-safe name for the HTML `class` attribute.
     */
    readonly className?: string;
    /**
     * The JS-safe name for the HTML `for` attribute.
     */
    readonly htmlFor?: string;
    /**
     * The dataset for the rendered DOM element.
     */
    readonly dataset?: ElementDataset;
    /**
     * The inline style for the rendered DOM element.
     */
    readonly style?: ElementInlineStyle;
};
/**
 * The full set of attributes supported by a virtual element node.
 *
 * This is the combination of the base element attributes, the inline
 * element event listeners, and the special element attributes.
 */
export declare type ElementAttrs = (ElementBaseAttrs & ElementEventAttrs & ElementSpecialAttrs);
/**
 * A virtual node which represents plain text content.
 *
 * #### Notes
 * User code will not typically create a `VirtualText` node directly.
 * Instead, the `h()` function will be used to create an element tree.
 */
export declare class VirtualText {
    /**
     * The text content for the node.
     */
    readonly content: string;
    /**
     * The type of the node.
     *
     * This value can be used as a type guard for discriminating the
     * `VirtualNode` union type.
     */
    readonly type: 'text';
    /**
     * Construct a new virtual text node.
     *
     * @param content - The text content for the node.
     */
    constructor(content: string);
}
/**
 * A virtual node which represents an HTML element.
 *
 * #### Notes
 * User code will not typically create a `VirtualElement` node directly.
 * Instead, the `h()` function will be used to create an element tree.
 */
export declare class VirtualElement {
    /**
     * The tag name for the element.
     */
    readonly tag: string;
    /**
     * The attributes for the element.
     */
    readonly attrs: ElementAttrs;
    /**
     * The children for the element.
     */
    readonly children: ReadonlyArray<VirtualNode>;
    /**
     * The type of the node.
     *
     * This value can be used as a type guard for discriminating the
     * `VirtualNode` union type.
     */
    readonly type: 'element';
    /**
     * Construct a new virtual element node.
     *
     * @param tag - The element tag name.
     *
     * @param attrs - The element attributes.
     *
     * @param children - The element children.
     */
    constructor(tag: string, attrs: ElementAttrs, children: ReadonlyArray<VirtualNode>);
}
/**
 * A type alias for a general virtual node.
 */
export declare type VirtualNode = VirtualElement | VirtualText;
/**
 * Create a new virtual element node.
 *
 * @param tag - The tag name for the element.
 *
 * @param attrs - The attributes for the element, if any.
 *
 * @param children - The children for the element, if any.
 *
 * @returns A new virtual element node for the given parameters.
 *
 * #### Notes
 * The children may be string literals, other virtual nodes, `null`, or
 * an array of those things. Strings are converted into text nodes, and
 * arrays are inlined as if the array contents were given as positional
 * arguments. This makes it simple to build up an array of children by
 * any desired means. `null` child values are simply ignored.
 *
 * A bound function for each HTML tag name is available as a static
 * function attached to the `h()` function. E.g. `h('div', ...)` is
 * equivalent to `h.div(...)`.
 */
export declare function h(tag: string, ...children: h.Child[]): VirtualElement;
export declare function h(tag: string, attrs: ElementAttrs, ...children: h.Child[]): VirtualElement;
/**
 * The namespace for the `h` function statics.
 */
export declare namespace h {
    /**
     * A type alias for the supported child argument types.
     */
    type Child = (string | VirtualNode | null) | Array<string | VirtualNode | null>;
    /**
     * A bound factory function for a specific `h()` tag.
     */
    interface IFactory {
        (...children: Child[]): VirtualElement;
        (attrs: ElementAttrs, ...children: Child[]): VirtualElement;
    }
    const a: IFactory;
    const abbr: IFactory;
    const address: IFactory;
    const area: IFactory;
    const article: IFactory;
    const aside: IFactory;
    const audio: IFactory;
    const b: IFactory;
    const bdi: IFactory;
    const bdo: IFactory;
    const blockquote: IFactory;
    const br: IFactory;
    const button: IFactory;
    const canvas: IFactory;
    const caption: IFactory;
    const cite: IFactory;
    const code: IFactory;
    const col: IFactory;
    const colgroup: IFactory;
    const data: IFactory;
    const datalist: IFactory;
    const dd: IFactory;
    const del: IFactory;
    const dfn: IFactory;
    const div: IFactory;
    const dl: IFactory;
    const dt: IFactory;
    const em: IFactory;
    const embed: IFactory;
    const fieldset: IFactory;
    const figcaption: IFactory;
    const figure: IFactory;
    const footer: IFactory;
    const form: IFactory;
    const h1: IFactory;
    const h2: IFactory;
    const h3: IFactory;
    const h4: IFactory;
    const h5: IFactory;
    const h6: IFactory;
    const header: IFactory;
    const hr: IFactory;
    const i: IFactory;
    const iframe: IFactory;
    const img: IFactory;
    const input: IFactory;
    const ins: IFactory;
    const kbd: IFactory;
    const label: IFactory;
    const legend: IFactory;
    const li: IFactory;
    const main: IFactory;
    const map: IFactory;
    const mark: IFactory;
    const meter: IFactory;
    const nav: IFactory;
    const noscript: IFactory;
    const object: IFactory;
    const ol: IFactory;
    const optgroup: IFactory;
    const option: IFactory;
    const output: IFactory;
    const p: IFactory;
    const param: IFactory;
    const pre: IFactory;
    const progress: IFactory;
    const q: IFactory;
    const rp: IFactory;
    const rt: IFactory;
    const ruby: IFactory;
    const s: IFactory;
    const samp: IFactory;
    const section: IFactory;
    const select: IFactory;
    const small: IFactory;
    const source: IFactory;
    const span: IFactory;
    const strong: IFactory;
    const sub: IFactory;
    const summary: IFactory;
    const sup: IFactory;
    const table: IFactory;
    const tbody: IFactory;
    const td: IFactory;
    const textarea: IFactory;
    const tfoot: IFactory;
    const th: IFactory;
    const thead: IFactory;
    const time: IFactory;
    const title: IFactory;
    const tr: IFactory;
    const track: IFactory;
    const u: IFactory;
    const ul: IFactory;
    const var_: IFactory;
    const video: IFactory;
    const wbr: IFactory;
}
/**
 * The namespace for the virtual DOM rendering functions.
 */
export declare namespace VirtualDOM {
    /**
     * Create a real DOM element from a virtual element node.
     *
     * @param node - The virtual element node to realize.
     *
     * @returns A new DOM element for the given virtual element node.
     *
     * #### Notes
     * This creates a brand new *real* DOM element with a structure which
     * matches the given virtual DOM node.
     *
     * If virtual diffing is desired, use the `render` function instead.
     */
    function realize(node: VirtualElement): HTMLElement;
    /**
     * Render virtual DOM content into a host element.
     *
     * @param content - The virtual DOM content to render.
     *
     * @param host - The host element for the rendered content.
     *
     * #### Notes
     * This renders the delta from the previous rendering. It assumes that
     * the content of the host element is not manipulated by external code.
     *
     * Providing `null` content will clear the rendering.
     *
     * Externally modifying the provided content or the host element will
     * result in undefined rendering behavior.
     */
    function render(content: VirtualNode | ReadonlyArray<VirtualNode> | null, host: HTMLElement): void;
}
