# CollaborationInviteRedemptionsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redeemed_at** | **datetime** | Time of this redemption (ISO 8601). Redeeming the invite again returns the same id with the time of that request. | 

## Example

```python
from tidal.models.collaboration_invite_redemptions_attributes import CollaborationInviteRedemptionsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CollaborationInviteRedemptionsAttributes from a JSON string
collaboration_invite_redemptions_attributes_instance = CollaborationInviteRedemptionsAttributes.from_json(json)
# print the JSON string representation of the object
print(CollaborationInviteRedemptionsAttributes.to_json())

# convert the object into a dict
collaboration_invite_redemptions_attributes_dict = collaboration_invite_redemptions_attributes_instance.to_dict()
# create an instance of CollaborationInviteRedemptionsAttributes from a dict
collaboration_invite_redemptions_attributes_from_dict = CollaborationInviteRedemptionsAttributes.from_dict(collaboration_invite_redemptions_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


