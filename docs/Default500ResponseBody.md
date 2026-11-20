# Default500ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[AtomicOperations500ResponseBodyErrorsInner]**](AtomicOperations500ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.default500_response_body import Default500ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of Default500ResponseBody from a JSON string
default500_response_body_instance = Default500ResponseBody.from_json(json)
# print the JSON string representation of the object
print(Default500ResponseBody.to_json())

# convert the object into a dict
default500_response_body_dict = default500_response_body_instance.to_dict()
# create an instance of Default500ResponseBody from a dict
default500_response_body_from_dict = Default500ResponseBody.from_dict(default500_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


