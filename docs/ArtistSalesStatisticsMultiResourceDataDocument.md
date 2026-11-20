# ArtistSalesStatisticsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ArtistSalesStatisticsResourceObject]**](ArtistSalesStatisticsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artist_sales_statistics_multi_resource_data_document import ArtistSalesStatisticsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistSalesStatisticsMultiResourceDataDocument from a JSON string
artist_sales_statistics_multi_resource_data_document_instance = ArtistSalesStatisticsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistSalesStatisticsMultiResourceDataDocument.to_json())

# convert the object into a dict
artist_sales_statistics_multi_resource_data_document_dict = artist_sales_statistics_multi_resource_data_document_instance.to_dict()
# create an instance of ArtistSalesStatisticsMultiResourceDataDocument from a dict
artist_sales_statistics_multi_resource_data_document_from_dict = ArtistSalesStatisticsMultiResourceDataDocument.from_dict(artist_sales_statistics_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


