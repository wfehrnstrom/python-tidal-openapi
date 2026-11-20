# ContentClaimsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claimed_resource** | [**ContentClaimsClaimedResourceSingleRelationshipDataDocument**](ContentClaimsClaimedResourceSingleRelationshipDataDocument.md) |  | [optional] 
**claiming_artist** | [**ContentClaimsClaimingArtistSingleRelationshipDataDocument**](ContentClaimsClaimingArtistSingleRelationshipDataDocument.md) |  | [optional] 
**owners** | [**ContentClaimsOwnersMultiRelationshipDataDocument**](ContentClaimsOwnersMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.content_claims_relationships import ContentClaimsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ContentClaimsRelationships from a JSON string
content_claims_relationships_instance = ContentClaimsRelationships.from_json(json)
# print the JSON string representation of the object
print(ContentClaimsRelationships.to_json())

# convert the object into a dict
content_claims_relationships_dict = content_claims_relationships_instance.to_dict()
# create an instance of ContentClaimsRelationships from a dict
content_claims_relationships_from_dict = ContentClaimsRelationships.from_dict(content_claims_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


