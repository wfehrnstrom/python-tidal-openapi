# ArtistSalesStatisticsTopSellersResourceIdentifierMeta

netSalesAmount is the product's net sales in the window, in the relationship's currency

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | What was sold. UNKNOWN: a kind this API does not know | 
**net_sales_amount** | **str** | Amount in the currency&#39;s major units | 
**rank** | **int** | 1-based position in the producer&#39;s ranking. Products this API cannot link are left out, so ranks can have gaps | 
**replacement** | [**ReplacementProvenance**](ReplacementProvenance.md) |  | [optional] 
**units** | **int** | Units sold in the window | 

## Example

```python
from tidal.models.artist_sales_statistics_top_sellers_resource_identifier_meta import ArtistSalesStatisticsTopSellersResourceIdentifierMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistSalesStatisticsTopSellersResourceIdentifierMeta from a JSON string
artist_sales_statistics_top_sellers_resource_identifier_meta_instance = ArtistSalesStatisticsTopSellersResourceIdentifierMeta.from_json(json)
# print the JSON string representation of the object
print(ArtistSalesStatisticsTopSellersResourceIdentifierMeta.to_json())

# convert the object into a dict
artist_sales_statistics_top_sellers_resource_identifier_meta_dict = artist_sales_statistics_top_sellers_resource_identifier_meta_instance.to_dict()
# create an instance of ArtistSalesStatisticsTopSellersResourceIdentifierMeta from a dict
artist_sales_statistics_top_sellers_resource_identifier_meta_from_dict = ArtistSalesStatisticsTopSellersResourceIdentifierMeta.from_dict(artist_sales_statistics_top_sellers_resource_identifier_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


