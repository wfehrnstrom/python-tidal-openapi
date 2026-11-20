# Default400ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[AtomicOperations400ResponseBodyErrorsInner]**](AtomicOperations400ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.default400_response_body import Default400ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of Default400ResponseBody from a JSON string
default400_response_body_instance = Default400ResponseBody.from_json(json)
# print the JSON string representation of the object
print(Default400ResponseBody.to_json())

# convert the object into a dict
default400_response_body_dict = default400_response_body_instance.to_dict()
# create an instance of Default400ResponseBody from a dict
default400_response_body_from_dict = Default400ResponseBody.from_dict(default400_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


