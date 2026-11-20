# TermsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**TermsAttributes**](TermsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**meta** | [**TermsResourceObjectMeta**](TermsResourceObjectMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.terms_resource_object import TermsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of TermsResourceObject from a JSON string
terms_resource_object_instance = TermsResourceObject.from_json(json)
# print the JSON string representation of the object
print(TermsResourceObject.to_json())

# convert the object into a dict
terms_resource_object_dict = terms_resource_object_instance.to_dict()
# create an instance of TermsResourceObject from a dict
terms_resource_object_from_dict = TermsResourceObject.from_dict(terms_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


