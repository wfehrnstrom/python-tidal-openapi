# ChangeEventStreamsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ChangeEventStreamsAttributes**](ChangeEventStreamsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.change_event_streams_resource_object import ChangeEventStreamsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeEventStreamsResourceObject from a JSON string
change_event_streams_resource_object_instance = ChangeEventStreamsResourceObject.from_json(json)
# print the JSON string representation of the object
print(ChangeEventStreamsResourceObject.to_json())

# convert the object into a dict
change_event_streams_resource_object_dict = change_event_streams_resource_object_instance.to_dict()
# create an instance of ChangeEventStreamsResourceObject from a dict
change_event_streams_resource_object_from_dict = ChangeEventStreamsResourceObject.from_dict(change_event_streams_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


