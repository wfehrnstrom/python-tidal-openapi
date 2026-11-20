# ArtistsClaimStatusSingleRelationshipDataDocument

Target resource types: `artistClaimStatuses`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artists_claim_status_single_relationship_data_document import ArtistsClaimStatusSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsClaimStatusSingleRelationshipDataDocument from a JSON string
artists_claim_status_single_relationship_data_document_instance = ArtistsClaimStatusSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistsClaimStatusSingleRelationshipDataDocument.to_json())

# convert the object into a dict
artists_claim_status_single_relationship_data_document_dict = artists_claim_status_single_relationship_data_document_instance.to_dict()
# create an instance of ArtistsClaimStatusSingleRelationshipDataDocument from a dict
artists_claim_status_single_relationship_data_document_from_dict = ArtistsClaimStatusSingleRelationshipDataDocument.from_dict(artists_claim_status_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


