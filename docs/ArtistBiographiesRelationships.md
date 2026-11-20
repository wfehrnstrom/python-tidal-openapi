# ArtistBiographiesRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owners** | [**ArtistBiographiesOwnersMultiRelationshipDataDocument**](ArtistBiographiesOwnersMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.artist_biographies_relationships import ArtistBiographiesRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistBiographiesRelationships from a JSON string
artist_biographies_relationships_instance = ArtistBiographiesRelationships.from_json(json)
# print the JSON string representation of the object
print(ArtistBiographiesRelationships.to_json())

# convert the object into a dict
artist_biographies_relationships_dict = artist_biographies_relationships_instance.to_dict()
# create an instance of ArtistBiographiesRelationships from a dict
artist_biographies_relationships_from_dict = ArtistBiographiesRelationships.from_dict(artist_biographies_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


