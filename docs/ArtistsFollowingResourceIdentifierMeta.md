# ArtistsFollowingResourceIdentifierMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**viewer** | [**ArtistsFollowersResourceMetaViewerContext**](ArtistsFollowersResourceMetaViewerContext.md) |  | [optional] 

## Example

```python
from tidal.models.artists_following_resource_identifier_meta import ArtistsFollowingResourceIdentifierMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsFollowingResourceIdentifierMeta from a JSON string
artists_following_resource_identifier_meta_instance = ArtistsFollowingResourceIdentifierMeta.from_json(json)
# print the JSON string representation of the object
print(ArtistsFollowingResourceIdentifierMeta.to_json())

# convert the object into a dict
artists_following_resource_identifier_meta_dict = artists_following_resource_identifier_meta_instance.to_dict()
# create an instance of ArtistsFollowingResourceIdentifierMeta from a dict
artists_following_resource_identifier_meta_from_dict = ArtistsFollowingResourceIdentifierMeta.from_dict(artists_following_resource_identifier_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


