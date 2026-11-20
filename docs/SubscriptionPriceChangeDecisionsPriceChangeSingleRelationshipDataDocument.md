# SubscriptionPriceChangeDecisionsPriceChangeSingleRelationshipDataDocument

Target resource types: `userSubscriptionPriceChanges`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.subscription_price_change_decisions_price_change_single_relationship_data_document import SubscriptionPriceChangeDecisionsPriceChangeSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPriceChangeDecisionsPriceChangeSingleRelationshipDataDocument from a JSON string
subscription_price_change_decisions_price_change_single_relationship_data_document_instance = SubscriptionPriceChangeDecisionsPriceChangeSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPriceChangeDecisionsPriceChangeSingleRelationshipDataDocument.to_json())

# convert the object into a dict
subscription_price_change_decisions_price_change_single_relationship_data_document_dict = subscription_price_change_decisions_price_change_single_relationship_data_document_instance.to_dict()
# create an instance of SubscriptionPriceChangeDecisionsPriceChangeSingleRelationshipDataDocument from a dict
subscription_price_change_decisions_price_change_single_relationship_data_document_from_dict = SubscriptionPriceChangeDecisionsPriceChangeSingleRelationshipDataDocument.from_dict(subscription_price_change_decisions_price_change_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


