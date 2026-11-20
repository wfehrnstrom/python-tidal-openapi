# ResourceGrantInvitationsSubjectResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**ResourceGrantInvitationsSubjectResourceIdentifierMeta**](ResourceGrantInvitationsSubjectResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.resource_grant_invitations_subject_resource_identifier import ResourceGrantInvitationsSubjectResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantInvitationsSubjectResourceIdentifier from a JSON string
resource_grant_invitations_subject_resource_identifier_instance = ResourceGrantInvitationsSubjectResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantInvitationsSubjectResourceIdentifier.to_json())

# convert the object into a dict
resource_grant_invitations_subject_resource_identifier_dict = resource_grant_invitations_subject_resource_identifier_instance.to_dict()
# create an instance of ResourceGrantInvitationsSubjectResourceIdentifier from a dict
resource_grant_invitations_subject_resource_identifier_from_dict = ResourceGrantInvitationsSubjectResourceIdentifier.from_dict(resource_grant_invitations_subject_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


