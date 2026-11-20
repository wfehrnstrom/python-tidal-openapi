# ReactionsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ReactionsCreateOperationPayloadDataAttributes**](ReactionsCreateOperationPayloadDataAttributes.md) |  | 
**relationships** | [**ReactionsCreateOperationPayloadDataRelationships**](ReactionsCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.reactions_create_operation_payload_data import ReactionsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of ReactionsCreateOperationPayloadData from a JSON string
reactions_create_operation_payload_data_instance = ReactionsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(ReactionsCreateOperationPayloadData.to_json())

# convert the object into a dict
reactions_create_operation_payload_data_dict = reactions_create_operation_payload_data_instance.to_dict()
# create an instance of ReactionsCreateOperationPayloadData from a dict
reactions_create_operation_payload_data_from_dict = ReactionsCreateOperationPayloadData.from_dict(reactions_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


