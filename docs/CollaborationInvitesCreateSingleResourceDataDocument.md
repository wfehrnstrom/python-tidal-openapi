# CollaborationInvitesCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CollaborationInvitesResourceObject**](CollaborationInvitesResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.collaboration_invites_create_single_resource_data_document import CollaborationInvitesCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of CollaborationInvitesCreateSingleResourceDataDocument from a JSON string
collaboration_invites_create_single_resource_data_document_instance = CollaborationInvitesCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(CollaborationInvitesCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
collaboration_invites_create_single_resource_data_document_dict = collaboration_invites_create_single_resource_data_document_instance.to_dict()
# create an instance of CollaborationInvitesCreateSingleResourceDataDocument from a dict
collaboration_invites_create_single_resource_data_document_from_dict = CollaborationInvitesCreateSingleResourceDataDocument.from_dict(collaboration_invites_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


