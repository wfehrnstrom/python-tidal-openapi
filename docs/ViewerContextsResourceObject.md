# ViewerContextsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ViewerContextsAttributes**](ViewerContextsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**ViewerContextsRelationships**](ViewerContextsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.viewer_contexts_resource_object import ViewerContextsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ViewerContextsResourceObject from a JSON string
viewer_contexts_resource_object_instance = ViewerContextsResourceObject.from_json(json)
# print the JSON string representation of the object
print(ViewerContextsResourceObject.to_json())

# convert the object into a dict
viewer_contexts_resource_object_dict = viewer_contexts_resource_object_instance.to_dict()
# create an instance of ViewerContextsResourceObject from a dict
viewer_contexts_resource_object_from_dict = ViewerContextsResourceObject.from_dict(viewer_contexts_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


