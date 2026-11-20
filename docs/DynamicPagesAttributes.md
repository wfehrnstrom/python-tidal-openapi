# DynamicPagesAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_type** | **str** | Type of the page eg. home, artist | 
**reporting_id** | **UUID** | Id used for reporting user events | 

## Example

```python
from tidal.models.dynamic_pages_attributes import DynamicPagesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicPagesAttributes from a JSON string
dynamic_pages_attributes_instance = DynamicPagesAttributes.from_json(json)
# print the JSON string representation of the object
print(DynamicPagesAttributes.to_json())

# convert the object into a dict
dynamic_pages_attributes_dict = dynamic_pages_attributes_instance.to_dict()
# create an instance of DynamicPagesAttributes from a dict
dynamic_pages_attributes_from_dict = DynamicPagesAttributes.from_dict(dynamic_pages_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


