# VideosArtistsMultiRelationshipDataDocument

Target resource types: `artists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.videos_artists_multi_relationship_data_document import VideosArtistsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of VideosArtistsMultiRelationshipDataDocument from a JSON string
videos_artists_multi_relationship_data_document_instance = VideosArtistsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(VideosArtistsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
videos_artists_multi_relationship_data_document_dict = videos_artists_multi_relationship_data_document_instance.to_dict()
# create an instance of VideosArtistsMultiRelationshipDataDocument from a dict
videos_artists_multi_relationship_data_document_from_dict = VideosArtistsMultiRelationshipDataDocument.from_dict(videos_artists_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


