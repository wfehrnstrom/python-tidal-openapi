# ManualArtistClaimsCreateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted_terms** | **bool** |  | [optional] 
**artist_id** | **str** |  | 
**distributor_name** | **str** |  | [optional] 
**error_reason** | **str** |  | [optional] 
**label_contact_email** | **str** |  | [optional] 
**label_contact_name** | **str** |  | [optional] 
**label_name** | **str** |  | [optional] 
**legal_first_name** | **str** |  | 
**legal_last_name** | **str** |  | 
**manager_email** | **str** |  | [optional] 
**manager_name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**selected_albums** | **List[str]** |  | [optional] 
**selected_singles** | **List[str]** |  | [optional] 
**social_link** | [**ManualArtistClaimsExternalLink**](ManualArtistClaimsExternalLink.md) |  | [optional] 
**upcs** | **List[str]** |  | [optional] 
**website_or_social_link** | [**ManualArtistClaimsExternalLink**](ManualArtistClaimsExternalLink.md) |  | 

## Example

```python
from tidal.models.manual_artist_claims_create_operation_payload_data_attributes import ManualArtistClaimsCreateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ManualArtistClaimsCreateOperationPayloadDataAttributes from a JSON string
manual_artist_claims_create_operation_payload_data_attributes_instance = ManualArtistClaimsCreateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(ManualArtistClaimsCreateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
manual_artist_claims_create_operation_payload_data_attributes_dict = manual_artist_claims_create_operation_payload_data_attributes_instance.to_dict()
# create an instance of ManualArtistClaimsCreateOperationPayloadDataAttributes from a dict
manual_artist_claims_create_operation_payload_data_attributes_from_dict = ManualArtistClaimsCreateOperationPayloadDataAttributes.from_dict(manual_artist_claims_create_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


