# PlaylistGenerationsBaseGenerationSingleRelationshipDataDocument

Target resource types: `playlistGenerations`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.playlist_generations_base_generation_single_relationship_data_document import PlaylistGenerationsBaseGenerationSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationsBaseGenerationSingleRelationshipDataDocument from a JSON string
playlist_generations_base_generation_single_relationship_data_document_instance = PlaylistGenerationsBaseGenerationSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationsBaseGenerationSingleRelationshipDataDocument.to_json())

# convert the object into a dict
playlist_generations_base_generation_single_relationship_data_document_dict = playlist_generations_base_generation_single_relationship_data_document_instance.to_dict()
# create an instance of PlaylistGenerationsBaseGenerationSingleRelationshipDataDocument from a dict
playlist_generations_base_generation_single_relationship_data_document_from_dict = PlaylistGenerationsBaseGenerationSingleRelationshipDataDocument.from_dict(playlist_generations_base_generation_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


