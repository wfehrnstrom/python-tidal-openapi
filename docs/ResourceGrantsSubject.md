# ResourceGrantsSubject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.resource_grants_subject import ResourceGrantsSubject

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantsSubject from a JSON string
resource_grants_subject_instance = ResourceGrantsSubject.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantsSubject.to_json())

# convert the object into a dict
resource_grants_subject_dict = resource_grants_subject_instance.to_dict()
# create an instance of ResourceGrantsSubject from a dict
resource_grants_subject_from_dict = ResourceGrantsSubject.from_dict(resource_grants_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


