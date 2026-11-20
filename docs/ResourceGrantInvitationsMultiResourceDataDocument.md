# ResourceGrantInvitationsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceGrantInvitationsResourceObject]**](ResourceGrantInvitationsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.resource_grant_invitations_multi_resource_data_document import ResourceGrantInvitationsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantInvitationsMultiResourceDataDocument from a JSON string
resource_grant_invitations_multi_resource_data_document_instance = ResourceGrantInvitationsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantInvitationsMultiResourceDataDocument.to_json())

# convert the object into a dict
resource_grant_invitations_multi_resource_data_document_dict = resource_grant_invitations_multi_resource_data_document_instance.to_dict()
# create an instance of ResourceGrantInvitationsMultiResourceDataDocument from a dict
resource_grant_invitations_multi_resource_data_document_from_dict = ResourceGrantInvitationsMultiResourceDataDocument.from_dict(resource_grant_invitations_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


