# SquareConnectionsCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SquareConnectionsCreateOperationPayloadData**](SquareConnectionsCreateOperationPayloadData.md) |  | 
**meta** | [**SquareConnectionsCreateOperationPayloadMeta**](SquareConnectionsCreateOperationPayloadMeta.md) |  | 

## Example

```python
from tidal.models.square_connections_create_operation_payload import SquareConnectionsCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SquareConnectionsCreateOperationPayload from a JSON string
square_connections_create_operation_payload_instance = SquareConnectionsCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(SquareConnectionsCreateOperationPayload.to_json())

# convert the object into a dict
square_connections_create_operation_payload_dict = square_connections_create_operation_payload_instance.to_dict()
# create an instance of SquareConnectionsCreateOperationPayload from a dict
square_connections_create_operation_payload_from_dict = SquareConnectionsCreateOperationPayload.from_dict(square_connections_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


