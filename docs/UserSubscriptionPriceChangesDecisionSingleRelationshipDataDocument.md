# UserSubscriptionPriceChangesDecisionSingleRelationshipDataDocument

Target resource types: `subscriptionPriceChangeDecisions`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_subscription_price_changes_decision_single_relationship_data_document import UserSubscriptionPriceChangesDecisionSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserSubscriptionPriceChangesDecisionSingleRelationshipDataDocument from a JSON string
user_subscription_price_changes_decision_single_relationship_data_document_instance = UserSubscriptionPriceChangesDecisionSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserSubscriptionPriceChangesDecisionSingleRelationshipDataDocument.to_json())

# convert the object into a dict
user_subscription_price_changes_decision_single_relationship_data_document_dict = user_subscription_price_changes_decision_single_relationship_data_document_instance.to_dict()
# create an instance of UserSubscriptionPriceChangesDecisionSingleRelationshipDataDocument from a dict
user_subscription_price_changes_decision_single_relationship_data_document_from_dict = UserSubscriptionPriceChangesDecisionSingleRelationshipDataDocument.from_dict(user_subscription_price_changes_decision_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


