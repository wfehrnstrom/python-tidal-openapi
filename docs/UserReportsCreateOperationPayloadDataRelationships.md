# UserReportsCreateOperationPayloadDataRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reported_resources** | [**UserReportsCreateOperationPayloadDataRelationshipsReportedResources**](UserReportsCreateOperationPayloadDataRelationshipsReportedResources.md) |  | 

## Example

```python
from tidal.models.user_reports_create_operation_payload_data_relationships import UserReportsCreateOperationPayloadDataRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of UserReportsCreateOperationPayloadDataRelationships from a JSON string
user_reports_create_operation_payload_data_relationships_instance = UserReportsCreateOperationPayloadDataRelationships.from_json(json)
# print the JSON string representation of the object
print(UserReportsCreateOperationPayloadDataRelationships.to_json())

# convert the object into a dict
user_reports_create_operation_payload_data_relationships_dict = user_reports_create_operation_payload_data_relationships_instance.to_dict()
# create an instance of UserReportsCreateOperationPayloadDataRelationships from a dict
user_reports_create_operation_payload_data_relationships_from_dict = UserReportsCreateOperationPayloadDataRelationships.from_dict(user_reports_create_operation_payload_data_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


