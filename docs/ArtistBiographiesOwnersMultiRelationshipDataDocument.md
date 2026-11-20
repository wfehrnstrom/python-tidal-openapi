# ArtistBiographiesOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artist_biographies_owners_multi_relationship_data_document import ArtistBiographiesOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistBiographiesOwnersMultiRelationshipDataDocument from a JSON string
artist_biographies_owners_multi_relationship_data_document_instance = ArtistBiographiesOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistBiographiesOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
artist_biographies_owners_multi_relationship_data_document_dict = artist_biographies_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of ArtistBiographiesOwnersMultiRelationshipDataDocument from a dict
artist_biographies_owners_multi_relationship_data_document_from_dict = ArtistBiographiesOwnersMultiRelationshipDataDocument.from_dict(artist_biographies_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


