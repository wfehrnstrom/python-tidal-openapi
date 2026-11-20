# ArtistsVideosResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**ArtistsVideosResourceIdentifierMeta**](ArtistsVideosResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.artists_videos_resource_identifier import ArtistsVideosResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsVideosResourceIdentifier from a JSON string
artists_videos_resource_identifier_instance = ArtistsVideosResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(ArtistsVideosResourceIdentifier.to_json())

# convert the object into a dict
artists_videos_resource_identifier_dict = artists_videos_resource_identifier_instance.to_dict()
# create an instance of ArtistsVideosResourceIdentifier from a dict
artists_videos_resource_identifier_from_dict = ArtistsVideosResourceIdentifier.from_dict(artists_videos_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


