# PurchasesAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Datetime of purchase (ISO 8601) | 
**status** | **str** | Current status of the purchase | 

## Example

```python
from tidal.models.purchases_attributes import PurchasesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of PurchasesAttributes from a JSON string
purchases_attributes_instance = PurchasesAttributes.from_json(json)
# print the JSON string representation of the object
print(PurchasesAttributes.to_json())

# convert the object into a dict
purchases_attributes_dict = purchases_attributes_instance.to_dict()
# create an instance of PurchasesAttributes from a dict
purchases_attributes_from_dict = PurchasesAttributes.from_dict(purchases_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


