# UserReportsCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserReportsCreateOperationPayloadData**](UserReportsCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.user_reports_create_operation_payload import UserReportsCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserReportsCreateOperationPayload from a JSON string
user_reports_create_operation_payload_instance = UserReportsCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(UserReportsCreateOperationPayload.to_json())

# convert the object into a dict
user_reports_create_operation_payload_dict = user_reports_create_operation_payload_instance.to_dict()
# create an instance of UserReportsCreateOperationPayload from a dict
user_reports_create_operation_payload_from_dict = UserReportsCreateOperationPayload.from_dict(user_reports_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


