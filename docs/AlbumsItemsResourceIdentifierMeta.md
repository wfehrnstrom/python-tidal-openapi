# AlbumsItemsResourceIdentifierMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replacement** | [**ReplacementProvenance**](ReplacementProvenance.md) |  | [optional] 
**track_number** | **int** | track number | 
**volume_number** | **int** | volume number | 

## Example

```python
from tidal.models.albums_items_resource_identifier_meta import AlbumsItemsResourceIdentifierMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsItemsResourceIdentifierMeta from a JSON string
albums_items_resource_identifier_meta_instance = AlbumsItemsResourceIdentifierMeta.from_json(json)
# print the JSON string representation of the object
print(AlbumsItemsResourceIdentifierMeta.to_json())

# convert the object into a dict
albums_items_resource_identifier_meta_dict = albums_items_resource_identifier_meta_instance.to_dict()
# create an instance of AlbumsItemsResourceIdentifierMeta from a dict
albums_items_resource_identifier_meta_from_dict = AlbumsItemsResourceIdentifierMeta.from_dict(albums_items_resource_identifier_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


