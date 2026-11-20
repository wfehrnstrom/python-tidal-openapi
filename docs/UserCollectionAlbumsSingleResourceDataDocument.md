# UserCollectionAlbumsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserCollectionAlbumsResourceObject**](UserCollectionAlbumsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_collection_albums_single_resource_data_document import UserCollectionAlbumsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionAlbumsSingleResourceDataDocument from a JSON string
user_collection_albums_single_resource_data_document_instance = UserCollectionAlbumsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserCollectionAlbumsSingleResourceDataDocument.to_json())

# convert the object into a dict
user_collection_albums_single_resource_data_document_dict = user_collection_albums_single_resource_data_document_instance.to_dict()
# create an instance of UserCollectionAlbumsSingleResourceDataDocument from a dict
user_collection_albums_single_resource_data_document_from_dict = UserCollectionAlbumsSingleResourceDataDocument.from_dict(user_collection_albums_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


