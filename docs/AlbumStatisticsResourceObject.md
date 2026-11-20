# AlbumStatisticsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**AlbumStatisticsAttributes**](AlbumStatisticsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**AlbumStatisticsRelationships**](AlbumStatisticsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.album_statistics_resource_object import AlbumStatisticsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumStatisticsResourceObject from a JSON string
album_statistics_resource_object_instance = AlbumStatisticsResourceObject.from_json(json)
# print the JSON string representation of the object
print(AlbumStatisticsResourceObject.to_json())

# convert the object into a dict
album_statistics_resource_object_dict = album_statistics_resource_object_instance.to_dict()
# create an instance of AlbumStatisticsResourceObject from a dict
album_statistics_resource_object_from_dict = AlbumStatisticsResourceObject.from_dict(album_statistics_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


