# AtomicOperationsRequestAtomicOperationsInnerOneOf

Creates a positive fixed-price variation linked by lid to the item added earlier in this atomic request. Inventory quantity is submitted separately.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SquareItemVariationsCreateOperationPayloadLocalData**](SquareItemVariationsCreateOperationPayloadLocalData.md) |  | 
**op** | **str** |  | 

## Example

```python
from tidal.models.atomic_operations_request_atomic_operations_inner_one_of import AtomicOperationsRequestAtomicOperationsInnerOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of AtomicOperationsRequestAtomicOperationsInnerOneOf from a JSON string
atomic_operations_request_atomic_operations_inner_one_of_instance = AtomicOperationsRequestAtomicOperationsInnerOneOf.from_json(json)
# print the JSON string representation of the object
print(AtomicOperationsRequestAtomicOperationsInnerOneOf.to_json())

# convert the object into a dict
atomic_operations_request_atomic_operations_inner_one_of_dict = atomic_operations_request_atomic_operations_inner_one_of_instance.to_dict()
# create an instance of AtomicOperationsRequestAtomicOperationsInnerOneOf from a dict
atomic_operations_request_atomic_operations_inner_one_of_from_dict = AtomicOperationsRequestAtomicOperationsInnerOneOf.from_dict(atomic_operations_request_atomic_operations_inner_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


