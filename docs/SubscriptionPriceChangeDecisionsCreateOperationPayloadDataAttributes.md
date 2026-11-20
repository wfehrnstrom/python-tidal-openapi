# SubscriptionPriceChangeDecisionsCreateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The decision to record. A decision may only be created once — changing a rejection to an acceptance is a PATCH. | 

## Example

```python
from tidal.models.subscription_price_change_decisions_create_operation_payload_data_attributes import SubscriptionPriceChangeDecisionsCreateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPriceChangeDecisionsCreateOperationPayloadDataAttributes from a JSON string
subscription_price_change_decisions_create_operation_payload_data_attributes_instance = SubscriptionPriceChangeDecisionsCreateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPriceChangeDecisionsCreateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
subscription_price_change_decisions_create_operation_payload_data_attributes_dict = subscription_price_change_decisions_create_operation_payload_data_attributes_instance.to_dict()
# create an instance of SubscriptionPriceChangeDecisionsCreateOperationPayloadDataAttributes from a dict
subscription_price_change_decisions_create_operation_payload_data_attributes_from_dict = SubscriptionPriceChangeDecisionsCreateOperationPayloadDataAttributes.from_dict(subscription_price_change_decisions_create_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


