# LegacyBarcodeId

List of UPCs retrieved from the DSP

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 

## Example

```python
from tidal.models.legacy_barcode_id import LegacyBarcodeId

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyBarcodeId from a JSON string
legacy_barcode_id_instance = LegacyBarcodeId.from_json(json)
# print the JSON string representation of the object
print(LegacyBarcodeId.to_json())

# convert the object into a dict
legacy_barcode_id_dict = legacy_barcode_id_instance.to_dict()
# create an instance of LegacyBarcodeId from a dict
legacy_barcode_id_from_dict = LegacyBarcodeId.from_dict(legacy_barcode_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


