# UserFeedItemTrackPlaylistedDetails

One of your tracks was added to user playlists. `eventCount` is the number of distinct playlists it was added to in the item's day, not people; actors are never listed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_type** | **str** | Type of activity represented by the group | 

## Example

```python
from tidal.models.user_feed_item_track_playlisted_details import UserFeedItemTrackPlaylistedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedItemTrackPlaylistedDetails from a JSON string
user_feed_item_track_playlisted_details_instance = UserFeedItemTrackPlaylistedDetails.from_json(json)
# print the JSON string representation of the object
print(UserFeedItemTrackPlaylistedDetails.to_json())

# convert the object into a dict
user_feed_item_track_playlisted_details_dict = user_feed_item_track_playlisted_details_instance.to_dict()
# create an instance of UserFeedItemTrackPlaylistedDetails from a dict
user_feed_item_track_playlisted_details_from_dict = UserFeedItemTrackPlaylistedDetails.from_dict(user_feed_item_track_playlisted_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


