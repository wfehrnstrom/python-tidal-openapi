# FoldersCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**FoldersCreateOperationPayloadDataAttributes**](FoldersCreateOperationPayloadDataAttributes.md) |  | 
**relationships** | [**FoldersCreateOperationPayloadDataRelationships**](FoldersCreateOperationPayloadDataRelationships.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from tidal.models.folders_create_operation_payload_data import FoldersCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of FoldersCreateOperationPayloadData from a JSON string
folders_create_operation_payload_data_instance = FoldersCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(FoldersCreateOperationPayloadData.to_json())

# convert the object into a dict
folders_create_operation_payload_data_dict = folders_create_operation_payload_data_instance.to_dict()
# create an instance of FoldersCreateOperationPayloadData from a dict
folders_create_operation_payload_data_from_dict = FoldersCreateOperationPayloadData.from_dict(folders_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


