# ResourceGrantInvitationsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceGrantInvitationsResourceObject**](ResourceGrantInvitationsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.resource_grant_invitations_single_resource_data_document import ResourceGrantInvitationsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantInvitationsSingleResourceDataDocument from a JSON string
resource_grant_invitations_single_resource_data_document_instance = ResourceGrantInvitationsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantInvitationsSingleResourceDataDocument.to_json())

# convert the object into a dict
resource_grant_invitations_single_resource_data_document_dict = resource_grant_invitations_single_resource_data_document_instance.to_dict()
# create an instance of ResourceGrantInvitationsSingleResourceDataDocument from a dict
resource_grant_invitations_single_resource_data_document_from_dict = ResourceGrantInvitationsSingleResourceDataDocument.from_dict(resource_grant_invitations_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


