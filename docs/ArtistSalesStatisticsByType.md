# ArtistSalesStatisticsByType

Net sales by product type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**downloads_amount** | **str** | Amount in the currency&#39;s major units | 
**merch_amount** | **str** | Amount in the currency&#39;s major units | 

## Example

```python
from tidal.models.artist_sales_statistics_by_type import ArtistSalesStatisticsByType

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistSalesStatisticsByType from a JSON string
artist_sales_statistics_by_type_instance = ArtistSalesStatisticsByType.from_json(json)
# print the JSON string representation of the object
print(ArtistSalesStatisticsByType.to_json())

# convert the object into a dict
artist_sales_statistics_by_type_dict = artist_sales_statistics_by_type_instance.to_dict()
# create an instance of ArtistSalesStatisticsByType from a dict
artist_sales_statistics_by_type_from_dict = ArtistSalesStatisticsByType.from_dict(artist_sales_statistics_by_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


