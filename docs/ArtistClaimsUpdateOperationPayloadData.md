# ArtistClaimsUpdateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **object** |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from tidal.models.artist_claims_update_operation_payload_data import ArtistClaimsUpdateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistClaimsUpdateOperationPayloadData from a JSON string
artist_claims_update_operation_payload_data_instance = ArtistClaimsUpdateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(ArtistClaimsUpdateOperationPayloadData.to_json())

# convert the object into a dict
artist_claims_update_operation_payload_data_dict = artist_claims_update_operation_payload_data_instance.to_dict()
# create an instance of ArtistClaimsUpdateOperationPayloadData from a dict
artist_claims_update_operation_payload_data_from_dict = ArtistClaimsUpdateOperationPayloadData.from_dict(artist_claims_update_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


