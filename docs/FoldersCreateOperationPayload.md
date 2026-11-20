# FoldersCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**FoldersCreateOperationPayloadData**](FoldersCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.folders_create_operation_payload import FoldersCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of FoldersCreateOperationPayload from a JSON string
folders_create_operation_payload_instance = FoldersCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(FoldersCreateOperationPayload.to_json())

# convert the object into a dict
folders_create_operation_payload_dict = folders_create_operation_payload_instance.to_dict()
# create an instance of FoldersCreateOperationPayload from a dict
folders_create_operation_payload_from_dict = FoldersCreateOperationPayload.from_dict(folders_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


