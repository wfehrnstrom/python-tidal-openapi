# TracksGenresMultiRelationshipDataDocument

Target resource types: `genres`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.tracks_genres_multi_relationship_data_document import TracksGenresMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TracksGenresMultiRelationshipDataDocument from a JSON string
tracks_genres_multi_relationship_data_document_instance = TracksGenresMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(TracksGenresMultiRelationshipDataDocument.to_json())

# convert the object into a dict
tracks_genres_multi_relationship_data_document_dict = tracks_genres_multi_relationship_data_document_instance.to_dict()
# create an instance of TracksGenresMultiRelationshipDataDocument from a dict
tracks_genres_multi_relationship_data_document_from_dict = TracksGenresMultiRelationshipDataDocument.from_dict(tracks_genres_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


