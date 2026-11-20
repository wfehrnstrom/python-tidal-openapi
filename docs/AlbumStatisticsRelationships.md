# AlbumStatisticsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owners** | [**AlbumStatisticsOwnersMultiRelationshipDataDocument**](AlbumStatisticsOwnersMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.album_statistics_relationships import AlbumStatisticsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumStatisticsRelationships from a JSON string
album_statistics_relationships_instance = AlbumStatisticsRelationships.from_json(json)
# print the JSON string representation of the object
print(AlbumStatisticsRelationships.to_json())

# convert the object into a dict
album_statistics_relationships_dict = album_statistics_relationships_instance.to_dict()
# create an instance of AlbumStatisticsRelationships from a dict
album_statistics_relationships_from_dict = AlbumStatisticsRelationships.from_dict(album_statistics_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


