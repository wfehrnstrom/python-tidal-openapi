# ArtworkLibrariesSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ArtworkLibrariesResourceObject**](ArtworkLibrariesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artwork_libraries_single_resource_data_document import ArtworkLibrariesSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtworkLibrariesSingleResourceDataDocument from a JSON string
artwork_libraries_single_resource_data_document_instance = ArtworkLibrariesSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtworkLibrariesSingleResourceDataDocument.to_json())

# convert the object into a dict
artwork_libraries_single_resource_data_document_dict = artwork_libraries_single_resource_data_document_instance.to_dict()
# create an instance of ArtworkLibrariesSingleResourceDataDocument from a dict
artwork_libraries_single_resource_data_document_from_dict = ArtworkLibrariesSingleResourceDataDocument.from_dict(artwork_libraries_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


