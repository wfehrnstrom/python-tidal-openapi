# UserCollectionFoldersUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserCollectionFoldersUpdateOperationPayloadData**](UserCollectionFoldersUpdateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.user_collection_folders_update_operation_payload import UserCollectionFoldersUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionFoldersUpdateOperationPayload from a JSON string
user_collection_folders_update_operation_payload_instance = UserCollectionFoldersUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(UserCollectionFoldersUpdateOperationPayload.to_json())

# convert the object into a dict
user_collection_folders_update_operation_payload_dict = user_collection_folders_update_operation_payload_instance.to_dict()
# create an instance of UserCollectionFoldersUpdateOperationPayload from a dict
user_collection_folders_update_operation_payload_from_dict = UserCollectionFoldersUpdateOperationPayload.from_dict(user_collection_folders_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


