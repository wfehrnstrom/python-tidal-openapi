# ReactionsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Datetime of the reaction creation (ISO 8601) | 
**emoji** | **str** | The type of reaction representing an emoji | 
**end_offset** | **str** | End offset of a source-file section. Omitted for a point or whole-subject reaction. | [optional] 
**start_offset** | **str** | Source-file offset (ISO 8601 duration). Omitted for the whole subject. | [optional] 

## Example

```python
from tidal.models.reactions_attributes import ReactionsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ReactionsAttributes from a JSON string
reactions_attributes_instance = ReactionsAttributes.from_json(json)
# print the JSON string representation of the object
print(ReactionsAttributes.to_json())

# convert the object into a dict
reactions_attributes_dict = reactions_attributes_instance.to_dict()
# create an instance of ReactionsAttributes from a dict
reactions_attributes_from_dict = ReactionsAttributes.from_dict(reactions_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


