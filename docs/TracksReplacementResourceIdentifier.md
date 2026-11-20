# TracksReplacementResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**TracksReplacementResourceIdentifierMeta**](TracksReplacementResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.tracks_replacement_resource_identifier import TracksReplacementResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of TracksReplacementResourceIdentifier from a JSON string
tracks_replacement_resource_identifier_instance = TracksReplacementResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(TracksReplacementResourceIdentifier.to_json())

# convert the object into a dict
tracks_replacement_resource_identifier_dict = tracks_replacement_resource_identifier_instance.to_dict()
# create an instance of TracksReplacementResourceIdentifier from a dict
tracks_replacement_resource_identifier_from_dict = TracksReplacementResourceIdentifier.from_dict(tracks_replacement_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


