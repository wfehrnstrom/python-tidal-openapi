# SubscriptionPriceChangeDecisionsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SubscriptionPriceChangeDecisionsAttributes**](SubscriptionPriceChangeDecisionsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**SubscriptionPriceChangeDecisionsRelationships**](SubscriptionPriceChangeDecisionsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.subscription_price_change_decisions_resource_object import SubscriptionPriceChangeDecisionsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPriceChangeDecisionsResourceObject from a JSON string
subscription_price_change_decisions_resource_object_instance = SubscriptionPriceChangeDecisionsResourceObject.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPriceChangeDecisionsResourceObject.to_json())

# convert the object into a dict
subscription_price_change_decisions_resource_object_dict = subscription_price_change_decisions_resource_object_instance.to_dict()
# create an instance of SubscriptionPriceChangeDecisionsResourceObject from a dict
subscription_price_change_decisions_resource_object_from_dict = SubscriptionPriceChangeDecisionsResourceObject.from_dict(subscription_price_change_decisions_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


