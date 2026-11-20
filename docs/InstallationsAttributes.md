# InstallationsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_provided_installation_id** | **str** | Client provided installation identifier | 
**name** | **str** | Human-readable name for the installation | 

## Example

```python
from tidal.models.installations_attributes import InstallationsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of InstallationsAttributes from a JSON string
installations_attributes_instance = InstallationsAttributes.from_json(json)
# print the JSON string representation of the object
print(InstallationsAttributes.to_json())

# convert the object into a dict
installations_attributes_dict = installations_attributes_instance.to_dict()
# create an instance of InstallationsAttributes from a dict
installations_attributes_from_dict = InstallationsAttributes.from_dict(installations_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


