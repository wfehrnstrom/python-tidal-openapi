# ResourceGrantsCreateOperationPayloadDataRelationships

Either `subject` and `grantee` for a direct grant, or only `invitation` to redeem it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grantee** | [**ResourceGrantsGranteeLinkage**](ResourceGrantsGranteeLinkage.md) |  | [optional] 
**invitation** | [**ResourceGrantsInvitationLinkage**](ResourceGrantsInvitationLinkage.md) |  | [optional] 
**subject** | [**ResourceGrantsSubjectLinkage**](ResourceGrantsSubjectLinkage.md) |  | [optional] 

## Example

```python
from tidal.models.resource_grants_create_operation_payload_data_relationships import ResourceGrantsCreateOperationPayloadDataRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantsCreateOperationPayloadDataRelationships from a JSON string
resource_grants_create_operation_payload_data_relationships_instance = ResourceGrantsCreateOperationPayloadDataRelationships.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantsCreateOperationPayloadDataRelationships.to_json())

# convert the object into a dict
resource_grants_create_operation_payload_data_relationships_dict = resource_grants_create_operation_payload_data_relationships_instance.to_dict()
# create an instance of ResourceGrantsCreateOperationPayloadDataRelationships from a dict
resource_grants_create_operation_payload_data_relationships_from_dict = ResourceGrantsCreateOperationPayloadDataRelationships.from_dict(resource_grants_create_operation_payload_data_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


