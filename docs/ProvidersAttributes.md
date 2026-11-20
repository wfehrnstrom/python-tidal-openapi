# ProvidersAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Provider name | 

## Example

```python
from tidal.models.providers_attributes import ProvidersAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ProvidersAttributes from a JSON string
providers_attributes_instance = ProvidersAttributes.from_json(json)
# print the JSON string representation of the object
print(ProvidersAttributes.to_json())

# convert the object into a dict
providers_attributes_dict = providers_attributes_instance.to_dict()
# create an instance of ProvidersAttributes from a dict
providers_attributes_from_dict = ProvidersAttributes.from_dict(providers_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


