# AlbumsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | **str** | Access type | [optional] 
**ai** | **bool** | Whether the album is AI-generated | [optional] 
**album_type** | **str** | Album type | 
**availability** | **List[str]** | Available usage for this album. Deprecated: use &#39;usageRules&#39; instead. This field will be removed in a future version. | [optional] 
**barcode_id** | **str** |  | 
**copyright** | [**Copyright**](Copyright.md) |  | [optional] 
**created_at** | **datetime** | Datetime of album creation (ISO 8601) | [optional] 
**duration** | **str** | Duration (ISO 8601) | 
**explicit** | **bool** | Explicit content | 
**external_links** | [**List[ExternalLink]**](ExternalLink.md) | Album links external to TIDAL API | [optional] 
**media_tags** | **List[str]** |  | 
**number_of_items** | **int** | Number of items in album | 
**number_of_volumes** | **int** | Number of volumes | 
**popularity** | **float** | Popularity (0.0 - 1.0) | 
**published** | **bool** | Whether the album is published and available to everyone. Present only for uploaded albums. | [optional] 
**release_date** | **date** | Release date (ISO-8601) | [optional] 
**title** | **str** | Album title | 
**type** | **str** | Album type. Deprecated: use &#39;albumType&#39; instead. This field will be removed in a future version. | [optional] 
**version** | **str** | Album version | [optional] 

## Example

```python
from tidal.models.albums_attributes import AlbumsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsAttributes from a JSON string
albums_attributes_instance = AlbumsAttributes.from_json(json)
# print the JSON string representation of the object
print(AlbumsAttributes.to_json())

# convert the object into a dict
albums_attributes_dict = albums_attributes_instance.to_dict()
# create an instance of AlbumsAttributes from a dict
albums_attributes_from_dict = AlbumsAttributes.from_dict(albums_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


