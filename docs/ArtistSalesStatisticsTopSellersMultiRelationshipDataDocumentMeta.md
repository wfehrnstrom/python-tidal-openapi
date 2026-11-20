# ArtistSalesStatisticsTopSellersMultiRelationshipDataDocumentMeta

status is the status of the sales statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency of netSalesAmount. Present when status is OK | [optional] 
**status** | **str** | Status of sales statistics. NOT_SET_UP: the artist has not set up sales. UNAVAILABLE: not available at the moment | 

## Example

```python
from tidal.models.artist_sales_statistics_top_sellers_multi_relationship_data_document_meta import ArtistSalesStatisticsTopSellersMultiRelationshipDataDocumentMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistSalesStatisticsTopSellersMultiRelationshipDataDocumentMeta from a JSON string
artist_sales_statistics_top_sellers_multi_relationship_data_document_meta_instance = ArtistSalesStatisticsTopSellersMultiRelationshipDataDocumentMeta.from_json(json)
# print the JSON string representation of the object
print(ArtistSalesStatisticsTopSellersMultiRelationshipDataDocumentMeta.to_json())

# convert the object into a dict
artist_sales_statistics_top_sellers_multi_relationship_data_document_meta_dict = artist_sales_statistics_top_sellers_multi_relationship_data_document_meta_instance.to_dict()
# create an instance of ArtistSalesStatisticsTopSellersMultiRelationshipDataDocumentMeta from a dict
artist_sales_statistics_top_sellers_multi_relationship_data_document_meta_from_dict = ArtistSalesStatisticsTopSellersMultiRelationshipDataDocumentMeta.from_dict(artist_sales_statistics_top_sellers_multi_relationship_data_document_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


