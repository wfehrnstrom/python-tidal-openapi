# UserDataExportRequestsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_type** | **str** | The type of data export flow | 

## Example

```python
from tidal.models.user_data_export_requests_attributes import UserDataExportRequestsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UserDataExportRequestsAttributes from a JSON string
user_data_export_requests_attributes_instance = UserDataExportRequestsAttributes.from_json(json)
# print the JSON string representation of the object
print(UserDataExportRequestsAttributes.to_json())

# convert the object into a dict
user_data_export_requests_attributes_dict = user_data_export_requests_attributes_instance.to_dict()
# create an instance of UserDataExportRequestsAttributes from a dict
user_data_export_requests_attributes_from_dict = UserDataExportRequestsAttributes.from_dict(user_data_export_requests_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


