# SubscriptionPriceChangeDecisionsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_change** | [**SubscriptionPriceChangeDecisionsPriceChangeSingleRelationshipDataDocument**](SubscriptionPriceChangeDecisionsPriceChangeSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.subscription_price_change_decisions_relationships import SubscriptionPriceChangeDecisionsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPriceChangeDecisionsRelationships from a JSON string
subscription_price_change_decisions_relationships_instance = SubscriptionPriceChangeDecisionsRelationships.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPriceChangeDecisionsRelationships.to_json())

# convert the object into a dict
subscription_price_change_decisions_relationships_dict = subscription_price_change_decisions_relationships_instance.to_dict()
# create an instance of SubscriptionPriceChangeDecisionsRelationships from a dict
subscription_price_change_decisions_relationships_from_dict = SubscriptionPriceChangeDecisionsRelationships.from_dict(subscription_price_change_decisions_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


