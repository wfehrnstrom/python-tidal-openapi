# ArtistsVideosResourceIdentifierMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replacement** | [**ReplacementProvenance**](ReplacementProvenance.md) |  | [optional] 

## Example

```python
from tidal.models.artists_videos_resource_identifier_meta import ArtistsVideosResourceIdentifierMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsVideosResourceIdentifierMeta from a JSON string
artists_videos_resource_identifier_meta_instance = ArtistsVideosResourceIdentifierMeta.from_json(json)
# print the JSON string representation of the object
print(ArtistsVideosResourceIdentifierMeta.to_json())

# convert the object into a dict
artists_videos_resource_identifier_meta_dict = artists_videos_resource_identifier_meta_instance.to_dict()
# create an instance of ArtistsVideosResourceIdentifierMeta from a dict
artists_videos_resource_identifier_meta_from_dict = ArtistsVideosResourceIdentifierMeta.from_dict(artists_videos_resource_identifier_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


