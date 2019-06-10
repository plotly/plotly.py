// @flow

import ShelfPack from '@mapbox/shelf-pack';

import { RGBAImage } from '../util/image';
import { register } from '../util/web_worker_transfer';

import type {StyleImage} from '../style/style_image';

const padding = 1;

type Rect = {
    x: number,
    y: number,
    w: number,
    h: number
};

export class ImagePosition {
    paddedRect: Rect;
    pixelRatio: number;

    constructor(paddedRect: Rect, {pixelRatio}: StyleImage) {
        this.paddedRect = paddedRect;
        this.pixelRatio = pixelRatio;
    }

    get tl(): [number, number] {
        return [
            this.paddedRect.x + padding,
            this.paddedRect.y + padding
        ];
    }

    get br(): [number, number] {
        return [
            this.paddedRect.x + this.paddedRect.w - padding,
            this.paddedRect.y + this.paddedRect.h - padding
        ];
    }

    get displaySize(): [number, number] {
        return [
            (this.paddedRect.w - padding * 2) / this.pixelRatio,
            (this.paddedRect.h - padding * 2) / this.pixelRatio
        ];
    }
}

export default class ImageAtlas {
    image: RGBAImage;
    positions: {[string]: ImagePosition};

    constructor(images: {[string]: StyleImage}) {
        const image = new RGBAImage({width: 0, height: 0});
        const positions = {};

        const pack = new ShelfPack(0, 0, {autoResize: true});

        for (const id in images) {
            const src = images[id];

            const bin = pack.packOne(
                src.data.width + 2 * padding,
                src.data.height + 2 * padding);

            image.resize({
                width: pack.w,
                height: pack.h
            });

            RGBAImage.copy(
                src.data,
                image,
                { x: 0, y: 0 },
                {
                    x: bin.x + padding,
                    y: bin.y + padding
                },
                src.data);

            positions[id] = new ImagePosition(bin, src);
        }

        pack.shrink();
        image.resize({
            width: pack.w,
            height: pack.h
        });

        this.image = image;
        this.positions = positions;
    }
}

register('ImagePosition', ImagePosition);
register('ImageAtlas', ImageAtlas);

