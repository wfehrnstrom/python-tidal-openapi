# TracksReplacementSingleRelationshipDataDocument

Target resource types: `tracks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TracksReplacementResourceIdentifier**](TracksReplacementResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.tracks_replacement_single_relationship_data_document import TracksReplacementSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TracksReplacementSingleRelationshipDataDocument from a JSON string
tracks_replacement_single_relationship_data_document_instance = TracksReplacementSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(TracksReplacementSingleRelationshipDataDocument.to_json())

# convert the object into a dict
tracks_replacement_single_relationship_data_document_dict = tracks_replacement_single_relationship_data_document_instance.to_dict()
# create an instance of TracksReplacementSingleRelationshipDataDocument from a dict
tracks_replacement_single_relationship_data_document_from_dict = TracksReplacementSingleRelationshipDataDocument.from_dict(tracks_replacement_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


