# AcceptedTermsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AcceptedTermsResourceObject]**](AcceptedTermsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.accepted_terms_multi_resource_data_document import AcceptedTermsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptedTermsMultiResourceDataDocument from a JSON string
accepted_terms_multi_resource_data_document_instance = AcceptedTermsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(AcceptedTermsMultiResourceDataDocument.to_json())

# convert the object into a dict
accepted_terms_multi_resource_data_document_dict = accepted_terms_multi_resource_data_document_instance.to_dict()
# create an instance of AcceptedTermsMultiResourceDataDocument from a dict
accepted_terms_multi_resource_data_document_from_dict = AcceptedTermsMultiResourceDataDocument.from_dict(accepted_terms_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


