# ResourceGrantInvitationsPreviewGrantSingleRelationshipDataDocument

Target resource types: `resourceGrants`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.resource_grant_invitations_preview_grant_single_relationship_data_document import ResourceGrantInvitationsPreviewGrantSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantInvitationsPreviewGrantSingleRelationshipDataDocument from a JSON string
resource_grant_invitations_preview_grant_single_relationship_data_document_instance = ResourceGrantInvitationsPreviewGrantSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantInvitationsPreviewGrantSingleRelationshipDataDocument.to_json())

# convert the object into a dict
resource_grant_invitations_preview_grant_single_relationship_data_document_dict = resource_grant_invitations_preview_grant_single_relationship_data_document_instance.to_dict()
# create an instance of ResourceGrantInvitationsPreviewGrantSingleRelationshipDataDocument from a dict
resource_grant_invitations_preview_grant_single_relationship_data_document_from_dict = ResourceGrantInvitationsPreviewGrantSingleRelationshipDataDocument.from_dict(resource_grant_invitations_preview_grant_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


