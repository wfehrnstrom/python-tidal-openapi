# AlbumsItemsResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**AlbumsItemsResourceIdentifierMeta**](AlbumsItemsResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.albums_items_resource_identifier import AlbumsItemsResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsItemsResourceIdentifier from a JSON string
albums_items_resource_identifier_instance = AlbumsItemsResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(AlbumsItemsResourceIdentifier.to_json())

# convert the object into a dict
albums_items_resource_identifier_dict = albums_items_resource_identifier_instance.to_dict()
# create an instance of AlbumsItemsResourceIdentifier from a dict
albums_items_resource_identifier_from_dict = AlbumsItemsResourceIdentifier.from_dict(albums_items_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


