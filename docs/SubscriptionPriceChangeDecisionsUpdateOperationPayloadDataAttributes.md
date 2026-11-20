# SubscriptionPriceChangeDecisionsUpdateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The decision to record. The only allowed transition is REJECTED -&gt; ACCEPTED; acceptance is permanent. | 

## Example

```python
from tidal.models.subscription_price_change_decisions_update_operation_payload_data_attributes import SubscriptionPriceChangeDecisionsUpdateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPriceChangeDecisionsUpdateOperationPayloadDataAttributes from a JSON string
subscription_price_change_decisions_update_operation_payload_data_attributes_instance = SubscriptionPriceChangeDecisionsUpdateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPriceChangeDecisionsUpdateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
subscription_price_change_decisions_update_operation_payload_data_attributes_dict = subscription_price_change_decisions_update_operation_payload_data_attributes_instance.to_dict()
# create an instance of SubscriptionPriceChangeDecisionsUpdateOperationPayloadDataAttributes from a dict
subscription_price_change_decisions_update_operation_payload_data_attributes_from_dict = SubscriptionPriceChangeDecisionsUpdateOperationPayloadDataAttributes.from_dict(subscription_price_change_decisions_update_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


