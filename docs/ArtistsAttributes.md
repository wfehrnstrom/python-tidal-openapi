# ArtistsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background_color** | **str** | Artist profile background colour override | [optional] 
**contributions_enabled** | **bool** | Is the artist enabled for contributions? | [optional] 
**contributions_sales_pitch** | **str** | Contributions sales pitch | [optional] 
**external_links** | [**List[ExternalLink]**](ExternalLink.md) | Artist links external to TIDAL API | [optional] 
**foreground_color** | **str** | Artist profile foreground colour override | [optional] 
**handle** | **str** | Artist handle | [optional] 
**name** | **str** | Artist name | 
**number_of_followers** | **int** | Number of users in the followers relationship | [optional] 
**number_of_following** | **int** | Number of artists in the following relationship | [optional] 
**owner_type** | **str** | Ownership type of the artist profile. LABEL: label-managed profile, USER: user-created profile, MIXED: claimed profile with both label and user content. May be null during rollout/backfill. | [optional] 
**popularity** | **float** | Artist popularity (0.0 - 1.0) | 
**spotlighted** | **bool** | Is the artist spotlighted? | [optional] 

## Example

```python
from tidal.models.artists_attributes import ArtistsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsAttributes from a JSON string
artists_attributes_instance = ArtistsAttributes.from_json(json)
# print the JSON string representation of the object
print(ArtistsAttributes.to_json())

# convert the object into a dict
artists_attributes_dict = artists_attributes_instance.to_dict()
# create an instance of ArtistsAttributes from a dict
artists_attributes_from_dict = ArtistsAttributes.from_dict(artists_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


