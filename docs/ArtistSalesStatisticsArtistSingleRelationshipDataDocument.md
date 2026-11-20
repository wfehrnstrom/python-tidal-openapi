# ArtistSalesStatisticsArtistSingleRelationshipDataDocument

Target resource types: `artists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artist_sales_statistics_artist_single_relationship_data_document import ArtistSalesStatisticsArtistSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistSalesStatisticsArtistSingleRelationshipDataDocument from a JSON string
artist_sales_statistics_artist_single_relationship_data_document_instance = ArtistSalesStatisticsArtistSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistSalesStatisticsArtistSingleRelationshipDataDocument.to_json())

# convert the object into a dict
artist_sales_statistics_artist_single_relationship_data_document_dict = artist_sales_statistics_artist_single_relationship_data_document_instance.to_dict()
# create an instance of ArtistSalesStatisticsArtistSingleRelationshipDataDocument from a dict
artist_sales_statistics_artist_single_relationship_data_document_from_dict = ArtistSalesStatisticsArtistSingleRelationshipDataDocument.from_dict(artist_sales_statistics_artist_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


