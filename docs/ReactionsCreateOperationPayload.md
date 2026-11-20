# ReactionsCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReactionsCreateOperationPayloadData**](ReactionsCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.reactions_create_operation_payload import ReactionsCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ReactionsCreateOperationPayload from a JSON string
reactions_create_operation_payload_instance = ReactionsCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(ReactionsCreateOperationPayload.to_json())

# convert the object into a dict
reactions_create_operation_payload_dict = reactions_create_operation_payload_instance.to_dict()
# create an instance of ReactionsCreateOperationPayload from a dict
reactions_create_operation_payload_from_dict = ReactionsCreateOperationPayload.from_dict(reactions_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


