# LyricsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LyricsResourceObject**](LyricsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.lyrics_single_resource_data_document import LyricsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of LyricsSingleResourceDataDocument from a JSON string
lyrics_single_resource_data_document_instance = LyricsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(LyricsSingleResourceDataDocument.to_json())

# convert the object into a dict
lyrics_single_resource_data_document_dict = lyrics_single_resource_data_document_instance.to_dict()
# create an instance of LyricsSingleResourceDataDocument from a dict
lyrics_single_resource_data_document_from_dict = LyricsSingleResourceDataDocument.from_dict(lyrics_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


