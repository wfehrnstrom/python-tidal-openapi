# ArtistRolesAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the artist role | 

## Example

```python
from tidal.models.artist_roles_attributes import ArtistRolesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistRolesAttributes from a JSON string
artist_roles_attributes_instance = ArtistRolesAttributes.from_json(json)
# print the JSON string representation of the object
print(ArtistRolesAttributes.to_json())

# convert the object into a dict
artist_roles_attributes_dict = artist_roles_attributes_instance.to_dict()
# create an instance of ArtistRolesAttributes from a dict
artist_roles_attributes_from_dict = ArtistRolesAttributes.from_dict(artist_roles_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


