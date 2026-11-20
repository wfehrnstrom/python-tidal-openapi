# Default404ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[AtomicOperations404ResponseBodyErrorsInner]**](AtomicOperations404ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.default404_response_body import Default404ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of Default404ResponseBody from a JSON string
default404_response_body_instance = Default404ResponseBody.from_json(json)
# print the JSON string representation of the object
print(Default404ResponseBody.to_json())

# convert the object into a dict
default404_response_body_dict = default404_response_body_instance.to_dict()
# create an instance of Default404ResponseBody from a dict
default404_response_body_from_dict = Default404ResponseBody.from_dict(default404_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


