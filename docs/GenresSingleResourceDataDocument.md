# GenresSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GenresResourceObject**](GenresResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.genres_single_resource_data_document import GenresSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of GenresSingleResourceDataDocument from a JSON string
genres_single_resource_data_document_instance = GenresSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(GenresSingleResourceDataDocument.to_json())

# convert the object into a dict
genres_single_resource_data_document_dict = genres_single_resource_data_document_instance.to_dict()
# create an instance of GenresSingleResourceDataDocument from a dict
genres_single_resource_data_document_from_dict = GenresSingleResourceDataDocument.from_dict(genres_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


