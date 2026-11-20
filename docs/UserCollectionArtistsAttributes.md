# UserCollectionArtistsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_modified_at** | **datetime** | When the collection was last modified | [optional] 
**number_of_items** | **int** | Number of items in the collection | 

## Example

```python
from tidal.models.user_collection_artists_attributes import UserCollectionArtistsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionArtistsAttributes from a JSON string
user_collection_artists_attributes_instance = UserCollectionArtistsAttributes.from_json(json)
# print the JSON string representation of the object
print(UserCollectionArtistsAttributes.to_json())

# convert the object into a dict
user_collection_artists_attributes_dict = user_collection_artists_attributes_instance.to_dict()
# create an instance of UserCollectionArtistsAttributes from a dict
user_collection_artists_attributes_from_dict = UserCollectionArtistsAttributes.from_dict(user_collection_artists_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


