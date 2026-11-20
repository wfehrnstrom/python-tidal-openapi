# ManualArtistClaimsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ManualArtistClaimsCreateOperationPayloadDataAttributes**](ManualArtistClaimsCreateOperationPayloadDataAttributes.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.manual_artist_claims_create_operation_payload_data import ManualArtistClaimsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of ManualArtistClaimsCreateOperationPayloadData from a JSON string
manual_artist_claims_create_operation_payload_data_instance = ManualArtistClaimsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(ManualArtistClaimsCreateOperationPayloadData.to_json())

# convert the object into a dict
manual_artist_claims_create_operation_payload_data_dict = manual_artist_claims_create_operation_payload_data_instance.to_dict()
# create an instance of ManualArtistClaimsCreateOperationPayloadData from a dict
manual_artist_claims_create_operation_payload_data_from_dict = ManualArtistClaimsCreateOperationPayloadData.from_dict(manual_artist_claims_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


