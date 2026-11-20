# UserDataExportsCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserDataExportsCreateOperationPayloadData**](UserDataExportsCreateOperationPayloadData.md) |  | 
**meta** | [**UserDataExportsCreateOperationPayloadMeta**](UserDataExportsCreateOperationPayloadMeta.md) |  | [optional] 

## Example

```python
from tidal.models.user_data_exports_create_operation_payload import UserDataExportsCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserDataExportsCreateOperationPayload from a JSON string
user_data_exports_create_operation_payload_instance = UserDataExportsCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(UserDataExportsCreateOperationPayload.to_json())

# convert the object into a dict
user_data_exports_create_operation_payload_dict = user_data_exports_create_operation_payload_instance.to_dict()
# create an instance of UserDataExportsCreateOperationPayload from a dict
user_data_exports_create_operation_payload_from_dict = UserDataExportsCreateOperationPayload.from_dict(user_data_exports_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


