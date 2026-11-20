# TrackSourceFilesRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_summary** | [**TrackSourceFilesCommentSummarySingleRelationshipDataDocument**](TrackSourceFilesCommentSummarySingleRelationshipDataDocument.md) |  | [optional] 
**owners** | [**TrackSourceFilesOwnersMultiRelationshipDataDocument**](TrackSourceFilesOwnersMultiRelationshipDataDocument.md) |  | [optional] 
**reaction_summary** | [**TrackSourceFilesReactionSummarySingleRelationshipDataDocument**](TrackSourceFilesReactionSummarySingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.track_source_files_relationships import TrackSourceFilesRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of TrackSourceFilesRelationships from a JSON string
track_source_files_relationships_instance = TrackSourceFilesRelationships.from_json(json)
# print the JSON string representation of the object
print(TrackSourceFilesRelationships.to_json())

# convert the object into a dict
track_source_files_relationships_dict = track_source_files_relationships_instance.to_dict()
# create an instance of TrackSourceFilesRelationships from a dict
track_source_files_relationships_from_dict = TrackSourceFilesRelationships.from_dict(track_source_files_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


