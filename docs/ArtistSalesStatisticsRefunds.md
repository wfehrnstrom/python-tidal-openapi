# ArtistSalesStatisticsRefunds

Refunds in the window. amount is the total refunded

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Amount in the currency&#39;s major units | 
**count** | **int** | Refunded orders | 

## Example

```python
from tidal.models.artist_sales_statistics_refunds import ArtistSalesStatisticsRefunds

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistSalesStatisticsRefunds from a JSON string
artist_sales_statistics_refunds_instance = ArtistSalesStatisticsRefunds.from_json(json)
# print the JSON string representation of the object
print(ArtistSalesStatisticsRefunds.to_json())

# convert the object into a dict
artist_sales_statistics_refunds_dict = artist_sales_statistics_refunds_instance.to_dict()
# create an instance of ArtistSalesStatisticsRefunds from a dict
artist_sales_statistics_refunds_from_dict = ArtistSalesStatisticsRefunds.from_dict(artist_sales_statistics_refunds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


