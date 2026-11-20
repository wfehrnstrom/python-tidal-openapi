# UserDataExportsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UserDataExportsCreateOperationPayloadDataAttributes**](UserDataExportsCreateOperationPayloadDataAttributes.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from tidal.models.user_data_exports_create_operation_payload_data import UserDataExportsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of UserDataExportsCreateOperationPayloadData from a JSON string
user_data_exports_create_operation_payload_data_instance = UserDataExportsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(UserDataExportsCreateOperationPayloadData.to_json())

# convert the object into a dict
user_data_exports_create_operation_payload_data_dict = user_data_exports_create_operation_payload_data_instance.to_dict()
# create an instance of UserDataExportsCreateOperationPayloadData from a dict
user_data_exports_create_operation_payload_data_from_dict = UserDataExportsCreateOperationPayloadData.from_dict(user_data_exports_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


