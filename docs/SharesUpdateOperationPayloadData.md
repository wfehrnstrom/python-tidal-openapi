# SharesUpdateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SharesUpdateOperationPayloadDataAttributes**](SharesUpdateOperationPayloadDataAttributes.md) |  | 
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.shares_update_operation_payload_data import SharesUpdateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of SharesUpdateOperationPayloadData from a JSON string
shares_update_operation_payload_data_instance = SharesUpdateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(SharesUpdateOperationPayloadData.to_json())

# convert the object into a dict
shares_update_operation_payload_data_dict = shares_update_operation_payload_data_instance.to_dict()
# create an instance of SharesUpdateOperationPayloadData from a dict
shares_update_operation_payload_data_from_dict = SharesUpdateOperationPayloadData.from_dict(shares_update_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


