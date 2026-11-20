# SubscriptionPriceChangeDecisionsCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SubscriptionPriceChangeDecisionsResourceObject**](SubscriptionPriceChangeDecisionsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.subscription_price_change_decisions_create_single_resource_data_document import SubscriptionPriceChangeDecisionsCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPriceChangeDecisionsCreateSingleResourceDataDocument from a JSON string
subscription_price_change_decisions_create_single_resource_data_document_instance = SubscriptionPriceChangeDecisionsCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPriceChangeDecisionsCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
subscription_price_change_decisions_create_single_resource_data_document_dict = subscription_price_change_decisions_create_single_resource_data_document_instance.to_dict()
# create an instance of SubscriptionPriceChangeDecisionsCreateSingleResourceDataDocument from a dict
subscription_price_change_decisions_create_single_resource_data_document_from_dict = SubscriptionPriceChangeDecisionsCreateSingleResourceDataDocument.from_dict(subscription_price_change_decisions_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


