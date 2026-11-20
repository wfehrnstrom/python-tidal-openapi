# VideosAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability** | **List[str]** | Available usage for this video. Deprecated: use &#39;usageRules&#39; instead. This field will be removed in a future version. | [optional] 
**copyright** | [**Copyright**](Copyright.md) |  | [optional] 
**duration** | **str** | Duration (ISO 8601) | 
**explicit** | **bool** | Explicit content | 
**external_links** | [**List[ExternalLink]**](ExternalLink.md) | Video links external to TIDAL API | [optional] 
**isrc** | **str** | International Standard Recording Code (ISRC) | 
**popularity** | **float** | Popularity (0.0 - 1.0) | 
**release_date** | **date** | Release date (ISO-8601) | [optional] 
**title** | **str** | Video title | 
**version** | **str** | Video version, complements title | [optional] 

## Example

```python
from tidal.models.videos_attributes import VideosAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of VideosAttributes from a JSON string
videos_attributes_instance = VideosAttributes.from_json(json)
# print the JSON string representation of the object
print(VideosAttributes.to_json())

# convert the object into a dict
videos_attributes_dict = videos_attributes_instance.to_dict()
# create an instance of VideosAttributes from a dict
videos_attributes_from_dict = VideosAttributes.from_dict(videos_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


