# AtomicOperations400ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[AtomicOperations400ResponseBodyErrorsInner]**](AtomicOperations400ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.atomic_operations400_response_body import AtomicOperations400ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of AtomicOperations400ResponseBody from a JSON string
atomic_operations400_response_body_instance = AtomicOperations400ResponseBody.from_json(json)
# print the JSON string representation of the object
print(AtomicOperations400ResponseBody.to_json())

# convert the object into a dict
atomic_operations400_response_body_dict = atomic_operations400_response_body_instance.to_dict()
# create an instance of AtomicOperations400ResponseBody from a dict
atomic_operations400_response_body_from_dict = AtomicOperations400ResponseBody.from_dict(atomic_operations400_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


