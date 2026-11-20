# ArtistSalesStatisticsTopSellersResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**ArtistSalesStatisticsTopSellersResourceIdentifierMeta**](ArtistSalesStatisticsTopSellersResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.artist_sales_statistics_top_sellers_resource_identifier import ArtistSalesStatisticsTopSellersResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistSalesStatisticsTopSellersResourceIdentifier from a JSON string
artist_sales_statistics_top_sellers_resource_identifier_instance = ArtistSalesStatisticsTopSellersResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(ArtistSalesStatisticsTopSellersResourceIdentifier.to_json())

# convert the object into a dict
artist_sales_statistics_top_sellers_resource_identifier_dict = artist_sales_statistics_top_sellers_resource_identifier_instance.to_dict()
# create an instance of ArtistSalesStatisticsTopSellersResourceIdentifier from a dict
artist_sales_statistics_top_sellers_resource_identifier_from_dict = ArtistSalesStatisticsTopSellersResourceIdentifier.from_dict(artist_sales_statistics_top_sellers_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


