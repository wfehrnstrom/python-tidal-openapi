# FolderItemsCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**FolderItemsCreateOperationPayloadData**](FolderItemsCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.folder_items_create_operation_payload import FolderItemsCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of FolderItemsCreateOperationPayload from a JSON string
folder_items_create_operation_payload_instance = FolderItemsCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(FolderItemsCreateOperationPayload.to_json())

# convert the object into a dict
folder_items_create_operation_payload_dict = folder_items_create_operation_payload_instance.to_dict()
# create an instance of FolderItemsCreateOperationPayload from a dict
folder_items_create_operation_payload_from_dict = FolderItemsCreateOperationPayload.from_dict(folder_items_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


