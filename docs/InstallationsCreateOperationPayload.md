# InstallationsCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**InstallationsCreateOperationPayloadData**](InstallationsCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.installations_create_operation_payload import InstallationsCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InstallationsCreateOperationPayload from a JSON string
installations_create_operation_payload_instance = InstallationsCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(InstallationsCreateOperationPayload.to_json())

# convert the object into a dict
installations_create_operation_payload_dict = installations_create_operation_payload_instance.to_dict()
# create an instance of InstallationsCreateOperationPayload from a dict
installations_create_operation_payload_from_dict = InstallationsCreateOperationPayload.from_dict(installations_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


