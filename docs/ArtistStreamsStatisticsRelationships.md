# ArtistStreamsStatisticsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artist** | [**ArtistStreamsStatisticsArtistSingleRelationshipDataDocument**](ArtistStreamsStatisticsArtistSingleRelationshipDataDocument.md) |  | [optional] 
**top_tracks** | [**ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocument**](ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.artist_streams_statistics_relationships import ArtistStreamsStatisticsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistStreamsStatisticsRelationships from a JSON string
artist_streams_statistics_relationships_instance = ArtistStreamsStatisticsRelationships.from_json(json)
# print the JSON string representation of the object
print(ArtistStreamsStatisticsRelationships.to_json())

# convert the object into a dict
artist_streams_statistics_relationships_dict = artist_streams_statistics_relationships_instance.to_dict()
# create an instance of ArtistStreamsStatisticsRelationships from a dict
artist_streams_statistics_relationships_from_dict = ArtistStreamsStatisticsRelationships.from_dict(artist_streams_statistics_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


