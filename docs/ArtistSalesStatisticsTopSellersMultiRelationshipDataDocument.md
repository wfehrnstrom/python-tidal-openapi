# ArtistSalesStatisticsTopSellersMultiRelationshipDataDocument

Target resource types: `albums`, `tracks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ArtistSalesStatisticsTopSellersResourceIdentifier]**](ArtistSalesStatisticsTopSellersResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 
**meta** | [**ArtistSalesStatisticsTopSellersMultiRelationshipDataDocumentMeta**](ArtistSalesStatisticsTopSellersMultiRelationshipDataDocumentMeta.md) |  | [optional] 

## Example

```python
from tidal.models.artist_sales_statistics_top_sellers_multi_relationship_data_document import ArtistSalesStatisticsTopSellersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistSalesStatisticsTopSellersMultiRelationshipDataDocument from a JSON string
artist_sales_statistics_top_sellers_multi_relationship_data_document_instance = ArtistSalesStatisticsTopSellersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistSalesStatisticsTopSellersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
artist_sales_statistics_top_sellers_multi_relationship_data_document_dict = artist_sales_statistics_top_sellers_multi_relationship_data_document_instance.to_dict()
# create an instance of ArtistSalesStatisticsTopSellersMultiRelationshipDataDocument from a dict
artist_sales_statistics_top_sellers_multi_relationship_data_document_from_dict = ArtistSalesStatisticsTopSellersMultiRelationshipDataDocument.from_dict(artist_sales_statistics_top_sellers_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


