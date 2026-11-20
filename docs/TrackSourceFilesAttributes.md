# TrackSourceFilesAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_link** | [**LinkObject**](LinkObject.md) |  | [optional] 
**md5_hash** | **str** | MD5 hash of file to be uploaded | [optional] 
**processing** | [**SourceProcessing**](SourceProcessing.md) |  | [optional] 
**size** | **int** | File size of the track in bytes | [optional] 
**status** | [**FileStatus**](FileStatus.md) |  | [optional] 
**upload_link** | [**FileUploadLink**](FileUploadLink.md) |  | [optional] 

## Example

```python
from tidal.models.track_source_files_attributes import TrackSourceFilesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of TrackSourceFilesAttributes from a JSON string
track_source_files_attributes_instance = TrackSourceFilesAttributes.from_json(json)
# print the JSON string representation of the object
print(TrackSourceFilesAttributes.to_json())

# convert the object into a dict
track_source_files_attributes_dict = track_source_files_attributes_instance.to_dict()
# create an instance of TrackSourceFilesAttributes from a dict
track_source_files_attributes_from_dict = TrackSourceFilesAttributes.from_dict(track_source_files_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


