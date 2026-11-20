# SharesCreateOperationPayloadDataRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shared_resources** | [**SharesCreateOperationPayloadDataRelationshipsSharedResources**](SharesCreateOperationPayloadDataRelationshipsSharedResources.md) |  | 

## Example

```python
from tidal.models.shares_create_operation_payload_data_relationships import SharesCreateOperationPayloadDataRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of SharesCreateOperationPayloadDataRelationships from a JSON string
shares_create_operation_payload_data_relationships_instance = SharesCreateOperationPayloadDataRelationships.from_json(json)
# print the JSON string representation of the object
print(SharesCreateOperationPayloadDataRelationships.to_json())

# convert the object into a dict
shares_create_operation_payload_data_relationships_dict = shares_create_operation_payload_data_relationships_instance.to_dict()
# create an instance of SharesCreateOperationPayloadDataRelationships from a dict
shares_create_operation_payload_data_relationships_from_dict = SharesCreateOperationPayloadDataRelationships.from_dict(shares_create_operation_payload_data_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


