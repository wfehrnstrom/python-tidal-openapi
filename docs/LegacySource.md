# LegacySource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.legacy_source import LegacySource

# TODO update the JSON string below
json = "{}"
# create an instance of LegacySource from a JSON string
legacy_source_instance = LegacySource.from_json(json)
# print the JSON string representation of the object
print(LegacySource.to_json())

# convert the object into a dict
legacy_source_dict = legacy_source_instance.to_dict()
# create an instance of LegacySource from a dict
legacy_source_from_dict = LegacySource.from_dict(legacy_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


