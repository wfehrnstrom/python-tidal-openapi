# TrackSourceFilesReactionSummarySingleRelationshipDataDocument

Target resource types: `reactionSummaries`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.track_source_files_reaction_summary_single_relationship_data_document import TrackSourceFilesReactionSummarySingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TrackSourceFilesReactionSummarySingleRelationshipDataDocument from a JSON string
track_source_files_reaction_summary_single_relationship_data_document_instance = TrackSourceFilesReactionSummarySingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(TrackSourceFilesReactionSummarySingleRelationshipDataDocument.to_json())

# convert the object into a dict
track_source_files_reaction_summary_single_relationship_data_document_dict = track_source_files_reaction_summary_single_relationship_data_document_instance.to_dict()
# create an instance of TrackSourceFilesReactionSummarySingleRelationshipDataDocument from a dict
track_source_files_reaction_summary_single_relationship_data_document_from_dict = TrackSourceFilesReactionSummarySingleRelationshipDataDocument.from_dict(track_source_files_reaction_summary_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


