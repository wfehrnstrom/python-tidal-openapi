# AlbumsItemsMultiRelationshipDataDocument

Target resource types: `tracks`, `videos`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AlbumsItemsResourceIdentifier]**](AlbumsItemsResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.albums_items_multi_relationship_data_document import AlbumsItemsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsItemsMultiRelationshipDataDocument from a JSON string
albums_items_multi_relationship_data_document_instance = AlbumsItemsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(AlbumsItemsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
albums_items_multi_relationship_data_document_dict = albums_items_multi_relationship_data_document_instance.to_dict()
# create an instance of AlbumsItemsMultiRelationshipDataDocument from a dict
albums_items_multi_relationship_data_document_from_dict = AlbumsItemsMultiRelationshipDataDocument.from_dict(albums_items_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


