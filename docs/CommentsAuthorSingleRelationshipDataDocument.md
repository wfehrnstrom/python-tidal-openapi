# CommentsAuthorSingleRelationshipDataDocument

Target resource types: `artists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.comments_author_single_relationship_data_document import CommentsAuthorSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsAuthorSingleRelationshipDataDocument from a JSON string
comments_author_single_relationship_data_document_instance = CommentsAuthorSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(CommentsAuthorSingleRelationshipDataDocument.to_json())

# convert the object into a dict
comments_author_single_relationship_data_document_dict = comments_author_single_relationship_data_document_instance.to_dict()
# create an instance of CommentsAuthorSingleRelationshipDataDocument from a dict
comments_author_single_relationship_data_document_from_dict = CommentsAuthorSingleRelationshipDataDocument.from_dict(comments_author_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


