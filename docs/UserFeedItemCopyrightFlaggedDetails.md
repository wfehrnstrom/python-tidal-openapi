# UserFeedItemCopyrightFlaggedDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_type** | **str** | Type of activity represented by the group | 
**match_count** | **int** | Number of copyright matches found for the upload | [optional] 

## Example

```python
from tidal.models.user_feed_item_copyright_flagged_details import UserFeedItemCopyrightFlaggedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedItemCopyrightFlaggedDetails from a JSON string
user_feed_item_copyright_flagged_details_instance = UserFeedItemCopyrightFlaggedDetails.from_json(json)
# print the JSON string representation of the object
print(UserFeedItemCopyrightFlaggedDetails.to_json())

# convert the object into a dict
user_feed_item_copyright_flagged_details_dict = user_feed_item_copyright_flagged_details_instance.to_dict()
# create an instance of UserFeedItemCopyrightFlaggedDetails from a dict
user_feed_item_copyright_flagged_details_from_dict = UserFeedItemCopyrightFlaggedDetails.from_dict(user_feed_item_copyright_flagged_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


