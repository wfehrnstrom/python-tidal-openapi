# CommentsReactionSummarySingleRelationshipDataDocument

Target resource types: `reactionSummaries`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.comments_reaction_summary_single_relationship_data_document import CommentsReactionSummarySingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsReactionSummarySingleRelationshipDataDocument from a JSON string
comments_reaction_summary_single_relationship_data_document_instance = CommentsReactionSummarySingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(CommentsReactionSummarySingleRelationshipDataDocument.to_json())

# convert the object into a dict
comments_reaction_summary_single_relationship_data_document_dict = comments_reaction_summary_single_relationship_data_document_instance.to_dict()
# create an instance of CommentsReactionSummarySingleRelationshipDataDocument from a dict
comments_reaction_summary_single_relationship_data_document_from_dict = CommentsReactionSummarySingleRelationshipDataDocument.from_dict(comments_reaction_summary_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


