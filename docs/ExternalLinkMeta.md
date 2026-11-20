# ExternalLinkMeta

metadata about an external link

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from tidal.models.external_link_meta import ExternalLinkMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalLinkMeta from a JSON string
external_link_meta_instance = ExternalLinkMeta.from_json(json)
# print the JSON string representation of the object
print(ExternalLinkMeta.to_json())

# convert the object into a dict
external_link_meta_dict = external_link_meta_instance.to_dict()
# create an instance of ExternalLinkMeta from a dict
external_link_meta_from_dict = ExternalLinkMeta.from_dict(external_link_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


