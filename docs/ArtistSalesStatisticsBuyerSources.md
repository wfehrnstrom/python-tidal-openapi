# ArtistSalesStatisticsBuyerSources

Where buyers came from. items is present exactly when status is OK, and an empty items is a measured empty result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ArtistSalesStatisticsBuyerSourceShare]**](ArtistSalesStatisticsBuyerSourceShare.md) |  | [optional] 
**status** | **str** | Status of artist statistics that may be withheld. OK: the data is present. SUPPRESSED: withheld because too few people are counted to show it. UNAVAILABLE: not available at the moment | 

## Example

```python
from tidal.models.artist_sales_statistics_buyer_sources import ArtistSalesStatisticsBuyerSources

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistSalesStatisticsBuyerSources from a JSON string
artist_sales_statistics_buyer_sources_instance = ArtistSalesStatisticsBuyerSources.from_json(json)
# print the JSON string representation of the object
print(ArtistSalesStatisticsBuyerSources.to_json())

# convert the object into a dict
artist_sales_statistics_buyer_sources_dict = artist_sales_statistics_buyer_sources_instance.to_dict()
# create an instance of ArtistSalesStatisticsBuyerSources from a dict
artist_sales_statistics_buyer_sources_from_dict = ArtistSalesStatisticsBuyerSources.from_dict(artist_sales_statistics_buyer_sources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


