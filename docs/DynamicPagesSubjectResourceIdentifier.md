# DynamicPagesSubjectResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**DynamicPagesSubjectResourceIdentifierMeta**](DynamicPagesSubjectResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.dynamic_pages_subject_resource_identifier import DynamicPagesSubjectResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicPagesSubjectResourceIdentifier from a JSON string
dynamic_pages_subject_resource_identifier_instance = DynamicPagesSubjectResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(DynamicPagesSubjectResourceIdentifier.to_json())

# convert the object into a dict
dynamic_pages_subject_resource_identifier_dict = dynamic_pages_subject_resource_identifier_instance.to_dict()
# create an instance of DynamicPagesSubjectResourceIdentifier from a dict
dynamic_pages_subject_resource_identifier_from_dict = DynamicPagesSubjectResourceIdentifier.from_dict(dynamic_pages_subject_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


