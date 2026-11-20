# ArtistSalesStatisticsSeries

Net sales per bucket

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_period** | [**ArtistStatisticsBucketPeriod**](ArtistStatisticsBucketPeriod.md) |  | [optional] 
**points** | [**List[ArtistSalesStatisticsSeriesPoint]**](ArtistSalesStatisticsSeriesPoint.md) |  | 

## Example

```python
from tidal.models.artist_sales_statistics_series import ArtistSalesStatisticsSeries

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistSalesStatisticsSeries from a JSON string
artist_sales_statistics_series_instance = ArtistSalesStatisticsSeries.from_json(json)
# print the JSON string representation of the object
print(ArtistSalesStatisticsSeries.to_json())

# convert the object into a dict
artist_sales_statistics_series_dict = artist_sales_statistics_series_instance.to_dict()
# create an instance of ArtistSalesStatisticsSeries from a dict
artist_sales_statistics_series_from_dict = ArtistSalesStatisticsSeries.from_dict(artist_sales_statistics_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


