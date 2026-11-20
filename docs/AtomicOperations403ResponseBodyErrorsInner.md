# AtomicOperations403ResponseBodyErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**detail** | **str** |  | [optional] 
**meta** | [**MissingTermsMeta**](MissingTermsMeta.md) |  | [optional] 
**status** | **str** |  | 

## Example

```python
from tidal.models.atomic_operations403_response_body_errors_inner import AtomicOperations403ResponseBodyErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AtomicOperations403ResponseBodyErrorsInner from a JSON string
atomic_operations403_response_body_errors_inner_instance = AtomicOperations403ResponseBodyErrorsInner.from_json(json)
# print the JSON string representation of the object
print(AtomicOperations403ResponseBodyErrorsInner.to_json())

# convert the object into a dict
atomic_operations403_response_body_errors_inner_dict = atomic_operations403_response_body_errors_inner_instance.to_dict()
# create an instance of AtomicOperations403ResponseBodyErrorsInner from a dict
atomic_operations403_response_body_errors_inner_from_dict = AtomicOperations403ResponseBodyErrorsInner.from_dict(atomic_operations403_response_body_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


