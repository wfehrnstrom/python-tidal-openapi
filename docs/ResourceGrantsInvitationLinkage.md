# ResourceGrantsInvitationLinkage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceGrantsInvitation**](ResourceGrantsInvitation.md) |  | 

## Example

```python
from tidal.models.resource_grants_invitation_linkage import ResourceGrantsInvitationLinkage

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantsInvitationLinkage from a JSON string
resource_grants_invitation_linkage_instance = ResourceGrantsInvitationLinkage.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantsInvitationLinkage.to_json())

# convert the object into a dict
resource_grants_invitation_linkage_dict = resource_grants_invitation_linkage_instance.to_dict()
# create an instance of ResourceGrantsInvitationLinkage from a dict
resource_grants_invitation_linkage_from_dict = ResourceGrantsInvitationLinkage.from_dict(resource_grants_invitation_linkage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


