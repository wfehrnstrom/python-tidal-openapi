# ManualArtistClaimsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ManualArtistClaimsAttributes**](ManualArtistClaimsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.manual_artist_claims_resource_object import ManualArtistClaimsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ManualArtistClaimsResourceObject from a JSON string
manual_artist_claims_resource_object_instance = ManualArtistClaimsResourceObject.from_json(json)
# print the JSON string representation of the object
print(ManualArtistClaimsResourceObject.to_json())

# convert the object into a dict
manual_artist_claims_resource_object_dict = manual_artist_claims_resource_object_instance.to_dict()
# create an instance of ManualArtistClaimsResourceObject from a dict
manual_artist_claims_resource_object_from_dict = ManualArtistClaimsResourceObject.from_dict(manual_artist_claims_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


