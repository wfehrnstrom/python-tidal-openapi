# ArtistClaimsCreateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artist_id** | **str** |  | 
**provider** | **str** |  | 

## Example

```python
from tidal.models.artist_claims_create_operation_payload_data_attributes import ArtistClaimsCreateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistClaimsCreateOperationPayloadDataAttributes from a JSON string
artist_claims_create_operation_payload_data_attributes_instance = ArtistClaimsCreateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(ArtistClaimsCreateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
artist_claims_create_operation_payload_data_attributes_dict = artist_claims_create_operation_payload_data_attributes_instance.to_dict()
# create an instance of ArtistClaimsCreateOperationPayloadDataAttributes from a dict
artist_claims_create_operation_payload_data_attributes_from_dict = ArtistClaimsCreateOperationPayloadDataAttributes.from_dict(artist_claims_create_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


