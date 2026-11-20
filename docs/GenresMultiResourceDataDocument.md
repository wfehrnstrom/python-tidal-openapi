# GenresMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GenresResourceObject]**](GenresResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.genres_multi_resource_data_document import GenresMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of GenresMultiResourceDataDocument from a JSON string
genres_multi_resource_data_document_instance = GenresMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(GenresMultiResourceDataDocument.to_json())

# convert the object into a dict
genres_multi_resource_data_document_dict = genres_multi_resource_data_document_instance.to_dict()
# create an instance of GenresMultiResourceDataDocument from a dict
genres_multi_resource_data_document_from_dict = GenresMultiResourceDataDocument.from_dict(genres_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


