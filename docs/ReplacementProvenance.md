# ReplacementProvenance

Relationship replacement projection provenance. ORIGINAL retains the requested identifier as the applicable resource, REPLACED projects another identifier, and NOT_REPLACED retains the requested identifier because no applicable replacement exists.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original** | [**ReplacementOriginalIdentifier**](ReplacementOriginalIdentifier.md) |  | [optional] 
**status** | **str** |  | 

## Example

```python
from tidal.models.replacement_provenance import ReplacementProvenance

# TODO update the JSON string below
json = "{}"
# create an instance of ReplacementProvenance from a JSON string
replacement_provenance_instance = ReplacementProvenance.from_json(json)
# print the JSON string representation of the object
print(ReplacementProvenance.to_json())

# convert the object into a dict
replacement_provenance_dict = replacement_provenance_instance.to_dict()
# create an instance of ReplacementProvenance from a dict
replacement_provenance_from_dict = ReplacementProvenance.from_dict(replacement_provenance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


