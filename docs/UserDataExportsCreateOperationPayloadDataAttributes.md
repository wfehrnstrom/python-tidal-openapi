# UserDataExportsCreateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_types** | **List[str]** | Data types to export. Every data type when absent; when present, at least one is required. | [optional] 

## Example

```python
from tidal.models.user_data_exports_create_operation_payload_data_attributes import UserDataExportsCreateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UserDataExportsCreateOperationPayloadDataAttributes from a JSON string
user_data_exports_create_operation_payload_data_attributes_instance = UserDataExportsCreateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(UserDataExportsCreateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
user_data_exports_create_operation_payload_data_attributes_dict = user_data_exports_create_operation_payload_data_attributes_instance.to_dict()
# create an instance of UserDataExportsCreateOperationPayloadDataAttributes from a dict
user_data_exports_create_operation_payload_data_attributes_from_dict = UserDataExportsCreateOperationPayloadDataAttributes.from_dict(user_data_exports_create_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


