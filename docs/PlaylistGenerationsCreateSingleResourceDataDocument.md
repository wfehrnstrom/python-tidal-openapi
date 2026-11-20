# PlaylistGenerationsCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlaylistGenerationsResourceObject**](PlaylistGenerationsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.playlist_generations_create_single_resource_data_document import PlaylistGenerationsCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationsCreateSingleResourceDataDocument from a JSON string
playlist_generations_create_single_resource_data_document_instance = PlaylistGenerationsCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationsCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
playlist_generations_create_single_resource_data_document_dict = playlist_generations_create_single_resource_data_document_instance.to_dict()
# create an instance of PlaylistGenerationsCreateSingleResourceDataDocument from a dict
playlist_generations_create_single_resource_data_document_from_dict = PlaylistGenerationsCreateSingleResourceDataDocument.from_dict(playlist_generations_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


