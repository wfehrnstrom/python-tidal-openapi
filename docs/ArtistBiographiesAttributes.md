# ArtistBiographiesAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**editable** | **bool** | Boolean to indicate if the biography is editable (source &#x3D; tidal or artist) | 
**source** | **str** | Source the biography is coming from | [optional] 
**text** | **str** | Artist biography | 

## Example

```python
from tidal.models.artist_biographies_attributes import ArtistBiographiesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistBiographiesAttributes from a JSON string
artist_biographies_attributes_instance = ArtistBiographiesAttributes.from_json(json)
# print the JSON string representation of the object
print(ArtistBiographiesAttributes.to_json())

# convert the object into a dict
artist_biographies_attributes_dict = artist_biographies_attributes_instance.to_dict()
# create an instance of ArtistBiographiesAttributes from a dict
artist_biographies_attributes_from_dict = ArtistBiographiesAttributes.from_dict(artist_biographies_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


