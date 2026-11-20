# SharesUpdateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Password a user must send to save the share. Never returned. Must be printable ASCII characters. A value sets or changes it; null removes it; omitted leaves it unchanged. Playlist shares and shares without VOUCHER cannot have one. | [optional] 

## Example

```python
from tidal.models.shares_update_operation_payload_data_attributes import SharesUpdateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SharesUpdateOperationPayloadDataAttributes from a JSON string
shares_update_operation_payload_data_attributes_instance = SharesUpdateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(SharesUpdateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
shares_update_operation_payload_data_attributes_dict = shares_update_operation_payload_data_attributes_instance.to_dict()
# create an instance of SharesUpdateOperationPayloadDataAttributes from a dict
shares_update_operation_payload_data_attributes_from_dict = SharesUpdateOperationPayloadDataAttributes.from_dict(shares_update_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


