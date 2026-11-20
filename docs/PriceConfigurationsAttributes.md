# PriceConfigurationsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency code (ISO 4217) | 
**price** | **str** | Amount in the currency&#39;s major units | 

## Example

```python
from tidal.models.price_configurations_attributes import PriceConfigurationsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of PriceConfigurationsAttributes from a JSON string
price_configurations_attributes_instance = PriceConfigurationsAttributes.from_json(json)
# print the JSON string representation of the object
print(PriceConfigurationsAttributes.to_json())

# convert the object into a dict
price_configurations_attributes_dict = price_configurations_attributes_instance.to_dict()
# create an instance of PriceConfigurationsAttributes from a dict
price_configurations_attributes_from_dict = PriceConfigurationsAttributes.from_dict(price_configurations_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


