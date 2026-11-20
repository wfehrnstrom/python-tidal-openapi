# SavedSharesCreateOperationPayloadMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Password of a password-protected share. Ignored for other shares. | [optional] 

## Example

```python
from tidal.models.saved_shares_create_operation_payload_meta import SavedSharesCreateOperationPayloadMeta

# TODO update the JSON string below
json = "{}"
# create an instance of SavedSharesCreateOperationPayloadMeta from a JSON string
saved_shares_create_operation_payload_meta_instance = SavedSharesCreateOperationPayloadMeta.from_json(json)
# print the JSON string representation of the object
print(SavedSharesCreateOperationPayloadMeta.to_json())

# convert the object into a dict
saved_shares_create_operation_payload_meta_dict = saved_shares_create_operation_payload_meta_instance.to_dict()
# create an instance of SavedSharesCreateOperationPayloadMeta from a dict
saved_shares_create_operation_payload_meta_from_dict = SavedSharesCreateOperationPayloadMeta.from_dict(saved_shares_create_operation_payload_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


