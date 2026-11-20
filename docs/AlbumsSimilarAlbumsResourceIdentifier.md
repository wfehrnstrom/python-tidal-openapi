# AlbumsSimilarAlbumsResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**AlbumsSimilarAlbumsResourceIdentifierMeta**](AlbumsSimilarAlbumsResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.albums_similar_albums_resource_identifier import AlbumsSimilarAlbumsResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsSimilarAlbumsResourceIdentifier from a JSON string
albums_similar_albums_resource_identifier_instance = AlbumsSimilarAlbumsResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(AlbumsSimilarAlbumsResourceIdentifier.to_json())

# convert the object into a dict
albums_similar_albums_resource_identifier_dict = albums_similar_albums_resource_identifier_instance.to_dict()
# create an instance of AlbumsSimilarAlbumsResourceIdentifier from a dict
albums_similar_albums_resource_identifier_from_dict = AlbumsSimilarAlbumsResourceIdentifier.from_dict(albums_similar_albums_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


