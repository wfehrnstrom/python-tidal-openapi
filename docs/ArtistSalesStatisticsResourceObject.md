# ArtistSalesStatisticsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ArtistSalesStatisticsAttributes**](ArtistSalesStatisticsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**ArtistSalesStatisticsRelationships**](ArtistSalesStatisticsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.artist_sales_statistics_resource_object import ArtistSalesStatisticsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistSalesStatisticsResourceObject from a JSON string
artist_sales_statistics_resource_object_instance = ArtistSalesStatisticsResourceObject.from_json(json)
# print the JSON string representation of the object
print(ArtistSalesStatisticsResourceObject.to_json())

# convert the object into a dict
artist_sales_statistics_resource_object_dict = artist_sales_statistics_resource_object_instance.to_dict()
# create an instance of ArtistSalesStatisticsResourceObject from a dict
artist_sales_statistics_resource_object_from_dict = ArtistSalesStatisticsResourceObject.from_dict(artist_sales_statistics_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


