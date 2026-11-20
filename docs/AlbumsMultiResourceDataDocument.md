# AlbumsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AlbumsResourceObject]**](AlbumsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.albums_multi_resource_data_document import AlbumsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsMultiResourceDataDocument from a JSON string
albums_multi_resource_data_document_instance = AlbumsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(AlbumsMultiResourceDataDocument.to_json())

# convert the object into a dict
albums_multi_resource_data_document_dict = albums_multi_resource_data_document_instance.to_dict()
# create an instance of AlbumsMultiResourceDataDocument from a dict
albums_multi_resource_data_document_from_dict = AlbumsMultiResourceDataDocument.from_dict(albums_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


