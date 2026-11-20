# ChangeEventStreamsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_stream_link** | [**LinkObject**](LinkObject.md) |  | 

## Example

```python
from tidal.models.change_event_streams_attributes import ChangeEventStreamsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeEventStreamsAttributes from a JSON string
change_event_streams_attributes_instance = ChangeEventStreamsAttributes.from_json(json)
# print the JSON string representation of the object
print(ChangeEventStreamsAttributes.to_json())

# convert the object into a dict
change_event_streams_attributes_dict = change_event_streams_attributes_instance.to_dict()
# create an instance of ChangeEventStreamsAttributes from a dict
change_event_streams_attributes_from_dict = ChangeEventStreamsAttributes.from_dict(change_event_streams_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


