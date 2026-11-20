# UserFeedItemAlbumReleasedDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_type** | **str** | Type of activity represented by the group | 
**release_source** | **str** | How the album was supplied to TIDAL | [optional] 

## Example

```python
from tidal.models.user_feed_item_album_released_details import UserFeedItemAlbumReleasedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedItemAlbumReleasedDetails from a JSON string
user_feed_item_album_released_details_instance = UserFeedItemAlbumReleasedDetails.from_json(json)
# print the JSON string representation of the object
print(UserFeedItemAlbumReleasedDetails.to_json())

# convert the object into a dict
user_feed_item_album_released_details_dict = user_feed_item_album_released_details_instance.to_dict()
# create an instance of UserFeedItemAlbumReleasedDetails from a dict
user_feed_item_album_released_details_from_dict = UserFeedItemAlbumReleasedDetails.from_dict(user_feed_item_album_released_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


