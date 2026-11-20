# TracksMetadataStatusAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the metadata detection job | 

## Example

```python
from tidal.models.tracks_metadata_status_attributes import TracksMetadataStatusAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of TracksMetadataStatusAttributes from a JSON string
tracks_metadata_status_attributes_instance = TracksMetadataStatusAttributes.from_json(json)
# print the JSON string representation of the object
print(TracksMetadataStatusAttributes.to_json())

# convert the object into a dict
tracks_metadata_status_attributes_dict = tracks_metadata_status_attributes_instance.to_dict()
# create an instance of TracksMetadataStatusAttributes from a dict
tracks_metadata_status_attributes_from_dict = TracksMetadataStatusAttributes.from_dict(tracks_metadata_status_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


