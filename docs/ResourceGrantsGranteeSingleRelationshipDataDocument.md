# ResourceGrantsGranteeSingleRelationshipDataDocument

Target resource types: `groups`, `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.resource_grants_grantee_single_relationship_data_document import ResourceGrantsGranteeSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantsGranteeSingleRelationshipDataDocument from a JSON string
resource_grants_grantee_single_relationship_data_document_instance = ResourceGrantsGranteeSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantsGranteeSingleRelationshipDataDocument.to_json())

# convert the object into a dict
resource_grants_grantee_single_relationship_data_document_dict = resource_grants_grantee_single_relationship_data_document_instance.to_dict()
# create an instance of ResourceGrantsGranteeSingleRelationshipDataDocument from a dict
resource_grants_grantee_single_relationship_data_document_from_dict = ResourceGrantsGranteeSingleRelationshipDataDocument.from_dict(resource_grants_grantee_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


