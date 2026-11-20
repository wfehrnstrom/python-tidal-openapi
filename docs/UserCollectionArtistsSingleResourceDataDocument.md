# UserCollectionArtistsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserCollectionArtistsResourceObject**](UserCollectionArtistsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_collection_artists_single_resource_data_document import UserCollectionArtistsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionArtistsSingleResourceDataDocument from a JSON string
user_collection_artists_single_resource_data_document_instance = UserCollectionArtistsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserCollectionArtistsSingleResourceDataDocument.to_json())

# convert the object into a dict
user_collection_artists_single_resource_data_document_dict = user_collection_artists_single_resource_data_document_instance.to_dict()
# create an instance of UserCollectionArtistsSingleResourceDataDocument from a dict
user_collection_artists_single_resource_data_document_from_dict = UserCollectionArtistsSingleResourceDataDocument.from_dict(user_collection_artists_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


