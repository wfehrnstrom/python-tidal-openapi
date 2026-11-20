# ResourceGrantsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grantee** | [**ResourceGrantsGranteeSingleRelationshipDataDocument**](ResourceGrantsGranteeSingleRelationshipDataDocument.md) |  | [optional] 
**invitation** | [**ResourceGrantsInvitationSingleRelationshipDataDocument**](ResourceGrantsInvitationSingleRelationshipDataDocument.md) |  | [optional] 
**subject** | [**ResourceGrantsSubjectSingleRelationshipDataDocument**](ResourceGrantsSubjectSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.resource_grants_relationships import ResourceGrantsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantsRelationships from a JSON string
resource_grants_relationships_instance = ResourceGrantsRelationships.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantsRelationships.to_json())

# convert the object into a dict
resource_grants_relationships_dict = resource_grants_relationships_instance.to_dict()
# create an instance of ResourceGrantsRelationships from a dict
resource_grants_relationships_from_dict = ResourceGrantsRelationships.from_dict(resource_grants_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


