# TrackStatisticsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TrackStatisticsResourceObject**](TrackStatisticsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.track_statistics_single_resource_data_document import TrackStatisticsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TrackStatisticsSingleResourceDataDocument from a JSON string
track_statistics_single_resource_data_document_instance = TrackStatisticsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(TrackStatisticsSingleResourceDataDocument.to_json())

# convert the object into a dict
track_statistics_single_resource_data_document_dict = track_statistics_single_resource_data_document_instance.to_dict()
# create an instance of TrackStatisticsSingleResourceDataDocument from a dict
track_statistics_single_resource_data_document_from_dict = TrackStatisticsSingleResourceDataDocument.from_dict(track_statistics_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


