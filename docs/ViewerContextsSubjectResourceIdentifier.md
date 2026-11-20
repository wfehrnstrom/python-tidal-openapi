# ViewerContextsSubjectResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**ViewerContextsSubjectResourceIdentifierMeta**](ViewerContextsSubjectResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.viewer_contexts_subject_resource_identifier import ViewerContextsSubjectResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ViewerContextsSubjectResourceIdentifier from a JSON string
viewer_contexts_subject_resource_identifier_instance = ViewerContextsSubjectResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(ViewerContextsSubjectResourceIdentifier.to_json())

# convert the object into a dict
viewer_contexts_subject_resource_identifier_dict = viewer_contexts_subject_resource_identifier_instance.to_dict()
# create an instance of ViewerContextsSubjectResourceIdentifier from a dict
viewer_contexts_subject_resource_identifier_from_dict = ViewerContextsSubjectResourceIdentifier.from_dict(viewer_contexts_subject_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


