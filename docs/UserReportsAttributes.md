# UserReportsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description | 
**reason** | **str** | Reason | 

## Example

```python
from tidal.models.user_reports_attributes import UserReportsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UserReportsAttributes from a JSON string
user_reports_attributes_instance = UserReportsAttributes.from_json(json)
# print the JSON string representation of the object
print(UserReportsAttributes.to_json())

# convert the object into a dict
user_reports_attributes_dict = user_reports_attributes_instance.to_dict()
# create an instance of UserReportsAttributes from a dict
user_reports_attributes_from_dict = UserReportsAttributes.from_dict(user_reports_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


