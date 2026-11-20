# ArtistsTracksMultiRelationshipDataDocument

Target resource types: `tracks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ArtistsTracksResourceIdentifier]**](ArtistsTracksResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artists_tracks_multi_relationship_data_document import ArtistsTracksMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsTracksMultiRelationshipDataDocument from a JSON string
artists_tracks_multi_relationship_data_document_instance = ArtistsTracksMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistsTracksMultiRelationshipDataDocument.to_json())

# convert the object into a dict
artists_tracks_multi_relationship_data_document_dict = artists_tracks_multi_relationship_data_document_instance.to_dict()
# create an instance of ArtistsTracksMultiRelationshipDataDocument from a dict
artists_tracks_multi_relationship_data_document_from_dict = ArtistsTracksMultiRelationshipDataDocument.from_dict(artists_tracks_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


