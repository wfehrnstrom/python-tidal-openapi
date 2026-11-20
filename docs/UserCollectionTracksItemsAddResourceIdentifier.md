# UserCollectionTracksItemsAddResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**meta** | [**UserCollectionTracksItemsAddResourceIdentifierMeta**](UserCollectionTracksItemsAddResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from tidal.models.user_collection_tracks_items_add_resource_identifier import UserCollectionTracksItemsAddResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionTracksItemsAddResourceIdentifier from a JSON string
user_collection_tracks_items_add_resource_identifier_instance = UserCollectionTracksItemsAddResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(UserCollectionTracksItemsAddResourceIdentifier.to_json())

# convert the object into a dict
user_collection_tracks_items_add_resource_identifier_dict = user_collection_tracks_items_add_resource_identifier_instance.to_dict()
# create an instance of UserCollectionTracksItemsAddResourceIdentifier from a dict
user_collection_tracks_items_add_resource_identifier_from_dict = UserCollectionTracksItemsAddResourceIdentifier.from_dict(user_collection_tracks_items_add_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


