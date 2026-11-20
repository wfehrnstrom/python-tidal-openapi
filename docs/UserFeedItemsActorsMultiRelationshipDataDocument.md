# UserFeedItemsActorsMultiRelationshipDataDocument

Target resource types: `artists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_feed_items_actors_multi_relationship_data_document import UserFeedItemsActorsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedItemsActorsMultiRelationshipDataDocument from a JSON string
user_feed_items_actors_multi_relationship_data_document_instance = UserFeedItemsActorsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserFeedItemsActorsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
user_feed_items_actors_multi_relationship_data_document_dict = user_feed_items_actors_multi_relationship_data_document_instance.to_dict()
# create an instance of UserFeedItemsActorsMultiRelationshipDataDocument from a dict
user_feed_items_actors_multi_relationship_data_document_from_dict = UserFeedItemsActorsMultiRelationshipDataDocument.from_dict(user_feed_items_actors_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


