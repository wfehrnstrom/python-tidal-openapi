# LinkObject

A JSON:API link object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | 
**type** | **str** | Media type hint for the linked resource | [optional] 

## Example

```python
from tidal.models.link_object import LinkObject

# TODO update the JSON string below
json = "{}"
# create an instance of LinkObject from a JSON string
link_object_instance = LinkObject.from_json(json)
# print the JSON string representation of the object
print(LinkObject.to_json())

# convert the object into a dict
link_object_dict = link_object_instance.to_dict()
# create an instance of LinkObject from a dict
link_object_from_dict = LinkObject.from_dict(link_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


