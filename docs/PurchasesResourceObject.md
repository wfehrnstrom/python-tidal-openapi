# PurchasesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**PurchasesAttributes**](PurchasesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**PurchasesRelationships**](PurchasesRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.purchases_resource_object import PurchasesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of PurchasesResourceObject from a JSON string
purchases_resource_object_instance = PurchasesResourceObject.from_json(json)
# print the JSON string representation of the object
print(PurchasesResourceObject.to_json())

# convert the object into a dict
purchases_resource_object_dict = purchases_resource_object_instance.to_dict()
# create an instance of PurchasesResourceObject from a dict
purchases_resource_object_from_dict = PurchasesResourceObject.from_dict(purchases_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


