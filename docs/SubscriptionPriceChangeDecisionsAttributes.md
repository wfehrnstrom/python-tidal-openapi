# SubscriptionPriceChangeDecisionsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decided_at** | **datetime** | When the user decided. Absent when the consent was implicit (derived from the subscription start). | [optional] 
**status** | **str** | The user&#39;s decision. ACCEPTED is permanent; REJECTED can still be flipped to ACCEPTED before the renewal. | 

## Example

```python
from tidal.models.subscription_price_change_decisions_attributes import SubscriptionPriceChangeDecisionsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPriceChangeDecisionsAttributes from a JSON string
subscription_price_change_decisions_attributes_instance = SubscriptionPriceChangeDecisionsAttributes.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPriceChangeDecisionsAttributes.to_json())

# convert the object into a dict
subscription_price_change_decisions_attributes_dict = subscription_price_change_decisions_attributes_instance.to_dict()
# create an instance of SubscriptionPriceChangeDecisionsAttributes from a dict
subscription_price_change_decisions_attributes_from_dict = SubscriptionPriceChangeDecisionsAttributes.from_dict(subscription_price_change_decisions_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


