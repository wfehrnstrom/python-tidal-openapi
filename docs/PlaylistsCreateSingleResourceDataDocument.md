# PlaylistsCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlaylistsResourceObject**](PlaylistsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.playlists_create_single_resource_data_document import PlaylistsCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsCreateSingleResourceDataDocument from a JSON string
playlists_create_single_resource_data_document_instance = PlaylistsCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlaylistsCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
playlists_create_single_resource_data_document_dict = playlists_create_single_resource_data_document_instance.to_dict()
# create an instance of PlaylistsCreateSingleResourceDataDocument from a dict
playlists_create_single_resource_data_document_from_dict = PlaylistsCreateSingleResourceDataDocument.from_dict(playlists_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


