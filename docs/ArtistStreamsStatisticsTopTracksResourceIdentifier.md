# ArtistStreamsStatisticsTopTracksResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**ArtistStreamsStatisticsTopTracksResourceIdentifierMeta**](ArtistStreamsStatisticsTopTracksResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.artist_streams_statistics_top_tracks_resource_identifier import ArtistStreamsStatisticsTopTracksResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistStreamsStatisticsTopTracksResourceIdentifier from a JSON string
artist_streams_statistics_top_tracks_resource_identifier_instance = ArtistStreamsStatisticsTopTracksResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(ArtistStreamsStatisticsTopTracksResourceIdentifier.to_json())

# convert the object into a dict
artist_streams_statistics_top_tracks_resource_identifier_dict = artist_streams_statistics_top_tracks_resource_identifier_instance.to_dict()
# create an instance of ArtistStreamsStatisticsTopTracksResourceIdentifier from a dict
artist_streams_statistics_top_tracks_resource_identifier_from_dict = ArtistStreamsStatisticsTopTracksResourceIdentifier.from_dict(artist_streams_statistics_top_tracks_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


