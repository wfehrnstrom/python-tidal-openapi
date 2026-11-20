# PlaylistsUpdateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlaylistsResourceObject**](PlaylistsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.playlists_update_single_resource_data_document import PlaylistsUpdateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsUpdateSingleResourceDataDocument from a JSON string
playlists_update_single_resource_data_document_instance = PlaylistsUpdateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlaylistsUpdateSingleResourceDataDocument.to_json())

# convert the object into a dict
playlists_update_single_resource_data_document_dict = playlists_update_single_resource_data_document_instance.to_dict()
# create an instance of PlaylistsUpdateSingleResourceDataDocument from a dict
playlists_update_single_resource_data_document_from_dict = PlaylistsUpdateSingleResourceDataDocument.from_dict(playlists_update_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


