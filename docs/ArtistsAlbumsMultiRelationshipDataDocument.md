# ArtistsAlbumsMultiRelationshipDataDocument

Target resource types: `albums`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ArtistsAlbumsResourceIdentifier]**](ArtistsAlbumsResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artists_albums_multi_relationship_data_document import ArtistsAlbumsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsAlbumsMultiRelationshipDataDocument from a JSON string
artists_albums_multi_relationship_data_document_instance = ArtistsAlbumsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistsAlbumsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
artists_albums_multi_relationship_data_document_dict = artists_albums_multi_relationship_data_document_instance.to_dict()
# create an instance of ArtistsAlbumsMultiRelationshipDataDocument from a dict
artists_albums_multi_relationship_data_document_from_dict = ArtistsAlbumsMultiRelationshipDataDocument.from_dict(artists_albums_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


