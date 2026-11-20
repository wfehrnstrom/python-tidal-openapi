# TracksAlbumsResourceIdentifierMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replacement** | [**ReplacementProvenance**](ReplacementProvenance.md) |  | [optional] 

## Example

```python
from tidal.models.tracks_albums_resource_identifier_meta import TracksAlbumsResourceIdentifierMeta

# TODO update the JSON string below
json = "{}"
# create an instance of TracksAlbumsResourceIdentifierMeta from a JSON string
tracks_albums_resource_identifier_meta_instance = TracksAlbumsResourceIdentifierMeta.from_json(json)
# print the JSON string representation of the object
print(TracksAlbumsResourceIdentifierMeta.to_json())

# convert the object into a dict
tracks_albums_resource_identifier_meta_dict = tracks_albums_resource_identifier_meta_instance.to_dict()
# create an instance of TracksAlbumsResourceIdentifierMeta from a dict
tracks_albums_resource_identifier_meta_from_dict = TracksAlbumsResourceIdentifierMeta.from_dict(tracks_albums_resource_identifier_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


