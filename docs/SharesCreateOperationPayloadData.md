# SharesCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SharesCreateOperationPayloadDataAttributes**](SharesCreateOperationPayloadDataAttributes.md) |  | 
**relationships** | [**SharesCreateOperationPayloadDataRelationships**](SharesCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.shares_create_operation_payload_data import SharesCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of SharesCreateOperationPayloadData from a JSON string
shares_create_operation_payload_data_instance = SharesCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(SharesCreateOperationPayloadData.to_json())

# convert the object into a dict
shares_create_operation_payload_data_dict = shares_create_operation_payload_data_instance.to_dict()
# create an instance of SharesCreateOperationPayloadData from a dict
shares_create_operation_payload_data_from_dict = SharesCreateOperationPayloadData.from_dict(shares_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


