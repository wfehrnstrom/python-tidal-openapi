# UserFeedItemTrackPlayMilestoneDetails

One of your uploaded tracks reached a total play count. The `subject` is the track. `eventCount` is always 1, and actors are never listed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_type** | **str** | Type of activity represented by the group | 
**threshold** | **int** | The total play count the track reached | 

## Example

```python
from tidal.models.user_feed_item_track_play_milestone_details import UserFeedItemTrackPlayMilestoneDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedItemTrackPlayMilestoneDetails from a JSON string
user_feed_item_track_play_milestone_details_instance = UserFeedItemTrackPlayMilestoneDetails.from_json(json)
# print the JSON string representation of the object
print(UserFeedItemTrackPlayMilestoneDetails.to_json())

# convert the object into a dict
user_feed_item_track_play_milestone_details_dict = user_feed_item_track_play_milestone_details_instance.to_dict()
# create an instance of UserFeedItemTrackPlayMilestoneDetails from a dict
user_feed_item_track_play_milestone_details_from_dict = UserFeedItemTrackPlayMilestoneDetails.from_dict(user_feed_item_track_play_milestone_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


