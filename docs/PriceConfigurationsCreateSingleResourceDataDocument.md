# PriceConfigurationsCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PriceConfigurationsResourceObject**](PriceConfigurationsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.price_configurations_create_single_resource_data_document import PriceConfigurationsCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PriceConfigurationsCreateSingleResourceDataDocument from a JSON string
price_configurations_create_single_resource_data_document_instance = PriceConfigurationsCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(PriceConfigurationsCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
price_configurations_create_single_resource_data_document_dict = price_configurations_create_single_resource_data_document_instance.to_dict()
# create an instance of PriceConfigurationsCreateSingleResourceDataDocument from a dict
price_configurations_create_single_resource_data_document_from_dict = PriceConfigurationsCreateSingleResourceDataDocument.from_dict(price_configurations_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


