// @flow

import DOM from '../../util/dom';

import { bindAll } from '../../util/util';

import type Map from '../map';

/**
 * A `LogoControl` is a control that adds the Mapbox watermark
 * to the map as required by the [terms of service](https://www.mapbox.com/tos/) for Mapbox
 * vector tiles and core styles.
 *
 * @implements {IControl}
 * @private
**/

class LogoControl {
    _map: Map;
    _container: HTMLElement;

    constructor() {
        bindAll(['_updateLogo'], this);
    }

    onAdd(map: Map) {
        this._map = map;
        this._container = DOM.create('div', 'mapboxgl-ctrl');
        const anchor = DOM.create('a', 'mapboxgl-ctrl-logo');
        anchor.target = "_blank";
        anchor.href = "https://www.mapbox.com/";
        anchor.setAttribute("aria-label", "Mapbox logo");
        this._container.appendChild(anchor);
        this._container.style.display = 'none';

        this._map.on('sourcedata', this._updateLogo);
        this._updateLogo();
        return this._container;
    }

    onRemove() {
        DOM.remove(this._container);
        this._map.off('sourcedata', this._updateLogo);
    }

    getDefaultPosition() {
        return 'bottom-left';
    }

    _updateLogo(e: any) {
        if (!e || e.sourceDataType === 'metadata') {
            this._container.style.display = this._logoRequired() ? 'block' : 'none';
        }
    }

    _logoRequired() {
        if (!this._map.style) return;

        const sourceCaches = this._map.style.sourceCaches;
        for (const id in sourceCaches) {
            const source = sourceCaches[id].getSource();
            if (source.mapbox_logo) {
                return true;
            }
        }

        return false;
    }

}


export default LogoControl;
