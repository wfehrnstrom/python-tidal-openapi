# UserCollectionFoldersUpdateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UserCollectionFoldersUpdateOperationPayloadDataAttributes**](UserCollectionFoldersUpdateOperationPayloadDataAttributes.md) |  | 
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.user_collection_folders_update_operation_payload_data import UserCollectionFoldersUpdateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionFoldersUpdateOperationPayloadData from a JSON string
user_collection_folders_update_operation_payload_data_instance = UserCollectionFoldersUpdateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(UserCollectionFoldersUpdateOperationPayloadData.to_json())

# convert the object into a dict
user_collection_folders_update_operation_payload_data_dict = user_collection_folders_update_operation_payload_data_instance.to_dict()
# create an instance of UserCollectionFoldersUpdateOperationPayloadData from a dict
user_collection_folders_update_operation_payload_data_from_dict = UserCollectionFoldersUpdateOperationPayloadData.from_dict(user_collection_folders_update_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


