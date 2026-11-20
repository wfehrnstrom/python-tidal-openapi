# CollaborationInvitesSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CollaborationInvitesResourceObject**](CollaborationInvitesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.collaboration_invites_single_resource_data_document import CollaborationInvitesSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of CollaborationInvitesSingleResourceDataDocument from a JSON string
collaboration_invites_single_resource_data_document_instance = CollaborationInvitesSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(CollaborationInvitesSingleResourceDataDocument.to_json())

# convert the object into a dict
collaboration_invites_single_resource_data_document_dict = collaboration_invites_single_resource_data_document_instance.to_dict()
# create an instance of CollaborationInvitesSingleResourceDataDocument from a dict
collaboration_invites_single_resource_data_document_from_dict = CollaborationInvitesSingleResourceDataDocument.from_dict(collaboration_invites_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


