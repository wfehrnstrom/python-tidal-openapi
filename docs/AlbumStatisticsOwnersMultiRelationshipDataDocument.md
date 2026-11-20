# AlbumStatisticsOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.album_statistics_owners_multi_relationship_data_document import AlbumStatisticsOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumStatisticsOwnersMultiRelationshipDataDocument from a JSON string
album_statistics_owners_multi_relationship_data_document_instance = AlbumStatisticsOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(AlbumStatisticsOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
album_statistics_owners_multi_relationship_data_document_dict = album_statistics_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of AlbumStatisticsOwnersMultiRelationshipDataDocument from a dict
album_statistics_owners_multi_relationship_data_document_from_dict = AlbumStatisticsOwnersMultiRelationshipDataDocument.from_dict(album_statistics_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


