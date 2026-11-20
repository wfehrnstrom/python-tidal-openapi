# CollaborationInviteRedemptionsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**CollaborationInviteRedemptionsAttributes**](CollaborationInviteRedemptionsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.collaboration_invite_redemptions_resource_object import CollaborationInviteRedemptionsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of CollaborationInviteRedemptionsResourceObject from a JSON string
collaboration_invite_redemptions_resource_object_instance = CollaborationInviteRedemptionsResourceObject.from_json(json)
# print the JSON string representation of the object
print(CollaborationInviteRedemptionsResourceObject.to_json())

# convert the object into a dict
collaboration_invite_redemptions_resource_object_dict = collaboration_invite_redemptions_resource_object_instance.to_dict()
# create an instance of CollaborationInviteRedemptionsResourceObject from a dict
collaboration_invite_redemptions_resource_object_from_dict = CollaborationInviteRedemptionsResourceObject.from_dict(collaboration_invite_redemptions_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


