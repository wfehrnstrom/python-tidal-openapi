# ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocumentMeta

status is the breakdownsStatus of the statistics. When it is not OK the entries are withheld, so the empty linkage is not a measured empty result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hidden_count** | **int** | Tracks left out because too few people listened to them. Present when status is OK | [optional] 
**status** | **str** | Status of artist statistics that may be withheld. OK: the data is present. SUPPRESSED: withheld because too few people are counted to show it. UNAVAILABLE: not available at the moment | 

## Example

```python
from tidal.models.artist_streams_statistics_top_tracks_multi_relationship_data_document_meta import ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocumentMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocumentMeta from a JSON string
artist_streams_statistics_top_tracks_multi_relationship_data_document_meta_instance = ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocumentMeta.from_json(json)
# print the JSON string representation of the object
print(ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocumentMeta.to_json())

# convert the object into a dict
artist_streams_statistics_top_tracks_multi_relationship_data_document_meta_dict = artist_streams_statistics_top_tracks_multi_relationship_data_document_meta_instance.to_dict()
# create an instance of ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocumentMeta from a dict
artist_streams_statistics_top_tracks_multi_relationship_data_document_meta_from_dict = ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocumentMeta.from_dict(artist_streams_statistics_top_tracks_multi_relationship_data_document_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


