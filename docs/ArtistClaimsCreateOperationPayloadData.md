# ArtistClaimsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ArtistClaimsCreateOperationPayloadDataAttributes**](ArtistClaimsCreateOperationPayloadDataAttributes.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.artist_claims_create_operation_payload_data import ArtistClaimsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistClaimsCreateOperationPayloadData from a JSON string
artist_claims_create_operation_payload_data_instance = ArtistClaimsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(ArtistClaimsCreateOperationPayloadData.to_json())

# convert the object into a dict
artist_claims_create_operation_payload_data_dict = artist_claims_create_operation_payload_data_instance.to_dict()
# create an instance of ArtistClaimsCreateOperationPayloadData from a dict
artist_claims_create_operation_payload_data_from_dict = ArtistClaimsCreateOperationPayloadData.from_dict(artist_claims_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


