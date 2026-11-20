# AlbumsSuggestedCoverArtsResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**AlbumsSuggestedCoverArtsResourceIdentifierMeta**](AlbumsSuggestedCoverArtsResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.albums_suggested_cover_arts_resource_identifier import AlbumsSuggestedCoverArtsResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsSuggestedCoverArtsResourceIdentifier from a JSON string
albums_suggested_cover_arts_resource_identifier_instance = AlbumsSuggestedCoverArtsResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(AlbumsSuggestedCoverArtsResourceIdentifier.to_json())

# convert the object into a dict
albums_suggested_cover_arts_resource_identifier_dict = albums_suggested_cover_arts_resource_identifier_instance.to_dict()
# create an instance of AlbumsSuggestedCoverArtsResourceIdentifier from a dict
albums_suggested_cover_arts_resource_identifier_from_dict = AlbumsSuggestedCoverArtsResourceIdentifier.from_dict(albums_suggested_cover_arts_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


