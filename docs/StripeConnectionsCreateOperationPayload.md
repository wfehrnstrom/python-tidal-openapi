# StripeConnectionsCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**StripeConnectionsCreateOperationPayloadData**](StripeConnectionsCreateOperationPayloadData.md) |  | 
**meta** | [**StripeConnectionsCreateOperationPayloadMeta**](StripeConnectionsCreateOperationPayloadMeta.md) |  | [optional] 

## Example

```python
from tidal.models.stripe_connections_create_operation_payload import StripeConnectionsCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of StripeConnectionsCreateOperationPayload from a JSON string
stripe_connections_create_operation_payload_instance = StripeConnectionsCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(StripeConnectionsCreateOperationPayload.to_json())

# convert the object into a dict
stripe_connections_create_operation_payload_dict = stripe_connections_create_operation_payload_instance.to_dict()
# create an instance of StripeConnectionsCreateOperationPayload from a dict
stripe_connections_create_operation_payload_from_dict = StripeConnectionsCreateOperationPayload.from_dict(stripe_connections_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


