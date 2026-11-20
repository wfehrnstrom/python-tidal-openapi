# AppreciationsCreateOperationPayloadDataRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appreciated_items** | [**AppreciationsCreateOperationPayloadDataRelationshipsAppreciatedItem**](AppreciationsCreateOperationPayloadDataRelationshipsAppreciatedItem.md) |  | 

## Example

```python
from tidal.models.appreciations_create_operation_payload_data_relationships import AppreciationsCreateOperationPayloadDataRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of AppreciationsCreateOperationPayloadDataRelationships from a JSON string
appreciations_create_operation_payload_data_relationships_instance = AppreciationsCreateOperationPayloadDataRelationships.from_json(json)
# print the JSON string representation of the object
print(AppreciationsCreateOperationPayloadDataRelationships.to_json())

# convert the object into a dict
appreciations_create_operation_payload_data_relationships_dict = appreciations_create_operation_payload_data_relationships_instance.to_dict()
# create an instance of AppreciationsCreateOperationPayloadDataRelationships from a dict
appreciations_create_operation_payload_data_relationships_from_dict = AppreciationsCreateOperationPayloadDataRelationships.from_dict(appreciations_create_operation_payload_data_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


