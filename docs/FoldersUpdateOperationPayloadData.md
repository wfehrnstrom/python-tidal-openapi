# FoldersUpdateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**FoldersUpdateOperationPayloadDataAttributes**](FoldersUpdateOperationPayloadDataAttributes.md) |  | 
**id** | **str** | Also accepts &#x60;me&#x60;. | 
**type** | **str** |  | 

## Example

```python
from tidal.models.folders_update_operation_payload_data import FoldersUpdateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of FoldersUpdateOperationPayloadData from a JSON string
folders_update_operation_payload_data_instance = FoldersUpdateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(FoldersUpdateOperationPayloadData.to_json())

# convert the object into a dict
folders_update_operation_payload_data_dict = folders_update_operation_payload_data_instance.to_dict()
# create an instance of FoldersUpdateOperationPayloadData from a dict
folders_update_operation_payload_data_from_dict = FoldersUpdateOperationPayloadData.from_dict(folders_update_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


