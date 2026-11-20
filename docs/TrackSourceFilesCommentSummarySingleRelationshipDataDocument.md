# TrackSourceFilesCommentSummarySingleRelationshipDataDocument

Target resource types: `commentSummaries`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.track_source_files_comment_summary_single_relationship_data_document import TrackSourceFilesCommentSummarySingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TrackSourceFilesCommentSummarySingleRelationshipDataDocument from a JSON string
track_source_files_comment_summary_single_relationship_data_document_instance = TrackSourceFilesCommentSummarySingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(TrackSourceFilesCommentSummarySingleRelationshipDataDocument.to_json())

# convert the object into a dict
track_source_files_comment_summary_single_relationship_data_document_dict = track_source_files_comment_summary_single_relationship_data_document_instance.to_dict()
# create an instance of TrackSourceFilesCommentSummarySingleRelationshipDataDocument from a dict
track_source_files_comment_summary_single_relationship_data_document_from_dict = TrackSourceFilesCommentSummarySingleRelationshipDataDocument.from_dict(track_source_files_comment_summary_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


