# LinksMeta

Non-standard meta information for links

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_cursor** | **str** | Only cursor part of next link | 

## Example

```python
from tidal.models.links_meta import LinksMeta

# TODO update the JSON string below
json = "{}"
# create an instance of LinksMeta from a JSON string
links_meta_instance = LinksMeta.from_json(json)
# print the JSON string representation of the object
print(LinksMeta.to_json())

# convert the object into a dict
links_meta_dict = links_meta_instance.to_dict()
# create an instance of LinksMeta from a dict
links_meta_from_dict = LinksMeta.from_dict(links_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


