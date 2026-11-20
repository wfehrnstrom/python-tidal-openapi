# UserReportsCreateResource403ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[UserReportsCreateResource403ResponseBodyErrorsInner]**](UserReportsCreateResource403ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.user_reports_create_resource403_response_body import UserReportsCreateResource403ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of UserReportsCreateResource403ResponseBody from a JSON string
user_reports_create_resource403_response_body_instance = UserReportsCreateResource403ResponseBody.from_json(json)
# print the JSON string representation of the object
print(UserReportsCreateResource403ResponseBody.to_json())

# convert the object into a dict
user_reports_create_resource403_response_body_dict = user_reports_create_resource403_response_body_instance.to_dict()
# create an instance of UserReportsCreateResource403ResponseBody from a dict
user_reports_create_resource403_response_body_from_dict = UserReportsCreateResource403ResponseBody.from_dict(user_reports_create_resource403_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


