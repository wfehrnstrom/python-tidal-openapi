# TracksSuggestedTracksMultiRelationshipDataDocument

Target resource types: `tracks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TracksSuggestedTracksResourceIdentifier]**](TracksSuggestedTracksResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.tracks_suggested_tracks_multi_relationship_data_document import TracksSuggestedTracksMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TracksSuggestedTracksMultiRelationshipDataDocument from a JSON string
tracks_suggested_tracks_multi_relationship_data_document_instance = TracksSuggestedTracksMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(TracksSuggestedTracksMultiRelationshipDataDocument.to_json())

# convert the object into a dict
tracks_suggested_tracks_multi_relationship_data_document_dict = tracks_suggested_tracks_multi_relationship_data_document_instance.to_dict()
# create an instance of TracksSuggestedTracksMultiRelationshipDataDocument from a dict
tracks_suggested_tracks_multi_relationship_data_document_from_dict = TracksSuggestedTracksMultiRelationshipDataDocument.from_dict(tracks_suggested_tracks_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


