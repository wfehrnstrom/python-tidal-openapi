# CreditsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreditsResourceObject**](CreditsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.credits_single_resource_data_document import CreditsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of CreditsSingleResourceDataDocument from a JSON string
credits_single_resource_data_document_instance = CreditsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(CreditsSingleResourceDataDocument.to_json())

# convert the object into a dict
credits_single_resource_data_document_dict = credits_single_resource_data_document_instance.to_dict()
# create an instance of CreditsSingleResourceDataDocument from a dict
credits_single_resource_data_document_from_dict = CreditsSingleResourceDataDocument.from_dict(credits_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


