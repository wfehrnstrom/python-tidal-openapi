# ArtistsCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ArtistsResourceObject**](ArtistsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artists_create_single_resource_data_document import ArtistsCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsCreateSingleResourceDataDocument from a JSON string
artists_create_single_resource_data_document_instance = ArtistsCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistsCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
artists_create_single_resource_data_document_dict = artists_create_single_resource_data_document_instance.to_dict()
# create an instance of ArtistsCreateSingleResourceDataDocument from a dict
artists_create_single_resource_data_document_from_dict = ArtistsCreateSingleResourceDataDocument.from_dict(artists_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


