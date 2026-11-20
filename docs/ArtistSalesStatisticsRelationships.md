# ArtistSalesStatisticsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artist** | [**ArtistSalesStatisticsArtistSingleRelationshipDataDocument**](ArtistSalesStatisticsArtistSingleRelationshipDataDocument.md) |  | [optional] 
**top_sellers** | [**ArtistSalesStatisticsTopSellersMultiRelationshipDataDocument**](ArtistSalesStatisticsTopSellersMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.artist_sales_statistics_relationships import ArtistSalesStatisticsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistSalesStatisticsRelationships from a JSON string
artist_sales_statistics_relationships_instance = ArtistSalesStatisticsRelationships.from_json(json)
# print the JSON string representation of the object
print(ArtistSalesStatisticsRelationships.to_json())

# convert the object into a dict
artist_sales_statistics_relationships_dict = artist_sales_statistics_relationships_instance.to_dict()
# create an instance of ArtistSalesStatisticsRelationships from a dict
artist_sales_statistics_relationships_from_dict = ArtistSalesStatisticsRelationships.from_dict(artist_sales_statistics_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


