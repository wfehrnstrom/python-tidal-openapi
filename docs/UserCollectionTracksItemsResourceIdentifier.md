# UserCollectionTracksItemsResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**UserCollectionTracksItemsResourceIdentifierMeta**](UserCollectionTracksItemsResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.user_collection_tracks_items_resource_identifier import UserCollectionTracksItemsResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionTracksItemsResourceIdentifier from a JSON string
user_collection_tracks_items_resource_identifier_instance = UserCollectionTracksItemsResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(UserCollectionTracksItemsResourceIdentifier.to_json())

# convert the object into a dict
user_collection_tracks_items_resource_identifier_dict = user_collection_tracks_items_resource_identifier_instance.to_dict()
# create an instance of UserCollectionTracksItemsResourceIdentifier from a dict
user_collection_tracks_items_resource_identifier_from_dict = UserCollectionTracksItemsResourceIdentifier.from_dict(user_collection_tracks_items_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


