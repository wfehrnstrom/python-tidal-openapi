# ArtistClaimStatusesAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claim_sources** | **List[str]** | Claim sources contributing to the current status. Empty when there is no active claim. | 
**status** | **str** | Whether the artist profile currently has an active claim | 

## Example

```python
from tidal.models.artist_claim_statuses_attributes import ArtistClaimStatusesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistClaimStatusesAttributes from a JSON string
artist_claim_statuses_attributes_instance = ArtistClaimStatusesAttributes.from_json(json)
# print the JSON string representation of the object
print(ArtistClaimStatusesAttributes.to_json())

# convert the object into a dict
artist_claim_statuses_attributes_dict = artist_claim_statuses_attributes_instance.to_dict()
# create an instance of ArtistClaimStatusesAttributes from a dict
artist_claim_statuses_attributes_from_dict = ArtistClaimStatusesAttributes.from_dict(artist_claim_statuses_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


