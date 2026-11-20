# InstallationsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**InstallationsCreateOperationPayloadDataAttributes**](InstallationsCreateOperationPayloadDataAttributes.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.installations_create_operation_payload_data import InstallationsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of InstallationsCreateOperationPayloadData from a JSON string
installations_create_operation_payload_data_instance = InstallationsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(InstallationsCreateOperationPayloadData.to_json())

# convert the object into a dict
installations_create_operation_payload_data_dict = installations_create_operation_payload_data_instance.to_dict()
# create an instance of InstallationsCreateOperationPayloadData from a dict
installations_create_operation_payload_data_from_dict = InstallationsCreateOperationPayloadData.from_dict(installations_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


