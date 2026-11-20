# FolderItemsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relationships** | [**FolderItemsCreateOperationPayloadDataRelationships**](FolderItemsCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.folder_items_create_operation_payload_data import FolderItemsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of FolderItemsCreateOperationPayloadData from a JSON string
folder_items_create_operation_payload_data_instance = FolderItemsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(FolderItemsCreateOperationPayloadData.to_json())

# convert the object into a dict
folder_items_create_operation_payload_data_dict = folder_items_create_operation_payload_data_instance.to_dict()
# create an instance of FolderItemsCreateOperationPayloadData from a dict
folder_items_create_operation_payload_data_from_dict = FolderItemsCreateOperationPayloadData.from_dict(folder_items_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


