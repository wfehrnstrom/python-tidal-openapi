# UserFeedItemTrackFavouritedDetails

Listeners saved one of your tracks. `eventCount` is the number of distinct people who saved it in the item's day; actors are never listed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_type** | **str** | Type of activity represented by the group | 

## Example

```python
from tidal.models.user_feed_item_track_favourited_details import UserFeedItemTrackFavouritedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedItemTrackFavouritedDetails from a JSON string
user_feed_item_track_favourited_details_instance = UserFeedItemTrackFavouritedDetails.from_json(json)
# print the JSON string representation of the object
print(UserFeedItemTrackFavouritedDetails.to_json())

# convert the object into a dict
user_feed_item_track_favourited_details_dict = user_feed_item_track_favourited_details_instance.to_dict()
# create an instance of UserFeedItemTrackFavouritedDetails from a dict
user_feed_item_track_favourited_details_from_dict = UserFeedItemTrackFavouritedDetails.from_dict(user_feed_item_track_favourited_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


