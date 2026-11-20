# ManualArtistClaimsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted_terms** | **bool** | Accepted terms and conditions | [optional] 
**artist_id** | **str** | Artist ID being claimed | 
**created_at** | **datetime** | Timestamp when the claim was created | [optional] 
**distributor_name** | **str** | Distributor name | [optional] 
**enrollment_type** | **str** | Enrollment type | [optional] 
**error_reason** | **str** | Error reason if claim failed | [optional] 
**label_contact_email** | **str** | Label contact email | [optional] 
**label_contact_name** | **str** | Label contact name | [optional] 
**label_name** | **str** | Label name | [optional] 
**last_modified_at** | **datetime** | Timestamp when the claim was last modified | [optional] 
**legal_first_name** | **str** | Legal first name | 
**legal_last_name** | **str** | Legal last name | 
**manager_email** | **str** | Manager email | [optional] 
**manager_name** | **str** | Manager name | [optional] 
**role** | **str** | Role | [optional] 
**selected_albums** | **List[str]** | Album IDs selected by user | [optional] 
**selected_singles** | **List[str]** | Single IDs selected by user | [optional] 
**social_link** | [**LinkObject**](LinkObject.md) |  | [optional] 
**status** | **str** | Claim status | [optional] 
**upcs** | **List[str]** | UPCs associated with the claim | [optional] 
**website_or_social_link** | [**LinkObject**](LinkObject.md) |  | 

## Example

```python
from tidal.models.manual_artist_claims_attributes import ManualArtistClaimsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ManualArtistClaimsAttributes from a JSON string
manual_artist_claims_attributes_instance = ManualArtistClaimsAttributes.from_json(json)
# print the JSON string representation of the object
print(ManualArtistClaimsAttributes.to_json())

# convert the object into a dict
manual_artist_claims_attributes_dict = manual_artist_claims_attributes_instance.to_dict()
# create an instance of ManualArtistClaimsAttributes from a dict
manual_artist_claims_attributes_from_dict = ManualArtistClaimsAttributes.from_dict(manual_artist_claims_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


