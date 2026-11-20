# ArtistsAlbumsResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**ArtistsAlbumsResourceIdentifierMeta**](ArtistsAlbumsResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.artists_albums_resource_identifier import ArtistsAlbumsResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsAlbumsResourceIdentifier from a JSON string
artists_albums_resource_identifier_instance = ArtistsAlbumsResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(ArtistsAlbumsResourceIdentifier.to_json())

# convert the object into a dict
artists_albums_resource_identifier_dict = artists_albums_resource_identifier_instance.to_dict()
# create an instance of ArtistsAlbumsResourceIdentifier from a dict
artists_albums_resource_identifier_from_dict = ArtistsAlbumsResourceIdentifier.from_dict(artists_albums_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


