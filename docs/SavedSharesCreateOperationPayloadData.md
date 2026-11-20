# SavedSharesCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relationships** | [**SavedSharesCreateOperationPayloadDataRelationships**](SavedSharesCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.saved_shares_create_operation_payload_data import SavedSharesCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of SavedSharesCreateOperationPayloadData from a JSON string
saved_shares_create_operation_payload_data_instance = SavedSharesCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(SavedSharesCreateOperationPayloadData.to_json())

# convert the object into a dict
saved_shares_create_operation_payload_data_dict = saved_shares_create_operation_payload_data_instance.to_dict()
# create an instance of SavedSharesCreateOperationPayloadData from a dict
saved_shares_create_operation_payload_data_from_dict = SavedSharesCreateOperationPayloadData.from_dict(saved_shares_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


