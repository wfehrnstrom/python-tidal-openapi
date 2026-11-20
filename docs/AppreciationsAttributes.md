# AppreciationsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Time when the appreciation was created | 

## Example

```python
from tidal.models.appreciations_attributes import AppreciationsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of AppreciationsAttributes from a JSON string
appreciations_attributes_instance = AppreciationsAttributes.from_json(json)
# print the JSON string representation of the object
print(AppreciationsAttributes.to_json())

# convert the object into a dict
appreciations_attributes_dict = appreciations_attributes_instance.to_dict()
# create an instance of AppreciationsAttributes from a dict
appreciations_attributes_from_dict = AppreciationsAttributes.from_dict(appreciations_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


