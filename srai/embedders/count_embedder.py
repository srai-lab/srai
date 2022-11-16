"""
Count Embedder.

This module contains count embedder implementation.

"""
from typing import List, Optional

import geopandas as gpd
import pandas as pd


class CountEmbedder:
    """Simple Embedder that counts occurences of feature values."""

    def __init__(self, expected_output_features: Optional[List[str]] = None) -> None:
        """
        Init CountEmbedder.

        Args:
            expected_output_features (List[str], optional): The features that are expected
                to be found in the resulting embedding. If not None, the missing features are added
                and filled with 0. The unexpected features are removed.
                The resulting columns are sorted accordingly. Defaults to None.

        """
        if expected_output_features is not None:
            self.expected_output_features = pd.Series(expected_output_features)
        else:
            self.expected_output_features = None

    def embed(
        self,
        regions_gdf: gpd.GeoDataFrame,
        features_gdf: gpd.GeoDataFrame,
        joint_gdf: gpd.GeoDataFrame,
    ) -> pd.DataFrame:
        """
        Embed a given GeoDataFrame.

        Creates region embeddings by counting the frequencies of each feature value.
        Expects features_gdf to be in wide format with each column
        being a separate type of feature (e.g. amenity, leisure)
        and rows to hold values of these features for each object.
        The resulting GeoDataFrame will have columns made by combining
        the feature name (column) and value (row) e.g. amenity_fuel or type_0.
        The rows will hold numbers of this type of feature in each region.

        Args:
            regions_gdf (gpd.GeoDataFrame): Region indexes and geometries.
            features_gdf (gpd.GeoDataFrame): Feature indexes, geometries and feature values.
            joint_gdf (gpd.GeoDataFrame): Joiner result with region-feature multi-index.

        Returns:
            pd.DataFrame: Embedding and geometry index for each region in regions_gdf.

        """
        if features_gdf.empty or joint_gdf.empty:
            if self.expected_output_features is not None:
                return pd.DataFrame(
                    0, index=regions_gdf.index, columns=self.expected_output_features
                )
            else:
                return pd.DataFrame()

        regions_df = self._remove_geometry_if_present(regions_gdf)
        features_df = self._remove_geometry_if_present(features_gdf)
        joint_df = self._remove_geometry_if_present(joint_gdf)

        joint_with_features = joint_df.join(features_df)
        region_embeddings = pd.get_dummies(joint_with_features).groupby(level=0).sum()

        if self.expected_output_features is not None:
            region_embeddings = self._filter_to_expected_features(region_embeddings)
        region_embedding_df = regions_df.join(region_embeddings, how="left").fillna(0)

        return region_embedding_df

    def _filter_to_expected_features(self, region_embeddings: pd.DataFrame) -> pd.DataFrame:
        """
        Add missing and remove excessive columns from embeddings.

        Args:
            region_embeddings (pd.DataFrame): Counted frequencies of each feature value.

        Returns:
            pd.DataFrame: Embeddings with expected columns only.

        """
        missing_features = self.expected_output_features[
            ~self.expected_output_features.isin(region_embeddings.columns)
        ]
        region_embeddings[missing_features] = 0
        region_embeddings = region_embeddings[self.expected_output_features]
        return region_embeddings

    def _remove_geometry_if_present(self, data: gpd.GeoDataFrame) -> pd.DataFrame:
        if "geometry" in data.columns:
            data = data.drop(columns="geometry")
        return pd.DataFrame(data)