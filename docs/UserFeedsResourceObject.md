# UserFeedsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UserFeedsAttributes**](UserFeedsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.user_feeds_resource_object import UserFeedsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedsResourceObject from a JSON string
user_feeds_resource_object_instance = UserFeedsResourceObject.from_json(json)
# print the JSON string representation of the object
print(UserFeedsResourceObject.to_json())

# convert the object into a dict
user_feeds_resource_object_dict = user_feeds_resource_object_instance.to_dict()
# create an instance of UserFeedsResourceObject from a dict
user_feeds_resource_object_from_dict = UserFeedsResourceObject.from_dict(user_feeds_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


