# UserReportsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UserReportsAttributes**](UserReportsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.user_reports_resource_object import UserReportsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserReportsResourceObject from a JSON string
user_reports_resource_object_instance = UserReportsResourceObject.from_json(json)
# print the JSON string representation of the object
print(UserReportsResourceObject.to_json())

# convert the object into a dict
user_reports_resource_object_dict = user_reports_resource_object_instance.to_dict()
# create an instance of UserReportsResourceObject from a dict
user_reports_resource_object_from_dict = UserReportsResourceObject.from_dict(user_reports_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


