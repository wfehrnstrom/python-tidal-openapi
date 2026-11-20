# SubscriptionPriceChangeDecisionsUpdateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SubscriptionPriceChangeDecisionsResourceObject**](SubscriptionPriceChangeDecisionsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.subscription_price_change_decisions_update_single_resource_data_document import SubscriptionPriceChangeDecisionsUpdateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPriceChangeDecisionsUpdateSingleResourceDataDocument from a JSON string
subscription_price_change_decisions_update_single_resource_data_document_instance = SubscriptionPriceChangeDecisionsUpdateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPriceChangeDecisionsUpdateSingleResourceDataDocument.to_json())

# convert the object into a dict
subscription_price_change_decisions_update_single_resource_data_document_dict = subscription_price_change_decisions_update_single_resource_data_document_instance.to_dict()
# create an instance of SubscriptionPriceChangeDecisionsUpdateSingleResourceDataDocument from a dict
subscription_price_change_decisions_update_single_resource_data_document_from_dict = SubscriptionPriceChangeDecisionsUpdateSingleResourceDataDocument.from_dict(subscription_price_change_decisions_update_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


