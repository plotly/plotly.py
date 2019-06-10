declare function matter(str: string, options?: matter.GrayMatterOption): any

declare namespace matter {
  interface GrayMatterOption {
    parser?: () => void;
    eval?: boolean;
    lang?: string;
    delims?: string | string[];
  }
  export function read(fp: string, options?: GrayMatterOption): any;
  export function stringify(str: string, data: object, options?: GrayMatterOption): string;
  export function test(str: string, options?: GrayMatterOption): string;
}

export = matter
