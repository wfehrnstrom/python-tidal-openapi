# ArtistSalesStatisticsBuyerSourceShare


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share_of_orders** | **float** | Share of orders | 
**source** | **str** | Where buyers came from. UNKNOWN: a source this API does not know | 

## Example

```python
from tidal.models.artist_sales_statistics_buyer_source_share import ArtistSalesStatisticsBuyerSourceShare

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistSalesStatisticsBuyerSourceShare from a JSON string
artist_sales_statistics_buyer_source_share_instance = ArtistSalesStatisticsBuyerSourceShare.from_json(json)
# print the JSON string representation of the object
print(ArtistSalesStatisticsBuyerSourceShare.to_json())

# convert the object into a dict
artist_sales_statistics_buyer_source_share_dict = artist_sales_statistics_buyer_source_share_instance.to_dict()
# create an instance of ArtistSalesStatisticsBuyerSourceShare from a dict
artist_sales_statistics_buyer_source_share_from_dict = ArtistSalesStatisticsBuyerSourceShare.from_dict(artist_sales_statistics_buyer_source_share_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


