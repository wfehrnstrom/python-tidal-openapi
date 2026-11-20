# VideoManifestsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**VideoManifestsResourceObject**](VideoManifestsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.video_manifests_single_resource_data_document import VideoManifestsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of VideoManifestsSingleResourceDataDocument from a JSON string
video_manifests_single_resource_data_document_instance = VideoManifestsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(VideoManifestsSingleResourceDataDocument.to_json())

# convert the object into a dict
video_manifests_single_resource_data_document_dict = video_manifests_single_resource_data_document_instance.to_dict()
# create an instance of VideoManifestsSingleResourceDataDocument from a dict
video_manifests_single_resource_data_document_from_dict = VideoManifestsSingleResourceDataDocument.from_dict(video_manifests_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


