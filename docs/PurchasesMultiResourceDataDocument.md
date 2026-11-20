# PurchasesMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PurchasesResourceObject]**](PurchasesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.purchases_multi_resource_data_document import PurchasesMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PurchasesMultiResourceDataDocument from a JSON string
purchases_multi_resource_data_document_instance = PurchasesMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(PurchasesMultiResourceDataDocument.to_json())

# convert the object into a dict
purchases_multi_resource_data_document_dict = purchases_multi_resource_data_document_instance.to_dict()
# create an instance of PurchasesMultiResourceDataDocument from a dict
purchases_multi_resource_data_document_from_dict = PurchasesMultiResourceDataDocument.from_dict(purchases_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


