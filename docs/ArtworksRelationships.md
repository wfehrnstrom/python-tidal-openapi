# ArtworksRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owners** | [**ArtworksOwnersMultiRelationshipDataDocument**](ArtworksOwnersMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.artworks_relationships import ArtworksRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ArtworksRelationships from a JSON string
artworks_relationships_instance = ArtworksRelationships.from_json(json)
# print the JSON string representation of the object
print(ArtworksRelationships.to_json())

# convert the object into a dict
artworks_relationships_dict = artworks_relationships_instance.to_dict()
# create an instance of ArtworksRelationships from a dict
artworks_relationships_from_dict = ArtworksRelationships.from_dict(artworks_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


