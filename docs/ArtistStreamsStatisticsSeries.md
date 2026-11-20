# ArtistStreamsStatisticsSeries

Plays per bucket

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_period** | [**ArtistStatisticsBucketPeriod**](ArtistStatisticsBucketPeriod.md) |  | [optional] 
**points** | [**List[ArtistStreamsStatisticsSeriesPoint]**](ArtistStreamsStatisticsSeriesPoint.md) |  | 

## Example

```python
from tidal.models.artist_streams_statistics_series import ArtistStreamsStatisticsSeries

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistStreamsStatisticsSeries from a JSON string
artist_streams_statistics_series_instance = ArtistStreamsStatisticsSeries.from_json(json)
# print the JSON string representation of the object
print(ArtistStreamsStatisticsSeries.to_json())

# convert the object into a dict
artist_streams_statistics_series_dict = artist_streams_statistics_series_instance.to_dict()
# create an instance of ArtistStreamsStatisticsSeries from a dict
artist_streams_statistics_series_from_dict = ArtistStreamsStatisticsSeries.from_dict(artist_streams_statistics_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


