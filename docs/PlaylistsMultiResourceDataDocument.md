# PlaylistsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlaylistsResourceObject]**](PlaylistsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.playlists_multi_resource_data_document import PlaylistsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsMultiResourceDataDocument from a JSON string
playlists_multi_resource_data_document_instance = PlaylistsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlaylistsMultiResourceDataDocument.to_json())

# convert the object into a dict
playlists_multi_resource_data_document_dict = playlists_multi_resource_data_document_instance.to_dict()
# create an instance of PlaylistsMultiResourceDataDocument from a dict
playlists_multi_resource_data_document_from_dict = PlaylistsMultiResourceDataDocument.from_dict(playlists_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


