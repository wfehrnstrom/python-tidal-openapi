# ResourceGrantsCreateResource403ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[ResourceGrantsCreateResource403ResponseBodyErrorsInner]**](ResourceGrantsCreateResource403ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.resource_grants_create_resource403_response_body import ResourceGrantsCreateResource403ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantsCreateResource403ResponseBody from a JSON string
resource_grants_create_resource403_response_body_instance = ResourceGrantsCreateResource403ResponseBody.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantsCreateResource403ResponseBody.to_json())

# convert the object into a dict
resource_grants_create_resource403_response_body_dict = resource_grants_create_resource403_response_body_instance.to_dict()
# create an instance of ResourceGrantsCreateResource403ResponseBody from a dict
resource_grants_create_resource403_response_body_from_dict = ResourceGrantsCreateResource403ResponseBody.from_dict(resource_grants_create_resource403_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


