# TracksAlbumsResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**TracksAlbumsResourceIdentifierMeta**](TracksAlbumsResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.tracks_albums_resource_identifier import TracksAlbumsResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of TracksAlbumsResourceIdentifier from a JSON string
tracks_albums_resource_identifier_instance = TracksAlbumsResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(TracksAlbumsResourceIdentifier.to_json())

# convert the object into a dict
tracks_albums_resource_identifier_dict = tracks_albums_resource_identifier_instance.to_dict()
# create an instance of TracksAlbumsResourceIdentifier from a dict
tracks_albums_resource_identifier_from_dict = TracksAlbumsResourceIdentifier.from_dict(tracks_albums_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


