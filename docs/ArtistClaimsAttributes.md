# ArtistClaimsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artist_id** | **str** | The artist id which is being claimed | 
**external_links** | [**List[ExternalLink]**](ExternalLink.md) | Artist claim links external to TIDAL API | [optional] 
**provider** | **str** | The DSP used for authentication | 
**recommendation** | **str** | The recommended claim resolution | [optional] 
**retrieved_upcs** | [**List[LegacyBarcodeId]**](LegacyBarcodeId.md) | List of UPCs retrieved from the DSP | [optional] 
**status** | **str** | Current status of this claim | 

## Example

```python
from tidal.models.artist_claims_attributes import ArtistClaimsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistClaimsAttributes from a JSON string
artist_claims_attributes_instance = ArtistClaimsAttributes.from_json(json)
# print the JSON string representation of the object
print(ArtistClaimsAttributes.to_json())

# convert the object into a dict
artist_claims_attributes_dict = artist_claims_attributes_instance.to_dict()
# create an instance of ArtistClaimsAttributes from a dict
artist_claims_attributes_from_dict = ArtistClaimsAttributes.from_dict(artist_claims_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


