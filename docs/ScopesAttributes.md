# ScopesAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent_text** | **str** | Text shown to the end user on the OAuth consent screen when this scope is requested. | [optional] 
**description** | **str** | Technical description of the scope. | 
**name** | **str** | Wire-format scope name as used in OAuth requests. | 
**required_access_tier** | **str** | Client access tier required to request this scope. A client whose access tier is at least this value can include the scope when initiating an OAuth flow. | 

## Example

```python
from tidal.models.scopes_attributes import ScopesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ScopesAttributes from a JSON string
scopes_attributes_instance = ScopesAttributes.from_json(json)
# print the JSON string representation of the object
print(ScopesAttributes.to_json())

# convert the object into a dict
scopes_attributes_dict = scopes_attributes_instance.to_dict()
# create an instance of ScopesAttributes from a dict
scopes_attributes_from_dict = ScopesAttributes.from_dict(scopes_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


