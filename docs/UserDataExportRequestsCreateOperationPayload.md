# UserDataExportRequestsCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserDataExportRequestsCreateOperationPayloadData**](UserDataExportRequestsCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.user_data_export_requests_create_operation_payload import UserDataExportRequestsCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserDataExportRequestsCreateOperationPayload from a JSON string
user_data_export_requests_create_operation_payload_instance = UserDataExportRequestsCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(UserDataExportRequestsCreateOperationPayload.to_json())

# convert the object into a dict
user_data_export_requests_create_operation_payload_dict = user_data_export_requests_create_operation_payload_instance.to_dict()
# create an instance of UserDataExportRequestsCreateOperationPayload from a dict
user_data_export_requests_create_operation_payload_from_dict = UserDataExportRequestsCreateOperationPayload.from_dict(user_data_export_requests_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


