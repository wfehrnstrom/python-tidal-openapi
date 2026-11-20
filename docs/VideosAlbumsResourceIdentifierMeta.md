# VideosAlbumsResourceIdentifierMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replacement** | [**ReplacementProvenance**](ReplacementProvenance.md) |  | [optional] 

## Example

```python
from tidal.models.videos_albums_resource_identifier_meta import VideosAlbumsResourceIdentifierMeta

# TODO update the JSON string below
json = "{}"
# create an instance of VideosAlbumsResourceIdentifierMeta from a JSON string
videos_albums_resource_identifier_meta_instance = VideosAlbumsResourceIdentifierMeta.from_json(json)
# print the JSON string representation of the object
print(VideosAlbumsResourceIdentifierMeta.to_json())

# convert the object into a dict
videos_albums_resource_identifier_meta_dict = videos_albums_resource_identifier_meta_instance.to_dict()
# create an instance of VideosAlbumsResourceIdentifierMeta from a dict
videos_albums_resource_identifier_meta_from_dict = VideosAlbumsResourceIdentifierMeta.from_dict(videos_albums_resource_identifier_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


