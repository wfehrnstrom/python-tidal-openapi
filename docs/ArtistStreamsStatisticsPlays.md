# ArtistStreamsStatisticsPlays


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous** | **int** | Plays in the previous window of the same length. Absent when there is no earlier window to compare with | [optional] 
**value** | **int** | Plays in the window | 

## Example

```python
from tidal.models.artist_streams_statistics_plays import ArtistStreamsStatisticsPlays

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistStreamsStatisticsPlays from a JSON string
artist_streams_statistics_plays_instance = ArtistStreamsStatisticsPlays.from_json(json)
# print the JSON string representation of the object
print(ArtistStreamsStatisticsPlays.to_json())

# convert the object into a dict
artist_streams_statistics_plays_dict = artist_streams_statistics_plays_instance.to_dict()
# create an instance of ArtistStreamsStatisticsPlays from a dict
artist_streams_statistics_plays_from_dict = ArtistStreamsStatisticsPlays.from_dict(artist_streams_statistics_plays_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


