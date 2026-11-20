# StripeConnectionsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Timestamp when the connection was created | [optional] 
**external_links** | [**List[ExternalLink]**](ExternalLink.md) | External links for Stripe connection | [optional] 
**last_modified_at** | **datetime** | Timestamp when the connection was last modified | [optional] 
**status** | **str** | Current status of this Stripe connection | 

## Example

```python
from tidal.models.stripe_connections_attributes import StripeConnectionsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of StripeConnectionsAttributes from a JSON string
stripe_connections_attributes_instance = StripeConnectionsAttributes.from_json(json)
# print the JSON string representation of the object
print(StripeConnectionsAttributes.to_json())

# convert the object into a dict
stripe_connections_attributes_dict = stripe_connections_attributes_instance.to_dict()
# create an instance of StripeConnectionsAttributes from a dict
stripe_connections_attributes_from_dict = StripeConnectionsAttributes.from_dict(stripe_connections_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


