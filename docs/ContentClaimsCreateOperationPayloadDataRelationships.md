# ContentClaimsCreateOperationPayloadDataRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claimed_resource** | [**ContentClaimsCreateOperationPayloadDataRelationshipsClaimedResource**](ContentClaimsCreateOperationPayloadDataRelationshipsClaimedResource.md) |  | 
**claiming_artist** | [**ContentClaimsCreateOperationPayloadDataRelationshipsClaimingArtist**](ContentClaimsCreateOperationPayloadDataRelationshipsClaimingArtist.md) |  | 

## Example

```python
from tidal.models.content_claims_create_operation_payload_data_relationships import ContentClaimsCreateOperationPayloadDataRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ContentClaimsCreateOperationPayloadDataRelationships from a JSON string
content_claims_create_operation_payload_data_relationships_instance = ContentClaimsCreateOperationPayloadDataRelationships.from_json(json)
# print the JSON string representation of the object
print(ContentClaimsCreateOperationPayloadDataRelationships.to_json())

# convert the object into a dict
content_claims_create_operation_payload_data_relationships_dict = content_claims_create_operation_payload_data_relationships_instance.to_dict()
# create an instance of ContentClaimsCreateOperationPayloadDataRelationships from a dict
content_claims_create_operation_payload_data_relationships_from_dict = ContentClaimsCreateOperationPayloadDataRelationships.from_dict(content_claims_create_operation_payload_data_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


