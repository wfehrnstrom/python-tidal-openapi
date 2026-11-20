# ArtistStreamsStatisticsTopCountries

Listeners by country. Without a note, items and otherListeners add up to all listeners, and an absent otherListeners means no listeners are left. With note HIDDEN, part of the listeners is withheld, so an absent otherListeners is unknown rather than zero

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ArtistStreamsStatisticsCountryListeners]**](ArtistStreamsStatisticsCountryListeners.md) |  | 
**note** | **str** | How a breakdown relates to its total. GROUPED: the remainder includes entries too small to show alone, and the breakdown still adds up to the total. HIDDEN: part of the total is withheld, so the breakdown adds up to less than the total. UNKNOWN: a note this API does not know, so the breakdown may not add up | [optional] 
**other_listeners** | **int** | Listeners in countries not in items. A present value, 0 included, is measured | [optional] 

## Example

```python
from tidal.models.artist_streams_statistics_top_countries import ArtistStreamsStatisticsTopCountries

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistStreamsStatisticsTopCountries from a JSON string
artist_streams_statistics_top_countries_instance = ArtistStreamsStatisticsTopCountries.from_json(json)
# print the JSON string representation of the object
print(ArtistStreamsStatisticsTopCountries.to_json())

# convert the object into a dict
artist_streams_statistics_top_countries_dict = artist_streams_statistics_top_countries_instance.to_dict()
# create an instance of ArtistStreamsStatisticsTopCountries from a dict
artist_streams_statistics_top_countries_from_dict = ArtistStreamsStatisticsTopCountries.from_dict(artist_streams_statistics_top_countries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


