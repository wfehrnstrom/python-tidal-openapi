# InstallationsCreateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_provided_installation_id** | **str** | Client provided installation identifier | 
**name** | **str** | Human-readable name | 

## Example

```python
from tidal.models.installations_create_operation_payload_data_attributes import InstallationsCreateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of InstallationsCreateOperationPayloadDataAttributes from a JSON string
installations_create_operation_payload_data_attributes_instance = InstallationsCreateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(InstallationsCreateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
installations_create_operation_payload_data_attributes_dict = installations_create_operation_payload_data_attributes_instance.to_dict()
# create an instance of InstallationsCreateOperationPayloadDataAttributes from a dict
installations_create_operation_payload_data_attributes_from_dict = InstallationsCreateOperationPayloadDataAttributes.from_dict(installations_create_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


