# UserFeedsAttributesInbox

Inbox read state

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seen_through_token** | **str** | Opaque position through which the surface has been seen. Omitted when unavailable. | [optional] 
**unread_count** | **int** | Number of unread inbox items | 

## Example

```python
from tidal.models.user_feeds_attributes_inbox import UserFeedsAttributesInbox

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedsAttributesInbox from a JSON string
user_feeds_attributes_inbox_instance = UserFeedsAttributesInbox.from_json(json)
# print the JSON string representation of the object
print(UserFeedsAttributesInbox.to_json())

# convert the object into a dict
user_feeds_attributes_inbox_dict = user_feeds_attributes_inbox_instance.to_dict()
# create an instance of UserFeedsAttributesInbox from a dict
user_feeds_attributes_inbox_from_dict = UserFeedsAttributesInbox.from_dict(user_feeds_attributes_inbox_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


