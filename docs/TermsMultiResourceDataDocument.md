# TermsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TermsResourceObject]**](TermsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.terms_multi_resource_data_document import TermsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TermsMultiResourceDataDocument from a JSON string
terms_multi_resource_data_document_instance = TermsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(TermsMultiResourceDataDocument.to_json())

# convert the object into a dict
terms_multi_resource_data_document_dict = terms_multi_resource_data_document_instance.to_dict()
# create an instance of TermsMultiResourceDataDocument from a dict
terms_multi_resource_data_document_from_dict = TermsMultiResourceDataDocument.from_dict(terms_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


