# ArtistClaimsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ArtistClaimsAttributes**](ArtistClaimsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**ArtistClaimsRelationships**](ArtistClaimsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.artist_claims_resource_object import ArtistClaimsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistClaimsResourceObject from a JSON string
artist_claims_resource_object_instance = ArtistClaimsResourceObject.from_json(json)
# print the JSON string representation of the object
print(ArtistClaimsResourceObject.to_json())

# convert the object into a dict
artist_claims_resource_object_dict = artist_claims_resource_object_instance.to_dict()
# create an instance of ArtistClaimsResourceObject from a dict
artist_claims_resource_object_from_dict = ArtistClaimsResourceObject.from_dict(artist_claims_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


