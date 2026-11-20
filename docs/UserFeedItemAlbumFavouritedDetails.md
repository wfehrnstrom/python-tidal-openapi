# UserFeedItemAlbumFavouritedDetails

Listeners saved one of your albums. `eventCount` is the number of distinct people who saved it in the item's day; actors are never listed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_type** | **str** | Type of activity represented by the group | 

## Example

```python
from tidal.models.user_feed_item_album_favourited_details import UserFeedItemAlbumFavouritedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedItemAlbumFavouritedDetails from a JSON string
user_feed_item_album_favourited_details_instance = UserFeedItemAlbumFavouritedDetails.from_json(json)
# print the JSON string representation of the object
print(UserFeedItemAlbumFavouritedDetails.to_json())

# convert the object into a dict
user_feed_item_album_favourited_details_dict = user_feed_item_album_favourited_details_instance.to_dict()
# create an instance of UserFeedItemAlbumFavouritedDetails from a dict
user_feed_item_album_favourited_details_from_dict = UserFeedItemAlbumFavouritedDetails.from_dict(user_feed_item_album_favourited_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


