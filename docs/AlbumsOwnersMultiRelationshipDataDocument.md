# AlbumsOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.albums_owners_multi_relationship_data_document import AlbumsOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsOwnersMultiRelationshipDataDocument from a JSON string
albums_owners_multi_relationship_data_document_instance = AlbumsOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(AlbumsOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
albums_owners_multi_relationship_data_document_dict = albums_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of AlbumsOwnersMultiRelationshipDataDocument from a dict
albums_owners_multi_relationship_data_document_from_dict = AlbumsOwnersMultiRelationshipDataDocument.from_dict(albums_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


