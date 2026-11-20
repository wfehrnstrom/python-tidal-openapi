# ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocument

Target resource types: `tracks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ArtistStreamsStatisticsTopTracksResourceIdentifier]**](ArtistStreamsStatisticsTopTracksResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 
**meta** | [**ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocumentMeta**](ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocumentMeta.md) |  | [optional] 

## Example

```python
from tidal.models.artist_streams_statistics_top_tracks_multi_relationship_data_document import ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocument from a JSON string
artist_streams_statistics_top_tracks_multi_relationship_data_document_instance = ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocument.to_json())

# convert the object into a dict
artist_streams_statistics_top_tracks_multi_relationship_data_document_dict = artist_streams_statistics_top_tracks_multi_relationship_data_document_instance.to_dict()
# create an instance of ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocument from a dict
artist_streams_statistics_top_tracks_multi_relationship_data_document_from_dict = ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocument.from_dict(artist_streams_statistics_top_tracks_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


