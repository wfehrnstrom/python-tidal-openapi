# AtomicOperationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**atomic_results** | [**List[AtomicOperationsResponseAtomicResultsInner]**](AtomicOperationsResponseAtomicResultsInner.md) |  | 

## Example

```python
from tidal.models.atomic_operations_response import AtomicOperationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AtomicOperationsResponse from a JSON string
atomic_operations_response_instance = AtomicOperationsResponse.from_json(json)
# print the JSON string representation of the object
print(AtomicOperationsResponse.to_json())

# convert the object into a dict
atomic_operations_response_dict = atomic_operations_response_instance.to_dict()
# create an instance of AtomicOperationsResponse from a dict
atomic_operations_response_from_dict = AtomicOperationsResponse.from_dict(atomic_operations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


