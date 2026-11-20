# SubscriptionPriceChangeDecisionsUpdateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SubscriptionPriceChangeDecisionsUpdateOperationPayloadDataAttributes**](SubscriptionPriceChangeDecisionsUpdateOperationPayloadDataAttributes.md) |  | 
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.subscription_price_change_decisions_update_operation_payload_data import SubscriptionPriceChangeDecisionsUpdateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPriceChangeDecisionsUpdateOperationPayloadData from a JSON string
subscription_price_change_decisions_update_operation_payload_data_instance = SubscriptionPriceChangeDecisionsUpdateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPriceChangeDecisionsUpdateOperationPayloadData.to_json())

# convert the object into a dict
subscription_price_change_decisions_update_operation_payload_data_dict = subscription_price_change_decisions_update_operation_payload_data_instance.to_dict()
# create an instance of SubscriptionPriceChangeDecisionsUpdateOperationPayloadData from a dict
subscription_price_change_decisions_update_operation_payload_data_from_dict = SubscriptionPriceChangeDecisionsUpdateOperationPayloadData.from_dict(subscription_price_change_decisions_update_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


