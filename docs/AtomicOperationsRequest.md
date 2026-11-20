# AtomicOperationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**atomic_operations** | [**List[AtomicOperationsRequestAtomicOperationsInner]**](AtomicOperationsRequestAtomicOperationsInner.md) |  | 

## Example

```python
from tidal.models.atomic_operations_request import AtomicOperationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AtomicOperationsRequest from a JSON string
atomic_operations_request_instance = AtomicOperationsRequest.from_json(json)
# print the JSON string representation of the object
print(AtomicOperationsRequest.to_json())

# convert the object into a dict
atomic_operations_request_dict = atomic_operations_request_instance.to_dict()
# create an instance of AtomicOperationsRequest from a dict
atomic_operations_request_from_dict = AtomicOperationsRequest.from_dict(atomic_operations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


