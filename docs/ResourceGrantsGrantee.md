# ResourceGrantsGrantee

A grant recipient. Identify the Everyone group with `type` set to `groups` and `id` set to `everyone`; only albums can be granted to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.resource_grants_grantee import ResourceGrantsGrantee

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantsGrantee from a JSON string
resource_grants_grantee_instance = ResourceGrantsGrantee.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantsGrantee.to_json())

# convert the object into a dict
resource_grants_grantee_dict = resource_grants_grantee_instance.to_dict()
# create an instance of ResourceGrantsGrantee from a dict
resource_grants_grantee_from_dict = ResourceGrantsGrantee.from_dict(resource_grants_grantee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


