# UserCollectionFoldersCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserCollectionFoldersCreateOperationPayloadData**](UserCollectionFoldersCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.user_collection_folders_create_operation_payload import UserCollectionFoldersCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionFoldersCreateOperationPayload from a JSON string
user_collection_folders_create_operation_payload_instance = UserCollectionFoldersCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(UserCollectionFoldersCreateOperationPayload.to_json())

# convert the object into a dict
user_collection_folders_create_operation_payload_dict = user_collection_folders_create_operation_payload_instance.to_dict()
# create an instance of UserCollectionFoldersCreateOperationPayload from a dict
user_collection_folders_create_operation_payload_from_dict = UserCollectionFoldersCreateOperationPayload.from_dict(user_collection_folders_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


