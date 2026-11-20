# LyricsCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LyricsResourceObject**](LyricsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.lyrics_create_single_resource_data_document import LyricsCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of LyricsCreateSingleResourceDataDocument from a JSON string
lyrics_create_single_resource_data_document_instance = LyricsCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(LyricsCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
lyrics_create_single_resource_data_document_dict = lyrics_create_single_resource_data_document_instance.to_dict()
# create an instance of LyricsCreateSingleResourceDataDocument from a dict
lyrics_create_single_resource_data_document_from_dict = LyricsCreateSingleResourceDataDocument.from_dict(lyrics_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


