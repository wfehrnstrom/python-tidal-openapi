# UserReportsCreateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**reason** | **str** |  | 

## Example

```python
from tidal.models.user_reports_create_operation_payload_data_attributes import UserReportsCreateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UserReportsCreateOperationPayloadDataAttributes from a JSON string
user_reports_create_operation_payload_data_attributes_instance = UserReportsCreateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(UserReportsCreateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
user_reports_create_operation_payload_data_attributes_dict = user_reports_create_operation_payload_data_attributes_instance.to_dict()
# create an instance of UserReportsCreateOperationPayloadDataAttributes from a dict
user_reports_create_operation_payload_data_attributes_from_dict = UserReportsCreateOperationPayloadDataAttributes.from_dict(user_reports_create_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


