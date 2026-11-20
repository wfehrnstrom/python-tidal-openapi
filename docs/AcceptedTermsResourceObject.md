# AcceptedTermsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**AcceptedTermsAttributes**](AcceptedTermsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**AcceptedTermsRelationships**](AcceptedTermsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.accepted_terms_resource_object import AcceptedTermsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptedTermsResourceObject from a JSON string
accepted_terms_resource_object_instance = AcceptedTermsResourceObject.from_json(json)
# print the JSON string representation of the object
print(AcceptedTermsResourceObject.to_json())

# convert the object into a dict
accepted_terms_resource_object_dict = accepted_terms_resource_object_instance.to_dict()
# create an instance of AcceptedTermsResourceObject from a dict
accepted_terms_resource_object_from_dict = AcceptedTermsResourceObject.from_dict(accepted_terms_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


