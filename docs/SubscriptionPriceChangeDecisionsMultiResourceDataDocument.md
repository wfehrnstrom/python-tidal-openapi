# SubscriptionPriceChangeDecisionsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SubscriptionPriceChangeDecisionsResourceObject]**](SubscriptionPriceChangeDecisionsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.subscription_price_change_decisions_multi_resource_data_document import SubscriptionPriceChangeDecisionsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPriceChangeDecisionsMultiResourceDataDocument from a JSON string
subscription_price_change_decisions_multi_resource_data_document_instance = SubscriptionPriceChangeDecisionsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPriceChangeDecisionsMultiResourceDataDocument.to_json())

# convert the object into a dict
subscription_price_change_decisions_multi_resource_data_document_dict = subscription_price_change_decisions_multi_resource_data_document_instance.to_dict()
# create an instance of SubscriptionPriceChangeDecisionsMultiResourceDataDocument from a dict
subscription_price_change_decisions_multi_resource_data_document_from_dict = SubscriptionPriceChangeDecisionsMultiResourceDataDocument.from_dict(subscription_price_change_decisions_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


