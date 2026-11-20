# UserFeedsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feed** | [**UserFeedsAttributesFeed**](UserFeedsAttributesFeed.md) |  | 
**inbox** | [**UserFeedsAttributesInbox**](UserFeedsAttributesInbox.md) |  | 

## Example

```python
from tidal.models.user_feeds_attributes import UserFeedsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedsAttributes from a JSON string
user_feeds_attributes_instance = UserFeedsAttributes.from_json(json)
# print the JSON string representation of the object
print(UserFeedsAttributes.to_json())

# convert the object into a dict
user_feeds_attributes_dict = user_feeds_attributes_instance.to_dict()
# create an instance of UserFeedsAttributes from a dict
user_feeds_attributes_from_dict = UserFeedsAttributes.from_dict(user_feeds_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


