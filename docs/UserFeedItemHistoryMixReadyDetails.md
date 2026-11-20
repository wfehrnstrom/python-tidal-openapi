# UserFeedItemHistoryMixReadyDetails

A new history mix of the viewer's own listening is ready. The `subject` is the mix, as a playlist. `frequency` is how often the mix is generated. `eventCount` is always 1, and actors are never listed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_type** | **str** | Type of activity represented by the group | 
**frequency** | **str** | Recurrence frequency defined by RFC 5545 | 
**period** | **str** | The calendar period the mix covers: &#x60;YYYY-MM&#x60; for a &#x60;MONTHLY&#x60; mix, &#x60;YYYY&#x60; for a &#x60;YEARLY&#x60; one | 

## Example

```python
from tidal.models.user_feed_item_history_mix_ready_details import UserFeedItemHistoryMixReadyDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedItemHistoryMixReadyDetails from a JSON string
user_feed_item_history_mix_ready_details_instance = UserFeedItemHistoryMixReadyDetails.from_json(json)
# print the JSON string representation of the object
print(UserFeedItemHistoryMixReadyDetails.to_json())

# convert the object into a dict
user_feed_item_history_mix_ready_details_dict = user_feed_item_history_mix_ready_details_instance.to_dict()
# create an instance of UserFeedItemHistoryMixReadyDetails from a dict
user_feed_item_history_mix_ready_details_from_dict = UserFeedItemHistoryMixReadyDetails.from_dict(user_feed_item_history_mix_ready_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


