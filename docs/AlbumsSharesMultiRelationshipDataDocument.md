# AlbumsSharesMultiRelationshipDataDocument

Target resource types: `shares`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.albums_shares_multi_relationship_data_document import AlbumsSharesMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsSharesMultiRelationshipDataDocument from a JSON string
albums_shares_multi_relationship_data_document_instance = AlbumsSharesMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(AlbumsSharesMultiRelationshipDataDocument.to_json())

# convert the object into a dict
albums_shares_multi_relationship_data_document_dict = albums_shares_multi_relationship_data_document_instance.to_dict()
# create an instance of AlbumsSharesMultiRelationshipDataDocument from a dict
albums_shares_multi_relationship_data_document_from_dict = AlbumsSharesMultiRelationshipDataDocument.from_dict(albums_shares_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


