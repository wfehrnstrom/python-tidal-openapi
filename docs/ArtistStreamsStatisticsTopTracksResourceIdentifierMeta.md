# ArtistStreamsStatisticsTopTracksResourceIdentifierMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plays** | **int** | Plays of the track in the window | 
**rank** | **int** | 1-based position in the producer&#39;s ranking. Tracks this API cannot link are left out, so ranks can have gaps | 
**replacement** | [**ReplacementProvenance**](ReplacementProvenance.md) |  | [optional] 

## Example

```python
from tidal.models.artist_streams_statistics_top_tracks_resource_identifier_meta import ArtistStreamsStatisticsTopTracksResourceIdentifierMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistStreamsStatisticsTopTracksResourceIdentifierMeta from a JSON string
artist_streams_statistics_top_tracks_resource_identifier_meta_instance = ArtistStreamsStatisticsTopTracksResourceIdentifierMeta.from_json(json)
# print the JSON string representation of the object
print(ArtistStreamsStatisticsTopTracksResourceIdentifierMeta.to_json())

# convert the object into a dict
artist_streams_statistics_top_tracks_resource_identifier_meta_dict = artist_streams_statistics_top_tracks_resource_identifier_meta_instance.to_dict()
# create an instance of ArtistStreamsStatisticsTopTracksResourceIdentifierMeta from a dict
artist_streams_statistics_top_tracks_resource_identifier_meta_from_dict = ArtistStreamsStatisticsTopTracksResourceIdentifierMeta.from_dict(artist_streams_statistics_top_tracks_resource_identifier_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


