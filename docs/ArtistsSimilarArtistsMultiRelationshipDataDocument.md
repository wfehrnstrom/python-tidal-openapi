# ArtistsSimilarArtistsMultiRelationshipDataDocument

Target resource types: `artists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artists_similar_artists_multi_relationship_data_document import ArtistsSimilarArtistsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsSimilarArtistsMultiRelationshipDataDocument from a JSON string
artists_similar_artists_multi_relationship_data_document_instance = ArtistsSimilarArtistsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistsSimilarArtistsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
artists_similar_artists_multi_relationship_data_document_dict = artists_similar_artists_multi_relationship_data_document_instance.to_dict()
# create an instance of ArtistsSimilarArtistsMultiRelationshipDataDocument from a dict
artists_similar_artists_multi_relationship_data_document_from_dict = ArtistsSimilarArtistsMultiRelationshipDataDocument.from_dict(artists_similar_artists_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


