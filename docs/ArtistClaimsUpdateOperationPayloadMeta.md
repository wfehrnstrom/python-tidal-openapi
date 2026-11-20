# ArtistClaimsUpdateOperationPayloadMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_code** | **str** |  | 
**redirect_uri** | **str** |  | 

## Example

```python
from tidal.models.artist_claims_update_operation_payload_meta import ArtistClaimsUpdateOperationPayloadMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistClaimsUpdateOperationPayloadMeta from a JSON string
artist_claims_update_operation_payload_meta_instance = ArtistClaimsUpdateOperationPayloadMeta.from_json(json)
# print the JSON string representation of the object
print(ArtistClaimsUpdateOperationPayloadMeta.to_json())

# convert the object into a dict
artist_claims_update_operation_payload_meta_dict = artist_claims_update_operation_payload_meta_instance.to_dict()
# create an instance of ArtistClaimsUpdateOperationPayloadMeta from a dict
artist_claims_update_operation_payload_meta_from_dict = ArtistClaimsUpdateOperationPayloadMeta.from_dict(artist_claims_update_operation_payload_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


