# UserDataExportsCreateOperationPayloadMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** | Language of the email sent when the export is ready. English when absent, malformed or not translated. | [optional] 

## Example

```python
from tidal.models.user_data_exports_create_operation_payload_meta import UserDataExportsCreateOperationPayloadMeta

# TODO update the JSON string below
json = "{}"
# create an instance of UserDataExportsCreateOperationPayloadMeta from a JSON string
user_data_exports_create_operation_payload_meta_instance = UserDataExportsCreateOperationPayloadMeta.from_json(json)
# print the JSON string representation of the object
print(UserDataExportsCreateOperationPayloadMeta.to_json())

# convert the object into a dict
user_data_exports_create_operation_payload_meta_dict = user_data_exports_create_operation_payload_meta_instance.to_dict()
# create an instance of UserDataExportsCreateOperationPayloadMeta from a dict
user_data_exports_create_operation_payload_meta_from_dict = UserDataExportsCreateOperationPayloadMeta.from_dict(user_data_exports_create_operation_payload_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


