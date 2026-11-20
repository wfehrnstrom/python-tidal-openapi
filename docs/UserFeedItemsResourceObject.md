# UserFeedItemsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UserFeedItemsAttributes**](UserFeedItemsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**UserFeedItemsRelationships**](UserFeedItemsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.user_feed_items_resource_object import UserFeedItemsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedItemsResourceObject from a JSON string
user_feed_items_resource_object_instance = UserFeedItemsResourceObject.from_json(json)
# print the JSON string representation of the object
print(UserFeedItemsResourceObject.to_json())

# convert the object into a dict
user_feed_items_resource_object_dict = user_feed_items_resource_object_instance.to_dict()
# create an instance of UserFeedItemsResourceObject from a dict
user_feed_items_resource_object_from_dict = UserFeedItemsResourceObject.from_dict(user_feed_items_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


