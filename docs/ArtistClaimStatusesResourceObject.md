# ArtistClaimStatusesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ArtistClaimStatusesAttributes**](ArtistClaimStatusesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.artist_claim_statuses_resource_object import ArtistClaimStatusesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistClaimStatusesResourceObject from a JSON string
artist_claim_statuses_resource_object_instance = ArtistClaimStatusesResourceObject.from_json(json)
# print the JSON string representation of the object
print(ArtistClaimStatusesResourceObject.to_json())

# convert the object into a dict
artist_claim_statuses_resource_object_dict = artist_claim_statuses_resource_object_instance.to_dict()
# create an instance of ArtistClaimStatusesResourceObject from a dict
artist_claim_statuses_resource_object_from_dict = ArtistClaimStatusesResourceObject.from_dict(artist_claim_statuses_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


