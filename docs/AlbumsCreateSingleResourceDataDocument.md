# AlbumsCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AlbumsResourceObject**](AlbumsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.albums_create_single_resource_data_document import AlbumsCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsCreateSingleResourceDataDocument from a JSON string
albums_create_single_resource_data_document_instance = AlbumsCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(AlbumsCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
albums_create_single_resource_data_document_dict = albums_create_single_resource_data_document_instance.to_dict()
# create an instance of AlbumsCreateSingleResourceDataDocument from a dict
albums_create_single_resource_data_document_from_dict = AlbumsCreateSingleResourceDataDocument.from_dict(albums_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


