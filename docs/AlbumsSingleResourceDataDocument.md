# AlbumsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AlbumsResourceObject**](AlbumsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.albums_single_resource_data_document import AlbumsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsSingleResourceDataDocument from a JSON string
albums_single_resource_data_document_instance = AlbumsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(AlbumsSingleResourceDataDocument.to_json())

# convert the object into a dict
albums_single_resource_data_document_dict = albums_single_resource_data_document_instance.to_dict()
# create an instance of AlbumsSingleResourceDataDocument from a dict
albums_single_resource_data_document_from_dict = AlbumsSingleResourceDataDocument.from_dict(albums_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


