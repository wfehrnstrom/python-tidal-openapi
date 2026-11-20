# VideosAlbumsResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**VideosAlbumsResourceIdentifierMeta**](VideosAlbumsResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.videos_albums_resource_identifier import VideosAlbumsResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of VideosAlbumsResourceIdentifier from a JSON string
videos_albums_resource_identifier_instance = VideosAlbumsResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(VideosAlbumsResourceIdentifier.to_json())

# convert the object into a dict
videos_albums_resource_identifier_dict = videos_albums_resource_identifier_instance.to_dict()
# create an instance of VideosAlbumsResourceIdentifier from a dict
videos_albums_resource_identifier_from_dict = VideosAlbumsResourceIdentifier.from_dict(videos_albums_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


