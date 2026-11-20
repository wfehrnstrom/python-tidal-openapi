# UserDataExportsCreateResource409ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[UserDataExportsCreateResource409ResponseBodyErrorsInner]**](UserDataExportsCreateResource409ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.user_data_exports_create_resource409_response_body import UserDataExportsCreateResource409ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of UserDataExportsCreateResource409ResponseBody from a JSON string
user_data_exports_create_resource409_response_body_instance = UserDataExportsCreateResource409ResponseBody.from_json(json)
# print the JSON string representation of the object
print(UserDataExportsCreateResource409ResponseBody.to_json())

# convert the object into a dict
user_data_exports_create_resource409_response_body_dict = user_data_exports_create_resource409_response_body_instance.to_dict()
# create an instance of UserDataExportsCreateResource409ResponseBody from a dict
user_data_exports_create_resource409_response_body_from_dict = UserDataExportsCreateResource409ResponseBody.from_dict(user_data_exports_create_resource409_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


