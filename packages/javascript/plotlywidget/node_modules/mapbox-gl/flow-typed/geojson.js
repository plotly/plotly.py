type GeoJSONPosition = [number, number] | [number, number, number];
type Geometry<T, C> = { type: T, coordinates: C }

declare type      GeoJSONPoint = Geometry<     'Point',       GeoJSONPosition>;
declare type GeoJSONMultiPoint = Geometry<'MultiPoint', Array<GeoJSONPosition>>;

declare type      GeoJSONLineString = Geometry<     'LineString',       Array<GeoJSONPosition>>;
declare type GeoJSONMultiLineString = Geometry<'MultiLineString', Array<Array<GeoJSONPosition>>>;

declare type      GeoJSONPolygon = Geometry<     'Polygon',       Array<Array<GeoJSONPosition>>>;
declare type GeoJSONMultiPolygon = Geometry<'MultiPolygon', Array<Array<Array<GeoJSONPosition>>>>;

declare type GeoJSONGeometry =
    | GeoJSONPoint
    | GeoJSONMultiPoint
    | GeoJSONLineString
    | GeoJSONMultiLineString
    | GeoJSONPolygon
    | GeoJSONMultiPolygon
    | GeoJSONGeometryCollection;

declare type GeoJSONGeometryCollection = {
    type: 'GeometryCollection',
    geometries: Array<GeoJSONGeometry>
};

declare type GeoJSONFeature = {
    type: 'Feature',
    geometry: ?GeoJSONGeometry,
    properties: {},
    id?: number | string
};

declare type GeoJSONFeatureCollection = {
    type: 'FeatureCollection',
    features: Array<GeoJSONFeature>
};

declare type GeoJSON = GeoJSONGeometry | GeoJSONFeature | GeoJSONFeatureCollection;
