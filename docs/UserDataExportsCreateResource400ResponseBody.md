# UserDataExportsCreateResource400ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[UserDataExportsCreateResource400ResponseBodyErrorsInner]**](UserDataExportsCreateResource400ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.user_data_exports_create_resource400_response_body import UserDataExportsCreateResource400ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of UserDataExportsCreateResource400ResponseBody from a JSON string
user_data_exports_create_resource400_response_body_instance = UserDataExportsCreateResource400ResponseBody.from_json(json)
# print the JSON string representation of the object
print(UserDataExportsCreateResource400ResponseBody.to_json())

# convert the object into a dict
user_data_exports_create_resource400_response_body_dict = user_data_exports_create_resource400_response_body_instance.to_dict()
# create an instance of UserDataExportsCreateResource400ResponseBody from a dict
user_data_exports_create_resource400_response_body_from_dict = UserDataExportsCreateResource400ResponseBody.from_dict(user_data_exports_create_resource400_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


