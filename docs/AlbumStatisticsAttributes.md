# AlbumStatisticsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_sales** | **int** | Number of sales | [optional] 
**total_playbacks** | **int** | Total playbacks | 
**unique_listeners** | **int** | Unique listeners | 

## Example

```python
from tidal.models.album_statistics_attributes import AlbumStatisticsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumStatisticsAttributes from a JSON string
album_statistics_attributes_instance = AlbumStatisticsAttributes.from_json(json)
# print the JSON string representation of the object
print(AlbumStatisticsAttributes.to_json())

# convert the object into a dict
album_statistics_attributes_dict = album_statistics_attributes_instance.to_dict()
# create an instance of AlbumStatisticsAttributes from a dict
album_statistics_attributes_from_dict = AlbumStatisticsAttributes.from_dict(album_statistics_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


