# IncludedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ViewerContextsAttributes**](ViewerContextsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**ViewerContextsRelationships**](ViewerContextsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 
**meta** | [**TermsResourceObjectMeta**](TermsResourceObjectMeta.md) |  | [optional] 

## Example

```python
from tidal.models.included_inner import IncludedInner

# TODO update the JSON string below
json = "{}"
# create an instance of IncludedInner from a JSON string
included_inner_instance = IncludedInner.from_json(json)
# print the JSON string representation of the object
print(IncludedInner.to_json())

# convert the object into a dict
included_inner_dict = included_inner_instance.to_dict()
# create an instance of IncludedInner from a dict
included_inner_from_dict = IncludedInner.from_dict(included_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


