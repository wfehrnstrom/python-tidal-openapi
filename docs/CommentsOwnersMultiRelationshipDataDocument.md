# CommentsOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.comments_owners_multi_relationship_data_document import CommentsOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsOwnersMultiRelationshipDataDocument from a JSON string
comments_owners_multi_relationship_data_document_instance = CommentsOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(CommentsOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
comments_owners_multi_relationship_data_document_dict = comments_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of CommentsOwnersMultiRelationshipDataDocument from a dict
comments_owners_multi_relationship_data_document_from_dict = CommentsOwnersMultiRelationshipDataDocument.from_dict(comments_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


