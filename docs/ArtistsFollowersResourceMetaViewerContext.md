# ArtistsFollowersResourceMetaViewerContext

Optional context about the relationship

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**follows_my_artist** | **bool** | Boolean to indicate if the artist is following my artist | [optional] [default to False]
**my_artist_follows** | **bool** | Boolean to indicate if my artist is following the artist | [optional] [default to False]

## Example

```python
from tidal.models.artists_followers_resource_meta_viewer_context import ArtistsFollowersResourceMetaViewerContext

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsFollowersResourceMetaViewerContext from a JSON string
artists_followers_resource_meta_viewer_context_instance = ArtistsFollowersResourceMetaViewerContext.from_json(json)
# print the JSON string representation of the object
print(ArtistsFollowersResourceMetaViewerContext.to_json())

# convert the object into a dict
artists_followers_resource_meta_viewer_context_dict = artists_followers_resource_meta_viewer_context_instance.to_dict()
# create an instance of ArtistsFollowersResourceMetaViewerContext from a dict
artists_followers_resource_meta_viewer_context_from_dict = ArtistsFollowersResourceMetaViewerContext.from_dict(artists_followers_resource_meta_viewer_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


