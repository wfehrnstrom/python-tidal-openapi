# UserFeedItemAlbumSharedDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_type** | **str** | Type of activity represented by the group | 

## Example

```python
from tidal.models.user_feed_item_album_shared_details import UserFeedItemAlbumSharedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedItemAlbumSharedDetails from a JSON string
user_feed_item_album_shared_details_instance = UserFeedItemAlbumSharedDetails.from_json(json)
# print the JSON string representation of the object
print(UserFeedItemAlbumSharedDetails.to_json())

# convert the object into a dict
user_feed_item_album_shared_details_dict = user_feed_item_album_shared_details_instance.to_dict()
# create an instance of UserFeedItemAlbumSharedDetails from a dict
user_feed_item_album_shared_details_from_dict = UserFeedItemAlbumSharedDetails.from_dict(user_feed_item_album_shared_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


