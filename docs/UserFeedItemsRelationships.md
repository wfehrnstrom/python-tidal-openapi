# UserFeedItemsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actors** | [**UserFeedItemsActorsMultiRelationshipDataDocument**](UserFeedItemsActorsMultiRelationshipDataDocument.md) |  | [optional] 
**subject** | [**UserFeedItemsSubjectSingleRelationshipDataDocument**](UserFeedItemsSubjectSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.user_feed_items_relationships import UserFeedItemsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedItemsRelationships from a JSON string
user_feed_items_relationships_instance = UserFeedItemsRelationships.from_json(json)
# print the JSON string representation of the object
print(UserFeedItemsRelationships.to_json())

# convert the object into a dict
user_feed_items_relationships_dict = user_feed_items_relationships_instance.to_dict()
# create an instance of UserFeedItemsRelationships from a dict
user_feed_items_relationships_from_dict = UserFeedItemsRelationships.from_dict(user_feed_items_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


