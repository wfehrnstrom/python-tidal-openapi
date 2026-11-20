# AtomicOperationsRequestAtomicOperationsInnerOneOf1

Creates an item together with 1–100 variation add operations in one atomic request. The item must precede its variations and have a local ID. Inventory counts are submitted separately. Optional sites linkage publishes the item and every variation in that site in the same catalog batch. Only the seller's selected site is supported; another site returns SITE_NOT_SELECTED. Omission leaves Square's default publication behavior unchanged.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SquareItemsCreateOperationPayloadData**](SquareItemsCreateOperationPayloadData.md) |  | 
**op** | **str** |  | 

## Example

```python
from tidal.models.atomic_operations_request_atomic_operations_inner_one_of1 import AtomicOperationsRequestAtomicOperationsInnerOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of AtomicOperationsRequestAtomicOperationsInnerOneOf1 from a JSON string
atomic_operations_request_atomic_operations_inner_one_of1_instance = AtomicOperationsRequestAtomicOperationsInnerOneOf1.from_json(json)
# print the JSON string representation of the object
print(AtomicOperationsRequestAtomicOperationsInnerOneOf1.to_json())

# convert the object into a dict
atomic_operations_request_atomic_operations_inner_one_of1_dict = atomic_operations_request_atomic_operations_inner_one_of1_instance.to_dict()
# create an instance of AtomicOperationsRequestAtomicOperationsInnerOneOf1 from a dict
atomic_operations_request_atomic_operations_inner_one_of1_from_dict = AtomicOperationsRequestAtomicOperationsInnerOneOf1.from_dict(atomic_operations_request_atomic_operations_inner_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


