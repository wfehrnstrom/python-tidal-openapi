# ArtistRolesSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ArtistRolesResourceObject**](ArtistRolesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artist_roles_single_resource_data_document import ArtistRolesSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistRolesSingleResourceDataDocument from a JSON string
artist_roles_single_resource_data_document_instance = ArtistRolesSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistRolesSingleResourceDataDocument.to_json())

# convert the object into a dict
artist_roles_single_resource_data_document_dict = artist_roles_single_resource_data_document_instance.to_dict()
# create an instance of ArtistRolesSingleResourceDataDocument from a dict
artist_roles_single_resource_data_document_from_dict = ArtistRolesSingleResourceDataDocument.from_dict(artist_roles_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


