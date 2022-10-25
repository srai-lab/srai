"""
Voronoi Regionizer.

This module contains voronoi regionizer implementation.
"""

from itertools import combinations

import geopandas as gpd

from ._spherical_voronoi import generate_voronoi_regions


class VoronoiRegionizer:
    """A Voronoi regionizer."""

    def __init__(self, seeds: gpd.GeoDataFrame, max_meters_between_points: int = 10_000) -> None:
        """
        VoronoiRegionizer.

        Voronoi [1] regionizer allows the given geometries to be divided into
        Thiessen polygons using geometries that are the seeds. To minimize distortions
        tessellation will be performed on a sphere using SphericalVoronoi [2] function
        from scipy library.

        All (multi)polygons from seeds GeoDataFrame will be transformed to their centroids,
        because scipy function requires only points as an input.

        Seeds laying on a single arc might result in a ValueError exception.

        Args:
            seeds (gpd.GeoDataFrame): GeoDataFrame with seeds for creating a tessellation.
            max_meters_between_points (int): Maximal distance in meters between two points
                in a resulting polygon. Higher number results lower resolution of a polygon.

        References:
            [1] https://en.wikipedia.org/wiki/Voronoi_diagram
            [2] https://docs.scipy.org/doc/scipy-1.9.2/reference/generated/scipy.spatial.SphericalVoronoi.html
        """  # noqa: W505, E501
        self.region_ids = []
        self.seeds = []
        self.max_meters_between_points = max_meters_between_points
        for index, row in seeds.iterrows():
            self.region_ids.append(index)
            self.seeds.append(row.geometry.centroid)

        if len(seeds) == 0:
            raise ValueError("Minimum one seed is required.")

        if any(p1.equals(p2) for p1, p2 in combinations(self.seeds, r=2)):
            raise ValueError("Duplicate seeds present.")

    def transform(self, gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        """
        Regionize a given GeoDataFrame.

        Args:
            gdf (gpd.GeoDataFrame): GeoDataFrame to be regionized.

        Returns:
            GeoDataFrame with the regionized data.
        """
        generated_regions = generate_voronoi_regions(self.seeds, self.max_meters_between_points)
        regions_gdf = gpd.GeoDataFrame(
            data={"geometry": generated_regions}, index=self.region_ids, crs=4326
        )
        clipped_regions_gdf = regions_gdf.clip(mask=gdf, keep_geom_type=False)
        return clipped_regions_gdf