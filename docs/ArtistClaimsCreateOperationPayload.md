# ArtistClaimsCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ArtistClaimsCreateOperationPayloadData**](ArtistClaimsCreateOperationPayloadData.md) |  | 
**meta** | [**ArtistClaimsCreateOperationPayloadMeta**](ArtistClaimsCreateOperationPayloadMeta.md) |  | 

## Example

```python
from tidal.models.artist_claims_create_operation_payload import ArtistClaimsCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistClaimsCreateOperationPayload from a JSON string
artist_claims_create_operation_payload_instance = ArtistClaimsCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(ArtistClaimsCreateOperationPayload.to_json())

# convert the object into a dict
artist_claims_create_operation_payload_dict = artist_claims_create_operation_payload_instance.to_dict()
# create an instance of ArtistClaimsCreateOperationPayload from a dict
artist_claims_create_operation_payload_from_dict = ArtistClaimsCreateOperationPayload.from_dict(artist_claims_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


