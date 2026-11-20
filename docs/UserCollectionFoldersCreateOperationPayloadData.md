# UserCollectionFoldersCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UserCollectionFoldersCreateOperationPayloadDataAttributes**](UserCollectionFoldersCreateOperationPayloadDataAttributes.md) |  | 
**relationships** | [**UserCollectionFoldersCreateOperationPayloadDataRelationships**](UserCollectionFoldersCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.user_collection_folders_create_operation_payload_data import UserCollectionFoldersCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionFoldersCreateOperationPayloadData from a JSON string
user_collection_folders_create_operation_payload_data_instance = UserCollectionFoldersCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(UserCollectionFoldersCreateOperationPayloadData.to_json())

# convert the object into a dict
user_collection_folders_create_operation_payload_data_dict = user_collection_folders_create_operation_payload_data_instance.to_dict()
# create an instance of UserCollectionFoldersCreateOperationPayloadData from a dict
user_collection_folders_create_operation_payload_data_from_dict = UserCollectionFoldersCreateOperationPayloadData.from_dict(user_collection_folders_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


