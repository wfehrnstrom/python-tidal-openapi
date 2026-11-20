# StripeConnectionsCreateOperationPayloadMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_type** | **str** | Integration type for Stripe onboarding | [default to 'REDIRECT']
**refresh_url** | **str** | REDIRECT only: URL to redirect to if seller drops from onboarding | [optional] 
**return_url** | **str** | REDIRECT only: URL to redirect to after completed onboarding | [optional] 

## Example

```python
from tidal.models.stripe_connections_create_operation_payload_meta import StripeConnectionsCreateOperationPayloadMeta

# TODO update the JSON string below
json = "{}"
# create an instance of StripeConnectionsCreateOperationPayloadMeta from a JSON string
stripe_connections_create_operation_payload_meta_instance = StripeConnectionsCreateOperationPayloadMeta.from_json(json)
# print the JSON string representation of the object
print(StripeConnectionsCreateOperationPayloadMeta.to_json())

# convert the object into a dict
stripe_connections_create_operation_payload_meta_dict = stripe_connections_create_operation_payload_meta_instance.to_dict()
# create an instance of StripeConnectionsCreateOperationPayloadMeta from a dict
stripe_connections_create_operation_payload_meta_from_dict = StripeConnectionsCreateOperationPayloadMeta.from_dict(stripe_connections_create_operation_payload_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


