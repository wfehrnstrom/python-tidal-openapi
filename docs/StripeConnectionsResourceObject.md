# StripeConnectionsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**StripeConnectionsAttributes**](StripeConnectionsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**StripeConnectionsRelationships**](StripeConnectionsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.stripe_connections_resource_object import StripeConnectionsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of StripeConnectionsResourceObject from a JSON string
stripe_connections_resource_object_instance = StripeConnectionsResourceObject.from_json(json)
# print the JSON string representation of the object
print(StripeConnectionsResourceObject.to_json())

# convert the object into a dict
stripe_connections_resource_object_dict = stripe_connections_resource_object_instance.to_dict()
# create an instance of StripeConnectionsResourceObject from a dict
stripe_connections_resource_object_from_dict = StripeConnectionsResourceObject.from_dict(stripe_connections_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


