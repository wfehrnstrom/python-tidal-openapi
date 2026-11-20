# ArtistStreamsStatisticsSourcePlays


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plays** | **int** |  | 
**share** | **float** | Share of all plays | 
**source** | **str** | Where plays started. UNKNOWN: a source this API does not know | 

## Example

```python
from tidal.models.artist_streams_statistics_source_plays import ArtistStreamsStatisticsSourcePlays

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistStreamsStatisticsSourcePlays from a JSON string
artist_streams_statistics_source_plays_instance = ArtistStreamsStatisticsSourcePlays.from_json(json)
# print the JSON string representation of the object
print(ArtistStreamsStatisticsSourcePlays.to_json())

# convert the object into a dict
artist_streams_statistics_source_plays_dict = artist_streams_statistics_source_plays_instance.to_dict()
# create an instance of ArtistStreamsStatisticsSourcePlays from a dict
artist_streams_statistics_source_plays_from_dict = ArtistStreamsStatisticsSourcePlays.from_dict(artist_streams_statistics_source_plays_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


