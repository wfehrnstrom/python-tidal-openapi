# ArtistSalesStatisticsNetSales

Sold minus refunded in the window. previousAmount is the same for the previous window of the same length and is absent when there is no earlier window to compare with

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Amount in the currency&#39;s major units | 
**previous_amount** | **str** | Amount in the currency&#39;s major units | [optional] 

## Example

```python
from tidal.models.artist_sales_statistics_net_sales import ArtistSalesStatisticsNetSales

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistSalesStatisticsNetSales from a JSON string
artist_sales_statistics_net_sales_instance = ArtistSalesStatisticsNetSales.from_json(json)
# print the JSON string representation of the object
print(ArtistSalesStatisticsNetSales.to_json())

# convert the object into a dict
artist_sales_statistics_net_sales_dict = artist_sales_statistics_net_sales_instance.to_dict()
# create an instance of ArtistSalesStatisticsNetSales from a dict
artist_sales_statistics_net_sales_from_dict = ArtistSalesStatisticsNetSales.from_dict(artist_sales_statistics_net_sales_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


