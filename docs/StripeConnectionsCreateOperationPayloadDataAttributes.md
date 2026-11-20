# StripeConnectionsCreateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_type** | **str** | Deprecated: use meta.integrationType instead. | [optional] [default to 'REDIRECT']
**refresh_url** | **str** | Deprecated: use meta.refreshUrl instead. | [optional] 
**return_url** | **str** | Deprecated: use meta.returnUrl instead. | [optional] 

## Example

```python
from tidal.models.stripe_connections_create_operation_payload_data_attributes import StripeConnectionsCreateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of StripeConnectionsCreateOperationPayloadDataAttributes from a JSON string
stripe_connections_create_operation_payload_data_attributes_instance = StripeConnectionsCreateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(StripeConnectionsCreateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
stripe_connections_create_operation_payload_data_attributes_dict = stripe_connections_create_operation_payload_data_attributes_instance.to_dict()
# create an instance of StripeConnectionsCreateOperationPayloadDataAttributes from a dict
stripe_connections_create_operation_payload_data_attributes_from_dict = StripeConnectionsCreateOperationPayloadDataAttributes.from_dict(stripe_connections_create_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


