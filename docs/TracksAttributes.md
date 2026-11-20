# TracksAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | **str** | Access type | [optional] 
**ai** | **bool** | Whether the track is AI-generated | [optional] 
**availability** | **List[str]** | Available usage for this track. Deprecated: use &#39;usageRules&#39; instead. This field will be removed in a future version. | [optional] 
**bpm** | **float** | Beats per minute | [optional] 
**copyright** | [**Copyright**](Copyright.md) |  | [optional] 
**created_at** | **datetime** | Datetime of track creation (ISO 8601) | [optional] 
**duration** | **str** | Duration (ISO 8601) | 
**explicit** | **bool** | Explicit content | 
**external_links** | [**List[ExternalLink]**](ExternalLink.md) | Track links external to TIDAL API | [optional] 
**isrc** | **str** | International Standard Recording Code (ISRC) | 
**key** | **str** | Key | 
**key_scale** | **str** | The scale of the key | 
**media_tags** | **List[str]** |  | 
**popularity** | **float** | Popularity (0.0 - 1.0) | 
**spotlighted** | **bool** | Is the track spotlighted? | [optional] 
**title** | **str** | Track title | 
**tone_tags** | **List[str]** |  | [optional] 
**version** | **str** | Track version, complements title | [optional] 

## Example

```python
from tidal.models.tracks_attributes import TracksAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of TracksAttributes from a JSON string
tracks_attributes_instance = TracksAttributes.from_json(json)
# print the JSON string representation of the object
print(TracksAttributes.to_json())

# convert the object into a dict
tracks_attributes_dict = tracks_attributes_instance.to_dict()
# create an instance of TracksAttributes from a dict
tracks_attributes_from_dict = TracksAttributes.from_dict(tracks_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


