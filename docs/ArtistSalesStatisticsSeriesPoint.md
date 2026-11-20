# ArtistSalesStatisticsSeriesPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | First day of the bucket | 
**downloads_amount** | **str** | Amount in the currency&#39;s major units | 
**merch_amount** | **str** | Amount in the currency&#39;s major units | 

## Example

```python
from tidal.models.artist_sales_statistics_series_point import ArtistSalesStatisticsSeriesPoint

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistSalesStatisticsSeriesPoint from a JSON string
artist_sales_statistics_series_point_instance = ArtistSalesStatisticsSeriesPoint.from_json(json)
# print the JSON string representation of the object
print(ArtistSalesStatisticsSeriesPoint.to_json())

# convert the object into a dict
artist_sales_statistics_series_point_dict = artist_sales_statistics_series_point_instance.to_dict()
# create an instance of ArtistSalesStatisticsSeriesPoint from a dict
artist_sales_statistics_series_point_from_dict = ArtistSalesStatisticsSeriesPoint.from_dict(artist_sales_statistics_series_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


