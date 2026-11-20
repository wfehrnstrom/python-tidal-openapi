# ReactionsCreateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emoji** | **str** |  | 
**end_offset** | **str** | Section end offset (ISO 8601 duration), at or after startOffset. Requires startOffset; omitted for a point reaction. | [optional] 
**start_offset** | **str** | Nonnegative source-file offset (ISO 8601 duration); omitted for the whole subject. | [optional] 

## Example

```python
from tidal.models.reactions_create_operation_payload_data_attributes import ReactionsCreateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ReactionsCreateOperationPayloadDataAttributes from a JSON string
reactions_create_operation_payload_data_attributes_instance = ReactionsCreateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(ReactionsCreateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
reactions_create_operation_payload_data_attributes_dict = reactions_create_operation_payload_data_attributes_instance.to_dict()
# create an instance of ReactionsCreateOperationPayloadDataAttributes from a dict
reactions_create_operation_payload_data_attributes_from_dict = ReactionsCreateOperationPayloadDataAttributes.from_dict(reactions_create_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


