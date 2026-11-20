# ViewerContextsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_effective_role** | [**EffectiveRole**](EffectiveRole.md) |  | [optional] 
**has_in_collection** | **object** | The viewer has the original subject in their normal collection. Present as an empty object when known present, otherwise omitted. Includes owned and saved playlists and saved mixes across folders; excludes Save for Later. | [optional] 
**has_purchased** | **object** | The viewer has a current qualifying purchase entitlement. Includes a track covered by its purchased album; excludes subscription access and free downloads. Reserved; not currently populated and omitted from responses. Omission does not indicate that the relation is absent. | [optional] 
**has_saved_for_later** | **object** | The viewer has saved the subject for later. Reserved; not currently populated and omitted from responses. Omission does not indicate that the relation is absent. | [optional] 
**is_followed_by** | **object** | The viewer is followed by the subject. Reserved; not currently populated and omitted from responses. Omission does not indicate that the relation is absent. | [optional] 
**is_following** | **object** | The viewer follows the subject. Reserved; not currently populated and omitted from responses. Omission does not indicate that the relation is absent. | [optional] 

## Example

```python
from tidal.models.viewer_contexts_attributes import ViewerContextsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ViewerContextsAttributes from a JSON string
viewer_contexts_attributes_instance = ViewerContextsAttributes.from_json(json)
# print the JSON string representation of the object
print(ViewerContextsAttributes.to_json())

# convert the object into a dict
viewer_contexts_attributes_dict = viewer_contexts_attributes_instance.to_dict()
# create an instance of ViewerContextsAttributes from a dict
viewer_contexts_attributes_from_dict = ViewerContextsAttributes.from_dict(viewer_contexts_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


