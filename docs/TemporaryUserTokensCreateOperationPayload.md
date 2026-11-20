# TemporaryUserTokensCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TemporaryUserTokensCreateOperationPayloadData**](TemporaryUserTokensCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.temporary_user_tokens_create_operation_payload import TemporaryUserTokensCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of TemporaryUserTokensCreateOperationPayload from a JSON string
temporary_user_tokens_create_operation_payload_instance = TemporaryUserTokensCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(TemporaryUserTokensCreateOperationPayload.to_json())

# convert the object into a dict
temporary_user_tokens_create_operation_payload_dict = temporary_user_tokens_create_operation_payload_instance.to_dict()
# create an instance of TemporaryUserTokensCreateOperationPayload from a dict
temporary_user_tokens_create_operation_payload_from_dict = TemporaryUserTokensCreateOperationPayload.from_dict(temporary_user_tokens_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


