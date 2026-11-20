# CollaborationInvitesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**CollaborationInvitesAttributes**](CollaborationInvitesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**CollaborationInvitesRelationships**](CollaborationInvitesRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.collaboration_invites_resource_object import CollaborationInvitesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of CollaborationInvitesResourceObject from a JSON string
collaboration_invites_resource_object_instance = CollaborationInvitesResourceObject.from_json(json)
# print the JSON string representation of the object
print(CollaborationInvitesResourceObject.to_json())

# convert the object into a dict
collaboration_invites_resource_object_dict = collaboration_invites_resource_object_instance.to_dict()
# create an instance of CollaborationInvitesResourceObject from a dict
collaboration_invites_resource_object_from_dict = CollaborationInvitesResourceObject.from_dict(collaboration_invites_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


