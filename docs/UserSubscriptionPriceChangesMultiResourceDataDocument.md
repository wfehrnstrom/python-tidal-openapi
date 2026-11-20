# UserSubscriptionPriceChangesMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserSubscriptionPriceChangesResourceObject]**](UserSubscriptionPriceChangesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_subscription_price_changes_multi_resource_data_document import UserSubscriptionPriceChangesMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserSubscriptionPriceChangesMultiResourceDataDocument from a JSON string
user_subscription_price_changes_multi_resource_data_document_instance = UserSubscriptionPriceChangesMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserSubscriptionPriceChangesMultiResourceDataDocument.to_json())

# convert the object into a dict
user_subscription_price_changes_multi_resource_data_document_dict = user_subscription_price_changes_multi_resource_data_document_instance.to_dict()
# create an instance of UserSubscriptionPriceChangesMultiResourceDataDocument from a dict
user_subscription_price_changes_multi_resource_data_document_from_dict = UserSubscriptionPriceChangesMultiResourceDataDocument.from_dict(user_subscription_price_changes_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


