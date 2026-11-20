# LyricsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**LyricsAttributes**](LyricsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**LyricsRelationships**](LyricsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.lyrics_resource_object import LyricsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of LyricsResourceObject from a JSON string
lyrics_resource_object_instance = LyricsResourceObject.from_json(json)
# print the JSON string representation of the object
print(LyricsResourceObject.to_json())

# convert the object into a dict
lyrics_resource_object_dict = lyrics_resource_object_instance.to_dict()
# create an instance of LyricsResourceObject from a dict
lyrics_resource_object_from_dict = LyricsResourceObject.from_dict(lyrics_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


