import shapely
import fiona
import geopandas
import pandas
import os


def points_to_poly(points):
    '''builds polygon from list of points
    '''
    mpt = gpd.GeoSeries([point['geometry'] for point in points])
    return mpt.unary_union.convex_hull

def get_paths(polygon, vector_layer):
    '''From polygon and layer of vectors, select vectors inside polygon
    '''
    
    
    
    return vectors[vectors.within(polygon)