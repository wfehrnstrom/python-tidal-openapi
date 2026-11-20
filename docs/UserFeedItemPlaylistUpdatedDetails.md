# UserFeedItemPlaylistUpdatedDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_type** | **str** | Type of activity represented by the group | 
**new_item_count** | **int** | Number of items added to the playlist | [optional] 

## Example

```python
from tidal.models.user_feed_item_playlist_updated_details import UserFeedItemPlaylistUpdatedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedItemPlaylistUpdatedDetails from a JSON string
user_feed_item_playlist_updated_details_instance = UserFeedItemPlaylistUpdatedDetails.from_json(json)
# print the JSON string representation of the object
print(UserFeedItemPlaylistUpdatedDetails.to_json())

# convert the object into a dict
user_feed_item_playlist_updated_details_dict = user_feed_item_playlist_updated_details_instance.to_dict()
# create an instance of UserFeedItemPlaylistUpdatedDetails from a dict
user_feed_item_playlist_updated_details_from_dict = UserFeedItemPlaylistUpdatedDetails.from_dict(user_feed_item_playlist_updated_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


