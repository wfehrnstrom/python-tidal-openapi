# ArtistStreamsStatisticsSeriesPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | First day of the bucket | 
**plays** | **int** |  | 

## Example

```python
from tidal.models.artist_streams_statistics_series_point import ArtistStreamsStatisticsSeriesPoint

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistStreamsStatisticsSeriesPoint from a JSON string
artist_streams_statistics_series_point_instance = ArtistStreamsStatisticsSeriesPoint.from_json(json)
# print the JSON string representation of the object
print(ArtistStreamsStatisticsSeriesPoint.to_json())

# convert the object into a dict
artist_streams_statistics_series_point_dict = artist_streams_statistics_series_point_instance.to_dict()
# create an instance of ArtistStreamsStatisticsSeriesPoint from a dict
artist_streams_statistics_series_point_from_dict = ArtistStreamsStatisticsSeriesPoint.from_dict(artist_streams_statistics_series_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


