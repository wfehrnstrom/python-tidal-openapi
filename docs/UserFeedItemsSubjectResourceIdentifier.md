# UserFeedItemsSubjectResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**UserFeedItemsSubjectResourceIdentifierMeta**](UserFeedItemsSubjectResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.user_feed_items_subject_resource_identifier import UserFeedItemsSubjectResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedItemsSubjectResourceIdentifier from a JSON string
user_feed_items_subject_resource_identifier_instance = UserFeedItemsSubjectResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(UserFeedItemsSubjectResourceIdentifier.to_json())

# convert the object into a dict
user_feed_items_subject_resource_identifier_dict = user_feed_items_subject_resource_identifier_instance.to_dict()
# create an instance of UserFeedItemsSubjectResourceIdentifier from a dict
user_feed_items_subject_resource_identifier_from_dict = UserFeedItemsSubjectResourceIdentifier.from_dict(user_feed_items_subject_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


