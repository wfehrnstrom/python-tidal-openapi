# UserReportsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UserReportsCreateOperationPayloadDataAttributes**](UserReportsCreateOperationPayloadDataAttributes.md) |  | 
**relationships** | [**UserReportsCreateOperationPayloadDataRelationships**](UserReportsCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.user_reports_create_operation_payload_data import UserReportsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of UserReportsCreateOperationPayloadData from a JSON string
user_reports_create_operation_payload_data_instance = UserReportsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(UserReportsCreateOperationPayloadData.to_json())

# convert the object into a dict
user_reports_create_operation_payload_data_dict = user_reports_create_operation_payload_data_instance.to_dict()
# create an instance of UserReportsCreateOperationPayloadData from a dict
user_reports_create_operation_payload_data_from_dict = UserReportsCreateOperationPayloadData.from_dict(user_reports_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


