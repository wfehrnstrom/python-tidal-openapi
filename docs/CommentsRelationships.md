# CommentsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**CommentsAuthorSingleRelationshipDataDocument**](CommentsAuthorSingleRelationshipDataDocument.md) |  | [optional] 
**comment_summary** | [**CommentsCommentSummarySingleRelationshipDataDocument**](CommentsCommentSummarySingleRelationshipDataDocument.md) |  | [optional] 
**owners** | [**CommentsOwnersMultiRelationshipDataDocument**](CommentsOwnersMultiRelationshipDataDocument.md) |  | [optional] 
**reaction_summary** | [**CommentsReactionSummarySingleRelationshipDataDocument**](CommentsReactionSummarySingleRelationshipDataDocument.md) |  | [optional] 
**root_subject** | [**CommentsRootSubjectSingleRelationshipDataDocument**](CommentsRootSubjectSingleRelationshipDataDocument.md) |  | [optional] 
**subject** | [**CommentsSubjectSingleRelationshipDataDocument**](CommentsSubjectSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.comments_relationships import CommentsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsRelationships from a JSON string
comments_relationships_instance = CommentsRelationships.from_json(json)
# print the JSON string representation of the object
print(CommentsRelationships.to_json())

# convert the object into a dict
comments_relationships_dict = comments_relationships_instance.to_dict()
# create an instance of CommentsRelationships from a dict
comments_relationships_from_dict = CommentsRelationships.from_dict(comments_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


