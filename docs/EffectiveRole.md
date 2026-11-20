# EffectiveRole

The viewer's effective role on the subject, from a grant or an implicit role such as an album's VIEWER through a grant on one of its tracks. Populated for owned albums, tracks and folders; omitted for other subjects. Share codes do not count.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | Effective role. | 

## Example

```python
from tidal.models.effective_role import EffectiveRole

# TODO update the JSON string below
json = "{}"
# create an instance of EffectiveRole from a JSON string
effective_role_instance = EffectiveRole.from_json(json)
# print the JSON string representation of the object
print(EffectiveRole.to_json())

# convert the object into a dict
effective_role_dict = effective_role_instance.to_dict()
# create an instance of EffectiveRole from a dict
effective_role_from_dict = EffectiveRole.from_dict(effective_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


