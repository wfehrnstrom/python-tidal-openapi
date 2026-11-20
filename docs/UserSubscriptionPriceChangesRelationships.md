# UserSubscriptionPriceChangesRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decision** | [**UserSubscriptionPriceChangesDecisionSingleRelationshipDataDocument**](UserSubscriptionPriceChangesDecisionSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.user_subscription_price_changes_relationships import UserSubscriptionPriceChangesRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of UserSubscriptionPriceChangesRelationships from a JSON string
user_subscription_price_changes_relationships_instance = UserSubscriptionPriceChangesRelationships.from_json(json)
# print the JSON string representation of the object
print(UserSubscriptionPriceChangesRelationships.to_json())

# convert the object into a dict
user_subscription_price_changes_relationships_dict = user_subscription_price_changes_relationships_instance.to_dict()
# create an instance of UserSubscriptionPriceChangesRelationships from a dict
user_subscription_price_changes_relationships_from_dict = UserSubscriptionPriceChangesRelationships.from_dict(user_subscription_price_changes_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


