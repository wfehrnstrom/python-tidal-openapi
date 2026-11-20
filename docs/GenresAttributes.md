# GenresAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**genre_name** | **str** | Genre name | 

## Example

```python
from tidal.models.genres_attributes import GenresAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of GenresAttributes from a JSON string
genres_attributes_instance = GenresAttributes.from_json(json)
# print the JSON string representation of the object
print(GenresAttributes.to_json())

# convert the object into a dict
genres_attributes_dict = genres_attributes_instance.to_dict()
# create an instance of GenresAttributes from a dict
genres_attributes_from_dict = GenresAttributes.from_dict(genres_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


