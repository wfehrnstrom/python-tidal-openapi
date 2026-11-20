# ArtistClaimsOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artist_claims_owners_multi_relationship_data_document import ArtistClaimsOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistClaimsOwnersMultiRelationshipDataDocument from a JSON string
artist_claims_owners_multi_relationship_data_document_instance = ArtistClaimsOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistClaimsOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
artist_claims_owners_multi_relationship_data_document_dict = artist_claims_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of ArtistClaimsOwnersMultiRelationshipDataDocument from a dict
artist_claims_owners_multi_relationship_data_document_from_dict = ArtistClaimsOwnersMultiRelationshipDataDocument.from_dict(artist_claims_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


