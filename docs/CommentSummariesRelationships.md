# CommentSummariesRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | [**CommentSummariesSubjectSingleRelationshipDataDocument**](CommentSummariesSubjectSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.comment_summaries_relationships import CommentSummariesRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of CommentSummariesRelationships from a JSON string
comment_summaries_relationships_instance = CommentSummariesRelationships.from_json(json)
# print the JSON string representation of the object
print(CommentSummariesRelationships.to_json())

# convert the object into a dict
comment_summaries_relationships_dict = comment_summaries_relationships_instance.to_dict()
# create an instance of CommentSummariesRelationships from a dict
comment_summaries_relationships_from_dict = CommentSummariesRelationships.from_dict(comment_summaries_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


