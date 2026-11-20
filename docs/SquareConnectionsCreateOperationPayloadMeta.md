# SquareConnectionsCreateOperationPayloadMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform** | **str** | Client platform initiating Square onboarding. | 
**redirect_url** | **str** | Optional post-finalize redirect URL. Otherwise uses platform default. | [optional] 

## Example

```python
from tidal.models.square_connections_create_operation_payload_meta import SquareConnectionsCreateOperationPayloadMeta

# TODO update the JSON string below
json = "{}"
# create an instance of SquareConnectionsCreateOperationPayloadMeta from a JSON string
square_connections_create_operation_payload_meta_instance = SquareConnectionsCreateOperationPayloadMeta.from_json(json)
# print the JSON string representation of the object
print(SquareConnectionsCreateOperationPayloadMeta.to_json())

# convert the object into a dict
square_connections_create_operation_payload_meta_dict = square_connections_create_operation_payload_meta_instance.to_dict()
# create an instance of SquareConnectionsCreateOperationPayloadMeta from a dict
square_connections_create_operation_payload_meta_from_dict = SquareConnectionsCreateOperationPayloadMeta.from_dict(square_connections_create_operation_payload_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


