# SquareItemVariationsUpdateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Variation name; an empty string clears it | [optional] 
**price** | **str** | Amount in the currency&#39;s major units | [optional] 
**stock_tracked** | **bool** | Stock tracking at the selected site&#39;s shipping location (merchant-main fallback) | [optional] 

## Example

```python
from tidal.models.square_item_variations_update_operation_payload_data_attributes import SquareItemVariationsUpdateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemVariationsUpdateOperationPayloadDataAttributes from a JSON string
square_item_variations_update_operation_payload_data_attributes_instance = SquareItemVariationsUpdateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(SquareItemVariationsUpdateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
square_item_variations_update_operation_payload_data_attributes_dict = square_item_variations_update_operation_payload_data_attributes_instance.to_dict()
# create an instance of SquareItemVariationsUpdateOperationPayloadDataAttributes from a dict
square_item_variations_update_operation_payload_data_attributes_from_dict = SquareItemVariationsUpdateOperationPayloadDataAttributes.from_dict(square_item_variations_update_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


