# ArtistBiographiesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ArtistBiographiesAttributes**](ArtistBiographiesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**ArtistBiographiesRelationships**](ArtistBiographiesRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.artist_biographies_resource_object import ArtistBiographiesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistBiographiesResourceObject from a JSON string
artist_biographies_resource_object_instance = ArtistBiographiesResourceObject.from_json(json)
# print the JSON string representation of the object
print(ArtistBiographiesResourceObject.to_json())

# convert the object into a dict
artist_biographies_resource_object_dict = artist_biographies_resource_object_instance.to_dict()
# create an instance of ArtistBiographiesResourceObject from a dict
artist_biographies_resource_object_from_dict = ArtistBiographiesResourceObject.from_dict(artist_biographies_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


