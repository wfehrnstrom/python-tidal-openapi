# SharesCreateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** | Time bearer access and acceptance expire; must be in the future and at most a year away. Defaults to seven days after creation when omitted or null. | [optional] 
**max_uses** | **int** | Number of saves the share permits. Every save counts as a use, and a used-up share also stops bearer access. Omit or send null for unlimited saves. | [optional] 
**password** | **str** | Password a user must send to save the share. Never returned. Must be printable ASCII characters. A protected share permits no bearer access. A password on a playlist share is rejected with 400. | [optional] 
**role** | **str** | Role offered by the share. | 

## Example

```python
from tidal.models.shares_create_operation_payload_data_attributes import SharesCreateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SharesCreateOperationPayloadDataAttributes from a JSON string
shares_create_operation_payload_data_attributes_instance = SharesCreateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(SharesCreateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
shares_create_operation_payload_data_attributes_dict = shares_create_operation_payload_data_attributes_instance.to_dict()
# create an instance of SharesCreateOperationPayloadDataAttributes from a dict
shares_create_operation_payload_data_attributes_from_dict = SharesCreateOperationPayloadDataAttributes.from_dict(shares_create_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


