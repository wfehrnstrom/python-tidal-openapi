# TracksSimilarTracksMultiRelationshipDataDocument

Target resource types: `tracks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TracksSimilarTracksResourceIdentifier]**](TracksSimilarTracksResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.tracks_similar_tracks_multi_relationship_data_document import TracksSimilarTracksMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TracksSimilarTracksMultiRelationshipDataDocument from a JSON string
tracks_similar_tracks_multi_relationship_data_document_instance = TracksSimilarTracksMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(TracksSimilarTracksMultiRelationshipDataDocument.to_json())

# convert the object into a dict
tracks_similar_tracks_multi_relationship_data_document_dict = tracks_similar_tracks_multi_relationship_data_document_instance.to_dict()
# create an instance of TracksSimilarTracksMultiRelationshipDataDocument from a dict
tracks_similar_tracks_multi_relationship_data_document_from_dict = TracksSimilarTracksMultiRelationshipDataDocument.from_dict(tracks_similar_tracks_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


