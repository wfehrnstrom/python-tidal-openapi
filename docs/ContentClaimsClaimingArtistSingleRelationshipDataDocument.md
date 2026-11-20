# ContentClaimsClaimingArtistSingleRelationshipDataDocument

Target resource types: `artists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.content_claims_claiming_artist_single_relationship_data_document import ContentClaimsClaimingArtistSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ContentClaimsClaimingArtistSingleRelationshipDataDocument from a JSON string
content_claims_claiming_artist_single_relationship_data_document_instance = ContentClaimsClaimingArtistSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ContentClaimsClaimingArtistSingleRelationshipDataDocument.to_json())

# convert the object into a dict
content_claims_claiming_artist_single_relationship_data_document_dict = content_claims_claiming_artist_single_relationship_data_document_instance.to_dict()
# create an instance of ContentClaimsClaimingArtistSingleRelationshipDataDocument from a dict
content_claims_claiming_artist_single_relationship_data_document_from_dict = ContentClaimsClaimingArtistSingleRelationshipDataDocument.from_dict(content_claims_claiming_artist_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


