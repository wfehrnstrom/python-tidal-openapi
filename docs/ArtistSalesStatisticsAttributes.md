# ArtistSalesStatisticsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer_sources** | [**ArtistSalesStatisticsBuyerSources**](ArtistSalesStatisticsBuyerSources.md) |  | [optional] 
**by_type** | [**ArtistSalesStatisticsByType**](ArtistSalesStatisticsByType.md) |  | [optional] 
**currency** | **str** | Currency of every amount | [optional] 
**data_through** | **date** | Last day included in the underlying data | 
**end_date** | **date** | Last day of the window, inclusive | 
**items_sold** | **int** | Items sold in the window | [optional] 
**last_modified_at** | **datetime** | When these statistics were computed | 
**net_sales** | [**ArtistSalesStatisticsNetSales**](ArtistSalesStatisticsNetSales.md) |  | [optional] 
**orders** | **int** | Orders in the window | [optional] 
**refunds** | [**ArtistSalesStatisticsRefunds**](ArtistSalesStatisticsRefunds.md) |  | [optional] 
**series** | [**ArtistSalesStatisticsSeries**](ArtistSalesStatisticsSeries.md) |  | [optional] 
**start_date** | **date** | First day of the window | 
**status** | **str** | Status of sales statistics. NOT_SET_UP: the artist has not set up sales. UNAVAILABLE: not available at the moment | 
**window_period** | [**ArtistStatisticsWindowPeriod**](ArtistStatisticsWindowPeriod.md) |  | 

## Example

```python
from tidal.models.artist_sales_statistics_attributes import ArtistSalesStatisticsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistSalesStatisticsAttributes from a JSON string
artist_sales_statistics_attributes_instance = ArtistSalesStatisticsAttributes.from_json(json)
# print the JSON string representation of the object
print(ArtistSalesStatisticsAttributes.to_json())

# convert the object into a dict
artist_sales_statistics_attributes_dict = artist_sales_statistics_attributes_instance.to_dict()
# create an instance of ArtistSalesStatisticsAttributes from a dict
artist_sales_statistics_attributes_from_dict = ArtistSalesStatisticsAttributes.from_dict(artist_sales_statistics_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


