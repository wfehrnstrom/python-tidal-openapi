# UserCollectionAlbumsItemsResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**UserCollectionAlbumsItemsResourceIdentifierMeta**](UserCollectionAlbumsItemsResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.user_collection_albums_items_resource_identifier import UserCollectionAlbumsItemsResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionAlbumsItemsResourceIdentifier from a JSON string
user_collection_albums_items_resource_identifier_instance = UserCollectionAlbumsItemsResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(UserCollectionAlbumsItemsResourceIdentifier.to_json())

# convert the object into a dict
user_collection_albums_items_resource_identifier_dict = user_collection_albums_items_resource_identifier_instance.to_dict()
# create an instance of UserCollectionAlbumsItemsResourceIdentifier from a dict
user_collection_albums_items_resource_identifier_from_dict = UserCollectionAlbumsItemsResourceIdentifier.from_dict(user_collection_albums_items_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


