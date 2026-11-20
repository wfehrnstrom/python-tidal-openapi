# StripeConnectionsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owners** | [**StripeConnectionsOwnersMultiRelationshipDataDocument**](StripeConnectionsOwnersMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.stripe_connections_relationships import StripeConnectionsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of StripeConnectionsRelationships from a JSON string
stripe_connections_relationships_instance = StripeConnectionsRelationships.from_json(json)
# print the JSON string representation of the object
print(StripeConnectionsRelationships.to_json())

# convert the object into a dict
stripe_connections_relationships_dict = stripe_connections_relationships_instance.to_dict()
# create an instance of StripeConnectionsRelationships from a dict
stripe_connections_relationships_from_dict = StripeConnectionsRelationships.from_dict(stripe_connections_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


