# SharesUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SharesUpdateOperationPayloadData**](SharesUpdateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.shares_update_operation_payload import SharesUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SharesUpdateOperationPayload from a JSON string
shares_update_operation_payload_instance = SharesUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(SharesUpdateOperationPayload.to_json())

# convert the object into a dict
shares_update_operation_payload_dict = shares_update_operation_payload_instance.to_dict()
# create an instance of SharesUpdateOperationPayload from a dict
shares_update_operation_payload_from_dict = SharesUpdateOperationPayload.from_dict(shares_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


