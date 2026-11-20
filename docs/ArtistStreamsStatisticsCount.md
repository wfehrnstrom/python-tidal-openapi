# ArtistStreamsStatisticsCount

A count in the window that may be withheld. value is present exactly when status is OK, and 0 is a measured zero

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of artist statistics that may be withheld. OK: the data is present. SUPPRESSED: withheld because too few people are counted to show it. UNAVAILABLE: not available at the moment | 
**value** | **int** |  | [optional] 

## Example

```python
from tidal.models.artist_streams_statistics_count import ArtistStreamsStatisticsCount

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistStreamsStatisticsCount from a JSON string
artist_streams_statistics_count_instance = ArtistStreamsStatisticsCount.from_json(json)
# print the JSON string representation of the object
print(ArtistStreamsStatisticsCount.to_json())

# convert the object into a dict
artist_streams_statistics_count_dict = artist_streams_statistics_count_instance.to_dict()
# create an instance of ArtistStreamsStatisticsCount from a dict
artist_streams_statistics_count_from_dict = ArtistStreamsStatisticsCount.from_dict(artist_streams_statistics_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


