# UserCollectionSaveForLatersAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_modified_at** | **datetime** | When the collection was last modified | [optional] 
**number_of_items** | **int** | Number of items in the collection | 

## Example

```python
from tidal.models.user_collection_save_for_laters_attributes import UserCollectionSaveForLatersAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionSaveForLatersAttributes from a JSON string
user_collection_save_for_laters_attributes_instance = UserCollectionSaveForLatersAttributes.from_json(json)
# print the JSON string representation of the object
print(UserCollectionSaveForLatersAttributes.to_json())

# convert the object into a dict
user_collection_save_for_laters_attributes_dict = user_collection_save_for_laters_attributes_instance.to_dict()
# create an instance of UserCollectionSaveForLatersAttributes from a dict
user_collection_save_for_laters_attributes_from_dict = UserCollectionSaveForLatersAttributes.from_dict(user_collection_save_for_laters_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


