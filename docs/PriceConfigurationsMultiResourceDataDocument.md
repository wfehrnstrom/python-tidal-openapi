# PriceConfigurationsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PriceConfigurationsResourceObject]**](PriceConfigurationsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.price_configurations_multi_resource_data_document import PriceConfigurationsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PriceConfigurationsMultiResourceDataDocument from a JSON string
price_configurations_multi_resource_data_document_instance = PriceConfigurationsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(PriceConfigurationsMultiResourceDataDocument.to_json())

# convert the object into a dict
price_configurations_multi_resource_data_document_dict = price_configurations_multi_resource_data_document_instance.to_dict()
# create an instance of PriceConfigurationsMultiResourceDataDocument from a dict
price_configurations_multi_resource_data_document_from_dict = PriceConfigurationsMultiResourceDataDocument.from_dict(price_configurations_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


