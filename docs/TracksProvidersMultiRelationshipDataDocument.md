# TracksProvidersMultiRelationshipDataDocument

Target resource types: `providers`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.tracks_providers_multi_relationship_data_document import TracksProvidersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TracksProvidersMultiRelationshipDataDocument from a JSON string
tracks_providers_multi_relationship_data_document_instance = TracksProvidersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(TracksProvidersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
tracks_providers_multi_relationship_data_document_dict = tracks_providers_multi_relationship_data_document_instance.to_dict()
# create an instance of TracksProvidersMultiRelationshipDataDocument from a dict
tracks_providers_multi_relationship_data_document_from_dict = TracksProvidersMultiRelationshipDataDocument.from_dict(tracks_providers_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


