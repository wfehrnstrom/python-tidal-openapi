# ResourceGrantsInvitation

The invitation whose redemption issued the grant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.resource_grants_invitation import ResourceGrantsInvitation

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantsInvitation from a JSON string
resource_grants_invitation_instance = ResourceGrantsInvitation.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantsInvitation.to_json())

# convert the object into a dict
resource_grants_invitation_dict = resource_grants_invitation_instance.to_dict()
# create an instance of ResourceGrantsInvitation from a dict
resource_grants_invitation_from_dict = ResourceGrantsInvitation.from_dict(resource_grants_invitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


