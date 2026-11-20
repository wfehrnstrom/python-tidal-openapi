# SubscriptionPriceChangeDecisionsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SubscriptionPriceChangeDecisionsCreateOperationPayloadDataAttributes**](SubscriptionPriceChangeDecisionsCreateOperationPayloadDataAttributes.md) |  | 
**relationships** | [**SubscriptionPriceChangeDecisionsCreateOperationPayloadDataRelationships**](SubscriptionPriceChangeDecisionsCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.subscription_price_change_decisions_create_operation_payload_data import SubscriptionPriceChangeDecisionsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPriceChangeDecisionsCreateOperationPayloadData from a JSON string
subscription_price_change_decisions_create_operation_payload_data_instance = SubscriptionPriceChangeDecisionsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPriceChangeDecisionsCreateOperationPayloadData.to_json())

# convert the object into a dict
subscription_price_change_decisions_create_operation_payload_data_dict = subscription_price_change_decisions_create_operation_payload_data_instance.to_dict()
# create an instance of SubscriptionPriceChangeDecisionsCreateOperationPayloadData from a dict
subscription_price_change_decisions_create_operation_payload_data_from_dict = SubscriptionPriceChangeDecisionsCreateOperationPayloadData.from_dict(subscription_price_change_decisions_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


