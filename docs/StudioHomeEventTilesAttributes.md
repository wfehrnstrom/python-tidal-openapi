# StudioHomeEventTilesAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required_terms** | **List[str]** | Terms types the user must accept before using this tile; empty when none are missing. | 

## Example

```python
from tidal.models.studio_home_event_tiles_attributes import StudioHomeEventTilesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of StudioHomeEventTilesAttributes from a JSON string
studio_home_event_tiles_attributes_instance = StudioHomeEventTilesAttributes.from_json(json)
# print the JSON string representation of the object
print(StudioHomeEventTilesAttributes.to_json())

# convert the object into a dict
studio_home_event_tiles_attributes_dict = studio_home_event_tiles_attributes_instance.to_dict()
# create an instance of StudioHomeEventTilesAttributes from a dict
studio_home_event_tiles_attributes_from_dict = StudioHomeEventTilesAttributes.from_dict(studio_home_event_tiles_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


