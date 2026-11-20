# ArtistRolesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ArtistRolesAttributes**](ArtistRolesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.artist_roles_resource_object import ArtistRolesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistRolesResourceObject from a JSON string
artist_roles_resource_object_instance = ArtistRolesResourceObject.from_json(json)
# print the JSON string representation of the object
print(ArtistRolesResourceObject.to_json())

# convert the object into a dict
artist_roles_resource_object_dict = artist_roles_resource_object_instance.to_dict()
# create an instance of ArtistRolesResourceObject from a dict
artist_roles_resource_object_from_dict = ArtistRolesResourceObject.from_dict(artist_roles_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


