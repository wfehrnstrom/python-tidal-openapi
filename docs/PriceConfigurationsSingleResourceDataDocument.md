# PriceConfigurationsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PriceConfigurationsResourceObject**](PriceConfigurationsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.price_configurations_single_resource_data_document import PriceConfigurationsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PriceConfigurationsSingleResourceDataDocument from a JSON string
price_configurations_single_resource_data_document_instance = PriceConfigurationsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(PriceConfigurationsSingleResourceDataDocument.to_json())

# convert the object into a dict
price_configurations_single_resource_data_document_dict = price_configurations_single_resource_data_document_instance.to_dict()
# create an instance of PriceConfigurationsSingleResourceDataDocument from a dict
price_configurations_single_resource_data_document_from_dict = PriceConfigurationsSingleResourceDataDocument.from_dict(price_configurations_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


