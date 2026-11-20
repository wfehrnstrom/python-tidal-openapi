# ResourceGrantsSubjectResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**ResourceGrantsSubjectResourceIdentifierMeta**](ResourceGrantsSubjectResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.resource_grants_subject_resource_identifier import ResourceGrantsSubjectResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantsSubjectResourceIdentifier from a JSON string
resource_grants_subject_resource_identifier_instance = ResourceGrantsSubjectResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantsSubjectResourceIdentifier.to_json())

# convert the object into a dict
resource_grants_subject_resource_identifier_dict = resource_grants_subject_resource_identifier_instance.to_dict()
# create an instance of ResourceGrantsSubjectResourceIdentifier from a dict
resource_grants_subject_resource_identifier_from_dict = ResourceGrantsSubjectResourceIdentifier.from_dict(resource_grants_subject_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


