# PriceConfigurationsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**PriceConfigurationsAttributes**](PriceConfigurationsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.price_configurations_resource_object import PriceConfigurationsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of PriceConfigurationsResourceObject from a JSON string
price_configurations_resource_object_instance = PriceConfigurationsResourceObject.from_json(json)
# print the JSON string representation of the object
print(PriceConfigurationsResourceObject.to_json())

# convert the object into a dict
price_configurations_resource_object_dict = price_configurations_resource_object_instance.to_dict()
# create an instance of PriceConfigurationsResourceObject from a dict
price_configurations_resource_object_from_dict = PriceConfigurationsResourceObject.from_dict(price_configurations_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


