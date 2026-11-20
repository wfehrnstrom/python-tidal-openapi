# SquareItemVariationPhysicalCountsCreateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**occurred_at** | **datetime** | Physical count event time; the first submission must be within the preceding 24 hours and not in the future | 
**quantity** | **int** |  | 

## Example

```python
from tidal.models.square_item_variation_physical_counts_create_operation_payload_data_attributes import SquareItemVariationPhysicalCountsCreateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemVariationPhysicalCountsCreateOperationPayloadDataAttributes from a JSON string
square_item_variation_physical_counts_create_operation_payload_data_attributes_instance = SquareItemVariationPhysicalCountsCreateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(SquareItemVariationPhysicalCountsCreateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
square_item_variation_physical_counts_create_operation_payload_data_attributes_dict = square_item_variation_physical_counts_create_operation_payload_data_attributes_instance.to_dict()
# create an instance of SquareItemVariationPhysicalCountsCreateOperationPayloadDataAttributes from a dict
square_item_variation_physical_counts_create_operation_payload_data_attributes_from_dict = SquareItemVariationPhysicalCountsCreateOperationPayloadDataAttributes.from_dict(square_item_variation_physical_counts_create_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


