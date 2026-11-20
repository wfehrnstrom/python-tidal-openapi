# UserCollectionSaveForLatersResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UserCollectionSaveForLatersAttributes**](UserCollectionSaveForLatersAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**UserCollectionSaveForLatersRelationships**](UserCollectionSaveForLatersRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.user_collection_save_for_laters_resource_object import UserCollectionSaveForLatersResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionSaveForLatersResourceObject from a JSON string
user_collection_save_for_laters_resource_object_instance = UserCollectionSaveForLatersResourceObject.from_json(json)
# print the JSON string representation of the object
print(UserCollectionSaveForLatersResourceObject.to_json())

# convert the object into a dict
user_collection_save_for_laters_resource_object_dict = user_collection_save_for_laters_resource_object_instance.to_dict()
# create an instance of UserCollectionSaveForLatersResourceObject from a dict
user_collection_save_for_laters_resource_object_from_dict = UserCollectionSaveForLatersResourceObject.from_dict(user_collection_save_for_laters_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


