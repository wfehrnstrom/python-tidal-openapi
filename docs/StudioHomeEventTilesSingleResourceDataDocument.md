# StudioHomeEventTilesSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**StudioHomeEventTilesResourceObject**](StudioHomeEventTilesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.studio_home_event_tiles_single_resource_data_document import StudioHomeEventTilesSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of StudioHomeEventTilesSingleResourceDataDocument from a JSON string
studio_home_event_tiles_single_resource_data_document_instance = StudioHomeEventTilesSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(StudioHomeEventTilesSingleResourceDataDocument.to_json())

# convert the object into a dict
studio_home_event_tiles_single_resource_data_document_dict = studio_home_event_tiles_single_resource_data_document_instance.to_dict()
# create an instance of StudioHomeEventTilesSingleResourceDataDocument from a dict
studio_home_event_tiles_single_resource_data_document_from_dict = StudioHomeEventTilesSingleResourceDataDocument.from_dict(studio_home_event_tiles_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


