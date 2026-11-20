# FileStatus

File status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_scanning_file_status** | **str** | Status of scanning the file for being AI-generated. Only present for file types that support AI scanning (e.g. track source files) and when a scanning status is available for the file; absent otherwise. | [optional] 
**moderation_file_status** | **str** | Moderation status for file | 
**technical_file_status** | **str** | Technical status for file | 

## Example

```python
from tidal.models.file_status import FileStatus

# TODO update the JSON string below
json = "{}"
# create an instance of FileStatus from a JSON string
file_status_instance = FileStatus.from_json(json)
# print the JSON string representation of the object
print(FileStatus.to_json())

# convert the object into a dict
file_status_dict = file_status_instance.to_dict()
# create an instance of FileStatus from a dict
file_status_from_dict = FileStatus.from_dict(file_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


