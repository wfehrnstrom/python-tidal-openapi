# UserFeedItemsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_details** | [**UserFeedItemActivityDetails**](UserFeedItemActivityDetails.md) |  | 
**count_is_people** | **bool** | Whether &#x60;eventCount&#x60; also counts distinct people | 
**event_count** | **int** | Number of events represented by the item | 
**first_at** | **datetime** | Time of the first event in the group | 
**last_at** | **datetime** | Time of the latest event in the group | 
**surface** | **str** | The feed surface containing the activity | 
**unread** | **bool** | Whether the item contains unseen activity | 

## Example

```python
from tidal.models.user_feed_items_attributes import UserFeedItemsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedItemsAttributes from a JSON string
user_feed_items_attributes_instance = UserFeedItemsAttributes.from_json(json)
# print the JSON string representation of the object
print(UserFeedItemsAttributes.to_json())

# convert the object into a dict
user_feed_items_attributes_dict = user_feed_items_attributes_instance.to_dict()
# create an instance of UserFeedItemsAttributes from a dict
user_feed_items_attributes_from_dict = UserFeedItemsAttributes.from_dict(user_feed_items_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


