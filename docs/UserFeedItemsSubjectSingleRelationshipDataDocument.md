# UserFeedItemsSubjectSingleRelationshipDataDocument

Target resource types: `albums`, `artists`, `comments`, `playlists`, `trackSourceFiles`, `tracks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserFeedItemsSubjectResourceIdentifier**](UserFeedItemsSubjectResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_feed_items_subject_single_relationship_data_document import UserFeedItemsSubjectSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedItemsSubjectSingleRelationshipDataDocument from a JSON string
user_feed_items_subject_single_relationship_data_document_instance = UserFeedItemsSubjectSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserFeedItemsSubjectSingleRelationshipDataDocument.to_json())

# convert the object into a dict
user_feed_items_subject_single_relationship_data_document_dict = user_feed_items_subject_single_relationship_data_document_instance.to_dict()
# create an instance of UserFeedItemsSubjectSingleRelationshipDataDocument from a dict
user_feed_items_subject_single_relationship_data_document_from_dict = UserFeedItemsSubjectSingleRelationshipDataDocument.from_dict(user_feed_items_subject_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


