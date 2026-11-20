# TermsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_link** | [**LinkObject**](LinkObject.md) |  | 
**country_code** | **str** |  | 
**effective_at** | **datetime** |  | 
**terms_type** | **str** |  | 

## Example

```python
from tidal.models.terms_attributes import TermsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of TermsAttributes from a JSON string
terms_attributes_instance = TermsAttributes.from_json(json)
# print the JSON string representation of the object
print(TermsAttributes.to_json())

# convert the object into a dict
terms_attributes_dict = terms_attributes_instance.to_dict()
# create an instance of TermsAttributes from a dict
terms_attributes_from_dict = TermsAttributes.from_dict(terms_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


