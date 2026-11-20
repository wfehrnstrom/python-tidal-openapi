# AtomicOperations409ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[AtomicOperations409ResponseBodyErrorsInner]**](AtomicOperations409ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.atomic_operations409_response_body import AtomicOperations409ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of AtomicOperations409ResponseBody from a JSON string
atomic_operations409_response_body_instance = AtomicOperations409ResponseBody.from_json(json)
# print the JSON string representation of the object
print(AtomicOperations409ResponseBody.to_json())

# convert the object into a dict
atomic_operations409_response_body_dict = atomic_operations409_response_body_instance.to_dict()
# create an instance of AtomicOperations409ResponseBody from a dict
atomic_operations409_response_body_from_dict = AtomicOperations409ResponseBody.from_dict(atomic_operations409_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


