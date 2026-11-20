# ResourceGrantsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code of a bearer grant: whoever presents it as &#x60;shareCode&#x60; holds the role on the subject and everything below it. | [optional] 
**expires_at** | **datetime** | Time a bearer grant stops applying. | [optional] 
**role** | **str** |  | 

## Example

```python
from tidal.models.resource_grants_attributes import ResourceGrantsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantsAttributes from a JSON string
resource_grants_attributes_instance = ResourceGrantsAttributes.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantsAttributes.to_json())

# convert the object into a dict
resource_grants_attributes_dict = resource_grants_attributes_instance.to_dict()
# create an instance of ResourceGrantsAttributes from a dict
resource_grants_attributes_from_dict = ResourceGrantsAttributes.from_dict(resource_grants_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


