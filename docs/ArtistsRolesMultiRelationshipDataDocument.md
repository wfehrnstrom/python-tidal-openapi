# ArtistsRolesMultiRelationshipDataDocument

Target resource types: `artistRoles`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artists_roles_multi_relationship_data_document import ArtistsRolesMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsRolesMultiRelationshipDataDocument from a JSON string
artists_roles_multi_relationship_data_document_instance = ArtistsRolesMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistsRolesMultiRelationshipDataDocument.to_json())

# convert the object into a dict
artists_roles_multi_relationship_data_document_dict = artists_roles_multi_relationship_data_document_instance.to_dict()
# create an instance of ArtistsRolesMultiRelationshipDataDocument from a dict
artists_roles_multi_relationship_data_document_from_dict = ArtistsRolesMultiRelationshipDataDocument.from_dict(artists_roles_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


