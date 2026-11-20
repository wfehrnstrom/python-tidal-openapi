# ResourceGrantInvitationsOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.resource_grant_invitations_owners_multi_relationship_data_document import ResourceGrantInvitationsOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantInvitationsOwnersMultiRelationshipDataDocument from a JSON string
resource_grant_invitations_owners_multi_relationship_data_document_instance = ResourceGrantInvitationsOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantInvitationsOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
resource_grant_invitations_owners_multi_relationship_data_document_dict = resource_grant_invitations_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of ResourceGrantInvitationsOwnersMultiRelationshipDataDocument from a dict
resource_grant_invitations_owners_multi_relationship_data_document_from_dict = ResourceGrantInvitationsOwnersMultiRelationshipDataDocument.from_dict(resource_grant_invitations_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


