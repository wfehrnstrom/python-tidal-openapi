# TrackManifestsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TrackManifestsResourceObject**](TrackManifestsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.track_manifests_single_resource_data_document import TrackManifestsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TrackManifestsSingleResourceDataDocument from a JSON string
track_manifests_single_resource_data_document_instance = TrackManifestsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(TrackManifestsSingleResourceDataDocument.to_json())

# convert the object into a dict
track_manifests_single_resource_data_document_dict = track_manifests_single_resource_data_document_instance.to_dict()
# create an instance of TrackManifestsSingleResourceDataDocument from a dict
track_manifests_single_resource_data_document_from_dict = TrackManifestsSingleResourceDataDocument.from_dict(track_manifests_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


