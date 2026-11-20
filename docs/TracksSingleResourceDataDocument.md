# TracksSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TracksResourceObject**](TracksResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.tracks_single_resource_data_document import TracksSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TracksSingleResourceDataDocument from a JSON string
tracks_single_resource_data_document_instance = TracksSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(TracksSingleResourceDataDocument.to_json())

# convert the object into a dict
tracks_single_resource_data_document_dict = tracks_single_resource_data_document_instance.to_dict()
# create an instance of TracksSingleResourceDataDocument from a dict
tracks_single_resource_data_document_from_dict = TracksSingleResourceDataDocument.from_dict(tracks_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


