declare module "@mapbox/shelf-pack" {
    declare type Bin = {
        id: number|string,
        x: number,
        y: number,
        w: number,
        h: number
    };

    declare class ShelfPack {
        w: number;
        h: number;

        constructor(w: number, h: number, options?: {autoResize: boolean}): ShelfPack;

        pack(bins: Array<{w: number, h: number}>, options?: {inPlace: boolean}): Array<Bin>;
        packOne(w: number, h: number, id?: number|string): Bin;
        shrink(): void;

        ref(bin: Bin): number;
        unref(bin: Bin): number;
    }

    declare module.exports: typeof ShelfPack;
}
