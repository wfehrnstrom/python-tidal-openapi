# VideosSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**VideosResourceObject**](VideosResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.videos_single_resource_data_document import VideosSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of VideosSingleResourceDataDocument from a JSON string
videos_single_resource_data_document_instance = VideosSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(VideosSingleResourceDataDocument.to_json())

# convert the object into a dict
videos_single_resource_data_document_dict = videos_single_resource_data_document_instance.to_dict()
# create an instance of VideosSingleResourceDataDocument from a dict
videos_single_resource_data_document_from_dict = VideosSingleResourceDataDocument.from_dict(videos_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


