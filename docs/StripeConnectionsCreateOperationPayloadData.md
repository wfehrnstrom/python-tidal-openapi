# StripeConnectionsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**StripeConnectionsCreateOperationPayloadDataAttributes**](StripeConnectionsCreateOperationPayloadDataAttributes.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from tidal.models.stripe_connections_create_operation_payload_data import StripeConnectionsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of StripeConnectionsCreateOperationPayloadData from a JSON string
stripe_connections_create_operation_payload_data_instance = StripeConnectionsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(StripeConnectionsCreateOperationPayloadData.to_json())

# convert the object into a dict
stripe_connections_create_operation_payload_data_dict = stripe_connections_create_operation_payload_data_instance.to_dict()
# create an instance of StripeConnectionsCreateOperationPayloadData from a dict
stripe_connections_create_operation_payload_data_from_dict = StripeConnectionsCreateOperationPayloadData.from_dict(stripe_connections_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


