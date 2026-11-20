# AlbumStatisticsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AlbumStatisticsResourceObject**](AlbumStatisticsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.album_statistics_single_resource_data_document import AlbumStatisticsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumStatisticsSingleResourceDataDocument from a JSON string
album_statistics_single_resource_data_document_instance = AlbumStatisticsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(AlbumStatisticsSingleResourceDataDocument.to_json())

# convert the object into a dict
album_statistics_single_resource_data_document_dict = album_statistics_single_resource_data_document_instance.to_dict()
# create an instance of AlbumStatisticsSingleResourceDataDocument from a dict
album_statistics_single_resource_data_document_from_dict = AlbumStatisticsSingleResourceDataDocument.from_dict(album_statistics_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


