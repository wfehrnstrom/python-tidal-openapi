# CollaborationInvitesMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CollaborationInvitesResourceObject]**](CollaborationInvitesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.collaboration_invites_multi_resource_data_document import CollaborationInvitesMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of CollaborationInvitesMultiResourceDataDocument from a JSON string
collaboration_invites_multi_resource_data_document_instance = CollaborationInvitesMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(CollaborationInvitesMultiResourceDataDocument.to_json())

# convert the object into a dict
collaboration_invites_multi_resource_data_document_dict = collaboration_invites_multi_resource_data_document_instance.to_dict()
# create an instance of CollaborationInvitesMultiResourceDataDocument from a dict
collaboration_invites_multi_resource_data_document_from_dict = CollaborationInvitesMultiResourceDataDocument.from_dict(collaboration_invites_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


