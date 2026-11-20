# Default406ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[AtomicOperations406ResponseBodyErrorsInner]**](AtomicOperations406ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.default406_response_body import Default406ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of Default406ResponseBody from a JSON string
default406_response_body_instance = Default406ResponseBody.from_json(json)
# print the JSON string representation of the object
print(Default406ResponseBody.to_json())

# convert the object into a dict
default406_response_body_dict = default406_response_body_instance.to_dict()
# create an instance of Default406ResponseBody from a dict
default406_response_body_from_dict = Default406ResponseBody.from_dict(default406_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


