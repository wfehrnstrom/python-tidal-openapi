# ArtistClaimsUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ArtistClaimsUpdateOperationPayloadData**](ArtistClaimsUpdateOperationPayloadData.md) |  | [optional] 
**meta** | [**ArtistClaimsUpdateOperationPayloadMeta**](ArtistClaimsUpdateOperationPayloadMeta.md) |  | 

## Example

```python
from tidal.models.artist_claims_update_operation_payload import ArtistClaimsUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistClaimsUpdateOperationPayload from a JSON string
artist_claims_update_operation_payload_instance = ArtistClaimsUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(ArtistClaimsUpdateOperationPayload.to_json())

# convert the object into a dict
artist_claims_update_operation_payload_dict = artist_claims_update_operation_payload_instance.to_dict()
# create an instance of ArtistClaimsUpdateOperationPayload from a dict
artist_claims_update_operation_payload_from_dict = ArtistClaimsUpdateOperationPayload.from_dict(artist_claims_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


