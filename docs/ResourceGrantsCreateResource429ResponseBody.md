# ResourceGrantsCreateResource429ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[ResourceGrantsCreateResource429ResponseBodyErrorsInner]**](ResourceGrantsCreateResource429ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.resource_grants_create_resource429_response_body import ResourceGrantsCreateResource429ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantsCreateResource429ResponseBody from a JSON string
resource_grants_create_resource429_response_body_instance = ResourceGrantsCreateResource429ResponseBody.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantsCreateResource429ResponseBody.to_json())

# convert the object into a dict
resource_grants_create_resource429_response_body_dict = resource_grants_create_resource429_response_body_instance.to_dict()
# create an instance of ResourceGrantsCreateResource429ResponseBody from a dict
resource_grants_create_resource429_response_body_from_dict = ResourceGrantsCreateResource429ResponseBody.from_dict(resource_grants_create_resource429_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


