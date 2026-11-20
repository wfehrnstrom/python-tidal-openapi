# TermsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TermsResourceObject**](TermsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.terms_single_resource_data_document import TermsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TermsSingleResourceDataDocument from a JSON string
terms_single_resource_data_document_instance = TermsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(TermsSingleResourceDataDocument.to_json())

# convert the object into a dict
terms_single_resource_data_document_dict = terms_single_resource_data_document_instance.to_dict()
# create an instance of TermsSingleResourceDataDocument from a dict
terms_single_resource_data_document_from_dict = TermsSingleResourceDataDocument.from_dict(terms_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


