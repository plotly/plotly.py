// @flow

export type CrossFaded<T> = {
    from: T,
    to: T,
    fromScale: number,
    toScale: number,
    t: number
};
