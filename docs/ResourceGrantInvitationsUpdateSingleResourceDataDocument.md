# ResourceGrantInvitationsUpdateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceGrantInvitationsResourceObject**](ResourceGrantInvitationsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.resource_grant_invitations_update_single_resource_data_document import ResourceGrantInvitationsUpdateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantInvitationsUpdateSingleResourceDataDocument from a JSON string
resource_grant_invitations_update_single_resource_data_document_instance = ResourceGrantInvitationsUpdateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantInvitationsUpdateSingleResourceDataDocument.to_json())

# convert the object into a dict
resource_grant_invitations_update_single_resource_data_document_dict = resource_grant_invitations_update_single_resource_data_document_instance.to_dict()
# create an instance of ResourceGrantInvitationsUpdateSingleResourceDataDocument from a dict
resource_grant_invitations_update_single_resource_data_document_from_dict = ResourceGrantInvitationsUpdateSingleResourceDataDocument.from_dict(resource_grant_invitations_update_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


