declare module 'binary-search-bounds' {
    interface BSearch {
        gt<T>(array:T[], y:T, compare?:((a:T, b:T) => number | null | undefined), lo?:number, hi?:number);
        ge<T>(array:T[], y:T, compare?:((a:T, b:T) => number | null | undefined), lo?:number, hi?:number);
        lt<T>(array:T[], y:T, compare?:((a:T, b:T) => number | null | undefined), lo?:number, hi?:number);
        le<T>(array:T[], y:T, compare?:((a:T, b:T) => number | null | undefined), lo?:number, hi?:number);
        eq<T>(array:T[], y:T, compare?:((a:T, b:T) => number | null | undefined), lo?:number, hi?:number);
    }
    const bsearch:BSearch;
    export = bsearch;
}