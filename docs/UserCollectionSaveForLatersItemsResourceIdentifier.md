# UserCollectionSaveForLatersItemsResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**UserCollectionSaveForLatersItemsResourceIdentifierMeta**](UserCollectionSaveForLatersItemsResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.user_collection_save_for_laters_items_resource_identifier import UserCollectionSaveForLatersItemsResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionSaveForLatersItemsResourceIdentifier from a JSON string
user_collection_save_for_laters_items_resource_identifier_instance = UserCollectionSaveForLatersItemsResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(UserCollectionSaveForLatersItemsResourceIdentifier.to_json())

# convert the object into a dict
user_collection_save_for_laters_items_resource_identifier_dict = user_collection_save_for_laters_items_resource_identifier_instance.to_dict()
# create an instance of UserCollectionSaveForLatersItemsResourceIdentifier from a dict
user_collection_save_for_laters_items_resource_identifier_from_dict = UserCollectionSaveForLatersItemsResourceIdentifier.from_dict(user_collection_save_for_laters_items_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


