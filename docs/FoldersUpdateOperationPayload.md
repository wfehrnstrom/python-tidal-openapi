# FoldersUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**FoldersUpdateOperationPayloadData**](FoldersUpdateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.folders_update_operation_payload import FoldersUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of FoldersUpdateOperationPayload from a JSON string
folders_update_operation_payload_instance = FoldersUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(FoldersUpdateOperationPayload.to_json())

# convert the object into a dict
folders_update_operation_payload_dict = folders_update_operation_payload_instance.to_dict()
# create an instance of FoldersUpdateOperationPayload from a dict
folders_update_operation_payload_from_dict = FoldersUpdateOperationPayload.from_dict(folders_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


