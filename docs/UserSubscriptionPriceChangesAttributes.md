# UserSubscriptionPriceChangesAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | ISO 4217 currency code | 
**current_price** | **str** | Amount in the currency&#39;s major units | 
**effective_date** | **date** | The date the new price takes effect | 
**new_price** | **str** | Amount in the currency&#39;s major units | 

## Example

```python
from tidal.models.user_subscription_price_changes_attributes import UserSubscriptionPriceChangesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UserSubscriptionPriceChangesAttributes from a JSON string
user_subscription_price_changes_attributes_instance = UserSubscriptionPriceChangesAttributes.from_json(json)
# print the JSON string representation of the object
print(UserSubscriptionPriceChangesAttributes.to_json())

# convert the object into a dict
user_subscription_price_changes_attributes_dict = user_subscription_price_changes_attributes_instance.to_dict()
# create an instance of UserSubscriptionPriceChangesAttributes from a dict
user_subscription_price_changes_attributes_from_dict = UserSubscriptionPriceChangesAttributes.from_dict(user_subscription_price_changes_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


