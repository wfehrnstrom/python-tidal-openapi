# UserFeedItemActivityDetails

Details of the activity represented by the group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_type** | **str** | Type of activity represented by the group | 
**release_source** | **str** | How the album was supplied to TIDAL | [optional] 
**match_count** | **int** | Number of copyright matches found for the upload | [optional] 
**frequency** | **str** | Recurrence frequency defined by RFC 5545 | 
**period** | **str** | The calendar period the mix covers: &#x60;YYYY-MM&#x60; for a &#x60;MONTHLY&#x60; mix, &#x60;YYYY&#x60; for a &#x60;YEARLY&#x60; one | 
**new_item_count** | **int** | Number of items added to the playlist | [optional] 
**threshold** | **int** | The total play count the track reached | 

## Example

```python
from tidal.models.user_feed_item_activity_details import UserFeedItemActivityDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedItemActivityDetails from a JSON string
user_feed_item_activity_details_instance = UserFeedItemActivityDetails.from_json(json)
# print the JSON string representation of the object
print(UserFeedItemActivityDetails.to_json())

# convert the object into a dict
user_feed_item_activity_details_dict = user_feed_item_activity_details_instance.to_dict()
# create an instance of UserFeedItemActivityDetails from a dict
user_feed_item_activity_details_from_dict = UserFeedItemActivityDetails.from_dict(user_feed_item_activity_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


