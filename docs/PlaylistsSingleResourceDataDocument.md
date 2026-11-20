# PlaylistsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlaylistsResourceObject**](PlaylistsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.playlists_single_resource_data_document import PlaylistsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsSingleResourceDataDocument from a JSON string
playlists_single_resource_data_document_instance = PlaylistsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlaylistsSingleResourceDataDocument.to_json())

# convert the object into a dict
playlists_single_resource_data_document_dict = playlists_single_resource_data_document_instance.to_dict()
# create an instance of PlaylistsSingleResourceDataDocument from a dict
playlists_single_resource_data_document_from_dict = PlaylistsSingleResourceDataDocument.from_dict(playlists_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


