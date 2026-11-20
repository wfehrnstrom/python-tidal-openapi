# ArtistsAlbumsResourceIdentifierMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replacement** | [**ReplacementProvenance**](ReplacementProvenance.md) |  | [optional] 

## Example

```python
from tidal.models.artists_albums_resource_identifier_meta import ArtistsAlbumsResourceIdentifierMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsAlbumsResourceIdentifierMeta from a JSON string
artists_albums_resource_identifier_meta_instance = ArtistsAlbumsResourceIdentifierMeta.from_json(json)
# print the JSON string representation of the object
print(ArtistsAlbumsResourceIdentifierMeta.to_json())

# convert the object into a dict
artists_albums_resource_identifier_meta_dict = artists_albums_resource_identifier_meta_instance.to_dict()
# create an instance of ArtistsAlbumsResourceIdentifierMeta from a dict
artists_albums_resource_identifier_meta_from_dict = ArtistsAlbumsResourceIdentifierMeta.from_dict(artists_albums_resource_identifier_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


