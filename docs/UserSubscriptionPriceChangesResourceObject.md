# UserSubscriptionPriceChangesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UserSubscriptionPriceChangesAttributes**](UserSubscriptionPriceChangesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**UserSubscriptionPriceChangesRelationships**](UserSubscriptionPriceChangesRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.user_subscription_price_changes_resource_object import UserSubscriptionPriceChangesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserSubscriptionPriceChangesResourceObject from a JSON string
user_subscription_price_changes_resource_object_instance = UserSubscriptionPriceChangesResourceObject.from_json(json)
# print the JSON string representation of the object
print(UserSubscriptionPriceChangesResourceObject.to_json())

# convert the object into a dict
user_subscription_price_changes_resource_object_dict = user_subscription_price_changes_resource_object_instance.to_dict()
# create an instance of UserSubscriptionPriceChangesResourceObject from a dict
user_subscription_price_changes_resource_object_from_dict = UserSubscriptionPriceChangesResourceObject.from_dict(user_subscription_price_changes_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


