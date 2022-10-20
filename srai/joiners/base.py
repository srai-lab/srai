"""Base class for joiners."""

import abc

import geopandas as gpd


class BaseJoiner(abc.ABC):
    """Base abstract class for joiners."""

    @abc.abstractmethod
    def join(self, regions: gpd.GeoDataFrame, features: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        """Join a given GeoDataFrame.

        Args:
            regions (gpd.GeoDataFrame): regions into which features are joined
            features (gpd.GeoDataFrame): features to be joined
        Returns:
            GeoDataFrame with the joined data
        """
        raise NotImplementedError
