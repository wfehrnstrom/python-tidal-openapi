# ResourceGrantInvitationsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ResourceGrantInvitationsAttributes**](ResourceGrantInvitationsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**ResourceGrantInvitationsRelationships**](ResourceGrantInvitationsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.resource_grant_invitations_resource_object import ResourceGrantInvitationsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantInvitationsResourceObject from a JSON string
resource_grant_invitations_resource_object_instance = ResourceGrantInvitationsResourceObject.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantInvitationsResourceObject.to_json())

# convert the object into a dict
resource_grant_invitations_resource_object_dict = resource_grant_invitations_resource_object_instance.to_dict()
# create an instance of ResourceGrantInvitationsResourceObject from a dict
resource_grant_invitations_resource_object_from_dict = ResourceGrantInvitationsResourceObject.from_dict(resource_grant_invitations_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


