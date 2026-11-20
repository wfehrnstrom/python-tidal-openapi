# ResourceGrantsInvitationSingleRelationshipDataDocument

Target resource types: `resourceGrantInvitations`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.resource_grants_invitation_single_relationship_data_document import ResourceGrantsInvitationSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantsInvitationSingleRelationshipDataDocument from a JSON string
resource_grants_invitation_single_relationship_data_document_instance = ResourceGrantsInvitationSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantsInvitationSingleRelationshipDataDocument.to_json())

# convert the object into a dict
resource_grants_invitation_single_relationship_data_document_dict = resource_grants_invitation_single_relationship_data_document_instance.to_dict()
# create an instance of ResourceGrantsInvitationSingleRelationshipDataDocument from a dict
resource_grants_invitation_single_relationship_data_document_from_dict = ResourceGrantsInvitationSingleRelationshipDataDocument.from_dict(resource_grants_invitation_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


