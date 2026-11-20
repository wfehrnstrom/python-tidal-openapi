# MissingTermsMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**missing_terms_types** | **List[str]** |  | 

## Example

```python
from tidal.models.missing_terms_meta import MissingTermsMeta

# TODO update the JSON string below
json = "{}"
# create an instance of MissingTermsMeta from a JSON string
missing_terms_meta_instance = MissingTermsMeta.from_json(json)
# print the JSON string representation of the object
print(MissingTermsMeta.to_json())

# convert the object into a dict
missing_terms_meta_dict = missing_terms_meta_instance.to_dict()
# create an instance of MissingTermsMeta from a dict
missing_terms_meta_from_dict = MissingTermsMeta.from_dict(missing_terms_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


