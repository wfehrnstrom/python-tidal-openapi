# UserFeedsAttributesFeed

Feed read state

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_unread** | **bool** | Whether the feed contains unread activity | 
**seen_through_token** | **str** | Opaque position through which the surface has been seen. Omitted when unavailable. | [optional] 

## Example

```python
from tidal.models.user_feeds_attributes_feed import UserFeedsAttributesFeed

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedsAttributesFeed from a JSON string
user_feeds_attributes_feed_instance = UserFeedsAttributesFeed.from_json(json)
# print the JSON string representation of the object
print(UserFeedsAttributesFeed.to_json())

# convert the object into a dict
user_feeds_attributes_feed_dict = user_feeds_attributes_feed_instance.to_dict()
# create an instance of UserFeedsAttributesFeed from a dict
user_feeds_attributes_feed_from_dict = UserFeedsAttributesFeed.from_dict(user_feeds_attributes_feed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


