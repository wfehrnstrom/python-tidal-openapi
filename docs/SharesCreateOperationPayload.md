# SharesCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SharesCreateOperationPayloadData**](SharesCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.shares_create_operation_payload import SharesCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SharesCreateOperationPayload from a JSON string
shares_create_operation_payload_instance = SharesCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(SharesCreateOperationPayload.to_json())

# convert the object into a dict
shares_create_operation_payload_dict = shares_create_operation_payload_instance.to_dict()
# create an instance of SharesCreateOperationPayload from a dict
shares_create_operation_payload_from_dict = SharesCreateOperationPayload.from_dict(shares_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


