# Default405ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[AtomicOperations405ResponseBodyErrorsInner]**](AtomicOperations405ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.default405_response_body import Default405ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of Default405ResponseBody from a JSON string
default405_response_body_instance = Default405ResponseBody.from_json(json)
# print the JSON string representation of the object
print(Default405ResponseBody.to_json())

# convert the object into a dict
default405_response_body_dict = default405_response_body_instance.to_dict()
# create an instance of Default405ResponseBody from a dict
default405_response_body_from_dict = Default405ResponseBody.from_dict(default405_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


