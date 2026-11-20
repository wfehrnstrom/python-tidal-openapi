# ArtistClaimsCreateOperationPayloadMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nonce** | **str** |  | [optional] 
**redirect_url** | **str** |  | 

## Example

```python
from tidal.models.artist_claims_create_operation_payload_meta import ArtistClaimsCreateOperationPayloadMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistClaimsCreateOperationPayloadMeta from a JSON string
artist_claims_create_operation_payload_meta_instance = ArtistClaimsCreateOperationPayloadMeta.from_json(json)
# print the JSON string representation of the object
print(ArtistClaimsCreateOperationPayloadMeta.to_json())

# convert the object into a dict
artist_claims_create_operation_payload_meta_dict = artist_claims_create_operation_payload_meta_instance.to_dict()
# create an instance of ArtistClaimsCreateOperationPayloadMeta from a dict
artist_claims_create_operation_payload_meta_from_dict = ArtistClaimsCreateOperationPayloadMeta.from_dict(artist_claims_create_operation_payload_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


