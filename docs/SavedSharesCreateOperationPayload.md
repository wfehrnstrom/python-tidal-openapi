# SavedSharesCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SavedSharesCreateOperationPayloadData**](SavedSharesCreateOperationPayloadData.md) |  | 
**meta** | [**SavedSharesCreateOperationPayloadMeta**](SavedSharesCreateOperationPayloadMeta.md) |  | [optional] 

## Example

```python
from tidal.models.saved_shares_create_operation_payload import SavedSharesCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SavedSharesCreateOperationPayload from a JSON string
saved_shares_create_operation_payload_instance = SavedSharesCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(SavedSharesCreateOperationPayload.to_json())

# convert the object into a dict
saved_shares_create_operation_payload_dict = saved_shares_create_operation_payload_instance.to_dict()
# create an instance of SavedSharesCreateOperationPayload from a dict
saved_shares_create_operation_payload_from_dict = SavedSharesCreateOperationPayload.from_dict(saved_shares_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


