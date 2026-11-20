# Default415ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[AtomicOperations415ResponseBodyErrorsInner]**](AtomicOperations415ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.default415_response_body import Default415ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of Default415ResponseBody from a JSON string
default415_response_body_instance = Default415ResponseBody.from_json(json)
# print the JSON string representation of the object
print(Default415ResponseBody.to_json())

# convert the object into a dict
default415_response_body_dict = default415_response_body_instance.to_dict()
# create an instance of Default415ResponseBody from a dict
default415_response_body_from_dict = Default415ResponseBody.from_dict(default415_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


