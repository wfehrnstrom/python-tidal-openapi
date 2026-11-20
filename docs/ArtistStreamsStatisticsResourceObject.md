# ArtistStreamsStatisticsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ArtistStreamsStatisticsAttributes**](ArtistStreamsStatisticsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**ArtistStreamsStatisticsRelationships**](ArtistStreamsStatisticsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.artist_streams_statistics_resource_object import ArtistStreamsStatisticsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistStreamsStatisticsResourceObject from a JSON string
artist_streams_statistics_resource_object_instance = ArtistStreamsStatisticsResourceObject.from_json(json)
# print the JSON string representation of the object
print(ArtistStreamsStatisticsResourceObject.to_json())

# convert the object into a dict
artist_streams_statistics_resource_object_dict = artist_streams_statistics_resource_object_instance.to_dict()
# create an instance of ArtistStreamsStatisticsResourceObject from a dict
artist_streams_statistics_resource_object_from_dict = ArtistStreamsStatisticsResourceObject.from_dict(artist_streams_statistics_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


