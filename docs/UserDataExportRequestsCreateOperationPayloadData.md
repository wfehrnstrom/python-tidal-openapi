# UserDataExportRequestsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UserDataExportRequestsCreateOperationPayloadDataAttributes**](UserDataExportRequestsCreateOperationPayloadDataAttributes.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.user_data_export_requests_create_operation_payload_data import UserDataExportRequestsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of UserDataExportRequestsCreateOperationPayloadData from a JSON string
user_data_export_requests_create_operation_payload_data_instance = UserDataExportRequestsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(UserDataExportRequestsCreateOperationPayloadData.to_json())

# convert the object into a dict
user_data_export_requests_create_operation_payload_data_dict = user_data_export_requests_create_operation_payload_data_instance.to_dict()
# create an instance of UserDataExportRequestsCreateOperationPayloadData from a dict
user_data_export_requests_create_operation_payload_data_from_dict = UserDataExportRequestsCreateOperationPayloadData.from_dict(user_data_export_requests_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


