# tidal
The TIDAL API is a [JSON:API](https://jsonapi.org/)-compliant web API exposing TIDAL's music catalogue, metadata, and user functionality. Guides, authorization documentation, and API key management live at [developer.tidal.com](https://developer.tidal.com).

All endpoints exchange `application/vnd.api+json` documents per the [JSON:API specification](https://jsonapi.org/format/): [resource objects](https://jsonapi.org/format/#document-resource-objects) with `attributes` and `relationships`, [compound documents](https://jsonapi.org/format/#document-compound-documents) via `include`, and standard [error objects](https://jsonapi.org/format/#error-objects).

### Authentication and authorization

Every request requires an OAuth 2.0 access token in the `Authorization: Bearer` header. Tokens are issued at `https://auth.tidal.com/v1/oauth2/token` via the client-credentials flow (server-to-server) or the authorization-code + PKCE flow (user context; authorize at `https://login.tidal.com/authorize`). Each endpoint documents which flows it accepts, the access tier it requires, and the scopes that apply. Scopes protect private user data: fields you are not authorized to read are redacted from the response rather than causing an error, and resources you cannot access at all behave as if they do not exist. See the [authorization guide](https://developer.tidal.com/documentation/api-sdk/api-sdk-authorization) for details.

### Common wire types and compatibility

Each property's schema is authoritative for its allowed values, format, requiredness, nullability, and constraints. A standard defines how a value is represented; an individual schema may support only a documented subset.

- **Enums** use `UPPER_CASE_UNDERSCORE`, except JSON:API resource types, which use plural camelCase names such as `playlistGenerationSchedules`. New values can be added to any enum at any time, so treat unknown values as forward-compatible rather than errors.
- **Resource IDs** are opaque strings. A few resources document well-known IDs for permanent system singleton instances; compare those IDs by exact value. Never parse, construct, or infer meaning from any other `id`, even when its current representation resembles an integer, UUID, or another recognizable value. Other properties explicitly marked with OpenAPI `format: uuid` are UUIDs.
- **Dates and times** use ISO 8601. Date-times use the OpenAPI `date-time` format (`2024-05-01T12:00:00Z`), dates use `YYYY-MM-DD`, and durations use values such as `PT3M5S`.
- **Recurrence frequencies** use RFC 5545 `FREQ` names such as `DAILY`, `WEEKLY`, and `MONTHLY`. The property's enum lists the frequencies that field currently supports.
- **Weekdays** use `MONDAY` through `SUNDAY`.
- **Time zones** use IANA Time Zone Database identifiers such as `Europe/Stockholm`, not abbreviations or raw UTC offsets for recurring civil-time schedules.
- **Country codes** use ISO 3166-1 alpha-2; the shared country type also accepts `WW` for worldwide. **Locales** use IETF BCP 47 language tags such as `en-US`.
- **Currencies** use ISO 4217 codes. Monetary amounts are decimal strings; each field defines its sign and precision constraints.
- **Colors** use three- or six-digit hexadecimal strings (`#RGB` or `#RRGGBB`). Resource links to external URLs use JSON:API link objects with an `href` member.

### Resource identifiers

Where supported, `filter[subject]=tracks:123` matches a related resource by type and ID;
`filter[subject.id]=123` and `filter[subject.type]=tracks` match either component.
Where multiple identifiers are accepted, comma-separated values match any complete pair.
When a member path names a to-many relationship, at least one related resource must match;
filtering does not trim that relationship. On collection and to-many relationship reads, the
reserved root `self` (`filter[self]=tracks:123`) filters primary data itself.
Each endpoint lists its supported filters and types.

Where supported, `me` aliases the authenticated user's dedicated resource ID for the referenced
resource type. It works in paths, resource-ID filters, compact identifiers (`type:me`), resource
PATCH primary IDs and standalone relationship mutation identifiers, with the same meaning as
the resolved ID. Reads using the alias are `no-store`.

### Relationships and includes

[Relationships](https://jsonapi.org/format/#document-resource-object-relationships) are returned only on request: [`include`](https://jsonapi.org/format/#fetching-includes) selects linkage and related content, while `includeLinkage` selects authorized linkage only. A relationship that was not requested is absent from the response, not empty. The full set of relationships a resource supports is documented in its schema.

For INTERNAL clients on resource GET endpoints, `includeLinkage` accepts comma-separated direct relationship names, for example `includeLinkage=subject,viewer`. It does not load related resources or add an `included` section. Nested paths and type qualifiers are unsupported. To-many linkage retains its normal pagination and relationship `next` links. Selecting the same relationship with both parameters applies full include behavior and reads the relationship once.

Request related resources in one round trip with `?include=`, a comma-separated list of dot-separated relationship paths — e.g. `include=coverArt,artists.profileArt` on an album. A nested path automatically embeds its intermediate resources: `artists.profileArt` includes the artists as well as their profile art. Include paths are always relative to the request's root resource, also on relationship endpoints. Including a relationship never changes the primary data; the related resources are added to `included`.

Include paths are validated: a path that cannot be resolved against the resources' documented relationships is rejected with `400`. Include trees are also bounded in path depth (default 3 levels) and in the total number of distinct resources they name (default 10); individual endpoints may apply different limits. Both selectors share the include-node limit, counting overlapping roots once. A request exceeding either limit is rejected with `400`, with the effective limit stated in the error.

### Filtering, sorting, pagination

- [`filter[<memberPath>]=value`](https://jsonapi.org/format/#fetching-filtering) filters primary data by equality. Each endpoint lists its available filters; most collections require at least one.
- Where explicitly documented, `filter[<memberPath>][ne]=value` negates the complete equality predicate. When the member path names a to-many relationship, no related ID may match any supplied value; a known-empty relationship matches. Operators are separate from values. Supplied comparisons combine with AND. For a required filter with multiple supported comparisons, at least one must be supplied; the parameter descriptions identify these alternatives. Unsupported operators and groups return `400`.
- Where documented, `filter[<path>][<operator>]=value` applies an endpoint-defined operator, such as `filter[self][matchesQuery]`. Its meaning is described per endpoint, and it combines with other filters by AND.
- [`sort=<memberPath>`](https://jsonapi.org/format/#fetching-sorting) sorts ascending, `-<memberPath>` descending (`sort=-addedAt`). Filter and sort member paths are relative to primary data.
- Parameters an endpoint cannot honor are rejected with `400`: a `filter[...]` parameter the endpoint does not document (the error lists the available filters), or `sort` on an endpoint that documents no sort values.
- [Pagination](https://jsonapi.org/format/#fetching-pagination) is cursor-based: responses carry `links.self` and, while more pages exist, `links.next` with an opaque `page[cursor]`. Follow `next` until absent — there are no offset or total-page parameters. Collection sizes, when available, appear as `meta.total` and may be approximate.

### Type qualifiers

Where a relationship can contain several resource types, a path segment may be prefixed with a concrete type to scope which type's member is accessed. A playlist's `items` are `tracks` or `videos`: `GET /playlists/{id}?include=items.tracks:albums` resolves `albums` only for the items that are tracks. Qualifiers scope member access — they never filter which resources appear in a relationship — and can be chained.

The same syntax applies to `filter` and `sort` member paths on endpoints that support it; where supported, the qualified member is listed among the endpoint's documented filters and sort values. The syntax follows JSON:API proposal [json-api#1695](https://github.com/json-api/json-api/issues/1695).

### Mutations

- [Partial updates](https://jsonapi.org/format/#crud-updating-resource-attributes) distinguish three wire states for nullable attributes: omission leaves the current value unchanged, an explicit `null` clears it, and a concrete value updates it.
- Every mutation accepts an [`Idempotency-Key`](https://www.ietf.org/archive/id/draft-ietf-httpapi-idempotency-key-header-07.html) header. Keys are scoped to the client and the authenticated user. Once the original request has completed, retrying it with the same key, method, path, query and payload within one hour replays its response; a retry while it is still processing is rejected with `409`, and the same key with a different method, path, query or payload with `422`.
- After a successful write, your own subsequent reads reflect the change; other clients may observe it with a delay.

### Revisions and concurrent editing

Where supported, `attributes.revision` identifies the resource's documented aggregate state; a separately versioned relationship collection uses document `meta.revision`. Revisions are nonnegative integers that increase when covered state changes. Compare them only within the same identity and scope, preserve the exact value, and never calculate the next revision. Related content, viewer projections and independent sources are not automatically covered. Domain fields named `version`, such as a music edition, are distinct; existing endpoints retain their documented contracts.

Guarded mutations accept the observed value as top-level `meta.expectedRevision`. Each operation declares its scope and whether the precondition is required. A mismatch returns `409`; missing required input returns `400`. Refresh and reconcile after a conflict, then submit a new operation with a new idempotency key. An identical retry with the original key replays a recorded success under the idempotency contract. These revisions are not HTTP ETags.

Returned revisions describe observed snapshots, not reservations for later writes. Background changes can advance them immediately after a successful response.

### Media resource replacements - BETA Internal only

Media resources (`tracks`, `videos`, and `albums`) can become unavailable in a country when licensing rights change. By default, TIDAL API returns the resource identifiers originally stored in a collection. This keeps ordinary reads predictable and consistent.

If a stored media resource is unavailable for the effective country, TIDAL may identify a contextually applicable alternative that is available there. Replacement is best effort, so an alternative is not always available. Replacement never changes the stored collection.

TIDAL API provides two ways to work with replacements:

1. **Inspect the `replacement` relationship.** A media resource can expose its applicable alternative through the `replacement` relationship. Include this relationship when a client needs both the original and replacement identifiers or wants to decide whether to use the replacement.

2. **Apply replacements with `replaceMedia`.** Clients can use `replaceMedia` to substitute applicable replacements directly into selected relationship data. The parameter accepts relationship paths using the same syntax as `include`. Projection affects only the response and preserves relationship order and metadata. Each identifier includes `meta.replacement` describing whether it was `ORIGINAL`, `REPLACED`, or `NOT_REPLACED`.

For example, `GET /playlists/{id}?include=items&replaceMedia=items` applies replacements to media identifiers in the playlist's `items` relationship.

### Compression

Responses are gzip-compressed when the request includes `Accept-Encoding: gzip` (bodies over 2 KB).

### Deprecation

Deprecated endpoints, parameters, and fields are marked `deprecated` in this specification, with the replacement noted in their description. Deprecated functionality keeps working for at least six months after being marked, and is only removed once a replacement is generally available.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.10.254
- Package version: 1.0.0
- Generator version: 7.27.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/orgs/tidal-music/discussions](https://github.com/orgs/tidal-music/discussions)

## Requirements.

Python 3.11+

Packaging uses standard `[project]` metadata and `[dependency-groups]` (PEP 621/735).
Install the package with `python -m pip install .`; install development dependencies
with Poetry 2.2 or newer using `poetry install`, or pip 25.1 or newer using
`python -m pip install --group dev`. The latter installs the group, not the package.

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import tidal
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import tidal
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import tidal
from tidal.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://openapi.tidal.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = tidal.Configuration(
    host = "https://openapi.tidal.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]


# Enter a context with an instance of the API client
with tidal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tidal.AcceptedTermsApi(api_client)
    filter_owners_id = ['filter_owners_id_example'] # List[str] | User id. Also accepts `me`.
    filter_terms_terms_type = ['filter_terms_terms_type_example'] # List[str] | One of: DEVELOPER, UPLOAD_MARKETPLACE, MERCH_GUIDELINES, TIDAL_CONNECT_DEVELOPER (e.g. `DEVELOPER`)
    filter_terms_is_latest_version = ['filter_terms_is_latest_version_example'] # List[str] | Filter by terms.isLatestVersion (optional)
    include = ['terms'] # List[str] | Include related resources. Available relationships: owners, terms (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)

    try:
        # Get multiple acceptedTerms.
        api_response = api_instance.accepted_terms_get(filter_owners_id, filter_terms_terms_type, filter_terms_is_latest_version=filter_terms_is_latest_version, include=include, include_linkage=include_linkage)
        print("The response of AcceptedTermsApi->accepted_terms_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcceptedTermsApi->accepted_terms_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://openapi.tidal.com/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AcceptedTermsApi* | [**accepted_terms_get**](docs/AcceptedTermsApi.md#accepted_terms_get) | **GET** /acceptedTerms | Get multiple acceptedTerms.
*AcceptedTermsApi* | [**accepted_terms_id_relationships_owners_get**](docs/AcceptedTermsApi.md#accepted_terms_id_relationships_owners_get) | **GET** /acceptedTerms/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*AcceptedTermsApi* | [**accepted_terms_id_relationships_terms_get**](docs/AcceptedTermsApi.md#accepted_terms_id_relationships_terms_get) | **GET** /acceptedTerms/{id}/relationships/terms | Get terms relationship (\&quot;to-one\&quot;).
*AcceptedTermsApi* | [**accepted_terms_post**](docs/AcceptedTermsApi.md#accepted_terms_post) | **POST** /acceptedTerms | Create single acceptedTerm.
*AlbumStatisticsApi* | [**album_statistics_id_get**](docs/AlbumStatisticsApi.md#album_statistics_id_get) | **GET** /albumStatistics/{id} | Get single albumStatistic.
*AlbumStatisticsApi* | [**album_statistics_id_relationships_owners_get**](docs/AlbumStatisticsApi.md#album_statistics_id_relationships_owners_get) | **GET** /albumStatistics/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*AlbumsApi* | [**albums_get**](docs/AlbumsApi.md#albums_get) | **GET** /albums | Get multiple albums.
*AlbumsApi* | [**albums_id_delete**](docs/AlbumsApi.md#albums_id_delete) | **DELETE** /albums/{id} | Delete single album.
*AlbumsApi* | [**albums_id_get**](docs/AlbumsApi.md#albums_id_get) | **GET** /albums/{id} | Get single album.
*AlbumsApi* | [**albums_id_patch**](docs/AlbumsApi.md#albums_id_patch) | **PATCH** /albums/{id} | Update single album.
*AlbumsApi* | [**albums_id_relationships_album_statistics_get**](docs/AlbumsApi.md#albums_id_relationships_album_statistics_get) | **GET** /albums/{id}/relationships/albumStatistics | Get albumStatistics relationship (\&quot;to-one\&quot;).
*AlbumsApi* | [**albums_id_relationships_artists_get**](docs/AlbumsApi.md#albums_id_relationships_artists_get) | **GET** /albums/{id}/relationships/artists | Get artists relationship (\&quot;to-many\&quot;).
*AlbumsApi* | [**albums_id_relationships_artists_patch**](docs/AlbumsApi.md#albums_id_relationships_artists_patch) | **PATCH** /albums/{id}/relationships/artists | Update artists relationship (\&quot;to-many\&quot;).
*AlbumsApi* | [**albums_id_relationships_cover_art_get**](docs/AlbumsApi.md#albums_id_relationships_cover_art_get) | **GET** /albums/{id}/relationships/coverArt | Get coverArt relationship (\&quot;to-many\&quot;).
*AlbumsApi* | [**albums_id_relationships_cover_art_patch**](docs/AlbumsApi.md#albums_id_relationships_cover_art_patch) | **PATCH** /albums/{id}/relationships/coverArt | Update coverArt relationship (\&quot;to-many\&quot;).
*AlbumsApi* | [**albums_id_relationships_genres_get**](docs/AlbumsApi.md#albums_id_relationships_genres_get) | **GET** /albums/{id}/relationships/genres | Get genres relationship (\&quot;to-many\&quot;).
*AlbumsApi* | [**albums_id_relationships_items_get**](docs/AlbumsApi.md#albums_id_relationships_items_get) | **GET** /albums/{id}/relationships/items | Get items relationship (\&quot;to-many\&quot;).
*AlbumsApi* | [**albums_id_relationships_items_patch**](docs/AlbumsApi.md#albums_id_relationships_items_patch) | **PATCH** /albums/{id}/relationships/items | Update items relationship (\&quot;to-many\&quot;).
*AlbumsApi* | [**albums_id_relationships_owners_get**](docs/AlbumsApi.md#albums_id_relationships_owners_get) | **GET** /albums/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*AlbumsApi* | [**albums_id_relationships_price_config_get**](docs/AlbumsApi.md#albums_id_relationships_price_config_get) | **GET** /albums/{id}/relationships/priceConfig | Get priceConfig relationship (\&quot;to-one\&quot;).
*AlbumsApi* | [**albums_id_relationships_providers_get**](docs/AlbumsApi.md#albums_id_relationships_providers_get) | **GET** /albums/{id}/relationships/providers | Get providers relationship (\&quot;to-many\&quot;).
*AlbumsApi* | [**albums_id_relationships_replacement_get**](docs/AlbumsApi.md#albums_id_relationships_replacement_get) | **GET** /albums/{id}/relationships/replacement | Get replacement relationship (\&quot;to-one\&quot;).
*AlbumsApi* | [**albums_id_relationships_shares_get**](docs/AlbumsApi.md#albums_id_relationships_shares_get) | **GET** /albums/{id}/relationships/shares | Get shares relationship (\&quot;to-many\&quot;).
*AlbumsApi* | [**albums_id_relationships_similar_albums_get**](docs/AlbumsApi.md#albums_id_relationships_similar_albums_get) | **GET** /albums/{id}/relationships/similarAlbums | Get similarAlbums relationship (\&quot;to-many\&quot;).
*AlbumsApi* | [**albums_id_relationships_suggested_cover_arts_get**](docs/AlbumsApi.md#albums_id_relationships_suggested_cover_arts_get) | **GET** /albums/{id}/relationships/suggestedCoverArts | Get suggestedCoverArts relationship (\&quot;to-many\&quot;).
*AlbumsApi* | [**albums_id_relationships_usage_rules_get**](docs/AlbumsApi.md#albums_id_relationships_usage_rules_get) | **GET** /albums/{id}/relationships/usageRules | Get usageRules relationship (\&quot;to-one\&quot;).
*AlbumsApi* | [**albums_post**](docs/AlbumsApi.md#albums_post) | **POST** /albums | Create single album.
*AppreciationsApi* | [**appreciations_post**](docs/AppreciationsApi.md#appreciations_post) | **POST** /appreciations | Create single appreciation.
*ArtistBiographiesApi* | [**artist_biographies_id_get**](docs/ArtistBiographiesApi.md#artist_biographies_id_get) | **GET** /artistBiographies/{id} | Get single artistBiographie.
*ArtistBiographiesApi* | [**artist_biographies_id_patch**](docs/ArtistBiographiesApi.md#artist_biographies_id_patch) | **PATCH** /artistBiographies/{id} | Update single artistBiographie.
*ArtistBiographiesApi* | [**artist_biographies_id_relationships_owners_get**](docs/ArtistBiographiesApi.md#artist_biographies_id_relationships_owners_get) | **GET** /artistBiographies/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*ArtistClaimStatusesApi* | [**artist_claim_statuses_get**](docs/ArtistClaimStatusesApi.md#artist_claim_statuses_get) | **GET** /artistClaimStatuses | Get multiple artistClaimStatuses.
*ArtistClaimsApi* | [**artist_claims_get**](docs/ArtistClaimsApi.md#artist_claims_get) | **GET** /artistClaims | Get multiple artistClaims.
*ArtistClaimsApi* | [**artist_claims_id_delete**](docs/ArtistClaimsApi.md#artist_claims_id_delete) | **DELETE** /artistClaims/{id} | Delete single artistClaim.
*ArtistClaimsApi* | [**artist_claims_id_get**](docs/ArtistClaimsApi.md#artist_claims_id_get) | **GET** /artistClaims/{id} | Get single artistClaim.
*ArtistClaimsApi* | [**artist_claims_id_patch**](docs/ArtistClaimsApi.md#artist_claims_id_patch) | **PATCH** /artistClaims/{id} | Update single artistClaim.
*ArtistClaimsApi* | [**artist_claims_id_relationships_accepted_artists_get**](docs/ArtistClaimsApi.md#artist_claims_id_relationships_accepted_artists_get) | **GET** /artistClaims/{id}/relationships/acceptedArtists | Get acceptedArtists relationship (\&quot;to-many\&quot;).
*ArtistClaimsApi* | [**artist_claims_id_relationships_accepted_artists_patch**](docs/ArtistClaimsApi.md#artist_claims_id_relationships_accepted_artists_patch) | **PATCH** /artistClaims/{id}/relationships/acceptedArtists | Update acceptedArtists relationship (\&quot;to-many\&quot;).
*ArtistClaimsApi* | [**artist_claims_id_relationships_owners_get**](docs/ArtistClaimsApi.md#artist_claims_id_relationships_owners_get) | **GET** /artistClaims/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*ArtistClaimsApi* | [**artist_claims_id_relationships_recommended_artists_get**](docs/ArtistClaimsApi.md#artist_claims_id_relationships_recommended_artists_get) | **GET** /artistClaims/{id}/relationships/recommendedArtists | Get recommendedArtists relationship (\&quot;to-many\&quot;).
*ArtistClaimsApi* | [**artist_claims_post**](docs/ArtistClaimsApi.md#artist_claims_post) | **POST** /artistClaims | Create single artistClaim.
*ArtistRolesApi* | [**artist_roles_id_get**](docs/ArtistRolesApi.md#artist_roles_id_get) | **GET** /artistRoles/{id} | Get single artistRole.
*ArtistSalesStatisticsApi* | [**artist_sales_statistics_get**](docs/ArtistSalesStatisticsApi.md#artist_sales_statistics_get) | **GET** /artistSalesStatistics | Get multiple artistSalesStatistics.
*ArtistSalesStatisticsApi* | [**artist_sales_statistics_id_relationships_artist_get**](docs/ArtistSalesStatisticsApi.md#artist_sales_statistics_id_relationships_artist_get) | **GET** /artistSalesStatistics/{id}/relationships/artist | Get artist relationship (\&quot;to-one\&quot;).
*ArtistSalesStatisticsApi* | [**artist_sales_statistics_id_relationships_top_sellers_get**](docs/ArtistSalesStatisticsApi.md#artist_sales_statistics_id_relationships_top_sellers_get) | **GET** /artistSalesStatistics/{id}/relationships/topSellers | Get topSellers relationship (\&quot;to-many\&quot;).
*ArtistStreamsStatisticsApi* | [**artist_streams_statistics_get**](docs/ArtistStreamsStatisticsApi.md#artist_streams_statistics_get) | **GET** /artistStreamsStatistics | Get multiple artistStreamsStatistics.
*ArtistStreamsStatisticsApi* | [**artist_streams_statistics_id_relationships_artist_get**](docs/ArtistStreamsStatisticsApi.md#artist_streams_statistics_id_relationships_artist_get) | **GET** /artistStreamsStatistics/{id}/relationships/artist | Get artist relationship (\&quot;to-one\&quot;).
*ArtistStreamsStatisticsApi* | [**artist_streams_statistics_id_relationships_top_tracks_get**](docs/ArtistStreamsStatisticsApi.md#artist_streams_statistics_id_relationships_top_tracks_get) | **GET** /artistStreamsStatistics/{id}/relationships/topTracks | Get topTracks relationship (\&quot;to-many\&quot;).
*ArtistsApi* | [**artists_get**](docs/ArtistsApi.md#artists_get) | **GET** /artists | Get multiple artists.
*ArtistsApi* | [**artists_id_get**](docs/ArtistsApi.md#artists_id_get) | **GET** /artists/{id} | Get single artist.
*ArtistsApi* | [**artists_id_patch**](docs/ArtistsApi.md#artists_id_patch) | **PATCH** /artists/{id} | Update single artist.
*ArtistsApi* | [**artists_id_relationships_albums_get**](docs/ArtistsApi.md#artists_id_relationships_albums_get) | **GET** /artists/{id}/relationships/albums | Get albums relationship (\&quot;to-many\&quot;).
*ArtistsApi* | [**artists_id_relationships_banner_art_get**](docs/ArtistsApi.md#artists_id_relationships_banner_art_get) | **GET** /artists/{id}/relationships/bannerArt | Get bannerArt relationship (\&quot;to-many\&quot;).
*ArtistsApi* | [**artists_id_relationships_banner_art_patch**](docs/ArtistsApi.md#artists_id_relationships_banner_art_patch) | **PATCH** /artists/{id}/relationships/bannerArt | Update bannerArt relationship (\&quot;to-many\&quot;).
*ArtistsApi* | [**artists_id_relationships_biography_get**](docs/ArtistsApi.md#artists_id_relationships_biography_get) | **GET** /artists/{id}/relationships/biography | Get biography relationship (\&quot;to-one\&quot;).
*ArtistsApi* | [**artists_id_relationships_claim_status_get**](docs/ArtistsApi.md#artists_id_relationships_claim_status_get) | **GET** /artists/{id}/relationships/claimStatus | Get claimStatus relationship (\&quot;to-one\&quot;).
*ArtistsApi* | [**artists_id_relationships_followers_get**](docs/ArtistsApi.md#artists_id_relationships_followers_get) | **GET** /artists/{id}/relationships/followers | Get followers relationship (\&quot;to-many\&quot;).
*ArtistsApi* | [**artists_id_relationships_following_delete**](docs/ArtistsApi.md#artists_id_relationships_following_delete) | **DELETE** /artists/{id}/relationships/following | Delete from following relationship (\&quot;to-many\&quot;).
*ArtistsApi* | [**artists_id_relationships_following_get**](docs/ArtistsApi.md#artists_id_relationships_following_get) | **GET** /artists/{id}/relationships/following | Get following relationship (\&quot;to-many\&quot;).
*ArtistsApi* | [**artists_id_relationships_following_post**](docs/ArtistsApi.md#artists_id_relationships_following_post) | **POST** /artists/{id}/relationships/following | Add to following relationship (\&quot;to-many\&quot;).
*ArtistsApi* | [**artists_id_relationships_logo_art_get**](docs/ArtistsApi.md#artists_id_relationships_logo_art_get) | **GET** /artists/{id}/relationships/logoArt | Get logoArt relationship (\&quot;to-many\&quot;).
*ArtistsApi* | [**artists_id_relationships_logo_art_patch**](docs/ArtistsApi.md#artists_id_relationships_logo_art_patch) | **PATCH** /artists/{id}/relationships/logoArt | Update logoArt relationship (\&quot;to-many\&quot;).
*ArtistsApi* | [**artists_id_relationships_owners_get**](docs/ArtistsApi.md#artists_id_relationships_owners_get) | **GET** /artists/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*ArtistsApi* | [**artists_id_relationships_profile_art_get**](docs/ArtistsApi.md#artists_id_relationships_profile_art_get) | **GET** /artists/{id}/relationships/profileArt | Get profileArt relationship (\&quot;to-many\&quot;).
*ArtistsApi* | [**artists_id_relationships_profile_art_patch**](docs/ArtistsApi.md#artists_id_relationships_profile_art_patch) | **PATCH** /artists/{id}/relationships/profileArt | Update profileArt relationship (\&quot;to-many\&quot;).
*ArtistsApi* | [**artists_id_relationships_radio_get**](docs/ArtistsApi.md#artists_id_relationships_radio_get) | **GET** /artists/{id}/relationships/radio | Get radio relationship (\&quot;to-many\&quot;).
*ArtistsApi* | [**artists_id_relationships_roles_get**](docs/ArtistsApi.md#artists_id_relationships_roles_get) | **GET** /artists/{id}/relationships/roles | Get roles relationship (\&quot;to-many\&quot;).
*ArtistsApi* | [**artists_id_relationships_similar_artists_get**](docs/ArtistsApi.md#artists_id_relationships_similar_artists_get) | **GET** /artists/{id}/relationships/similarArtists | Get similarArtists relationship (\&quot;to-many\&quot;).
*ArtistsApi* | [**artists_id_relationships_track_providers_get**](docs/ArtistsApi.md#artists_id_relationships_track_providers_get) | **GET** /artists/{id}/relationships/trackProviders | Get trackProviders relationship (\&quot;to-many\&quot;).
*ArtistsApi* | [**artists_id_relationships_tracks_get**](docs/ArtistsApi.md#artists_id_relationships_tracks_get) | **GET** /artists/{id}/relationships/tracks | Get tracks relationship (\&quot;to-many\&quot;).
*ArtistsApi* | [**artists_id_relationships_videos_get**](docs/ArtistsApi.md#artists_id_relationships_videos_get) | **GET** /artists/{id}/relationships/videos | Get videos relationship (\&quot;to-many\&quot;).
*ArtistsApi* | [**artists_post**](docs/ArtistsApi.md#artists_post) | **POST** /artists | Create single artist.
*ArtworkLibrariesApi* | [**artwork_libraries_get**](docs/ArtworkLibrariesApi.md#artwork_libraries_get) | **GET** /artworkLibraries | Get multiple artworkLibraries.
*ArtworkLibrariesApi* | [**artwork_libraries_id_get**](docs/ArtworkLibrariesApi.md#artwork_libraries_id_get) | **GET** /artworkLibraries/{id} | Get single artworkLibrarie.
*ArtworkLibrariesApi* | [**artwork_libraries_id_relationships_artworks_get**](docs/ArtworkLibrariesApi.md#artwork_libraries_id_relationships_artworks_get) | **GET** /artworkLibraries/{id}/relationships/artworks | Get artworks relationship (\&quot;to-many\&quot;).
*ArtworkLibrariesApi* | [**artwork_libraries_id_relationships_random_artwork_get**](docs/ArtworkLibrariesApi.md#artwork_libraries_id_relationships_random_artwork_get) | **GET** /artworkLibraries/{id}/relationships/randomArtwork | Get randomArtwork relationship (\&quot;to-one\&quot;).
*ArtworksApi* | [**artworks_get**](docs/ArtworksApi.md#artworks_get) | **GET** /artworks | Get multiple artworks.
*ArtworksApi* | [**artworks_id_get**](docs/ArtworksApi.md#artworks_id_get) | **GET** /artworks/{id} | Get single artwork.
*ArtworksApi* | [**artworks_id_relationships_owners_get**](docs/ArtworksApi.md#artworks_id_relationships_owners_get) | **GET** /artworks/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*ArtworksApi* | [**artworks_post**](docs/ArtworksApi.md#artworks_post) | **POST** /artworks | Create single artwork.
*ClientCertificatesApi* | [**client_certificates_id_get**](docs/ClientCertificatesApi.md#client_certificates_id_get) | **GET** /clientCertificates/{id} | Get single clientCertificate.
*ClientCertificatesApi* | [**client_certificates_id_relationships_owners_get**](docs/ClientCertificatesApi.md#client_certificates_id_relationships_owners_get) | **GET** /clientCertificates/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*ClientCertificatesApi* | [**client_certificates_post**](docs/ClientCertificatesApi.md#client_certificates_post) | **POST** /clientCertificates | Create single clientCertificate.
*ClientsApi* | [**clients_get**](docs/ClientsApi.md#clients_get) | **GET** /clients | Get multiple clients.
*ClientsApi* | [**clients_id_delete**](docs/ClientsApi.md#clients_id_delete) | **DELETE** /clients/{id} | Delete single client.
*ClientsApi* | [**clients_id_get**](docs/ClientsApi.md#clients_id_get) | **GET** /clients/{id} | Get single client.
*ClientsApi* | [**clients_id_patch**](docs/ClientsApi.md#clients_id_patch) | **PATCH** /clients/{id} | Update single client.
*ClientsApi* | [**clients_id_relationships_certificates_get**](docs/ClientsApi.md#clients_id_relationships_certificates_get) | **GET** /clients/{id}/relationships/certificates | Get certificates relationship (\&quot;to-many\&quot;).
*ClientsApi* | [**clients_id_relationships_owners_get**](docs/ClientsApi.md#clients_id_relationships_owners_get) | **GET** /clients/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*ClientsApi* | [**clients_post**](docs/ClientsApi.md#clients_post) | **POST** /clients | Create single client.
*CollaborationInviteRedemptionsApi* | [**collaboration_invite_redemptions_post**](docs/CollaborationInviteRedemptionsApi.md#collaboration_invite_redemptions_post) | **POST** /collaborationInviteRedemptions | Create single collaborationInviteRedemption.
*CollaborationInvitesApi* | [**collaboration_invites_get**](docs/CollaborationInvitesApi.md#collaboration_invites_get) | **GET** /collaborationInvites | Get multiple collaborationInvites.
*CollaborationInvitesApi* | [**collaboration_invites_id_delete**](docs/CollaborationInvitesApi.md#collaboration_invites_id_delete) | **DELETE** /collaborationInvites/{id} | Delete single collaborationInvite.
*CollaborationInvitesApi* | [**collaboration_invites_id_get**](docs/CollaborationInvitesApi.md#collaboration_invites_id_get) | **GET** /collaborationInvites/{id} | Get single collaborationInvite.
*CollaborationInvitesApi* | [**collaboration_invites_id_relationships_owners_get**](docs/CollaborationInvitesApi.md#collaboration_invites_id_relationships_owners_get) | **GET** /collaborationInvites/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*CollaborationInvitesApi* | [**collaboration_invites_id_relationships_subject_get**](docs/CollaborationInvitesApi.md#collaboration_invites_id_relationships_subject_get) | **GET** /collaborationInvites/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).
*CollaborationInvitesApi* | [**collaboration_invites_post**](docs/CollaborationInvitesApi.md#collaboration_invites_post) | **POST** /collaborationInvites | Create single collaborationInvite.
*CommentSummariesApi* | [**comment_summaries_get**](docs/CommentSummariesApi.md#comment_summaries_get) | **GET** /commentSummaries | Get multiple commentSummaries.
*CommentSummariesApi* | [**comment_summaries_id_relationships_subject_get**](docs/CommentSummariesApi.md#comment_summaries_id_relationships_subject_get) | **GET** /commentSummaries/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).
*CommentsApi* | [**comments_get**](docs/CommentsApi.md#comments_get) | **GET** /comments | Get multiple comments.
*CommentsApi* | [**comments_id_delete**](docs/CommentsApi.md#comments_id_delete) | **DELETE** /comments/{id} | Delete single comment.
*CommentsApi* | [**comments_id_get**](docs/CommentsApi.md#comments_id_get) | **GET** /comments/{id} | Get single comment.
*CommentsApi* | [**comments_id_patch**](docs/CommentsApi.md#comments_id_patch) | **PATCH** /comments/{id} | Update single comment.
*CommentsApi* | [**comments_id_relationships_author_get**](docs/CommentsApi.md#comments_id_relationships_author_get) | **GET** /comments/{id}/relationships/author | Get author relationship (\&quot;to-one\&quot;).
*CommentsApi* | [**comments_id_relationships_comment_summary_get**](docs/CommentsApi.md#comments_id_relationships_comment_summary_get) | **GET** /comments/{id}/relationships/commentSummary | Get commentSummary relationship (\&quot;to-one\&quot;).
*CommentsApi* | [**comments_id_relationships_owners_get**](docs/CommentsApi.md#comments_id_relationships_owners_get) | **GET** /comments/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*CommentsApi* | [**comments_id_relationships_reaction_summary_get**](docs/CommentsApi.md#comments_id_relationships_reaction_summary_get) | **GET** /comments/{id}/relationships/reactionSummary | Get reactionSummary relationship (\&quot;to-one\&quot;).
*CommentsApi* | [**comments_id_relationships_root_subject_get**](docs/CommentsApi.md#comments_id_relationships_root_subject_get) | **GET** /comments/{id}/relationships/rootSubject | Get rootSubject relationship (\&quot;to-one\&quot;).
*CommentsApi* | [**comments_id_relationships_subject_get**](docs/CommentsApi.md#comments_id_relationships_subject_get) | **GET** /comments/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).
*CommentsApi* | [**comments_post**](docs/CommentsApi.md#comments_post) | **POST** /comments | Create single comment.
*ContentClaimsApi* | [**content_claims_get**](docs/ContentClaimsApi.md#content_claims_get) | **GET** /contentClaims | Get multiple contentClaims.
*ContentClaimsApi* | [**content_claims_id_get**](docs/ContentClaimsApi.md#content_claims_id_get) | **GET** /contentClaims/{id} | Get single contentClaim.
*ContentClaimsApi* | [**content_claims_id_relationships_claimed_resource_get**](docs/ContentClaimsApi.md#content_claims_id_relationships_claimed_resource_get) | **GET** /contentClaims/{id}/relationships/claimedResource | Get claimedResource relationship (\&quot;to-one\&quot;).
*ContentClaimsApi* | [**content_claims_id_relationships_claiming_artist_get**](docs/ContentClaimsApi.md#content_claims_id_relationships_claiming_artist_get) | **GET** /contentClaims/{id}/relationships/claimingArtist | Get claimingArtist relationship (\&quot;to-one\&quot;).
*ContentClaimsApi* | [**content_claims_id_relationships_owners_get**](docs/ContentClaimsApi.md#content_claims_id_relationships_owners_get) | **GET** /contentClaims/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*ContentClaimsApi* | [**content_claims_post**](docs/ContentClaimsApi.md#content_claims_post) | **POST** /contentClaims | Create single contentClaim.
*CreditsApi* | [**credits_id_get**](docs/CreditsApi.md#credits_id_get) | **GET** /credits/{id} | Get single credit.
*CreditsApi* | [**credits_id_relationships_artist_get**](docs/CreditsApi.md#credits_id_relationships_artist_get) | **GET** /credits/{id}/relationships/artist | Get artist relationship (\&quot;to-one\&quot;).
*CreditsApi* | [**credits_id_relationships_category_get**](docs/CreditsApi.md#credits_id_relationships_category_get) | **GET** /credits/{id}/relationships/category | Get category relationship (\&quot;to-one\&quot;).
*DownloadsApi* | [**downloads_get**](docs/DownloadsApi.md#downloads_get) | **GET** /downloads | Get multiple downloads.
*DownloadsApi* | [**downloads_id_get**](docs/DownloadsApi.md#downloads_id_get) | **GET** /downloads/{id} | Get single download.
*DownloadsApi* | [**downloads_id_relationships_owners_get**](docs/DownloadsApi.md#downloads_id_relationships_owners_get) | **GET** /downloads/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*DspSharingLinksApi* | [**dsp_sharing_links_get**](docs/DspSharingLinksApi.md#dsp_sharing_links_get) | **GET** /dspSharingLinks | Get multiple dspSharingLinks.
*DspSharingLinksApi* | [**dsp_sharing_links_id_relationships_subject_get**](docs/DspSharingLinksApi.md#dsp_sharing_links_id_relationships_subject_get) | **GET** /dspSharingLinks/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).
*DynamicModulesApi* | [**dynamic_modules_get**](docs/DynamicModulesApi.md#dynamic_modules_get) | **GET** /dynamicModules | Get multiple dynamicModules.
*DynamicModulesApi* | [**dynamic_modules_id_get**](docs/DynamicModulesApi.md#dynamic_modules_id_get) | **GET** /dynamicModules/{id} | Get single dynamicModule.
*DynamicModulesApi* | [**dynamic_modules_id_relationships_items_get**](docs/DynamicModulesApi.md#dynamic_modules_id_relationships_items_get) | **GET** /dynamicModules/{id}/relationships/items | Get items relationship (\&quot;to-many\&quot;).
*DynamicModulesApi* | [**dynamic_modules_id_relationships_seed_item_get**](docs/DynamicModulesApi.md#dynamic_modules_id_relationships_seed_item_get) | **GET** /dynamicModules/{id}/relationships/seedItem | Get seedItem relationship (\&quot;to-one\&quot;).
*DynamicPagesApi* | [**dynamic_pages_get**](docs/DynamicPagesApi.md#dynamic_pages_get) | **GET** /dynamicPages | Get multiple dynamicPages.
*DynamicPagesApi* | [**dynamic_pages_id_relationships_modules_get**](docs/DynamicPagesApi.md#dynamic_pages_id_relationships_modules_get) | **GET** /dynamicPages/{id}/relationships/modules | Get modules relationship (\&quot;to-many\&quot;).
*DynamicPagesApi* | [**dynamic_pages_id_relationships_subject_get**](docs/DynamicPagesApi.md#dynamic_pages_id_relationships_subject_get) | **GET** /dynamicPages/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).
*FolderItemsApi* | [**folder_items_get**](docs/FolderItemsApi.md#folder_items_get) | **GET** /folderItems | Get multiple folderItems.
*FolderItemsApi* | [**folder_items_id_delete**](docs/FolderItemsApi.md#folder_items_id_delete) | **DELETE** /folderItems/{id} | Delete single folderItem.
*FolderItemsApi* | [**folder_items_id_get**](docs/FolderItemsApi.md#folder_items_id_get) | **GET** /folderItems/{id} | Get single folderItem.
*FolderItemsApi* | [**folder_items_id_relationships_breadcrumb_get**](docs/FolderItemsApi.md#folder_items_id_relationships_breadcrumb_get) | **GET** /folderItems/{id}/relationships/breadcrumb | Get breadcrumb relationship (\&quot;to-many\&quot;).
*FolderItemsApi* | [**folder_items_id_relationships_owners_get**](docs/FolderItemsApi.md#folder_items_id_relationships_owners_get) | **GET** /folderItems/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*FolderItemsApi* | [**folder_items_id_relationships_parent_get**](docs/FolderItemsApi.md#folder_items_id_relationships_parent_get) | **GET** /folderItems/{id}/relationships/parent | Get parent relationship (\&quot;to-one\&quot;).
*FolderItemsApi* | [**folder_items_id_relationships_parent_patch**](docs/FolderItemsApi.md#folder_items_id_relationships_parent_patch) | **PATCH** /folderItems/{id}/relationships/parent | Update parent relationship (\&quot;to-one\&quot;).
*FolderItemsApi* | [**folder_items_id_relationships_sharing_summary_get**](docs/FolderItemsApi.md#folder_items_id_relationships_sharing_summary_get) | **GET** /folderItems/{id}/relationships/sharingSummary | Get sharingSummary relationship (\&quot;to-one\&quot;).
*FolderItemsApi* | [**folder_items_id_relationships_subject_get**](docs/FolderItemsApi.md#folder_items_id_relationships_subject_get) | **GET** /folderItems/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).
*FolderItemsApi* | [**folder_items_post**](docs/FolderItemsApi.md#folder_items_post) | **POST** /folderItems | Create single folderItem.
*FoldersApi* | [**folders_get**](docs/FoldersApi.md#folders_get) | **GET** /folders | Get multiple folders.
*FoldersApi* | [**folders_id_delete**](docs/FoldersApi.md#folders_id_delete) | **DELETE** /folders/{id} | Delete single folder.
*FoldersApi* | [**folders_id_get**](docs/FoldersApi.md#folders_id_get) | **GET** /folders/{id} | Get single folder.
*FoldersApi* | [**folders_id_patch**](docs/FoldersApi.md#folders_id_patch) | **PATCH** /folders/{id} | Update single folder.
*FoldersApi* | [**folders_id_relationships_children_get**](docs/FoldersApi.md#folders_id_relationships_children_get) | **GET** /folders/{id}/relationships/children | Get children relationship (\&quot;to-many\&quot;).
*FoldersApi* | [**folders_id_relationships_owners_get**](docs/FoldersApi.md#folders_id_relationships_owners_get) | **GET** /folders/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*FoldersApi* | [**folders_id_relationships_parent_get**](docs/FoldersApi.md#folders_id_relationships_parent_get) | **GET** /folders/{id}/relationships/parent | Get parent relationship (\&quot;to-one\&quot;).
*FoldersApi* | [**folders_id_relationships_preview_get**](docs/FoldersApi.md#folders_id_relationships_preview_get) | **GET** /folders/{id}/relationships/preview | Get preview relationship (\&quot;to-many\&quot;).
*FoldersApi* | [**folders_id_relationships_shares_get**](docs/FoldersApi.md#folders_id_relationships_shares_get) | **GET** /folders/{id}/relationships/shares | Get shares relationship (\&quot;to-many\&quot;).
*FoldersApi* | [**folders_post**](docs/FoldersApi.md#folders_post) | **POST** /folders | Create single folder.
*GenresApi* | [**genres_get**](docs/GenresApi.md#genres_get) | **GET** /genres | Get multiple genres.
*GenresApi* | [**genres_id_get**](docs/GenresApi.md#genres_id_get) | **GET** /genres/{id} | Get single genre.
*GroupsApi* | [**groups_get**](docs/GroupsApi.md#groups_get) | **GET** /groups | Get multiple groups.
*GroupsApi* | [**groups_id_get**](docs/GroupsApi.md#groups_id_get) | **GET** /groups/{id} | Get single group.
*InstallationsApi* | [**installations_get**](docs/InstallationsApi.md#installations_get) | **GET** /installations | Get multiple installations.
*InstallationsApi* | [**installations_id_get**](docs/InstallationsApi.md#installations_id_get) | **GET** /installations/{id} | Get single installation.
*InstallationsApi* | [**installations_id_relationships_offline_inventory_delete**](docs/InstallationsApi.md#installations_id_relationships_offline_inventory_delete) | **DELETE** /installations/{id}/relationships/offlineInventory | Delete from offlineInventory relationship (\&quot;to-many\&quot;).
*InstallationsApi* | [**installations_id_relationships_offline_inventory_get**](docs/InstallationsApi.md#installations_id_relationships_offline_inventory_get) | **GET** /installations/{id}/relationships/offlineInventory | Get offlineInventory relationship (\&quot;to-many\&quot;).
*InstallationsApi* | [**installations_id_relationships_offline_inventory_post**](docs/InstallationsApi.md#installations_id_relationships_offline_inventory_post) | **POST** /installations/{id}/relationships/offlineInventory | Add to offlineInventory relationship (\&quot;to-many\&quot;).
*InstallationsApi* | [**installations_id_relationships_owners_get**](docs/InstallationsApi.md#installations_id_relationships_owners_get) | **GET** /installations/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*InstallationsApi* | [**installations_post**](docs/InstallationsApi.md#installations_post) | **POST** /installations | Create single installation.
*LyricsApi* | [**lyrics_id_delete**](docs/LyricsApi.md#lyrics_id_delete) | **DELETE** /lyrics/{id} | Delete single lyric.
*LyricsApi* | [**lyrics_id_get**](docs/LyricsApi.md#lyrics_id_get) | **GET** /lyrics/{id} | Get single lyric.
*LyricsApi* | [**lyrics_id_patch**](docs/LyricsApi.md#lyrics_id_patch) | **PATCH** /lyrics/{id} | Update single lyric.
*LyricsApi* | [**lyrics_id_relationships_owners_get**](docs/LyricsApi.md#lyrics_id_relationships_owners_get) | **GET** /lyrics/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*LyricsApi* | [**lyrics_id_relationships_track_get**](docs/LyricsApi.md#lyrics_id_relationships_track_get) | **GET** /lyrics/{id}/relationships/track | Get track relationship (\&quot;to-one\&quot;).
*LyricsApi* | [**lyrics_post**](docs/LyricsApi.md#lyrics_post) | **POST** /lyrics | Create single lyric.
*ManualArtistClaimsApi* | [**manual_artist_claims_post**](docs/ManualArtistClaimsApi.md#manual_artist_claims_post) | **POST** /manualArtistClaims | Create single manualArtistClaim.
*OfflineTasksApi* | [**offline_tasks_get**](docs/OfflineTasksApi.md#offline_tasks_get) | **GET** /offlineTasks | Get multiple offlineTasks.
*OfflineTasksApi* | [**offline_tasks_id_get**](docs/OfflineTasksApi.md#offline_tasks_id_get) | **GET** /offlineTasks/{id} | Get single offlineTask.
*OfflineTasksApi* | [**offline_tasks_id_patch**](docs/OfflineTasksApi.md#offline_tasks_id_patch) | **PATCH** /offlineTasks/{id} | Update single offlineTask.
*OfflineTasksApi* | [**offline_tasks_id_relationships_collection_get**](docs/OfflineTasksApi.md#offline_tasks_id_relationships_collection_get) | **GET** /offlineTasks/{id}/relationships/collection | Get collection relationship (\&quot;to-one\&quot;).
*OfflineTasksApi* | [**offline_tasks_id_relationships_item_get**](docs/OfflineTasksApi.md#offline_tasks_id_relationships_item_get) | **GET** /offlineTasks/{id}/relationships/item | Get item relationship (\&quot;to-one\&quot;).
*OfflineTasksApi* | [**offline_tasks_id_relationships_owners_get**](docs/OfflineTasksApi.md#offline_tasks_id_relationships_owners_get) | **GET** /offlineTasks/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*PlayQueuesApi* | [**play_queues_get**](docs/PlayQueuesApi.md#play_queues_get) | **GET** /playQueues | Get multiple playQueues.
*PlayQueuesApi* | [**play_queues_id_delete**](docs/PlayQueuesApi.md#play_queues_id_delete) | **DELETE** /playQueues/{id} | Delete single playQueue.
*PlayQueuesApi* | [**play_queues_id_get**](docs/PlayQueuesApi.md#play_queues_id_get) | **GET** /playQueues/{id} | Get single playQueue.
*PlayQueuesApi* | [**play_queues_id_patch**](docs/PlayQueuesApi.md#play_queues_id_patch) | **PATCH** /playQueues/{id} | Update single playQueue.
*PlayQueuesApi* | [**play_queues_id_relationships_change_event_stream_get**](docs/PlayQueuesApi.md#play_queues_id_relationships_change_event_stream_get) | **GET** /playQueues/{id}/relationships/changeEventStream | Get changeEventStream relationship (\&quot;to-one\&quot;).
*PlayQueuesApi* | [**play_queues_id_relationships_current_get**](docs/PlayQueuesApi.md#play_queues_id_relationships_current_get) | **GET** /playQueues/{id}/relationships/current | Get current relationship (\&quot;to-one\&quot;).
*PlayQueuesApi* | [**play_queues_id_relationships_current_patch**](docs/PlayQueuesApi.md#play_queues_id_relationships_current_patch) | **PATCH** /playQueues/{id}/relationships/current | Update current relationship (\&quot;to-one\&quot;).
*PlayQueuesApi* | [**play_queues_id_relationships_future_delete**](docs/PlayQueuesApi.md#play_queues_id_relationships_future_delete) | **DELETE** /playQueues/{id}/relationships/future | Delete from future relationship (\&quot;to-many\&quot;).
*PlayQueuesApi* | [**play_queues_id_relationships_future_get**](docs/PlayQueuesApi.md#play_queues_id_relationships_future_get) | **GET** /playQueues/{id}/relationships/future | Get future relationship (\&quot;to-many\&quot;).
*PlayQueuesApi* | [**play_queues_id_relationships_future_patch**](docs/PlayQueuesApi.md#play_queues_id_relationships_future_patch) | **PATCH** /playQueues/{id}/relationships/future | Update future relationship (\&quot;to-many\&quot;).
*PlayQueuesApi* | [**play_queues_id_relationships_future_post**](docs/PlayQueuesApi.md#play_queues_id_relationships_future_post) | **POST** /playQueues/{id}/relationships/future | Add to future relationship (\&quot;to-many\&quot;).
*PlayQueuesApi* | [**play_queues_id_relationships_owners_get**](docs/PlayQueuesApi.md#play_queues_id_relationships_owners_get) | **GET** /playQueues/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*PlayQueuesApi* | [**play_queues_id_relationships_past_get**](docs/PlayQueuesApi.md#play_queues_id_relationships_past_get) | **GET** /playQueues/{id}/relationships/past | Get past relationship (\&quot;to-many\&quot;).
*PlayQueuesApi* | [**play_queues_post**](docs/PlayQueuesApi.md#play_queues_post) | **POST** /playQueues | Create single playQueue.
*PlaylistGenerationSchedulesApi* | [**playlist_generation_schedules_get**](docs/PlaylistGenerationSchedulesApi.md#playlist_generation_schedules_get) | **GET** /playlistGenerationSchedules | Get multiple playlistGenerationSchedules.
*PlaylistGenerationSchedulesApi* | [**playlist_generation_schedules_id_delete**](docs/PlaylistGenerationSchedulesApi.md#playlist_generation_schedules_id_delete) | **DELETE** /playlistGenerationSchedules/{id} | Delete single playlistGenerationSchedule.
*PlaylistGenerationSchedulesApi* | [**playlist_generation_schedules_id_get**](docs/PlaylistGenerationSchedulesApi.md#playlist_generation_schedules_id_get) | **GET** /playlistGenerationSchedules/{id} | Get single playlistGenerationSchedule.
*PlaylistGenerationSchedulesApi* | [**playlist_generation_schedules_id_patch**](docs/PlaylistGenerationSchedulesApi.md#playlist_generation_schedules_id_patch) | **PATCH** /playlistGenerationSchedules/{id} | Update single playlistGenerationSchedule.
*PlaylistGenerationSchedulesApi* | [**playlist_generation_schedules_id_relationships_playlist_get**](docs/PlaylistGenerationSchedulesApi.md#playlist_generation_schedules_id_relationships_playlist_get) | **GET** /playlistGenerationSchedules/{id}/relationships/playlist | Get playlist relationship (\&quot;to-one\&quot;).
*PlaylistGenerationSchedulesApi* | [**playlist_generation_schedules_post**](docs/PlaylistGenerationSchedulesApi.md#playlist_generation_schedules_post) | **POST** /playlistGenerationSchedules | Create single playlistGenerationSchedule.
*PlaylistGenerationsApi* | [**playlist_generations_get**](docs/PlaylistGenerationsApi.md#playlist_generations_get) | **GET** /playlistGenerations | Get multiple playlistGenerations.
*PlaylistGenerationsApi* | [**playlist_generations_id_get**](docs/PlaylistGenerationsApi.md#playlist_generations_id_get) | **GET** /playlistGenerations/{id} | Get single playlistGeneration.
*PlaylistGenerationsApi* | [**playlist_generations_id_relationships_base_generation_get**](docs/PlaylistGenerationsApi.md#playlist_generations_id_relationships_base_generation_get) | **GET** /playlistGenerations/{id}/relationships/baseGeneration | Get baseGeneration relationship (\&quot;to-one\&quot;).
*PlaylistGenerationsApi* | [**playlist_generations_id_relationships_playlist_get**](docs/PlaylistGenerationsApi.md#playlist_generations_id_relationships_playlist_get) | **GET** /playlistGenerations/{id}/relationships/playlist | Get playlist relationship (\&quot;to-one\&quot;).
*PlaylistGenerationsApi* | [**playlist_generations_id_relationships_track_preferences_delete**](docs/PlaylistGenerationsApi.md#playlist_generations_id_relationships_track_preferences_delete) | **DELETE** /playlistGenerations/{id}/relationships/trackPreferences | Delete from trackPreferences relationship (\&quot;to-many\&quot;).
*PlaylistGenerationsApi* | [**playlist_generations_id_relationships_track_preferences_get**](docs/PlaylistGenerationsApi.md#playlist_generations_id_relationships_track_preferences_get) | **GET** /playlistGenerations/{id}/relationships/trackPreferences | Get trackPreferences relationship (\&quot;to-many\&quot;).
*PlaylistGenerationsApi* | [**playlist_generations_id_relationships_track_preferences_patch**](docs/PlaylistGenerationsApi.md#playlist_generations_id_relationships_track_preferences_patch) | **PATCH** /playlistGenerations/{id}/relationships/trackPreferences | Update trackPreferences relationship (\&quot;to-many\&quot;).
*PlaylistGenerationsApi* | [**playlist_generations_id_relationships_track_preferences_post**](docs/PlaylistGenerationsApi.md#playlist_generations_id_relationships_track_preferences_post) | **POST** /playlistGenerations/{id}/relationships/trackPreferences | Add to trackPreferences relationship (\&quot;to-many\&quot;).
*PlaylistGenerationsApi* | [**playlist_generations_post**](docs/PlaylistGenerationsApi.md#playlist_generations_post) | **POST** /playlistGenerations | Create single playlistGeneration.
*PlaylistsApi* | [**playlists_get**](docs/PlaylistsApi.md#playlists_get) | **GET** /playlists | Get multiple playlists.
*PlaylistsApi* | [**playlists_id_delete**](docs/PlaylistsApi.md#playlists_id_delete) | **DELETE** /playlists/{id} | Delete single playlist.
*PlaylistsApi* | [**playlists_id_get**](docs/PlaylistsApi.md#playlists_id_get) | **GET** /playlists/{id} | Get single playlist.
*PlaylistsApi* | [**playlists_id_patch**](docs/PlaylistsApi.md#playlists_id_patch) | **PATCH** /playlists/{id} | Update single playlist.
*PlaylistsApi* | [**playlists_id_relationships_collaborator_profiles_delete**](docs/PlaylistsApi.md#playlists_id_relationships_collaborator_profiles_delete) | **DELETE** /playlists/{id}/relationships/collaboratorProfiles | Delete from collaboratorProfiles relationship (\&quot;to-many\&quot;).
*PlaylistsApi* | [**playlists_id_relationships_collaborator_profiles_get**](docs/PlaylistsApi.md#playlists_id_relationships_collaborator_profiles_get) | **GET** /playlists/{id}/relationships/collaboratorProfiles | Get collaboratorProfiles relationship (\&quot;to-many\&quot;).
*PlaylistsApi* | [**playlists_id_relationships_collaborators_get**](docs/PlaylistsApi.md#playlists_id_relationships_collaborators_get) | **GET** /playlists/{id}/relationships/collaborators | Get collaborators relationship (\&quot;to-many\&quot;).
*PlaylistsApi* | [**playlists_id_relationships_cover_art_get**](docs/PlaylistsApi.md#playlists_id_relationships_cover_art_get) | **GET** /playlists/{id}/relationships/coverArt | Get coverArt relationship (\&quot;to-many\&quot;).
*PlaylistsApi* | [**playlists_id_relationships_cover_art_patch**](docs/PlaylistsApi.md#playlists_id_relationships_cover_art_patch) | **PATCH** /playlists/{id}/relationships/coverArt | Update coverArt relationship (\&quot;to-many\&quot;).
*PlaylistsApi* | [**playlists_id_relationships_curators_get**](docs/PlaylistsApi.md#playlists_id_relationships_curators_get) | **GET** /playlists/{id}/relationships/curators | Get curators relationship (\&quot;to-many\&quot;).
*PlaylistsApi* | [**playlists_id_relationships_items_delete**](docs/PlaylistsApi.md#playlists_id_relationships_items_delete) | **DELETE** /playlists/{id}/relationships/items | Delete from items relationship (\&quot;to-many\&quot;).
*PlaylistsApi* | [**playlists_id_relationships_items_get**](docs/PlaylistsApi.md#playlists_id_relationships_items_get) | **GET** /playlists/{id}/relationships/items | Get items relationship (\&quot;to-many\&quot;).
*PlaylistsApi* | [**playlists_id_relationships_items_patch**](docs/PlaylistsApi.md#playlists_id_relationships_items_patch) | **PATCH** /playlists/{id}/relationships/items | Update items relationship (\&quot;to-many\&quot;).
*PlaylistsApi* | [**playlists_id_relationships_items_post**](docs/PlaylistsApi.md#playlists_id_relationships_items_post) | **POST** /playlists/{id}/relationships/items | Add to items relationship (\&quot;to-many\&quot;).
*PlaylistsApi* | [**playlists_id_relationships_owner_profiles_get**](docs/PlaylistsApi.md#playlists_id_relationships_owner_profiles_get) | **GET** /playlists/{id}/relationships/ownerProfiles | Get ownerProfiles relationship (\&quot;to-many\&quot;).
*PlaylistsApi* | [**playlists_id_relationships_owners_get**](docs/PlaylistsApi.md#playlists_id_relationships_owners_get) | **GET** /playlists/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*PlaylistsApi* | [**playlists_id_relationships_suggested_cover_arts_get**](docs/PlaylistsApi.md#playlists_id_relationships_suggested_cover_arts_get) | **GET** /playlists/{id}/relationships/suggestedCoverArts | Get suggestedCoverArts relationship (\&quot;to-many\&quot;).
*PlaylistsApi* | [**playlists_post**](docs/PlaylistsApi.md#playlists_post) | **POST** /playlists | Create single playlist.
*PriceConfigurationsApi* | [**price_configurations_get**](docs/PriceConfigurationsApi.md#price_configurations_get) | **GET** /priceConfigurations | Get multiple priceConfigurations.
*PriceConfigurationsApi* | [**price_configurations_id_get**](docs/PriceConfigurationsApi.md#price_configurations_id_get) | **GET** /priceConfigurations/{id} | Get single priceConfiguration.
*PriceConfigurationsApi* | [**price_configurations_post**](docs/PriceConfigurationsApi.md#price_configurations_post) | **POST** /priceConfigurations | Create single priceConfiguration.
*ProviderOwnersApi* | [**provider_owners_get**](docs/ProviderOwnersApi.md#provider_owners_get) | **GET** /providerOwners | Get multiple providerOwners.
*ProviderOwnersApi* | [**provider_owners_id_relationships_owners_get**](docs/ProviderOwnersApi.md#provider_owners_id_relationships_owners_get) | **GET** /providerOwners/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*ProviderOwnersApi* | [**provider_owners_id_relationships_provider_get**](docs/ProviderOwnersApi.md#provider_owners_id_relationships_provider_get) | **GET** /providerOwners/{id}/relationships/provider | Get provider relationship (\&quot;to-one\&quot;).
*ProviderProductInfosApi* | [**provider_product_infos_get**](docs/ProviderProductInfosApi.md#provider_product_infos_get) | **GET** /providerProductInfos | Get multiple providerProductInfos.
*ProviderProductInfosApi* | [**provider_product_infos_id_relationships_provider_get**](docs/ProviderProductInfosApi.md#provider_product_infos_id_relationships_provider_get) | **GET** /providerProductInfos/{id}/relationships/provider | Get provider relationship (\&quot;to-one\&quot;).
*ProviderProductInfosApi* | [**provider_product_infos_id_relationships_subject_get**](docs/ProviderProductInfosApi.md#provider_product_infos_id_relationships_subject_get) | **GET** /providerProductInfos/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).
*ProvidersApi* | [**providers_id_get**](docs/ProvidersApi.md#providers_id_get) | **GET** /providers/{id} | Get single provider.
*PurchasesApi* | [**purchases_get**](docs/PurchasesApi.md#purchases_get) | **GET** /purchases | Get multiple purchases.
*PurchasesApi* | [**purchases_id_relationships_owners_get**](docs/PurchasesApi.md#purchases_id_relationships_owners_get) | **GET** /purchases/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*PurchasesApi* | [**purchases_id_relationships_subject_get**](docs/PurchasesApi.md#purchases_id_relationships_subject_get) | **GET** /purchases/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).
*ReactionSummariesApi* | [**reaction_summaries_get**](docs/ReactionSummariesApi.md#reaction_summaries_get) | **GET** /reactionSummaries | Get multiple reactionSummaries.
*ReactionSummariesApi* | [**reaction_summaries_id_relationships_subject_get**](docs/ReactionSummariesApi.md#reaction_summaries_id_relationships_subject_get) | **GET** /reactionSummaries/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).
*ReactionsApi* | [**reactions_get**](docs/ReactionsApi.md#reactions_get) | **GET** /reactions | Get multiple reactions.
*ReactionsApi* | [**reactions_id_delete**](docs/ReactionsApi.md#reactions_id_delete) | **DELETE** /reactions/{id} | Delete single reaction.
*ReactionsApi* | [**reactions_id_relationships_author_get**](docs/ReactionsApi.md#reactions_id_relationships_author_get) | **GET** /reactions/{id}/relationships/author | Get author relationship (\&quot;to-one\&quot;).
*ReactionsApi* | [**reactions_id_relationships_owners_get**](docs/ReactionsApi.md#reactions_id_relationships_owners_get) | **GET** /reactions/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*ReactionsApi* | [**reactions_id_relationships_subject_get**](docs/ReactionsApi.md#reactions_id_relationships_subject_get) | **GET** /reactions/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).
*ReactionsApi* | [**reactions_post**](docs/ReactionsApi.md#reactions_post) | **POST** /reactions | Create single reaction.
*ResourceGrantInvitationsApi* | [**resource_grant_invitations_get**](docs/ResourceGrantInvitationsApi.md#resource_grant_invitations_get) | **GET** /resourceGrantInvitations | Get multiple resourceGrantInvitations.
*ResourceGrantInvitationsApi* | [**resource_grant_invitations_id_delete**](docs/ResourceGrantInvitationsApi.md#resource_grant_invitations_id_delete) | **DELETE** /resourceGrantInvitations/{id} | Delete single resourceGrantInvitation.
*ResourceGrantInvitationsApi* | [**resource_grant_invitations_id_get**](docs/ResourceGrantInvitationsApi.md#resource_grant_invitations_id_get) | **GET** /resourceGrantInvitations/{id} | Get single resourceGrantInvitation.
*ResourceGrantInvitationsApi* | [**resource_grant_invitations_id_patch**](docs/ResourceGrantInvitationsApi.md#resource_grant_invitations_id_patch) | **PATCH** /resourceGrantInvitations/{id} | Update single resourceGrantInvitation.
*ResourceGrantInvitationsApi* | [**resource_grant_invitations_id_relationships_owners_get**](docs/ResourceGrantInvitationsApi.md#resource_grant_invitations_id_relationships_owners_get) | **GET** /resourceGrantInvitations/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*ResourceGrantInvitationsApi* | [**resource_grant_invitations_id_relationships_preview_grant_get**](docs/ResourceGrantInvitationsApi.md#resource_grant_invitations_id_relationships_preview_grant_get) | **GET** /resourceGrantInvitations/{id}/relationships/previewGrant | Get previewGrant relationship (\&quot;to-one\&quot;).
*ResourceGrantInvitationsApi* | [**resource_grant_invitations_id_relationships_subject_get**](docs/ResourceGrantInvitationsApi.md#resource_grant_invitations_id_relationships_subject_get) | **GET** /resourceGrantInvitations/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).
*ResourceGrantInvitationsApi* | [**resource_grant_invitations_post**](docs/ResourceGrantInvitationsApi.md#resource_grant_invitations_post) | **POST** /resourceGrantInvitations | Create single resourceGrantInvitation.
*ResourceGrantsApi* | [**resource_grants_get**](docs/ResourceGrantsApi.md#resource_grants_get) | **GET** /resourceGrants | Get multiple resourceGrants.
*ResourceGrantsApi* | [**resource_grants_id_delete**](docs/ResourceGrantsApi.md#resource_grants_id_delete) | **DELETE** /resourceGrants/{id} | Delete single resourceGrant.
*ResourceGrantsApi* | [**resource_grants_id_get**](docs/ResourceGrantsApi.md#resource_grants_id_get) | **GET** /resourceGrants/{id} | Get single resourceGrant.
*ResourceGrantsApi* | [**resource_grants_id_patch**](docs/ResourceGrantsApi.md#resource_grants_id_patch) | **PATCH** /resourceGrants/{id} | Update single resourceGrant.
*ResourceGrantsApi* | [**resource_grants_id_relationships_grantee_get**](docs/ResourceGrantsApi.md#resource_grants_id_relationships_grantee_get) | **GET** /resourceGrants/{id}/relationships/grantee | Get grantee relationship (\&quot;to-one\&quot;).
*ResourceGrantsApi* | [**resource_grants_id_relationships_invitation_get**](docs/ResourceGrantsApi.md#resource_grants_id_relationships_invitation_get) | **GET** /resourceGrants/{id}/relationships/invitation | Get invitation relationship (\&quot;to-one\&quot;).
*ResourceGrantsApi* | [**resource_grants_id_relationships_subject_get**](docs/ResourceGrantsApi.md#resource_grants_id_relationships_subject_get) | **GET** /resourceGrants/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).
*ResourceGrantsApi* | [**resource_grants_post**](docs/ResourceGrantsApi.md#resource_grants_post) | **POST** /resourceGrants | Create single resourceGrant.
*SavedSharesApi* | [**saved_shares_post**](docs/SavedSharesApi.md#saved_shares_post) | **POST** /savedShares | Create single savedShare.
*ScopesApi* | [**scopes_get**](docs/ScopesApi.md#scopes_get) | **GET** /scopes | Get multiple scopes.
*SearchHistoryEntriesApi* | [**search_history_entries_id_delete**](docs/SearchHistoryEntriesApi.md#search_history_entries_id_delete) | **DELETE** /searchHistoryEntries/{id} | Delete single searchHistoryEntrie.
*SearchResultsApi* | [**search_results_get**](docs/SearchResultsApi.md#search_results_get) | **GET** /searchResults | Get search results by query.
*SearchResultsApi* | [**search_results_id_relationships_albums_get**](docs/SearchResultsApi.md#search_results_id_relationships_albums_get) | **GET** /searchResults/{id}/relationships/albums | Get albums relationship (\&quot;to-many\&quot;).
*SearchResultsApi* | [**search_results_id_relationships_artists_get**](docs/SearchResultsApi.md#search_results_id_relationships_artists_get) | **GET** /searchResults/{id}/relationships/artists | Get artists relationship (\&quot;to-many\&quot;).
*SearchResultsApi* | [**search_results_id_relationships_playlists_get**](docs/SearchResultsApi.md#search_results_id_relationships_playlists_get) | **GET** /searchResults/{id}/relationships/playlists | Get playlists relationship (\&quot;to-many\&quot;).
*SearchResultsApi* | [**search_results_id_relationships_top_hits_get**](docs/SearchResultsApi.md#search_results_id_relationships_top_hits_get) | **GET** /searchResults/{id}/relationships/topHits | Get topHits relationship (\&quot;to-many\&quot;).
*SearchResultsApi* | [**search_results_id_relationships_tracks_get**](docs/SearchResultsApi.md#search_results_id_relationships_tracks_get) | **GET** /searchResults/{id}/relationships/tracks | Get tracks relationship (\&quot;to-many\&quot;).
*SearchResultsApi* | [**search_results_id_relationships_videos_get**](docs/SearchResultsApi.md#search_results_id_relationships_videos_get) | **GET** /searchResults/{id}/relationships/videos | Get videos relationship (\&quot;to-many\&quot;).
*SearchSuggestionsApi* | [**search_suggestions_get**](docs/SearchSuggestionsApi.md#search_suggestions_get) | **GET** /searchSuggestions | Get search suggestions by query.
*SearchSuggestionsApi* | [**search_suggestions_id_relationships_direct_hits_get**](docs/SearchSuggestionsApi.md#search_suggestions_id_relationships_direct_hits_get) | **GET** /searchSuggestions/{id}/relationships/directHits | Get directHits relationship (\&quot;to-many\&quot;).
*SearchSuggestionsApi* | [**search_suggestions_id_relationships_history_get**](docs/SearchSuggestionsApi.md#search_suggestions_id_relationships_history_get) | **GET** /searchSuggestions/{id}/relationships/history | Get history relationship (\&quot;to-many\&quot;).
*SharesApi* | [**shares_get**](docs/SharesApi.md#shares_get) | **GET** /shares | Get multiple shares.
*SharesApi* | [**shares_id_delete**](docs/SharesApi.md#shares_id_delete) | **DELETE** /shares/{id} | Delete single share.
*SharesApi* | [**shares_id_get**](docs/SharesApi.md#shares_id_get) | **GET** /shares/{id} | Get single share.
*SharesApi* | [**shares_id_patch**](docs/SharesApi.md#shares_id_patch) | **PATCH** /shares/{id} | Update single share.
*SharesApi* | [**shares_id_relationships_owners_get**](docs/SharesApi.md#shares_id_relationships_owners_get) | **GET** /shares/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*SharesApi* | [**shares_id_relationships_shared_resources_get**](docs/SharesApi.md#shares_id_relationships_shared_resources_get) | **GET** /shares/{id}/relationships/sharedResources | Get sharedResources relationship (\&quot;to-many\&quot;).
*SharesApi* | [**shares_post**](docs/SharesApi.md#shares_post) | **POST** /shares | Create single share.
*SharingSummariesApi* | [**sharing_summaries_get**](docs/SharingSummariesApi.md#sharing_summaries_get) | **GET** /sharingSummaries | Get multiple sharingSummaries.
*SharingSummariesApi* | [**sharing_summaries_id_relationships_subject_get**](docs/SharingSummariesApi.md#sharing_summaries_id_relationships_subject_get) | **GET** /sharingSummaries/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).
*SquareConnectionsApi* | [**square_connections_id_get**](docs/SquareConnectionsApi.md#square_connections_id_get) | **GET** /squareConnections/{id} | Get single squareConnection.
*SquareConnectionsApi* | [**square_connections_id_relationships_selected_site_get**](docs/SquareConnectionsApi.md#square_connections_id_relationships_selected_site_get) | **GET** /squareConnections/{id}/relationships/selectedSite | Get selectedSite relationship (\&quot;to-one\&quot;).
*SquareConnectionsApi* | [**square_connections_id_relationships_selected_site_patch**](docs/SquareConnectionsApi.md#square_connections_id_relationships_selected_site_patch) | **PATCH** /squareConnections/{id}/relationships/selectedSite | Update selectedSite relationship (\&quot;to-one\&quot;).
*SquareConnectionsApi* | [**square_connections_id_relationships_sites_get**](docs/SquareConnectionsApi.md#square_connections_id_relationships_sites_get) | **GET** /squareConnections/{id}/relationships/sites | Get sites relationship (\&quot;to-many\&quot;).
*SquareConnectionsApi* | [**square_connections_post**](docs/SquareConnectionsApi.md#square_connections_post) | **POST** /squareConnections | Create single squareConnection.
*SquareItemVariationPhysicalCountsApi* | [**square_item_variation_physical_counts_post**](docs/SquareItemVariationPhysicalCountsApi.md#square_item_variation_physical_counts_post) | **POST** /squareItemVariationPhysicalCounts | Create single squareItemVariationPhysicalCount.
*SquareItemVariationsApi* | [**operations_post**](docs/SquareItemVariationsApi.md#operations_post) | **POST** /operations | Commit atomic resource operations
*SquareItemVariationsApi* | [**square_item_variations_id_delete**](docs/SquareItemVariationsApi.md#square_item_variations_id_delete) | **DELETE** /squareItemVariations/{id} | Delete single squareItemVariation.
*SquareItemVariationsApi* | [**square_item_variations_id_get**](docs/SquareItemVariationsApi.md#square_item_variations_id_get) | **GET** /squareItemVariations/{id} | Get single squareItemVariation.
*SquareItemVariationsApi* | [**square_item_variations_id_patch**](docs/SquareItemVariationsApi.md#square_item_variations_id_patch) | **PATCH** /squareItemVariations/{id} | Update single squareItemVariation.
*SquareItemVariationsApi* | [**square_item_variations_id_relationships_artworks_get**](docs/SquareItemVariationsApi.md#square_item_variations_id_relationships_artworks_get) | **GET** /squareItemVariations/{id}/relationships/artworks | Get artworks relationship (\&quot;to-many\&quot;).
*SquareItemVariationsApi* | [**square_item_variations_id_relationships_artworks_patch**](docs/SquareItemVariationsApi.md#square_item_variations_id_relationships_artworks_patch) | **PATCH** /squareItemVariations/{id}/relationships/artworks | Update artworks relationship (\&quot;to-many\&quot;).
*SquareItemVariationsApi* | [**square_item_variations_id_relationships_owners_get**](docs/SquareItemVariationsApi.md#square_item_variations_id_relationships_owners_get) | **GET** /squareItemVariations/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*SquareItemVariationsApi* | [**square_item_variations_post**](docs/SquareItemVariationsApi.md#square_item_variations_post) | **POST** /squareItemVariations | Create single squareItemVariation.
*SquareItemsApi* | [**operations_post**](docs/SquareItemsApi.md#operations_post) | **POST** /operations | Commit atomic resource operations
*SquareItemsApi* | [**square_items_get**](docs/SquareItemsApi.md#square_items_get) | **GET** /squareItems | Get multiple squareItems.
*SquareItemsApi* | [**square_items_id_delete**](docs/SquareItemsApi.md#square_items_id_delete) | **DELETE** /squareItems/{id} | Delete single squareItem.
*SquareItemsApi* | [**square_items_id_get**](docs/SquareItemsApi.md#square_items_id_get) | **GET** /squareItems/{id} | Get single squareItem.
*SquareItemsApi* | [**square_items_id_patch**](docs/SquareItemsApi.md#square_items_id_patch) | **PATCH** /squareItems/{id} | Update single squareItem.
*SquareItemsApi* | [**square_items_id_relationships_artworks_get**](docs/SquareItemsApi.md#square_items_id_relationships_artworks_get) | **GET** /squareItems/{id}/relationships/artworks | Get artworks relationship (\&quot;to-many\&quot;).
*SquareItemsApi* | [**square_items_id_relationships_artworks_patch**](docs/SquareItemsApi.md#square_items_id_relationships_artworks_patch) | **PATCH** /squareItems/{id}/relationships/artworks | Update artworks relationship (\&quot;to-many\&quot;).
*SquareItemsApi* | [**square_items_id_relationships_owners_get**](docs/SquareItemsApi.md#square_items_id_relationships_owners_get) | **GET** /squareItems/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*SquareItemsApi* | [**square_items_id_relationships_variations_get**](docs/SquareItemsApi.md#square_items_id_relationships_variations_get) | **GET** /squareItems/{id}/relationships/variations | Get variations relationship (\&quot;to-many\&quot;).
*SquareItemsApi* | [**square_items_id_relationships_variations_patch**](docs/SquareItemsApi.md#square_items_id_relationships_variations_patch) | **PATCH** /squareItems/{id}/relationships/variations | Update variations relationship (\&quot;to-many\&quot;).
*SquareSitesApi* | [**square_sites_id_relationships_items_delete**](docs/SquareSitesApi.md#square_sites_id_relationships_items_delete) | **DELETE** /squareSites/{id}/relationships/items | Delete from items relationship (\&quot;to-many\&quot;).
*SquareSitesApi* | [**square_sites_id_relationships_items_get**](docs/SquareSitesApi.md#square_sites_id_relationships_items_get) | **GET** /squareSites/{id}/relationships/items | Get items relationship (\&quot;to-many\&quot;).
*SquareSitesApi* | [**square_sites_id_relationships_items_post**](docs/SquareSitesApi.md#square_sites_id_relationships_items_post) | **POST** /squareSites/{id}/relationships/items | Add to items relationship (\&quot;to-many\&quot;).
*StripeConnectionsApi* | [**stripe_connections_get**](docs/StripeConnectionsApi.md#stripe_connections_get) | **GET** /stripeConnections | Get multiple stripeConnections.
*StripeConnectionsApi* | [**stripe_connections_id_relationships_owners_get**](docs/StripeConnectionsApi.md#stripe_connections_id_relationships_owners_get) | **GET** /stripeConnections/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*StripeConnectionsApi* | [**stripe_connections_post**](docs/StripeConnectionsApi.md#stripe_connections_post) | **POST** /stripeConnections | Create single stripeConnection.
*StripeDashboardLinksApi* | [**stripe_dashboard_links_get**](docs/StripeDashboardLinksApi.md#stripe_dashboard_links_get) | **GET** /stripeDashboardLinks | Get multiple stripeDashboardLinks.
*StripeDashboardLinksApi* | [**stripe_dashboard_links_id_relationships_owners_get**](docs/StripeDashboardLinksApi.md#stripe_dashboard_links_id_relationships_owners_get) | **GET** /stripeDashboardLinks/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*StudioHomeEventTilesApi* | [**studio_home_event_tiles_id_get**](docs/StudioHomeEventTilesApi.md#studio_home_event_tiles_id_get) | **GET** /studioHomeEventTiles/{id} | Get single studioHomeEventTile.
*StudioHomeInsightTilesApi* | [**studio_home_insight_tiles_id_get**](docs/StudioHomeInsightTilesApi.md#studio_home_insight_tiles_id_get) | **GET** /studioHomeInsightTiles/{id} | Get single studioHomeInsightTile.
*StudioHomeMerchTilesApi* | [**studio_home_merch_tiles_id_get**](docs/StudioHomeMerchTilesApi.md#studio_home_merch_tiles_id_get) | **GET** /studioHomeMerchTiles/{id} | Get single studioHomeMerchTile.
*StudioHomeMerchTilesApi* | [**studio_home_merch_tiles_id_relationships_items_get**](docs/StudioHomeMerchTilesApi.md#studio_home_merch_tiles_id_relationships_items_get) | **GET** /studioHomeMerchTiles/{id}/relationships/items | Get items relationship (\&quot;to-many\&quot;).
*StudioHomeMusicTilesApi* | [**studio_home_music_tiles_id_get**](docs/StudioHomeMusicTilesApi.md#studio_home_music_tiles_id_get) | **GET** /studioHomeMusicTiles/{id} | Get single studioHomeMusicTile.
*SubscriptionPriceChangeDecisionsApi* | [**subscription_price_change_decisions_get**](docs/SubscriptionPriceChangeDecisionsApi.md#subscription_price_change_decisions_get) | **GET** /subscriptionPriceChangeDecisions | Get multiple subscriptionPriceChangeDecisions.
*SubscriptionPriceChangeDecisionsApi* | [**subscription_price_change_decisions_id_patch**](docs/SubscriptionPriceChangeDecisionsApi.md#subscription_price_change_decisions_id_patch) | **PATCH** /subscriptionPriceChangeDecisions/{id} | Update single subscriptionPriceChangeDecision.
*SubscriptionPriceChangeDecisionsApi* | [**subscription_price_change_decisions_id_relationships_price_change_get**](docs/SubscriptionPriceChangeDecisionsApi.md#subscription_price_change_decisions_id_relationships_price_change_get) | **GET** /subscriptionPriceChangeDecisions/{id}/relationships/priceChange | Get priceChange relationship (\&quot;to-one\&quot;).
*SubscriptionPriceChangeDecisionsApi* | [**subscription_price_change_decisions_post**](docs/SubscriptionPriceChangeDecisionsApi.md#subscription_price_change_decisions_post) | **POST** /subscriptionPriceChangeDecisions | Create single subscriptionPriceChangeDecision.
*TemporaryUserTokensApi* | [**temporary_user_tokens_id_get**](docs/TemporaryUserTokensApi.md#temporary_user_tokens_id_get) | **GET** /temporaryUserTokens/{id} | Get single temporaryUserToken.
*TemporaryUserTokensApi* | [**temporary_user_tokens_id_relationships_owners_get**](docs/TemporaryUserTokensApi.md#temporary_user_tokens_id_relationships_owners_get) | **GET** /temporaryUserTokens/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*TemporaryUserTokensApi* | [**temporary_user_tokens_post**](docs/TemporaryUserTokensApi.md#temporary_user_tokens_post) | **POST** /temporaryUserTokens | Create single temporaryUserToken.
*TermsApi* | [**terms_get**](docs/TermsApi.md#terms_get) | **GET** /terms | Get multiple terms.
*TermsApi* | [**terms_id_get**](docs/TermsApi.md#terms_id_get) | **GET** /terms/{id} | Get single term.
*TrackFilesApi* | [**track_files_id_get**](docs/TrackFilesApi.md#track_files_id_get) | **GET** /trackFiles/{id} | Get single trackFile.
*TrackManifestsApi* | [**track_manifests_id_get**](docs/TrackManifestsApi.md#track_manifests_id_get) | **GET** /trackManifests/{id} | Get single trackManifest.
*TrackSourceFilesApi* | [**track_source_files_id_get**](docs/TrackSourceFilesApi.md#track_source_files_id_get) | **GET** /trackSourceFiles/{id} | Get single trackSourceFile.
*TrackSourceFilesApi* | [**track_source_files_id_relationships_comment_summary_get**](docs/TrackSourceFilesApi.md#track_source_files_id_relationships_comment_summary_get) | **GET** /trackSourceFiles/{id}/relationships/commentSummary | Get commentSummary relationship (\&quot;to-one\&quot;).
*TrackSourceFilesApi* | [**track_source_files_id_relationships_owners_get**](docs/TrackSourceFilesApi.md#track_source_files_id_relationships_owners_get) | **GET** /trackSourceFiles/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*TrackSourceFilesApi* | [**track_source_files_id_relationships_reaction_summary_get**](docs/TrackSourceFilesApi.md#track_source_files_id_relationships_reaction_summary_get) | **GET** /trackSourceFiles/{id}/relationships/reactionSummary | Get reactionSummary relationship (\&quot;to-one\&quot;).
*TrackSourceFilesApi* | [**track_source_files_post**](docs/TrackSourceFilesApi.md#track_source_files_post) | **POST** /trackSourceFiles | Create single trackSourceFile.
*TrackStatisticsApi* | [**track_statistics_id_get**](docs/TrackStatisticsApi.md#track_statistics_id_get) | **GET** /trackStatistics/{id} | Get single trackStatistic.
*TrackStatisticsApi* | [**track_statistics_id_relationships_owners_get**](docs/TrackStatisticsApi.md#track_statistics_id_relationships_owners_get) | **GET** /trackStatistics/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*TracksApi* | [**tracks_get**](docs/TracksApi.md#tracks_get) | **GET** /tracks | Get multiple tracks.
*TracksApi* | [**tracks_id_delete**](docs/TracksApi.md#tracks_id_delete) | **DELETE** /tracks/{id} | Delete single track.
*TracksApi* | [**tracks_id_get**](docs/TracksApi.md#tracks_id_get) | **GET** /tracks/{id} | Get single track.
*TracksApi* | [**tracks_id_patch**](docs/TracksApi.md#tracks_id_patch) | **PATCH** /tracks/{id} | Update single track.
*TracksApi* | [**tracks_id_relationships_albums_get**](docs/TracksApi.md#tracks_id_relationships_albums_get) | **GET** /tracks/{id}/relationships/albums | Get albums relationship (\&quot;to-many\&quot;).
*TracksApi* | [**tracks_id_relationships_albums_patch**](docs/TracksApi.md#tracks_id_relationships_albums_patch) | **PATCH** /tracks/{id}/relationships/albums | Update albums relationship (\&quot;to-many\&quot;).
*TracksApi* | [**tracks_id_relationships_artists_get**](docs/TracksApi.md#tracks_id_relationships_artists_get) | **GET** /tracks/{id}/relationships/artists | Get artists relationship (\&quot;to-many\&quot;).
*TracksApi* | [**tracks_id_relationships_artists_patch**](docs/TracksApi.md#tracks_id_relationships_artists_patch) | **PATCH** /tracks/{id}/relationships/artists | Update artists relationship (\&quot;to-many\&quot;).
*TracksApi* | [**tracks_id_relationships_credits_get**](docs/TracksApi.md#tracks_id_relationships_credits_get) | **GET** /tracks/{id}/relationships/credits | Get credits relationship (\&quot;to-many\&quot;).
*TracksApi* | [**tracks_id_relationships_download_get**](docs/TracksApi.md#tracks_id_relationships_download_get) | **GET** /tracks/{id}/relationships/download | Get download relationship (\&quot;to-one\&quot;).
*TracksApi* | [**tracks_id_relationships_genres_get**](docs/TracksApi.md#tracks_id_relationships_genres_get) | **GET** /tracks/{id}/relationships/genres | Get genres relationship (\&quot;to-many\&quot;).
*TracksApi* | [**tracks_id_relationships_lyrics_get**](docs/TracksApi.md#tracks_id_relationships_lyrics_get) | **GET** /tracks/{id}/relationships/lyrics | Get lyrics relationship (\&quot;to-many\&quot;).
*TracksApi* | [**tracks_id_relationships_metadata_status_get**](docs/TracksApi.md#tracks_id_relationships_metadata_status_get) | **GET** /tracks/{id}/relationships/metadataStatus | Get metadataStatus relationship (\&quot;to-one\&quot;).
*TracksApi* | [**tracks_id_relationships_owners_get**](docs/TracksApi.md#tracks_id_relationships_owners_get) | **GET** /tracks/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*TracksApi* | [**tracks_id_relationships_price_config_get**](docs/TracksApi.md#tracks_id_relationships_price_config_get) | **GET** /tracks/{id}/relationships/priceConfig | Get priceConfig relationship (\&quot;to-one\&quot;).
*TracksApi* | [**tracks_id_relationships_providers_get**](docs/TracksApi.md#tracks_id_relationships_providers_get) | **GET** /tracks/{id}/relationships/providers | Get providers relationship (\&quot;to-many\&quot;).
*TracksApi* | [**tracks_id_relationships_radio_get**](docs/TracksApi.md#tracks_id_relationships_radio_get) | **GET** /tracks/{id}/relationships/radio | Get radio relationship (\&quot;to-many\&quot;).
*TracksApi* | [**tracks_id_relationships_replacement_get**](docs/TracksApi.md#tracks_id_relationships_replacement_get) | **GET** /tracks/{id}/relationships/replacement | Get replacement relationship (\&quot;to-one\&quot;).
*TracksApi* | [**tracks_id_relationships_shares_get**](docs/TracksApi.md#tracks_id_relationships_shares_get) | **GET** /tracks/{id}/relationships/shares | Get shares relationship (\&quot;to-many\&quot;).
*TracksApi* | [**tracks_id_relationships_similar_tracks_get**](docs/TracksApi.md#tracks_id_relationships_similar_tracks_get) | **GET** /tracks/{id}/relationships/similarTracks | Get similarTracks relationship (\&quot;to-many\&quot;).
*TracksApi* | [**tracks_id_relationships_source_file_get**](docs/TracksApi.md#tracks_id_relationships_source_file_get) | **GET** /tracks/{id}/relationships/sourceFile | Get sourceFile relationship (\&quot;to-one\&quot;).
*TracksApi* | [**tracks_id_relationships_suggested_tracks_get**](docs/TracksApi.md#tracks_id_relationships_suggested_tracks_get) | **GET** /tracks/{id}/relationships/suggestedTracks | Get suggestedTracks relationship (\&quot;to-many\&quot;).
*TracksApi* | [**tracks_id_relationships_track_statistics_get**](docs/TracksApi.md#tracks_id_relationships_track_statistics_get) | **GET** /tracks/{id}/relationships/trackStatistics | Get trackStatistics relationship (\&quot;to-one\&quot;).
*TracksApi* | [**tracks_id_relationships_usage_rules_get**](docs/TracksApi.md#tracks_id_relationships_usage_rules_get) | **GET** /tracks/{id}/relationships/usageRules | Get usageRules relationship (\&quot;to-one\&quot;).
*TracksApi* | [**tracks_post**](docs/TracksApi.md#tracks_post) | **POST** /tracks | Create single track.
*TracksMetadataStatusApi* | [**tracks_metadata_status_id_get**](docs/TracksMetadataStatusApi.md#tracks_metadata_status_id_get) | **GET** /tracksMetadataStatus/{id} | Get single tracksMetadataStatu.
*UsageRulesApi* | [**usage_rules_id_get**](docs/UsageRulesApi.md#usage_rules_id_get) | **GET** /usageRules/{id} | Get single usageRule.
*UsageRulesApi* | [**usage_rules_post**](docs/UsageRulesApi.md#usage_rules_post) | **POST** /usageRules | Create single usageRule.
*UserCollectionAlbumsApi* | [**user_collection_albums_id_get**](docs/UserCollectionAlbumsApi.md#user_collection_albums_id_get) | **GET** /userCollectionAlbums/{id} | Get single userCollectionAlbum.
*UserCollectionAlbumsApi* | [**user_collection_albums_id_relationships_items_delete**](docs/UserCollectionAlbumsApi.md#user_collection_albums_id_relationships_items_delete) | **DELETE** /userCollectionAlbums/{id}/relationships/items | Delete from items relationship (\&quot;to-many\&quot;).
*UserCollectionAlbumsApi* | [**user_collection_albums_id_relationships_items_get**](docs/UserCollectionAlbumsApi.md#user_collection_albums_id_relationships_items_get) | **GET** /userCollectionAlbums/{id}/relationships/items | Get items relationship (\&quot;to-many\&quot;).
*UserCollectionAlbumsApi* | [**user_collection_albums_id_relationships_items_post**](docs/UserCollectionAlbumsApi.md#user_collection_albums_id_relationships_items_post) | **POST** /userCollectionAlbums/{id}/relationships/items | Add to items relationship (\&quot;to-many\&quot;).
*UserCollectionAlbumsApi* | [**user_collection_albums_id_relationships_owners_get**](docs/UserCollectionAlbumsApi.md#user_collection_albums_id_relationships_owners_get) | **GET** /userCollectionAlbums/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*UserCollectionArtistsApi* | [**user_collection_artists_id_get**](docs/UserCollectionArtistsApi.md#user_collection_artists_id_get) | **GET** /userCollectionArtists/{id} | Get single userCollectionArtist.
*UserCollectionArtistsApi* | [**user_collection_artists_id_relationships_items_delete**](docs/UserCollectionArtistsApi.md#user_collection_artists_id_relationships_items_delete) | **DELETE** /userCollectionArtists/{id}/relationships/items | Delete from items relationship (\&quot;to-many\&quot;).
*UserCollectionArtistsApi* | [**user_collection_artists_id_relationships_items_get**](docs/UserCollectionArtistsApi.md#user_collection_artists_id_relationships_items_get) | **GET** /userCollectionArtists/{id}/relationships/items | Get items relationship (\&quot;to-many\&quot;).
*UserCollectionArtistsApi* | [**user_collection_artists_id_relationships_items_post**](docs/UserCollectionArtistsApi.md#user_collection_artists_id_relationships_items_post) | **POST** /userCollectionArtists/{id}/relationships/items | Add to items relationship (\&quot;to-many\&quot;).
*UserCollectionArtistsApi* | [**user_collection_artists_id_relationships_owners_get**](docs/UserCollectionArtistsApi.md#user_collection_artists_id_relationships_owners_get) | **GET** /userCollectionArtists/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*UserCollectionFoldersApi* | [**user_collection_folders_get**](docs/UserCollectionFoldersApi.md#user_collection_folders_get) | **GET** /userCollectionFolders | Get multiple userCollectionFolders.
*UserCollectionFoldersApi* | [**user_collection_folders_id_delete**](docs/UserCollectionFoldersApi.md#user_collection_folders_id_delete) | **DELETE** /userCollectionFolders/{id} | Delete single userCollectionFolder.
*UserCollectionFoldersApi* | [**user_collection_folders_id_get**](docs/UserCollectionFoldersApi.md#user_collection_folders_id_get) | **GET** /userCollectionFolders/{id} | Get single userCollectionFolder.
*UserCollectionFoldersApi* | [**user_collection_folders_id_patch**](docs/UserCollectionFoldersApi.md#user_collection_folders_id_patch) | **PATCH** /userCollectionFolders/{id} | Update single userCollectionFolder.
*UserCollectionFoldersApi* | [**user_collection_folders_id_relationships_items_delete**](docs/UserCollectionFoldersApi.md#user_collection_folders_id_relationships_items_delete) | **DELETE** /userCollectionFolders/{id}/relationships/items | Delete from items relationship (\&quot;to-many\&quot;).
*UserCollectionFoldersApi* | [**user_collection_folders_id_relationships_items_get**](docs/UserCollectionFoldersApi.md#user_collection_folders_id_relationships_items_get) | **GET** /userCollectionFolders/{id}/relationships/items | Get items relationship (\&quot;to-many\&quot;).
*UserCollectionFoldersApi* | [**user_collection_folders_id_relationships_items_post**](docs/UserCollectionFoldersApi.md#user_collection_folders_id_relationships_items_post) | **POST** /userCollectionFolders/{id}/relationships/items | Add to items relationship (\&quot;to-many\&quot;).
*UserCollectionFoldersApi* | [**user_collection_folders_id_relationships_owners_get**](docs/UserCollectionFoldersApi.md#user_collection_folders_id_relationships_owners_get) | **GET** /userCollectionFolders/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*UserCollectionFoldersApi* | [**user_collection_folders_id_relationships_user_collection_get**](docs/UserCollectionFoldersApi.md#user_collection_folders_id_relationships_user_collection_get) | **GET** /userCollectionFolders/{id}/relationships/userCollection | Get userCollection relationship (\&quot;to-one\&quot;).
*UserCollectionFoldersApi* | [**user_collection_folders_post**](docs/UserCollectionFoldersApi.md#user_collection_folders_post) | **POST** /userCollectionFolders | Create single userCollectionFolder.
*UserCollectionPlaylistsApi* | [**user_collection_playlists_id_get**](docs/UserCollectionPlaylistsApi.md#user_collection_playlists_id_get) | **GET** /userCollectionPlaylists/{id} | Get single userCollectionPlaylist.
*UserCollectionPlaylistsApi* | [**user_collection_playlists_id_relationships_items_delete**](docs/UserCollectionPlaylistsApi.md#user_collection_playlists_id_relationships_items_delete) | **DELETE** /userCollectionPlaylists/{id}/relationships/items | Delete from items relationship (\&quot;to-many\&quot;).
*UserCollectionPlaylistsApi* | [**user_collection_playlists_id_relationships_items_get**](docs/UserCollectionPlaylistsApi.md#user_collection_playlists_id_relationships_items_get) | **GET** /userCollectionPlaylists/{id}/relationships/items | Get items relationship (\&quot;to-many\&quot;).
*UserCollectionPlaylistsApi* | [**user_collection_playlists_id_relationships_items_post**](docs/UserCollectionPlaylistsApi.md#user_collection_playlists_id_relationships_items_post) | **POST** /userCollectionPlaylists/{id}/relationships/items | Add to items relationship (\&quot;to-many\&quot;).
*UserCollectionPlaylistsApi* | [**user_collection_playlists_id_relationships_owners_get**](docs/UserCollectionPlaylistsApi.md#user_collection_playlists_id_relationships_owners_get) | **GET** /userCollectionPlaylists/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*UserCollectionSaveForLatersApi* | [**user_collection_save_for_laters_id_get**](docs/UserCollectionSaveForLatersApi.md#user_collection_save_for_laters_id_get) | **GET** /userCollectionSaveForLaters/{id} | Get single userCollectionSaveForLater.
*UserCollectionSaveForLatersApi* | [**user_collection_save_for_laters_id_relationships_items_delete**](docs/UserCollectionSaveForLatersApi.md#user_collection_save_for_laters_id_relationships_items_delete) | **DELETE** /userCollectionSaveForLaters/{id}/relationships/items | Delete from items relationship (\&quot;to-many\&quot;).
*UserCollectionSaveForLatersApi* | [**user_collection_save_for_laters_id_relationships_items_get**](docs/UserCollectionSaveForLatersApi.md#user_collection_save_for_laters_id_relationships_items_get) | **GET** /userCollectionSaveForLaters/{id}/relationships/items | Get items relationship (\&quot;to-many\&quot;).
*UserCollectionSaveForLatersApi* | [**user_collection_save_for_laters_id_relationships_items_post**](docs/UserCollectionSaveForLatersApi.md#user_collection_save_for_laters_id_relationships_items_post) | **POST** /userCollectionSaveForLaters/{id}/relationships/items | Add to items relationship (\&quot;to-many\&quot;).
*UserCollectionSaveForLatersApi* | [**user_collection_save_for_laters_id_relationships_owners_get**](docs/UserCollectionSaveForLatersApi.md#user_collection_save_for_laters_id_relationships_owners_get) | **GET** /userCollectionSaveForLaters/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*UserCollectionTracksApi* | [**user_collection_tracks_id_get**](docs/UserCollectionTracksApi.md#user_collection_tracks_id_get) | **GET** /userCollectionTracks/{id} | Get single userCollectionTrack.
*UserCollectionTracksApi* | [**user_collection_tracks_id_relationships_items_delete**](docs/UserCollectionTracksApi.md#user_collection_tracks_id_relationships_items_delete) | **DELETE** /userCollectionTracks/{id}/relationships/items | Delete from items relationship (\&quot;to-many\&quot;).
*UserCollectionTracksApi* | [**user_collection_tracks_id_relationships_items_get**](docs/UserCollectionTracksApi.md#user_collection_tracks_id_relationships_items_get) | **GET** /userCollectionTracks/{id}/relationships/items | Get items relationship (\&quot;to-many\&quot;).
*UserCollectionTracksApi* | [**user_collection_tracks_id_relationships_items_post**](docs/UserCollectionTracksApi.md#user_collection_tracks_id_relationships_items_post) | **POST** /userCollectionTracks/{id}/relationships/items | Add to items relationship (\&quot;to-many\&quot;).
*UserCollectionTracksApi* | [**user_collection_tracks_id_relationships_owners_get**](docs/UserCollectionTracksApi.md#user_collection_tracks_id_relationships_owners_get) | **GET** /userCollectionTracks/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*UserCollectionVideosApi* | [**user_collection_videos_id_get**](docs/UserCollectionVideosApi.md#user_collection_videos_id_get) | **GET** /userCollectionVideos/{id} | Get single userCollectionVideo.
*UserCollectionVideosApi* | [**user_collection_videos_id_relationships_items_delete**](docs/UserCollectionVideosApi.md#user_collection_videos_id_relationships_items_delete) | **DELETE** /userCollectionVideos/{id}/relationships/items | Delete from items relationship (\&quot;to-many\&quot;).
*UserCollectionVideosApi* | [**user_collection_videos_id_relationships_items_get**](docs/UserCollectionVideosApi.md#user_collection_videos_id_relationships_items_get) | **GET** /userCollectionVideos/{id}/relationships/items | Get items relationship (\&quot;to-many\&quot;).
*UserCollectionVideosApi* | [**user_collection_videos_id_relationships_items_post**](docs/UserCollectionVideosApi.md#user_collection_videos_id_relationships_items_post) | **POST** /userCollectionVideos/{id}/relationships/items | Add to items relationship (\&quot;to-many\&quot;).
*UserCollectionVideosApi* | [**user_collection_videos_id_relationships_owners_get**](docs/UserCollectionVideosApi.md#user_collection_videos_id_relationships_owners_get) | **GET** /userCollectionVideos/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*UserDailyMixesApi* | [**user_daily_mixes_id_get**](docs/UserDailyMixesApi.md#user_daily_mixes_id_get) | **GET** /userDailyMixes/{id} | Get single userDailyMixe.
*UserDailyMixesApi* | [**user_daily_mixes_id_relationships_items_get**](docs/UserDailyMixesApi.md#user_daily_mixes_id_relationships_items_get) | **GET** /userDailyMixes/{id}/relationships/items | Get items relationship (\&quot;to-many\&quot;).
*UserDataExportRequestsApi* | [**user_data_export_requests_post**](docs/UserDataExportRequestsApi.md#user_data_export_requests_post) | **POST** /userDataExportRequests | Create single userDataExportRequest.
*UserDataExportsApi* | [**user_data_exports_get**](docs/UserDataExportsApi.md#user_data_exports_get) | **GET** /userDataExports | Get multiple userDataExports.
*UserDataExportsApi* | [**user_data_exports_id_get**](docs/UserDataExportsApi.md#user_data_exports_id_get) | **GET** /userDataExports/{id} | Get single userDataExport.
*UserDataExportsApi* | [**user_data_exports_id_relationships_owners_get**](docs/UserDataExportsApi.md#user_data_exports_id_relationships_owners_get) | **GET** /userDataExports/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*UserDataExportsApi* | [**user_data_exports_post**](docs/UserDataExportsApi.md#user_data_exports_post) | **POST** /userDataExports | Create single userDataExport.
*UserDiscoveryMixesApi* | [**user_discovery_mixes_id_get**](docs/UserDiscoveryMixesApi.md#user_discovery_mixes_id_get) | **GET** /userDiscoveryMixes/{id} | Get single userDiscoveryMixe.
*UserDiscoveryMixesApi* | [**user_discovery_mixes_id_relationships_items_get**](docs/UserDiscoveryMixesApi.md#user_discovery_mixes_id_relationships_items_get) | **GET** /userDiscoveryMixes/{id}/relationships/items | Get items relationship (\&quot;to-many\&quot;).
*UserFeedItemsApi* | [**user_feed_items_get**](docs/UserFeedItemsApi.md#user_feed_items_get) | **GET** /userFeedItems | Get multiple userFeedItems.
*UserFeedItemsApi* | [**user_feed_items_id_relationships_actors_get**](docs/UserFeedItemsApi.md#user_feed_items_id_relationships_actors_get) | **GET** /userFeedItems/{id}/relationships/actors | Get actors relationship (\&quot;to-many\&quot;).
*UserFeedItemsApi* | [**user_feed_items_id_relationships_subject_get**](docs/UserFeedItemsApi.md#user_feed_items_id_relationships_subject_get) | **GET** /userFeedItems/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).
*UserFeedsApi* | [**user_feeds_id_get**](docs/UserFeedsApi.md#user_feeds_id_get) | **GET** /userFeeds/{id} | Get single userFeed.
*UserFeedsApi* | [**user_feeds_id_patch**](docs/UserFeedsApi.md#user_feeds_id_patch) | **PATCH** /userFeeds/{id} | Update single userFeed.
*UserNewReleaseMixesApi* | [**user_new_release_mixes_id_get**](docs/UserNewReleaseMixesApi.md#user_new_release_mixes_id_get) | **GET** /userNewReleaseMixes/{id} | Get single userNewReleaseMixe.
*UserNewReleaseMixesApi* | [**user_new_release_mixes_id_relationships_items_get**](docs/UserNewReleaseMixesApi.md#user_new_release_mixes_id_relationships_items_get) | **GET** /userNewReleaseMixes/{id}/relationships/items | Get items relationship (\&quot;to-many\&quot;).
*UserOfflineMixesApi* | [**user_offline_mixes_id_get**](docs/UserOfflineMixesApi.md#user_offline_mixes_id_get) | **GET** /userOfflineMixes/{id} | Get single userOfflineMixe.
*UserOfflineMixesApi* | [**user_offline_mixes_id_relationships_items_get**](docs/UserOfflineMixesApi.md#user_offline_mixes_id_relationships_items_get) | **GET** /userOfflineMixes/{id}/relationships/items | Get items relationship (\&quot;to-many\&quot;).
*UserPlaybackStatesApi* | [**user_playback_states_id_get**](docs/UserPlaybackStatesApi.md#user_playback_states_id_get) | **GET** /userPlaybackStates/{id} | Get single userPlaybackState.
*UserPlaybackStatesApi* | [**user_playback_states_id_patch**](docs/UserPlaybackStatesApi.md#user_playback_states_id_patch) | **PATCH** /userPlaybackStates/{id} | Update single userPlaybackState.
*UserPlaybackStatesApi* | [**user_playback_states_id_relationships_active_player_get**](docs/UserPlaybackStatesApi.md#user_playback_states_id_relationships_active_player_get) | **GET** /userPlaybackStates/{id}/relationships/activePlayer | Get activePlayer relationship (\&quot;to-one\&quot;).
*UserPlaybackStatesApi* | [**user_playback_states_id_relationships_active_player_patch**](docs/UserPlaybackStatesApi.md#user_playback_states_id_relationships_active_player_patch) | **PATCH** /userPlaybackStates/{id}/relationships/activePlayer | Update activePlayer relationship (\&quot;to-one\&quot;).
*UserPlaybackStatesApi* | [**user_playback_states_id_relationships_available_players_delete**](docs/UserPlaybackStatesApi.md#user_playback_states_id_relationships_available_players_delete) | **DELETE** /userPlaybackStates/{id}/relationships/availablePlayers | Delete from availablePlayers relationship (\&quot;to-many\&quot;).
*UserPlaybackStatesApi* | [**user_playback_states_id_relationships_available_players_get**](docs/UserPlaybackStatesApi.md#user_playback_states_id_relationships_available_players_get) | **GET** /userPlaybackStates/{id}/relationships/availablePlayers | Get availablePlayers relationship (\&quot;to-many\&quot;).
*UserPlaybackStatesApi* | [**user_playback_states_id_relationships_available_players_post**](docs/UserPlaybackStatesApi.md#user_playback_states_id_relationships_available_players_post) | **POST** /userPlaybackStates/{id}/relationships/availablePlayers | Add to availablePlayers relationship (\&quot;to-many\&quot;).
*UserPlaybackStatesApi* | [**user_playback_states_id_relationships_change_event_stream_get**](docs/UserPlaybackStatesApi.md#user_playback_states_id_relationships_change_event_stream_get) | **GET** /userPlaybackStates/{id}/relationships/changeEventStream | Get changeEventStream relationship (\&quot;to-one\&quot;).
*UserPlaybackStatesApi* | [**user_playback_states_id_relationships_play_queue_get**](docs/UserPlaybackStatesApi.md#user_playback_states_id_relationships_play_queue_get) | **GET** /userPlaybackStates/{id}/relationships/playQueue | Get playQueue relationship (\&quot;to-one\&quot;).
*UserPlaybackStatesApi* | [**user_playback_states_id_relationships_play_queue_patch**](docs/UserPlaybackStatesApi.md#user_playback_states_id_relationships_play_queue_patch) | **PATCH** /userPlaybackStates/{id}/relationships/playQueue | Update playQueue relationship (\&quot;to-one\&quot;).
*UserRecommendationBlocksApi* | [**user_recommendation_blocks_id_get**](docs/UserRecommendationBlocksApi.md#user_recommendation_blocks_id_get) | **GET** /userRecommendationBlocks/{id} | Get single userRecommendationBlock.
*UserRecommendationBlocksApi* | [**user_recommendation_blocks_id_relationships_artists_delete**](docs/UserRecommendationBlocksApi.md#user_recommendation_blocks_id_relationships_artists_delete) | **DELETE** /userRecommendationBlocks/{id}/relationships/artists | Delete from artists relationship (\&quot;to-many\&quot;).
*UserRecommendationBlocksApi* | [**user_recommendation_blocks_id_relationships_artists_get**](docs/UserRecommendationBlocksApi.md#user_recommendation_blocks_id_relationships_artists_get) | **GET** /userRecommendationBlocks/{id}/relationships/artists | Get artists relationship (\&quot;to-many\&quot;).
*UserRecommendationBlocksApi* | [**user_recommendation_blocks_id_relationships_artists_post**](docs/UserRecommendationBlocksApi.md#user_recommendation_blocks_id_relationships_artists_post) | **POST** /userRecommendationBlocks/{id}/relationships/artists | Add to artists relationship (\&quot;to-many\&quot;).
*UserRecommendationBlocksApi* | [**user_recommendation_blocks_id_relationships_owners_get**](docs/UserRecommendationBlocksApi.md#user_recommendation_blocks_id_relationships_owners_get) | **GET** /userRecommendationBlocks/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
*UserRecommendationBlocksApi* | [**user_recommendation_blocks_id_relationships_tracks_delete**](docs/UserRecommendationBlocksApi.md#user_recommendation_blocks_id_relationships_tracks_delete) | **DELETE** /userRecommendationBlocks/{id}/relationships/tracks | Delete from tracks relationship (\&quot;to-many\&quot;).
*UserRecommendationBlocksApi* | [**user_recommendation_blocks_id_relationships_tracks_get**](docs/UserRecommendationBlocksApi.md#user_recommendation_blocks_id_relationships_tracks_get) | **GET** /userRecommendationBlocks/{id}/relationships/tracks | Get tracks relationship (\&quot;to-many\&quot;).
*UserRecommendationBlocksApi* | [**user_recommendation_blocks_id_relationships_tracks_post**](docs/UserRecommendationBlocksApi.md#user_recommendation_blocks_id_relationships_tracks_post) | **POST** /userRecommendationBlocks/{id}/relationships/tracks | Add to tracks relationship (\&quot;to-many\&quot;).
*UserRecommendationBlocksApi* | [**user_recommendation_blocks_id_relationships_videos_delete**](docs/UserRecommendationBlocksApi.md#user_recommendation_blocks_id_relationships_videos_delete) | **DELETE** /userRecommendationBlocks/{id}/relationships/videos | Delete from videos relationship (\&quot;to-many\&quot;).
*UserRecommendationBlocksApi* | [**user_recommendation_blocks_id_relationships_videos_get**](docs/UserRecommendationBlocksApi.md#user_recommendation_blocks_id_relationships_videos_get) | **GET** /userRecommendationBlocks/{id}/relationships/videos | Get videos relationship (\&quot;to-many\&quot;).
*UserRecommendationBlocksApi* | [**user_recommendation_blocks_id_relationships_videos_post**](docs/UserRecommendationBlocksApi.md#user_recommendation_blocks_id_relationships_videos_post) | **POST** /userRecommendationBlocks/{id}/relationships/videos | Add to videos relationship (\&quot;to-many\&quot;).
*UserReportsApi* | [**user_reports_post**](docs/UserReportsApi.md#user_reports_post) | **POST** /userReports | Create single userReport.
*UserSubscriptionPriceChangesApi* | [**user_subscription_price_changes_get**](docs/UserSubscriptionPriceChangesApi.md#user_subscription_price_changes_get) | **GET** /userSubscriptionPriceChanges | Get multiple userSubscriptionPriceChanges.
*UserSubscriptionPriceChangesApi* | [**user_subscription_price_changes_id_relationships_decision_get**](docs/UserSubscriptionPriceChangesApi.md#user_subscription_price_changes_id_relationships_decision_get) | **GET** /userSubscriptionPriceChanges/{id}/relationships/decision | Get decision relationship (\&quot;to-one\&quot;).
*UsersApi* | [**users_id_get**](docs/UsersApi.md#users_id_get) | **GET** /users/{id} | Get single user.
*UsersApi* | [**users_id_relationships_artist_get**](docs/UsersApi.md#users_id_relationships_artist_get) | **GET** /users/{id}/relationships/artist | Get artist relationship (\&quot;to-one\&quot;).
*VideoManifestsApi* | [**video_manifests_id_get**](docs/VideoManifestsApi.md#video_manifests_id_get) | **GET** /videoManifests/{id} | Get single videoManifest.
*VideosApi* | [**videos_get**](docs/VideosApi.md#videos_get) | **GET** /videos | Get multiple videos.
*VideosApi* | [**videos_id_get**](docs/VideosApi.md#videos_id_get) | **GET** /videos/{id} | Get single video.
*VideosApi* | [**videos_id_relationships_albums_get**](docs/VideosApi.md#videos_id_relationships_albums_get) | **GET** /videos/{id}/relationships/albums | Get albums relationship (\&quot;to-many\&quot;).
*VideosApi* | [**videos_id_relationships_artists_get**](docs/VideosApi.md#videos_id_relationships_artists_get) | **GET** /videos/{id}/relationships/artists | Get artists relationship (\&quot;to-many\&quot;).
*VideosApi* | [**videos_id_relationships_credits_get**](docs/VideosApi.md#videos_id_relationships_credits_get) | **GET** /videos/{id}/relationships/credits | Get credits relationship (\&quot;to-many\&quot;).
*VideosApi* | [**videos_id_relationships_providers_get**](docs/VideosApi.md#videos_id_relationships_providers_get) | **GET** /videos/{id}/relationships/providers | Get providers relationship (\&quot;to-many\&quot;).
*VideosApi* | [**videos_id_relationships_replacement_get**](docs/VideosApi.md#videos_id_relationships_replacement_get) | **GET** /videos/{id}/relationships/replacement | Get replacement relationship (\&quot;to-one\&quot;).
*VideosApi* | [**videos_id_relationships_similar_videos_get**](docs/VideosApi.md#videos_id_relationships_similar_videos_get) | **GET** /videos/{id}/relationships/similarVideos | Get similarVideos relationship (\&quot;to-many\&quot;).
*VideosApi* | [**videos_id_relationships_suggested_videos_get**](docs/VideosApi.md#videos_id_relationships_suggested_videos_get) | **GET** /videos/{id}/relationships/suggestedVideos | Get suggestedVideos relationship (\&quot;to-many\&quot;).
*VideosApi* | [**videos_id_relationships_thumbnail_art_get**](docs/VideosApi.md#videos_id_relationships_thumbnail_art_get) | **GET** /videos/{id}/relationships/thumbnailArt | Get thumbnailArt relationship (\&quot;to-many\&quot;).
*VideosApi* | [**videos_id_relationships_usage_rules_get**](docs/VideosApi.md#videos_id_relationships_usage_rules_get) | **GET** /videos/{id}/relationships/usageRules | Get usageRules relationship (\&quot;to-one\&quot;).
*ViewerContextsApi* | [**viewer_contexts_get**](docs/ViewerContextsApi.md#viewer_contexts_get) | **GET** /viewerContexts | Get multiple viewerContexts.
*ViewerContextsApi* | [**viewer_contexts_id_get**](docs/ViewerContextsApi.md#viewer_contexts_id_get) | **GET** /viewerContexts/{id} | Get single viewerContext.
*ViewerContextsApi* | [**viewer_contexts_id_relationships_comments_get**](docs/ViewerContextsApi.md#viewer_contexts_id_relationships_comments_get) | **GET** /viewerContexts/{id}/relationships/comments | Get comments relationship (\&quot;to-many\&quot;).
*ViewerContextsApi* | [**viewer_contexts_id_relationships_reactions_get**](docs/ViewerContextsApi.md#viewer_contexts_id_relationships_reactions_get) | **GET** /viewerContexts/{id}/relationships/reactions | Get reactions relationship (\&quot;to-many\&quot;).
*ViewerContextsApi* | [**viewer_contexts_id_relationships_subject_get**](docs/ViewerContextsApi.md#viewer_contexts_id_relationships_subject_get) | **GET** /viewerContexts/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).
*ViewerContextsApi* | [**viewer_contexts_id_relationships_viewer_get**](docs/ViewerContextsApi.md#viewer_contexts_id_relationships_viewer_get) | **GET** /viewerContexts/{id}/relationships/viewer | Get viewer relationship (\&quot;to-one\&quot;).


## Documentation For Models

 - [AcceptedTermsAttributes](docs/AcceptedTermsAttributes.md)
 - [AcceptedTermsCreateOperationPayload](docs/AcceptedTermsCreateOperationPayload.md)
 - [AcceptedTermsCreateOperationPayloadData](docs/AcceptedTermsCreateOperationPayloadData.md)
 - [AcceptedTermsCreateOperationPayloadDataRelationships](docs/AcceptedTermsCreateOperationPayloadDataRelationships.md)
 - [AcceptedTermsCreateOperationPayloadDataRelationshipsTerms](docs/AcceptedTermsCreateOperationPayloadDataRelationshipsTerms.md)
 - [AcceptedTermsCreateOperationPayloadDataRelationshipsTermsData](docs/AcceptedTermsCreateOperationPayloadDataRelationshipsTermsData.md)
 - [AcceptedTermsCreateSingleResourceDataDocument](docs/AcceptedTermsCreateSingleResourceDataDocument.md)
 - [AcceptedTermsMultiResourceDataDocument](docs/AcceptedTermsMultiResourceDataDocument.md)
 - [AcceptedTermsOwnersMultiRelationshipDataDocument](docs/AcceptedTermsOwnersMultiRelationshipDataDocument.md)
 - [AcceptedTermsRelationships](docs/AcceptedTermsRelationships.md)
 - [AcceptedTermsResourceObject](docs/AcceptedTermsResourceObject.md)
 - [AcceptedTermsTermsSingleRelationshipDataDocument](docs/AcceptedTermsTermsSingleRelationshipDataDocument.md)
 - [AlbumStatisticsAttributes](docs/AlbumStatisticsAttributes.md)
 - [AlbumStatisticsOwnersMultiRelationshipDataDocument](docs/AlbumStatisticsOwnersMultiRelationshipDataDocument.md)
 - [AlbumStatisticsRelationships](docs/AlbumStatisticsRelationships.md)
 - [AlbumStatisticsResourceObject](docs/AlbumStatisticsResourceObject.md)
 - [AlbumStatisticsSingleResourceDataDocument](docs/AlbumStatisticsSingleResourceDataDocument.md)
 - [AlbumsAlbumStatisticsSingleRelationshipDataDocument](docs/AlbumsAlbumStatisticsSingleRelationshipDataDocument.md)
 - [AlbumsArtistsMultiRelationshipDataDocument](docs/AlbumsArtistsMultiRelationshipDataDocument.md)
 - [AlbumsArtistsRelationshipUpdateOperationPayload](docs/AlbumsArtistsRelationshipUpdateOperationPayload.md)
 - [AlbumsArtistsRelationshipUpdateOperationPayloadData](docs/AlbumsArtistsRelationshipUpdateOperationPayloadData.md)
 - [AlbumsArtistsRelationshipUpdateOperationPayloadMeta](docs/AlbumsArtistsRelationshipUpdateOperationPayloadMeta.md)
 - [AlbumsAttributes](docs/AlbumsAttributes.md)
 - [AlbumsCoverArtMultiRelationshipDataDocument](docs/AlbumsCoverArtMultiRelationshipDataDocument.md)
 - [AlbumsCoverArtRelationshipUpdateOperationPayload](docs/AlbumsCoverArtRelationshipUpdateOperationPayload.md)
 - [AlbumsCoverArtRelationshipUpdateOperationPayloadData](docs/AlbumsCoverArtRelationshipUpdateOperationPayloadData.md)
 - [AlbumsCreateOperationPayload](docs/AlbumsCreateOperationPayload.md)
 - [AlbumsCreateOperationPayloadData](docs/AlbumsCreateOperationPayloadData.md)
 - [AlbumsCreateOperationPayloadDataAttributes](docs/AlbumsCreateOperationPayloadDataAttributes.md)
 - [AlbumsCreateOperationPayloadDataRelationships](docs/AlbumsCreateOperationPayloadDataRelationships.md)
 - [AlbumsCreateOperationPayloadDataRelationshipsArtists](docs/AlbumsCreateOperationPayloadDataRelationshipsArtists.md)
 - [AlbumsCreateOperationPayloadDataRelationshipsArtistsData](docs/AlbumsCreateOperationPayloadDataRelationshipsArtistsData.md)
 - [AlbumsCreateOperationPayloadDataRelationshipsGenres](docs/AlbumsCreateOperationPayloadDataRelationshipsGenres.md)
 - [AlbumsCreateOperationPayloadDataRelationshipsGenresData](docs/AlbumsCreateOperationPayloadDataRelationshipsGenresData.md)
 - [AlbumsCreateSingleResourceDataDocument](docs/AlbumsCreateSingleResourceDataDocument.md)
 - [AlbumsGenresMultiRelationshipDataDocument](docs/AlbumsGenresMultiRelationshipDataDocument.md)
 - [AlbumsItemsMultiRelationshipDataDocument](docs/AlbumsItemsMultiRelationshipDataDocument.md)
 - [AlbumsItemsRelationshipUpdateOperationPayload](docs/AlbumsItemsRelationshipUpdateOperationPayload.md)
 - [AlbumsItemsRelationshipUpdateOperationPayloadData](docs/AlbumsItemsRelationshipUpdateOperationPayloadData.md)
 - [AlbumsItemsRelationshipUpdateOperationPayloadMeta](docs/AlbumsItemsRelationshipUpdateOperationPayloadMeta.md)
 - [AlbumsItemsResourceIdentifier](docs/AlbumsItemsResourceIdentifier.md)
 - [AlbumsItemsResourceIdentifierMeta](docs/AlbumsItemsResourceIdentifierMeta.md)
 - [AlbumsMultiResourceDataDocument](docs/AlbumsMultiResourceDataDocument.md)
 - [AlbumsOwnersMultiRelationshipDataDocument](docs/AlbumsOwnersMultiRelationshipDataDocument.md)
 - [AlbumsPriceConfigSingleRelationshipDataDocument](docs/AlbumsPriceConfigSingleRelationshipDataDocument.md)
 - [AlbumsProvidersMultiRelationshipDataDocument](docs/AlbumsProvidersMultiRelationshipDataDocument.md)
 - [AlbumsRelationships](docs/AlbumsRelationships.md)
 - [AlbumsReplacementResourceIdentifier](docs/AlbumsReplacementResourceIdentifier.md)
 - [AlbumsReplacementResourceIdentifierMeta](docs/AlbumsReplacementResourceIdentifierMeta.md)
 - [AlbumsReplacementSingleRelationshipDataDocument](docs/AlbumsReplacementSingleRelationshipDataDocument.md)
 - [AlbumsResourceObject](docs/AlbumsResourceObject.md)
 - [AlbumsSharesMultiRelationshipDataDocument](docs/AlbumsSharesMultiRelationshipDataDocument.md)
 - [AlbumsSimilarAlbumsMultiRelationshipDataDocument](docs/AlbumsSimilarAlbumsMultiRelationshipDataDocument.md)
 - [AlbumsSimilarAlbumsResourceIdentifier](docs/AlbumsSimilarAlbumsResourceIdentifier.md)
 - [AlbumsSimilarAlbumsResourceIdentifierMeta](docs/AlbumsSimilarAlbumsResourceIdentifierMeta.md)
 - [AlbumsSingleResourceDataDocument](docs/AlbumsSingleResourceDataDocument.md)
 - [AlbumsSuggestedCoverArtsMultiRelationshipDataDocument](docs/AlbumsSuggestedCoverArtsMultiRelationshipDataDocument.md)
 - [AlbumsSuggestedCoverArtsMultiRelationshipDataDocumentMeta](docs/AlbumsSuggestedCoverArtsMultiRelationshipDataDocumentMeta.md)
 - [AlbumsSuggestedCoverArtsResourceIdentifier](docs/AlbumsSuggestedCoverArtsResourceIdentifier.md)
 - [AlbumsSuggestedCoverArtsResourceIdentifierMeta](docs/AlbumsSuggestedCoverArtsResourceIdentifierMeta.md)
 - [AlbumsUpdateOperationPayload](docs/AlbumsUpdateOperationPayload.md)
 - [AlbumsUpdateOperationPayloadData](docs/AlbumsUpdateOperationPayloadData.md)
 - [AlbumsUpdateOperationPayloadDataAttributes](docs/AlbumsUpdateOperationPayloadDataAttributes.md)
 - [AlbumsUpdateOperationPayloadDataRelationships](docs/AlbumsUpdateOperationPayloadDataRelationships.md)
 - [AlbumsUpdateOperationPayloadDataRelationshipsGenres](docs/AlbumsUpdateOperationPayloadDataRelationshipsGenres.md)
 - [AlbumsUpdateOperationPayloadDataRelationshipsGenresData](docs/AlbumsUpdateOperationPayloadDataRelationshipsGenresData.md)
 - [AlbumsUsageRulesSingleRelationshipDataDocument](docs/AlbumsUsageRulesSingleRelationshipDataDocument.md)
 - [AppreciationsAttributes](docs/AppreciationsAttributes.md)
 - [AppreciationsCreateOperationPayload](docs/AppreciationsCreateOperationPayload.md)
 - [AppreciationsCreateOperationPayloadData](docs/AppreciationsCreateOperationPayloadData.md)
 - [AppreciationsCreateOperationPayloadDataRelationships](docs/AppreciationsCreateOperationPayloadDataRelationships.md)
 - [AppreciationsCreateOperationPayloadDataRelationshipsAppreciatedItem](docs/AppreciationsCreateOperationPayloadDataRelationshipsAppreciatedItem.md)
 - [AppreciationsCreateOperationPayloadDataRelationshipsAppreciatedItemData](docs/AppreciationsCreateOperationPayloadDataRelationshipsAppreciatedItemData.md)
 - [AppreciationsCreateOperationPayloadMeta](docs/AppreciationsCreateOperationPayloadMeta.md)
 - [AppreciationsCreateSingleResourceDataDocument](docs/AppreciationsCreateSingleResourceDataDocument.md)
 - [AppreciationsResourceObject](docs/AppreciationsResourceObject.md)
 - [ArtistBiographiesAttributes](docs/ArtistBiographiesAttributes.md)
 - [ArtistBiographiesOwnersMultiRelationshipDataDocument](docs/ArtistBiographiesOwnersMultiRelationshipDataDocument.md)
 - [ArtistBiographiesRelationships](docs/ArtistBiographiesRelationships.md)
 - [ArtistBiographiesResourceObject](docs/ArtistBiographiesResourceObject.md)
 - [ArtistBiographiesSingleResourceDataDocument](docs/ArtistBiographiesSingleResourceDataDocument.md)
 - [ArtistBiographiesUpdateOperationPayload](docs/ArtistBiographiesUpdateOperationPayload.md)
 - [ArtistBiographiesUpdateOperationPayloadData](docs/ArtistBiographiesUpdateOperationPayloadData.md)
 - [ArtistBiographiesUpdateOperationPayloadDataAttributes](docs/ArtistBiographiesUpdateOperationPayloadDataAttributes.md)
 - [ArtistClaimStatusesAttributes](docs/ArtistClaimStatusesAttributes.md)
 - [ArtistClaimStatusesMultiResourceDataDocument](docs/ArtistClaimStatusesMultiResourceDataDocument.md)
 - [ArtistClaimStatusesResourceObject](docs/ArtistClaimStatusesResourceObject.md)
 - [ArtistClaimsAcceptedArtistsMultiRelationshipDataDocument](docs/ArtistClaimsAcceptedArtistsMultiRelationshipDataDocument.md)
 - [ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayload](docs/ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayload.md)
 - [ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayloadData](docs/ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayloadData.md)
 - [ArtistClaimsAttributes](docs/ArtistClaimsAttributes.md)
 - [ArtistClaimsCreateOperationPayload](docs/ArtistClaimsCreateOperationPayload.md)
 - [ArtistClaimsCreateOperationPayloadData](docs/ArtistClaimsCreateOperationPayloadData.md)
 - [ArtistClaimsCreateOperationPayloadDataAttributes](docs/ArtistClaimsCreateOperationPayloadDataAttributes.md)
 - [ArtistClaimsCreateOperationPayloadMeta](docs/ArtistClaimsCreateOperationPayloadMeta.md)
 - [ArtistClaimsCreateSingleResourceDataDocument](docs/ArtistClaimsCreateSingleResourceDataDocument.md)
 - [ArtistClaimsMultiResourceDataDocument](docs/ArtistClaimsMultiResourceDataDocument.md)
 - [ArtistClaimsOwnersMultiRelationshipDataDocument](docs/ArtistClaimsOwnersMultiRelationshipDataDocument.md)
 - [ArtistClaimsRecommendedArtistsMultiRelationshipDataDocument](docs/ArtistClaimsRecommendedArtistsMultiRelationshipDataDocument.md)
 - [ArtistClaimsRelationships](docs/ArtistClaimsRelationships.md)
 - [ArtistClaimsResourceObject](docs/ArtistClaimsResourceObject.md)
 - [ArtistClaimsSingleResourceDataDocument](docs/ArtistClaimsSingleResourceDataDocument.md)
 - [ArtistClaimsUpdateOperationPayload](docs/ArtistClaimsUpdateOperationPayload.md)
 - [ArtistClaimsUpdateOperationPayloadData](docs/ArtistClaimsUpdateOperationPayloadData.md)
 - [ArtistClaimsUpdateOperationPayloadMeta](docs/ArtistClaimsUpdateOperationPayloadMeta.md)
 - [ArtistRolesAttributes](docs/ArtistRolesAttributes.md)
 - [ArtistRolesResourceObject](docs/ArtistRolesResourceObject.md)
 - [ArtistRolesSingleResourceDataDocument](docs/ArtistRolesSingleResourceDataDocument.md)
 - [ArtistSalesStatisticsArtistSingleRelationshipDataDocument](docs/ArtistSalesStatisticsArtistSingleRelationshipDataDocument.md)
 - [ArtistSalesStatisticsAttributes](docs/ArtistSalesStatisticsAttributes.md)
 - [ArtistSalesStatisticsBuyerSourceShare](docs/ArtistSalesStatisticsBuyerSourceShare.md)
 - [ArtistSalesStatisticsBuyerSources](docs/ArtistSalesStatisticsBuyerSources.md)
 - [ArtistSalesStatisticsByType](docs/ArtistSalesStatisticsByType.md)
 - [ArtistSalesStatisticsMultiResourceDataDocument](docs/ArtistSalesStatisticsMultiResourceDataDocument.md)
 - [ArtistSalesStatisticsNetSales](docs/ArtistSalesStatisticsNetSales.md)
 - [ArtistSalesStatisticsRefunds](docs/ArtistSalesStatisticsRefunds.md)
 - [ArtistSalesStatisticsRelationships](docs/ArtistSalesStatisticsRelationships.md)
 - [ArtistSalesStatisticsResourceObject](docs/ArtistSalesStatisticsResourceObject.md)
 - [ArtistSalesStatisticsSeries](docs/ArtistSalesStatisticsSeries.md)
 - [ArtistSalesStatisticsSeriesPoint](docs/ArtistSalesStatisticsSeriesPoint.md)
 - [ArtistSalesStatisticsTopSellersMultiRelationshipDataDocument](docs/ArtistSalesStatisticsTopSellersMultiRelationshipDataDocument.md)
 - [ArtistSalesStatisticsTopSellersMultiRelationshipDataDocumentMeta](docs/ArtistSalesStatisticsTopSellersMultiRelationshipDataDocumentMeta.md)
 - [ArtistSalesStatisticsTopSellersResourceIdentifier](docs/ArtistSalesStatisticsTopSellersResourceIdentifier.md)
 - [ArtistSalesStatisticsTopSellersResourceIdentifierMeta](docs/ArtistSalesStatisticsTopSellersResourceIdentifierMeta.md)
 - [ArtistStatisticsBucketPeriod](docs/ArtistStatisticsBucketPeriod.md)
 - [ArtistStatisticsWindowPeriod](docs/ArtistStatisticsWindowPeriod.md)
 - [ArtistStreamsStatisticsArtistSingleRelationshipDataDocument](docs/ArtistStreamsStatisticsArtistSingleRelationshipDataDocument.md)
 - [ArtistStreamsStatisticsAttributes](docs/ArtistStreamsStatisticsAttributes.md)
 - [ArtistStreamsStatisticsCount](docs/ArtistStreamsStatisticsCount.md)
 - [ArtistStreamsStatisticsCountryListeners](docs/ArtistStreamsStatisticsCountryListeners.md)
 - [ArtistStreamsStatisticsMultiResourceDataDocument](docs/ArtistStreamsStatisticsMultiResourceDataDocument.md)
 - [ArtistStreamsStatisticsOtherPlays](docs/ArtistStreamsStatisticsOtherPlays.md)
 - [ArtistStreamsStatisticsPlays](docs/ArtistStreamsStatisticsPlays.md)
 - [ArtistStreamsStatisticsPlaysBySource](docs/ArtistStreamsStatisticsPlaysBySource.md)
 - [ArtistStreamsStatisticsRelationships](docs/ArtistStreamsStatisticsRelationships.md)
 - [ArtistStreamsStatisticsResourceObject](docs/ArtistStreamsStatisticsResourceObject.md)
 - [ArtistStreamsStatisticsSeries](docs/ArtistStreamsStatisticsSeries.md)
 - [ArtistStreamsStatisticsSeriesPoint](docs/ArtistStreamsStatisticsSeriesPoint.md)
 - [ArtistStreamsStatisticsSourcePlays](docs/ArtistStreamsStatisticsSourcePlays.md)
 - [ArtistStreamsStatisticsTopCountries](docs/ArtistStreamsStatisticsTopCountries.md)
 - [ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocument](docs/ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocument.md)
 - [ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocumentMeta](docs/ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocumentMeta.md)
 - [ArtistStreamsStatisticsTopTracksResourceIdentifier](docs/ArtistStreamsStatisticsTopTracksResourceIdentifier.md)
 - [ArtistStreamsStatisticsTopTracksResourceIdentifierMeta](docs/ArtistStreamsStatisticsTopTracksResourceIdentifierMeta.md)
 - [ArtistsAlbumsMultiRelationshipDataDocument](docs/ArtistsAlbumsMultiRelationshipDataDocument.md)
 - [ArtistsAlbumsResourceIdentifier](docs/ArtistsAlbumsResourceIdentifier.md)
 - [ArtistsAlbumsResourceIdentifierMeta](docs/ArtistsAlbumsResourceIdentifierMeta.md)
 - [ArtistsAttributes](docs/ArtistsAttributes.md)
 - [ArtistsBannerArtMultiRelationshipDataDocument](docs/ArtistsBannerArtMultiRelationshipDataDocument.md)
 - [ArtistsBannerArtRelationshipUpdateOperationPayload](docs/ArtistsBannerArtRelationshipUpdateOperationPayload.md)
 - [ArtistsBannerArtRelationshipUpdateOperationPayloadData](docs/ArtistsBannerArtRelationshipUpdateOperationPayloadData.md)
 - [ArtistsBiographySingleRelationshipDataDocument](docs/ArtistsBiographySingleRelationshipDataDocument.md)
 - [ArtistsClaimStatusSingleRelationshipDataDocument](docs/ArtistsClaimStatusSingleRelationshipDataDocument.md)
 - [ArtistsCreateOperationPayload](docs/ArtistsCreateOperationPayload.md)
 - [ArtistsCreateOperationPayloadData](docs/ArtistsCreateOperationPayloadData.md)
 - [ArtistsCreateOperationPayloadDataAttributes](docs/ArtistsCreateOperationPayloadDataAttributes.md)
 - [ArtistsCreateOperationPayloadMeta](docs/ArtistsCreateOperationPayloadMeta.md)
 - [ArtistsCreateSingleResourceDataDocument](docs/ArtistsCreateSingleResourceDataDocument.md)
 - [ArtistsFollowersMultiRelationshipDataDocument](docs/ArtistsFollowersMultiRelationshipDataDocument.md)
 - [ArtistsFollowersResourceIdentifier](docs/ArtistsFollowersResourceIdentifier.md)
 - [ArtistsFollowersResourceIdentifierMeta](docs/ArtistsFollowersResourceIdentifierMeta.md)
 - [ArtistsFollowersResourceMetaViewerContext](docs/ArtistsFollowersResourceMetaViewerContext.md)
 - [ArtistsFollowingMultiRelationshipDataDocument](docs/ArtistsFollowingMultiRelationshipDataDocument.md)
 - [ArtistsFollowingRelationshipAddOperationPayload](docs/ArtistsFollowingRelationshipAddOperationPayload.md)
 - [ArtistsFollowingRelationshipAddOperationPayloadData](docs/ArtistsFollowingRelationshipAddOperationPayloadData.md)
 - [ArtistsFollowingRelationshipRemoveOperationPayload](docs/ArtistsFollowingRelationshipRemoveOperationPayload.md)
 - [ArtistsFollowingRelationshipRemoveOperationPayloadData](docs/ArtistsFollowingRelationshipRemoveOperationPayloadData.md)
 - [ArtistsFollowingResourceIdentifier](docs/ArtistsFollowingResourceIdentifier.md)
 - [ArtistsFollowingResourceIdentifierMeta](docs/ArtistsFollowingResourceIdentifierMeta.md)
 - [ArtistsLogoArtMultiRelationshipDataDocument](docs/ArtistsLogoArtMultiRelationshipDataDocument.md)
 - [ArtistsLogoArtRelationshipUpdateOperationPayload](docs/ArtistsLogoArtRelationshipUpdateOperationPayload.md)
 - [ArtistsLogoArtRelationshipUpdateOperationPayloadData](docs/ArtistsLogoArtRelationshipUpdateOperationPayloadData.md)
 - [ArtistsMultiResourceDataDocument](docs/ArtistsMultiResourceDataDocument.md)
 - [ArtistsOwnersMultiRelationshipDataDocument](docs/ArtistsOwnersMultiRelationshipDataDocument.md)
 - [ArtistsProfileArtMultiRelationshipDataDocument](docs/ArtistsProfileArtMultiRelationshipDataDocument.md)
 - [ArtistsProfileArtRelationshipUpdateOperationPayload](docs/ArtistsProfileArtRelationshipUpdateOperationPayload.md)
 - [ArtistsProfileArtRelationshipUpdateOperationPayloadData](docs/ArtistsProfileArtRelationshipUpdateOperationPayloadData.md)
 - [ArtistsRadioMultiRelationshipDataDocument](docs/ArtistsRadioMultiRelationshipDataDocument.md)
 - [ArtistsRelationships](docs/ArtistsRelationships.md)
 - [ArtistsResourceObject](docs/ArtistsResourceObject.md)
 - [ArtistsRolesMultiRelationshipDataDocument](docs/ArtistsRolesMultiRelationshipDataDocument.md)
 - [ArtistsSimilarArtistsMultiRelationshipDataDocument](docs/ArtistsSimilarArtistsMultiRelationshipDataDocument.md)
 - [ArtistsSingleResourceDataDocument](docs/ArtistsSingleResourceDataDocument.md)
 - [ArtistsTrackProvidersMultiRelationshipDataDocument](docs/ArtistsTrackProvidersMultiRelationshipDataDocument.md)
 - [ArtistsTrackProvidersResourceIdentifier](docs/ArtistsTrackProvidersResourceIdentifier.md)
 - [ArtistsTrackProvidersResourceIdentifierMeta](docs/ArtistsTrackProvidersResourceIdentifierMeta.md)
 - [ArtistsTracksMultiRelationshipDataDocument](docs/ArtistsTracksMultiRelationshipDataDocument.md)
 - [ArtistsTracksResourceIdentifier](docs/ArtistsTracksResourceIdentifier.md)
 - [ArtistsTracksResourceIdentifierMeta](docs/ArtistsTracksResourceIdentifierMeta.md)
 - [ArtistsUpdateOperationPayload](docs/ArtistsUpdateOperationPayload.md)
 - [ArtistsUpdateOperationPayloadData](docs/ArtistsUpdateOperationPayloadData.md)
 - [ArtistsUpdateOperationPayloadDataAttributes](docs/ArtistsUpdateOperationPayloadDataAttributes.md)
 - [ArtistsUpdateOperationPayloadMeta](docs/ArtistsUpdateOperationPayloadMeta.md)
 - [ArtistsVideosMultiRelationshipDataDocument](docs/ArtistsVideosMultiRelationshipDataDocument.md)
 - [ArtistsVideosResourceIdentifier](docs/ArtistsVideosResourceIdentifier.md)
 - [ArtistsVideosResourceIdentifierMeta](docs/ArtistsVideosResourceIdentifierMeta.md)
 - [Artwork](docs/Artwork.md)
 - [ArtworkFile](docs/ArtworkFile.md)
 - [ArtworkFileMeta](docs/ArtworkFileMeta.md)
 - [ArtworkLibrariesArtworksMultiRelationshipDataDocument](docs/ArtworkLibrariesArtworksMultiRelationshipDataDocument.md)
 - [ArtworkLibrariesArtworksResourceIdentifier](docs/ArtworkLibrariesArtworksResourceIdentifier.md)
 - [ArtworkLibrariesArtworksResourceIdentifierMeta](docs/ArtworkLibrariesArtworksResourceIdentifierMeta.md)
 - [ArtworkLibrariesAttributes](docs/ArtworkLibrariesAttributes.md)
 - [ArtworkLibrariesMultiResourceDataDocument](docs/ArtworkLibrariesMultiResourceDataDocument.md)
 - [ArtworkLibrariesRandomArtworkResourceIdentifier](docs/ArtworkLibrariesRandomArtworkResourceIdentifier.md)
 - [ArtworkLibrariesRandomArtworkResourceIdentifierMeta](docs/ArtworkLibrariesRandomArtworkResourceIdentifierMeta.md)
 - [ArtworkLibrariesRandomArtworkSingleRelationshipDataDocument](docs/ArtworkLibrariesRandomArtworkSingleRelationshipDataDocument.md)
 - [ArtworkLibrariesRelationships](docs/ArtworkLibrariesRelationships.md)
 - [ArtworkLibrariesResourceObject](docs/ArtworkLibrariesResourceObject.md)
 - [ArtworkLibrariesSingleResourceDataDocument](docs/ArtworkLibrariesSingleResourceDataDocument.md)
 - [ArtworkSourceFile](docs/ArtworkSourceFile.md)
 - [ArtworkVisualMetadata](docs/ArtworkVisualMetadata.md)
 - [ArtworksAttributes](docs/ArtworksAttributes.md)
 - [ArtworksCreateOperationPayload](docs/ArtworksCreateOperationPayload.md)
 - [ArtworksCreateOperationPayloadData](docs/ArtworksCreateOperationPayloadData.md)
 - [ArtworksCreateOperationPayloadDataAttributes](docs/ArtworksCreateOperationPayloadDataAttributes.md)
 - [ArtworksCreateOperationPayloadDataAttributesSourceFile](docs/ArtworksCreateOperationPayloadDataAttributesSourceFile.md)
 - [ArtworksCreateSingleResourceDataDocument](docs/ArtworksCreateSingleResourceDataDocument.md)
 - [ArtworksMultiResourceDataDocument](docs/ArtworksMultiResourceDataDocument.md)
 - [ArtworksOwnersMultiRelationshipDataDocument](docs/ArtworksOwnersMultiRelationshipDataDocument.md)
 - [ArtworksRelationships](docs/ArtworksRelationships.md)
 - [ArtworksResourceObject](docs/ArtworksResourceObject.md)
 - [ArtworksSingleResourceDataDocument](docs/ArtworksSingleResourceDataDocument.md)
 - [AtomicOperations400ResponseBody](docs/AtomicOperations400ResponseBody.md)
 - [AtomicOperations400ResponseBodyErrorsInner](docs/AtomicOperations400ResponseBodyErrorsInner.md)
 - [AtomicOperations403ResponseBody](docs/AtomicOperations403ResponseBody.md)
 - [AtomicOperations403ResponseBodyErrorsInner](docs/AtomicOperations403ResponseBodyErrorsInner.md)
 - [AtomicOperations404ResponseBody](docs/AtomicOperations404ResponseBody.md)
 - [AtomicOperations404ResponseBodyErrorsInner](docs/AtomicOperations404ResponseBodyErrorsInner.md)
 - [AtomicOperations405ResponseBody](docs/AtomicOperations405ResponseBody.md)
 - [AtomicOperations405ResponseBodyErrorsInner](docs/AtomicOperations405ResponseBodyErrorsInner.md)
 - [AtomicOperations406ResponseBody](docs/AtomicOperations406ResponseBody.md)
 - [AtomicOperations406ResponseBodyErrorsInner](docs/AtomicOperations406ResponseBodyErrorsInner.md)
 - [AtomicOperations409ResponseBody](docs/AtomicOperations409ResponseBody.md)
 - [AtomicOperations409ResponseBodyErrorsInner](docs/AtomicOperations409ResponseBodyErrorsInner.md)
 - [AtomicOperations415ResponseBody](docs/AtomicOperations415ResponseBody.md)
 - [AtomicOperations415ResponseBodyErrorsInner](docs/AtomicOperations415ResponseBodyErrorsInner.md)
 - [AtomicOperations422ResponseBody](docs/AtomicOperations422ResponseBody.md)
 - [AtomicOperations422ResponseBodyErrorsInner](docs/AtomicOperations422ResponseBodyErrorsInner.md)
 - [AtomicOperations429ResponseBody](docs/AtomicOperations429ResponseBody.md)
 - [AtomicOperations429ResponseBodyErrorsInner](docs/AtomicOperations429ResponseBodyErrorsInner.md)
 - [AtomicOperations500ResponseBody](docs/AtomicOperations500ResponseBody.md)
 - [AtomicOperations500ResponseBodyErrorsInner](docs/AtomicOperations500ResponseBodyErrorsInner.md)
 - [AtomicOperations503ResponseBody](docs/AtomicOperations503ResponseBody.md)
 - [AtomicOperations503ResponseBodyErrorsInner](docs/AtomicOperations503ResponseBodyErrorsInner.md)
 - [AtomicOperationsRequest](docs/AtomicOperationsRequest.md)
 - [AtomicOperationsRequestAtomicOperationsInner](docs/AtomicOperationsRequestAtomicOperationsInner.md)
 - [AtomicOperationsRequestAtomicOperationsInnerOneOf](docs/AtomicOperationsRequestAtomicOperationsInnerOneOf.md)
 - [AtomicOperationsRequestAtomicOperationsInnerOneOf1](docs/AtomicOperationsRequestAtomicOperationsInnerOneOf1.md)
 - [AtomicOperationsResponse](docs/AtomicOperationsResponse.md)
 - [AtomicOperationsResponseAtomicResultsInner](docs/AtomicOperationsResponseAtomicResultsInner.md)
 - [AtomicOperationsResponseAtomicResultsInnerOneOf](docs/AtomicOperationsResponseAtomicResultsInnerOneOf.md)
 - [AtomicOperationsResponseAtomicResultsInnerOneOf1](docs/AtomicOperationsResponseAtomicResultsInnerOneOf1.md)
 - [Audio](docs/Audio.md)
 - [AudioNormalizationData](docs/AudioNormalizationData.md)
 - [ChangeEventStreamsAttributes](docs/ChangeEventStreamsAttributes.md)
 - [ChangeEventStreamsResourceObject](docs/ChangeEventStreamsResourceObject.md)
 - [ClientCertificatesAttributes](docs/ClientCertificatesAttributes.md)
 - [ClientCertificatesCreateOperationPayload](docs/ClientCertificatesCreateOperationPayload.md)
 - [ClientCertificatesCreateOperationPayloadData](docs/ClientCertificatesCreateOperationPayloadData.md)
 - [ClientCertificatesCreateOperationPayloadDataRelationships](docs/ClientCertificatesCreateOperationPayloadDataRelationships.md)
 - [ClientCertificatesCreateOperationPayloadDataRelationshipsClient](docs/ClientCertificatesCreateOperationPayloadDataRelationshipsClient.md)
 - [ClientCertificatesCreateOperationPayloadDataRelationshipsClientData](docs/ClientCertificatesCreateOperationPayloadDataRelationshipsClientData.md)
 - [ClientCertificatesCreateSingleResourceDataDocument](docs/ClientCertificatesCreateSingleResourceDataDocument.md)
 - [ClientCertificatesOwnersMultiRelationshipDataDocument](docs/ClientCertificatesOwnersMultiRelationshipDataDocument.md)
 - [ClientCertificatesRelationships](docs/ClientCertificatesRelationships.md)
 - [ClientCertificatesResourceObject](docs/ClientCertificatesResourceObject.md)
 - [ClientCertificatesSingleResourceDataDocument](docs/ClientCertificatesSingleResourceDataDocument.md)
 - [ClientsAttributes](docs/ClientsAttributes.md)
 - [ClientsCertificatesMultiRelationshipDataDocument](docs/ClientsCertificatesMultiRelationshipDataDocument.md)
 - [ClientsCreateOperationPayload](docs/ClientsCreateOperationPayload.md)
 - [ClientsCreateOperationPayloadData](docs/ClientsCreateOperationPayloadData.md)
 - [ClientsCreateOperationPayloadDataAttributes](docs/ClientsCreateOperationPayloadDataAttributes.md)
 - [ClientsCreateSingleResourceDataDocument](docs/ClientsCreateSingleResourceDataDocument.md)
 - [ClientsMultiResourceDataDocument](docs/ClientsMultiResourceDataDocument.md)
 - [ClientsOwnersMultiRelationshipDataDocument](docs/ClientsOwnersMultiRelationshipDataDocument.md)
 - [ClientsRelationships](docs/ClientsRelationships.md)
 - [ClientsResourceObject](docs/ClientsResourceObject.md)
 - [ClientsSingleResourceDataDocument](docs/ClientsSingleResourceDataDocument.md)
 - [ClientsUpdateOperationPayload](docs/ClientsUpdateOperationPayload.md)
 - [ClientsUpdateOperationPayloadData](docs/ClientsUpdateOperationPayloadData.md)
 - [ClientsUpdateOperationPayloadDataAttributes](docs/ClientsUpdateOperationPayloadDataAttributes.md)
 - [ClientsUpdateSingleResourceDataDocument](docs/ClientsUpdateSingleResourceDataDocument.md)
 - [CollaborationInviteRedemptionsAttributes](docs/CollaborationInviteRedemptionsAttributes.md)
 - [CollaborationInviteRedemptionsCreateOperationPayload](docs/CollaborationInviteRedemptionsCreateOperationPayload.md)
 - [CollaborationInviteRedemptionsCreateOperationPayloadData](docs/CollaborationInviteRedemptionsCreateOperationPayloadData.md)
 - [CollaborationInviteRedemptionsCreateOperationPayloadDataRelationships](docs/CollaborationInviteRedemptionsCreateOperationPayloadDataRelationships.md)
 - [CollaborationInviteRedemptionsCreateOperationPayloadDataRelationshipsInvite](docs/CollaborationInviteRedemptionsCreateOperationPayloadDataRelationshipsInvite.md)
 - [CollaborationInviteRedemptionsCreateOperationPayloadDataRelationshipsInviteData](docs/CollaborationInviteRedemptionsCreateOperationPayloadDataRelationshipsInviteData.md)
 - [CollaborationInviteRedemptionsCreateSingleResourceDataDocument](docs/CollaborationInviteRedemptionsCreateSingleResourceDataDocument.md)
 - [CollaborationInviteRedemptionsResourceObject](docs/CollaborationInviteRedemptionsResourceObject.md)
 - [CollaborationInvitesAttributes](docs/CollaborationInvitesAttributes.md)
 - [CollaborationInvitesCreateOperationPayload](docs/CollaborationInvitesCreateOperationPayload.md)
 - [CollaborationInvitesCreateOperationPayloadData](docs/CollaborationInvitesCreateOperationPayloadData.md)
 - [CollaborationInvitesCreateOperationPayloadDataRelationships](docs/CollaborationInvitesCreateOperationPayloadDataRelationships.md)
 - [CollaborationInvitesCreateOperationPayloadDataRelationshipsSubject](docs/CollaborationInvitesCreateOperationPayloadDataRelationshipsSubject.md)
 - [CollaborationInvitesCreateOperationPayloadDataRelationshipsSubjectData](docs/CollaborationInvitesCreateOperationPayloadDataRelationshipsSubjectData.md)
 - [CollaborationInvitesCreateSingleResourceDataDocument](docs/CollaborationInvitesCreateSingleResourceDataDocument.md)
 - [CollaborationInvitesMultiResourceDataDocument](docs/CollaborationInvitesMultiResourceDataDocument.md)
 - [CollaborationInvitesOwnersMultiRelationshipDataDocument](docs/CollaborationInvitesOwnersMultiRelationshipDataDocument.md)
 - [CollaborationInvitesRelationships](docs/CollaborationInvitesRelationships.md)
 - [CollaborationInvitesResourceObject](docs/CollaborationInvitesResourceObject.md)
 - [CollaborationInvitesSingleResourceDataDocument](docs/CollaborationInvitesSingleResourceDataDocument.md)
 - [CollaborationInvitesSubjectSingleRelationshipDataDocument](docs/CollaborationInvitesSubjectSingleRelationshipDataDocument.md)
 - [CommentSummariesAttributes](docs/CommentSummariesAttributes.md)
 - [CommentSummariesMultiResourceDataDocument](docs/CommentSummariesMultiResourceDataDocument.md)
 - [CommentSummariesRelationships](docs/CommentSummariesRelationships.md)
 - [CommentSummariesResourceObject](docs/CommentSummariesResourceObject.md)
 - [CommentSummariesSubjectSingleRelationshipDataDocument](docs/CommentSummariesSubjectSingleRelationshipDataDocument.md)
 - [CommentsAttributes](docs/CommentsAttributes.md)
 - [CommentsAuthorSingleRelationshipDataDocument](docs/CommentsAuthorSingleRelationshipDataDocument.md)
 - [CommentsCommentSummarySingleRelationshipDataDocument](docs/CommentsCommentSummarySingleRelationshipDataDocument.md)
 - [CommentsCreateOperationPayload](docs/CommentsCreateOperationPayload.md)
 - [CommentsCreateOperationPayloadData](docs/CommentsCreateOperationPayloadData.md)
 - [CommentsCreateOperationPayloadDataAttributes](docs/CommentsCreateOperationPayloadDataAttributes.md)
 - [CommentsCreateOperationPayloadDataRelationships](docs/CommentsCreateOperationPayloadDataRelationships.md)
 - [CommentsCreateOperationPayloadDataRelationshipsSubject](docs/CommentsCreateOperationPayloadDataRelationshipsSubject.md)
 - [CommentsCreateOperationPayloadDataRelationshipsSubjectData](docs/CommentsCreateOperationPayloadDataRelationshipsSubjectData.md)
 - [CommentsCreateSingleResourceDataDocument](docs/CommentsCreateSingleResourceDataDocument.md)
 - [CommentsMultiResourceDataDocument](docs/CommentsMultiResourceDataDocument.md)
 - [CommentsOwnersMultiRelationshipDataDocument](docs/CommentsOwnersMultiRelationshipDataDocument.md)
 - [CommentsReactionSummarySingleRelationshipDataDocument](docs/CommentsReactionSummarySingleRelationshipDataDocument.md)
 - [CommentsRelationships](docs/CommentsRelationships.md)
 - [CommentsResourceObject](docs/CommentsResourceObject.md)
 - [CommentsRootSubjectSingleRelationshipDataDocument](docs/CommentsRootSubjectSingleRelationshipDataDocument.md)
 - [CommentsSingleResourceDataDocument](docs/CommentsSingleResourceDataDocument.md)
 - [CommentsSubjectSingleRelationshipDataDocument](docs/CommentsSubjectSingleRelationshipDataDocument.md)
 - [CommentsUpdateOperationPayload](docs/CommentsUpdateOperationPayload.md)
 - [CommentsUpdateOperationPayloadData](docs/CommentsUpdateOperationPayloadData.md)
 - [CommentsUpdateOperationPayloadDataAttributes](docs/CommentsUpdateOperationPayloadDataAttributes.md)
 - [ContentClaimsAttributes](docs/ContentClaimsAttributes.md)
 - [ContentClaimsClaimedResourceResourceIdentifier](docs/ContentClaimsClaimedResourceResourceIdentifier.md)
 - [ContentClaimsClaimedResourceResourceIdentifierMeta](docs/ContentClaimsClaimedResourceResourceIdentifierMeta.md)
 - [ContentClaimsClaimedResourceSingleRelationshipDataDocument](docs/ContentClaimsClaimedResourceSingleRelationshipDataDocument.md)
 - [ContentClaimsClaimingArtistSingleRelationshipDataDocument](docs/ContentClaimsClaimingArtistSingleRelationshipDataDocument.md)
 - [ContentClaimsCreateOperationPayload](docs/ContentClaimsCreateOperationPayload.md)
 - [ContentClaimsCreateOperationPayloadData](docs/ContentClaimsCreateOperationPayloadData.md)
 - [ContentClaimsCreateOperationPayloadDataAttributes](docs/ContentClaimsCreateOperationPayloadDataAttributes.md)
 - [ContentClaimsCreateOperationPayloadDataRelationships](docs/ContentClaimsCreateOperationPayloadDataRelationships.md)
 - [ContentClaimsCreateOperationPayloadDataRelationshipsClaimedResource](docs/ContentClaimsCreateOperationPayloadDataRelationshipsClaimedResource.md)
 - [ContentClaimsCreateOperationPayloadDataRelationshipsClaimedResourceData](docs/ContentClaimsCreateOperationPayloadDataRelationshipsClaimedResourceData.md)
 - [ContentClaimsCreateOperationPayloadDataRelationshipsClaimingArtist](docs/ContentClaimsCreateOperationPayloadDataRelationshipsClaimingArtist.md)
 - [ContentClaimsCreateOperationPayloadDataRelationshipsClaimingArtistData](docs/ContentClaimsCreateOperationPayloadDataRelationshipsClaimingArtistData.md)
 - [ContentClaimsCreateSingleResourceDataDocument](docs/ContentClaimsCreateSingleResourceDataDocument.md)
 - [ContentClaimsMultiResourceDataDocument](docs/ContentClaimsMultiResourceDataDocument.md)
 - [ContentClaimsOwnersMultiRelationshipDataDocument](docs/ContentClaimsOwnersMultiRelationshipDataDocument.md)
 - [ContentClaimsRelationships](docs/ContentClaimsRelationships.md)
 - [ContentClaimsResourceObject](docs/ContentClaimsResourceObject.md)
 - [ContentClaimsSingleResourceDataDocument](docs/ContentClaimsSingleResourceDataDocument.md)
 - [Copyright](docs/Copyright.md)
 - [CreditsArtistSingleRelationshipDataDocument](docs/CreditsArtistSingleRelationshipDataDocument.md)
 - [CreditsAttributes](docs/CreditsAttributes.md)
 - [CreditsCategorySingleRelationshipDataDocument](docs/CreditsCategorySingleRelationshipDataDocument.md)
 - [CreditsRelationships](docs/CreditsRelationships.md)
 - [CreditsResourceObject](docs/CreditsResourceObject.md)
 - [CreditsSingleResourceDataDocument](docs/CreditsSingleResourceDataDocument.md)
 - [Default400ResponseBody](docs/Default400ResponseBody.md)
 - [Default404ResponseBody](docs/Default404ResponseBody.md)
 - [Default405ResponseBody](docs/Default405ResponseBody.md)
 - [Default406ResponseBody](docs/Default406ResponseBody.md)
 - [Default415ResponseBody](docs/Default415ResponseBody.md)
 - [Default429ResponseBody](docs/Default429ResponseBody.md)
 - [Default500ResponseBody](docs/Default500ResponseBody.md)
 - [Default503ResponseBody](docs/Default503ResponseBody.md)
 - [DownloadLink](docs/DownloadLink.md)
 - [DownloadLinkMeta](docs/DownloadLinkMeta.md)
 - [DownloadsAttributes](docs/DownloadsAttributes.md)
 - [DownloadsMultiResourceDataDocument](docs/DownloadsMultiResourceDataDocument.md)
 - [DownloadsOwnersMultiRelationshipDataDocument](docs/DownloadsOwnersMultiRelationshipDataDocument.md)
 - [DownloadsRelationships](docs/DownloadsRelationships.md)
 - [DownloadsResourceObject](docs/DownloadsResourceObject.md)
 - [DownloadsSingleResourceDataDocument](docs/DownloadsSingleResourceDataDocument.md)
 - [DrmData](docs/DrmData.md)
 - [DspSharingLinksAttributes](docs/DspSharingLinksAttributes.md)
 - [DspSharingLinksMultiResourceDataDocument](docs/DspSharingLinksMultiResourceDataDocument.md)
 - [DspSharingLinksRelationships](docs/DspSharingLinksRelationships.md)
 - [DspSharingLinksResourceObject](docs/DspSharingLinksResourceObject.md)
 - [DspSharingLinksSubjectResourceIdentifier](docs/DspSharingLinksSubjectResourceIdentifier.md)
 - [DspSharingLinksSubjectResourceIdentifierMeta](docs/DspSharingLinksSubjectResourceIdentifierMeta.md)
 - [DspSharingLinksSubjectSingleRelationshipDataDocument](docs/DspSharingLinksSubjectSingleRelationshipDataDocument.md)
 - [DynamicModulesAttributes](docs/DynamicModulesAttributes.md)
 - [DynamicModulesItemsMultiRelationshipDataDocument](docs/DynamicModulesItemsMultiRelationshipDataDocument.md)
 - [DynamicModulesItemsResourceIdentifier](docs/DynamicModulesItemsResourceIdentifier.md)
 - [DynamicModulesItemsResourceIdentifierMeta](docs/DynamicModulesItemsResourceIdentifierMeta.md)
 - [DynamicModulesMultiResourceDataDocument](docs/DynamicModulesMultiResourceDataDocument.md)
 - [DynamicModulesRelationships](docs/DynamicModulesRelationships.md)
 - [DynamicModulesResourceObject](docs/DynamicModulesResourceObject.md)
 - [DynamicModulesSeedItemResourceIdentifier](docs/DynamicModulesSeedItemResourceIdentifier.md)
 - [DynamicModulesSeedItemResourceIdentifierMeta](docs/DynamicModulesSeedItemResourceIdentifierMeta.md)
 - [DynamicModulesSeedItemSingleRelationshipDataDocument](docs/DynamicModulesSeedItemSingleRelationshipDataDocument.md)
 - [DynamicModulesSingleResourceDataDocument](docs/DynamicModulesSingleResourceDataDocument.md)
 - [DynamicPagesAttributes](docs/DynamicPagesAttributes.md)
 - [DynamicPagesModulesMultiRelationshipDataDocument](docs/DynamicPagesModulesMultiRelationshipDataDocument.md)
 - [DynamicPagesMultiResourceDataDocument](docs/DynamicPagesMultiResourceDataDocument.md)
 - [DynamicPagesRelationships](docs/DynamicPagesRelationships.md)
 - [DynamicPagesResourceObject](docs/DynamicPagesResourceObject.md)
 - [DynamicPagesSubjectResourceIdentifier](docs/DynamicPagesSubjectResourceIdentifier.md)
 - [DynamicPagesSubjectResourceIdentifierMeta](docs/DynamicPagesSubjectResourceIdentifierMeta.md)
 - [DynamicPagesSubjectSingleRelationshipDataDocument](docs/DynamicPagesSubjectSingleRelationshipDataDocument.md)
 - [EffectiveRole](docs/EffectiveRole.md)
 - [ErrorObject](docs/ErrorObject.md)
 - [ErrorObjectSource](docs/ErrorObjectSource.md)
 - [ErrorsDocument](docs/ErrorsDocument.md)
 - [ExternalLink](docs/ExternalLink.md)
 - [ExternalLinkMeta](docs/ExternalLinkMeta.md)
 - [ExternalLinkPayload](docs/ExternalLinkPayload.md)
 - [FileStatus](docs/FileStatus.md)
 - [FileUploadLink](docs/FileUploadLink.md)
 - [FileUploadLinkMeta](docs/FileUploadLinkMeta.md)
 - [FolderItemsAttributes](docs/FolderItemsAttributes.md)
 - [FolderItemsBreadcrumbMultiRelationshipDataDocument](docs/FolderItemsBreadcrumbMultiRelationshipDataDocument.md)
 - [FolderItemsCreateOperationPayload](docs/FolderItemsCreateOperationPayload.md)
 - [FolderItemsCreateOperationPayloadData](docs/FolderItemsCreateOperationPayloadData.md)
 - [FolderItemsCreateOperationPayloadDataRelationships](docs/FolderItemsCreateOperationPayloadDataRelationships.md)
 - [FolderItemsCreateOperationPayloadDataRelationshipsParent](docs/FolderItemsCreateOperationPayloadDataRelationshipsParent.md)
 - [FolderItemsCreateOperationPayloadDataRelationshipsParentData](docs/FolderItemsCreateOperationPayloadDataRelationshipsParentData.md)
 - [FolderItemsCreateOperationPayloadDataRelationshipsSubject](docs/FolderItemsCreateOperationPayloadDataRelationshipsSubject.md)
 - [FolderItemsCreateOperationPayloadDataRelationshipsSubjectData](docs/FolderItemsCreateOperationPayloadDataRelationshipsSubjectData.md)
 - [FolderItemsCreateResource400ResponseBody](docs/FolderItemsCreateResource400ResponseBody.md)
 - [FolderItemsCreateResource400ResponseBodyErrorsInner](docs/FolderItemsCreateResource400ResponseBodyErrorsInner.md)
 - [FolderItemsCreateSingleResourceDataDocument](docs/FolderItemsCreateSingleResourceDataDocument.md)
 - [FolderItemsMultiResourceDataDocument](docs/FolderItemsMultiResourceDataDocument.md)
 - [FolderItemsOwnersMultiRelationshipDataDocument](docs/FolderItemsOwnersMultiRelationshipDataDocument.md)
 - [FolderItemsParentRelationshipUpdateOperationPayload](docs/FolderItemsParentRelationshipUpdateOperationPayload.md)
 - [FolderItemsParentRelationshipUpdateOperationPayloadData](docs/FolderItemsParentRelationshipUpdateOperationPayloadData.md)
 - [FolderItemsParentSingleRelationshipDataDocument](docs/FolderItemsParentSingleRelationshipDataDocument.md)
 - [FolderItemsParentUpdateResourceIdentifier](docs/FolderItemsParentUpdateResourceIdentifier.md)
 - [FolderItemsParentUpdateSingleDataRelationship400ResponseBody](docs/FolderItemsParentUpdateSingleDataRelationship400ResponseBody.md)
 - [FolderItemsParentUpdateSingleRelationshipDataDocument](docs/FolderItemsParentUpdateSingleRelationshipDataDocument.md)
 - [FolderItemsRelationships](docs/FolderItemsRelationships.md)
 - [FolderItemsResourceObject](docs/FolderItemsResourceObject.md)
 - [FolderItemsSharingSummarySingleRelationshipDataDocument](docs/FolderItemsSharingSummarySingleRelationshipDataDocument.md)
 - [FolderItemsSingleResourceDataDocument](docs/FolderItemsSingleResourceDataDocument.md)
 - [FolderItemsSubjectResourceIdentifier](docs/FolderItemsSubjectResourceIdentifier.md)
 - [FolderItemsSubjectResourceIdentifierMeta](docs/FolderItemsSubjectResourceIdentifierMeta.md)
 - [FolderItemsSubjectSingleRelationshipDataDocument](docs/FolderItemsSubjectSingleRelationshipDataDocument.md)
 - [FoldersAttributes](docs/FoldersAttributes.md)
 - [FoldersChildrenMultiRelationshipDataDocument](docs/FoldersChildrenMultiRelationshipDataDocument.md)
 - [FoldersCreateOperationPayload](docs/FoldersCreateOperationPayload.md)
 - [FoldersCreateOperationPayloadData](docs/FoldersCreateOperationPayloadData.md)
 - [FoldersCreateOperationPayloadDataAttributes](docs/FoldersCreateOperationPayloadDataAttributes.md)
 - [FoldersCreateOperationPayloadDataRelationships](docs/FoldersCreateOperationPayloadDataRelationships.md)
 - [FoldersCreateOperationPayloadDataRelationshipsParent](docs/FoldersCreateOperationPayloadDataRelationshipsParent.md)
 - [FoldersCreateSingleResourceDataDocument](docs/FoldersCreateSingleResourceDataDocument.md)
 - [FoldersDeleteResource400ResponseBody](docs/FoldersDeleteResource400ResponseBody.md)
 - [FoldersDeleteResource400ResponseBodyErrorsInner](docs/FoldersDeleteResource400ResponseBodyErrorsInner.md)
 - [FoldersMultiResourceDataDocument](docs/FoldersMultiResourceDataDocument.md)
 - [FoldersOwnersMultiRelationshipDataDocument](docs/FoldersOwnersMultiRelationshipDataDocument.md)
 - [FoldersParentIdentifier](docs/FoldersParentIdentifier.md)
 - [FoldersParentSingleRelationshipDataDocument](docs/FoldersParentSingleRelationshipDataDocument.md)
 - [FoldersPreviewMultiRelationshipDataDocument](docs/FoldersPreviewMultiRelationshipDataDocument.md)
 - [FoldersRelationships](docs/FoldersRelationships.md)
 - [FoldersResourceObject](docs/FoldersResourceObject.md)
 - [FoldersSharesMultiRelationshipDataDocument](docs/FoldersSharesMultiRelationshipDataDocument.md)
 - [FoldersSingleResourceDataDocument](docs/FoldersSingleResourceDataDocument.md)
 - [FoldersUpdateOperationPayload](docs/FoldersUpdateOperationPayload.md)
 - [FoldersUpdateOperationPayloadData](docs/FoldersUpdateOperationPayloadData.md)
 - [FoldersUpdateOperationPayloadDataAttributes](docs/FoldersUpdateOperationPayloadDataAttributes.md)
 - [FoldersUpdateResource400ResponseBody](docs/FoldersUpdateResource400ResponseBody.md)
 - [FoldersUpdateSingleResourceDataDocument](docs/FoldersUpdateSingleResourceDataDocument.md)
 - [GenresAttributes](docs/GenresAttributes.md)
 - [GenresMultiResourceDataDocument](docs/GenresMultiResourceDataDocument.md)
 - [GenresResourceObject](docs/GenresResourceObject.md)
 - [GenresSingleResourceDataDocument](docs/GenresSingleResourceDataDocument.md)
 - [GroupsAttributes](docs/GroupsAttributes.md)
 - [GroupsMultiResourceDataDocument](docs/GroupsMultiResourceDataDocument.md)
 - [GroupsResourceObject](docs/GroupsResourceObject.md)
 - [GroupsSingleResourceDataDocument](docs/GroupsSingleResourceDataDocument.md)
 - [Idempotency409ResponseBody](docs/Idempotency409ResponseBody.md)
 - [Idempotency409ResponseBodyErrorsInner](docs/Idempotency409ResponseBodyErrorsInner.md)
 - [Idempotency422ResponseBody](docs/Idempotency422ResponseBody.md)
 - [IncludedInner](docs/IncludedInner.md)
 - [InstallationsAttributes](docs/InstallationsAttributes.md)
 - [InstallationsCreateOperationPayload](docs/InstallationsCreateOperationPayload.md)
 - [InstallationsCreateOperationPayloadData](docs/InstallationsCreateOperationPayloadData.md)
 - [InstallationsCreateOperationPayloadDataAttributes](docs/InstallationsCreateOperationPayloadDataAttributes.md)
 - [InstallationsCreateSingleResourceDataDocument](docs/InstallationsCreateSingleResourceDataDocument.md)
 - [InstallationsMultiResourceDataDocument](docs/InstallationsMultiResourceDataDocument.md)
 - [InstallationsOfflineInventoryItemIdentifier](docs/InstallationsOfflineInventoryItemIdentifier.md)
 - [InstallationsOfflineInventoryMultiRelationshipDataDocument](docs/InstallationsOfflineInventoryMultiRelationshipDataDocument.md)
 - [InstallationsOfflineInventoryRelationshipAddOperationPayload](docs/InstallationsOfflineInventoryRelationshipAddOperationPayload.md)
 - [InstallationsOfflineInventoryRelationshipRemoveOperationPayload](docs/InstallationsOfflineInventoryRelationshipRemoveOperationPayload.md)
 - [InstallationsOfflineInventoryResourceIdentifier](docs/InstallationsOfflineInventoryResourceIdentifier.md)
 - [InstallationsOfflineInventoryResourceIdentifierMeta](docs/InstallationsOfflineInventoryResourceIdentifierMeta.md)
 - [InstallationsOwnersMultiRelationshipDataDocument](docs/InstallationsOwnersMultiRelationshipDataDocument.md)
 - [InstallationsRelationships](docs/InstallationsRelationships.md)
 - [InstallationsResourceObject](docs/InstallationsResourceObject.md)
 - [InstallationsSingleResourceDataDocument](docs/InstallationsSingleResourceDataDocument.md)
 - [Item](docs/Item.md)
 - [ItemArtwork](docs/ItemArtwork.md)
 - [ItemVariation](docs/ItemVariation.md)
 - [LegacyBarcodeId](docs/LegacyBarcodeId.md)
 - [LegacySource](docs/LegacySource.md)
 - [LinkObject](docs/LinkObject.md)
 - [Links](docs/Links.md)
 - [LinksMeta](docs/LinksMeta.md)
 - [LyricsAttributes](docs/LyricsAttributes.md)
 - [LyricsCreateOperationPayload](docs/LyricsCreateOperationPayload.md)
 - [LyricsCreateOperationPayloadData](docs/LyricsCreateOperationPayloadData.md)
 - [LyricsCreateOperationPayloadDataAttributes](docs/LyricsCreateOperationPayloadDataAttributes.md)
 - [LyricsCreateOperationPayloadDataRelationships](docs/LyricsCreateOperationPayloadDataRelationships.md)
 - [LyricsCreateOperationPayloadDataRelationshipsTrack](docs/LyricsCreateOperationPayloadDataRelationshipsTrack.md)
 - [LyricsCreateOperationPayloadDataRelationshipsTrackData](docs/LyricsCreateOperationPayloadDataRelationshipsTrackData.md)
 - [LyricsCreateOperationPayloadMeta](docs/LyricsCreateOperationPayloadMeta.md)
 - [LyricsCreateSingleResourceDataDocument](docs/LyricsCreateSingleResourceDataDocument.md)
 - [LyricsOwnersMultiRelationshipDataDocument](docs/LyricsOwnersMultiRelationshipDataDocument.md)
 - [LyricsProvider](docs/LyricsProvider.md)
 - [LyricsRelationships](docs/LyricsRelationships.md)
 - [LyricsResourceObject](docs/LyricsResourceObject.md)
 - [LyricsSingleResourceDataDocument](docs/LyricsSingleResourceDataDocument.md)
 - [LyricsTrackResourceIdentifier](docs/LyricsTrackResourceIdentifier.md)
 - [LyricsTrackResourceIdentifierMeta](docs/LyricsTrackResourceIdentifierMeta.md)
 - [LyricsTrackSingleRelationshipDataDocument](docs/LyricsTrackSingleRelationshipDataDocument.md)
 - [LyricsUpdateOperationPayload](docs/LyricsUpdateOperationPayload.md)
 - [LyricsUpdateOperationPayloadData](docs/LyricsUpdateOperationPayloadData.md)
 - [LyricsUpdateOperationPayloadDataAttributes](docs/LyricsUpdateOperationPayloadDataAttributes.md)
 - [ManualArtistClaimsAttributes](docs/ManualArtistClaimsAttributes.md)
 - [ManualArtistClaimsCreateOperationPayload](docs/ManualArtistClaimsCreateOperationPayload.md)
 - [ManualArtistClaimsCreateOperationPayloadData](docs/ManualArtistClaimsCreateOperationPayloadData.md)
 - [ManualArtistClaimsCreateOperationPayloadDataAttributes](docs/ManualArtistClaimsCreateOperationPayloadDataAttributes.md)
 - [ManualArtistClaimsCreateSingleResourceDataDocument](docs/ManualArtistClaimsCreateSingleResourceDataDocument.md)
 - [ManualArtistClaimsExternalLink](docs/ManualArtistClaimsExternalLink.md)
 - [ManualArtistClaimsResourceObject](docs/ManualArtistClaimsResourceObject.md)
 - [MissingTermsMeta](docs/MissingTermsMeta.md)
 - [MutationResponseDocument](docs/MutationResponseDocument.md)
 - [OfflineTasksAttributes](docs/OfflineTasksAttributes.md)
 - [OfflineTasksCollectionResourceIdentifier](docs/OfflineTasksCollectionResourceIdentifier.md)
 - [OfflineTasksCollectionResourceIdentifierMeta](docs/OfflineTasksCollectionResourceIdentifierMeta.md)
 - [OfflineTasksCollectionSingleRelationshipDataDocument](docs/OfflineTasksCollectionSingleRelationshipDataDocument.md)
 - [OfflineTasksItemResourceIdentifier](docs/OfflineTasksItemResourceIdentifier.md)
 - [OfflineTasksItemResourceIdentifierMeta](docs/OfflineTasksItemResourceIdentifierMeta.md)
 - [OfflineTasksItemSingleRelationshipDataDocument](docs/OfflineTasksItemSingleRelationshipDataDocument.md)
 - [OfflineTasksMultiResourceDataDocument](docs/OfflineTasksMultiResourceDataDocument.md)
 - [OfflineTasksOwnersMultiRelationshipDataDocument](docs/OfflineTasksOwnersMultiRelationshipDataDocument.md)
 - [OfflineTasksRelationships](docs/OfflineTasksRelationships.md)
 - [OfflineTasksResourceObject](docs/OfflineTasksResourceObject.md)
 - [OfflineTasksSingleResourceDataDocument](docs/OfflineTasksSingleResourceDataDocument.md)
 - [OfflineTasksUpdateOperationPayload](docs/OfflineTasksUpdateOperationPayload.md)
 - [OfflineTasksUpdateOperationPayloadData](docs/OfflineTasksUpdateOperationPayloadData.md)
 - [OfflineTasksUpdateOperationPayloadDataAttributes](docs/OfflineTasksUpdateOperationPayloadDataAttributes.md)
 - [PlayQueuesAttributes](docs/PlayQueuesAttributes.md)
 - [PlayQueuesChangeEventStreamSingleRelationshipDataDocument](docs/PlayQueuesChangeEventStreamSingleRelationshipDataDocument.md)
 - [PlayQueuesCreateOperationPayload](docs/PlayQueuesCreateOperationPayload.md)
 - [PlayQueuesCreateOperationPayloadData](docs/PlayQueuesCreateOperationPayloadData.md)
 - [PlayQueuesCreateSingleResourceDataDocument](docs/PlayQueuesCreateSingleResourceDataDocument.md)
 - [PlayQueuesCreateSingleResourceDataDocumentMeta](docs/PlayQueuesCreateSingleResourceDataDocumentMeta.md)
 - [PlayQueuesCurrentRelationshipUpdateOperationPayload](docs/PlayQueuesCurrentRelationshipUpdateOperationPayload.md)
 - [PlayQueuesCurrentRelationshipUpdateOperationPayloadData](docs/PlayQueuesCurrentRelationshipUpdateOperationPayloadData.md)
 - [PlayQueuesCurrentRelationshipUpdateOperationPayloadDataMeta](docs/PlayQueuesCurrentRelationshipUpdateOperationPayloadDataMeta.md)
 - [PlayQueuesCurrentResourceIdentifier](docs/PlayQueuesCurrentResourceIdentifier.md)
 - [PlayQueuesCurrentResourceIdentifierMeta](docs/PlayQueuesCurrentResourceIdentifierMeta.md)
 - [PlayQueuesCurrentSingleRelationshipDataDocument](docs/PlayQueuesCurrentSingleRelationshipDataDocument.md)
 - [PlayQueuesCurrentUpdateResourceIdentifier](docs/PlayQueuesCurrentUpdateResourceIdentifier.md)
 - [PlayQueuesCurrentUpdateResourceIdentifierMeta](docs/PlayQueuesCurrentUpdateResourceIdentifierMeta.md)
 - [PlayQueuesCurrentUpdateSingleRelationshipDataDocument](docs/PlayQueuesCurrentUpdateSingleRelationshipDataDocument.md)
 - [PlayQueuesCurrentUpdateSingleRelationshipDataDocumentMeta](docs/PlayQueuesCurrentUpdateSingleRelationshipDataDocumentMeta.md)
 - [PlayQueuesFutureAddMultiRelationshipDataDocument](docs/PlayQueuesFutureAddMultiRelationshipDataDocument.md)
 - [PlayQueuesFutureAddMultiRelationshipDataDocumentMeta](docs/PlayQueuesFutureAddMultiRelationshipDataDocumentMeta.md)
 - [PlayQueuesFutureAddResourceIdentifier](docs/PlayQueuesFutureAddResourceIdentifier.md)
 - [PlayQueuesFutureMultiRelationshipDataDocument](docs/PlayQueuesFutureMultiRelationshipDataDocument.md)
 - [PlayQueuesFutureRelationshipAddOperationPayload](docs/PlayQueuesFutureRelationshipAddOperationPayload.md)
 - [PlayQueuesFutureRelationshipAddOperationPayloadData](docs/PlayQueuesFutureRelationshipAddOperationPayloadData.md)
 - [PlayQueuesFutureRelationshipAddOperationPayloadMeta](docs/PlayQueuesFutureRelationshipAddOperationPayloadMeta.md)
 - [PlayQueuesFutureRelationshipRemoveOperationPayload](docs/PlayQueuesFutureRelationshipRemoveOperationPayload.md)
 - [PlayQueuesFutureRelationshipRemoveOperationPayloadData](docs/PlayQueuesFutureRelationshipRemoveOperationPayloadData.md)
 - [PlayQueuesFutureRelationshipRemoveOperationPayloadDataMeta](docs/PlayQueuesFutureRelationshipRemoveOperationPayloadDataMeta.md)
 - [PlayQueuesFutureRelationshipSource](docs/PlayQueuesFutureRelationshipSource.md)
 - [PlayQueuesFutureRelationshipUpdateOperationPayload](docs/PlayQueuesFutureRelationshipUpdateOperationPayload.md)
 - [PlayQueuesFutureRelationshipUpdateOperationPayloadData](docs/PlayQueuesFutureRelationshipUpdateOperationPayloadData.md)
 - [PlayQueuesFutureRelationshipUpdateOperationPayloadDataMeta](docs/PlayQueuesFutureRelationshipUpdateOperationPayloadDataMeta.md)
 - [PlayQueuesFutureRelationshipUpdateOperationPayloadMeta](docs/PlayQueuesFutureRelationshipUpdateOperationPayloadMeta.md)
 - [PlayQueuesFutureResourceIdentifier](docs/PlayQueuesFutureResourceIdentifier.md)
 - [PlayQueuesFutureResourceIdentifierMeta](docs/PlayQueuesFutureResourceIdentifierMeta.md)
 - [PlayQueuesFutureUpdateMultiRelationshipDataDocument](docs/PlayQueuesFutureUpdateMultiRelationshipDataDocument.md)
 - [PlayQueuesFutureUpdateMultiRelationshipDataDocumentMeta](docs/PlayQueuesFutureUpdateMultiRelationshipDataDocumentMeta.md)
 - [PlayQueuesFutureUpdateResourceIdentifier](docs/PlayQueuesFutureUpdateResourceIdentifier.md)
 - [PlayQueuesMultiResourceDataDocument](docs/PlayQueuesMultiResourceDataDocument.md)
 - [PlayQueuesOwnersMultiRelationshipDataDocument](docs/PlayQueuesOwnersMultiRelationshipDataDocument.md)
 - [PlayQueuesPastMultiRelationshipDataDocument](docs/PlayQueuesPastMultiRelationshipDataDocument.md)
 - [PlayQueuesPastResourceIdentifier](docs/PlayQueuesPastResourceIdentifier.md)
 - [PlayQueuesPastResourceIdentifierMeta](docs/PlayQueuesPastResourceIdentifierMeta.md)
 - [PlayQueuesRelationships](docs/PlayQueuesRelationships.md)
 - [PlayQueuesResourceObject](docs/PlayQueuesResourceObject.md)
 - [PlayQueuesSingleResourceDataDocument](docs/PlayQueuesSingleResourceDataDocument.md)
 - [PlayQueuesUpdateOperationCurrent](docs/PlayQueuesUpdateOperationCurrent.md)
 - [PlayQueuesUpdateOperationCurrentMeta](docs/PlayQueuesUpdateOperationCurrentMeta.md)
 - [PlayQueuesUpdateOperationFuture](docs/PlayQueuesUpdateOperationFuture.md)
 - [PlayQueuesUpdateOperationFutureData](docs/PlayQueuesUpdateOperationFutureData.md)
 - [PlayQueuesUpdateOperationFutureMeta](docs/PlayQueuesUpdateOperationFutureMeta.md)
 - [PlayQueuesUpdateOperationPayload](docs/PlayQueuesUpdateOperationPayload.md)
 - [PlayQueuesUpdateOperationPayloadData](docs/PlayQueuesUpdateOperationPayloadData.md)
 - [PlayQueuesUpdateOperationPayloadDataAttributes](docs/PlayQueuesUpdateOperationPayloadDataAttributes.md)
 - [PlayQueuesUpdateOperationPayloadDataRelationships](docs/PlayQueuesUpdateOperationPayloadDataRelationships.md)
 - [PlayQueuesUpdateSingleResourceDataDocument](docs/PlayQueuesUpdateSingleResourceDataDocument.md)
 - [PlayQueuesUpdateSingleResourceDataDocumentMeta](docs/PlayQueuesUpdateSingleResourceDataDocumentMeta.md)
 - [PlaylistGenerationProgress](docs/PlaylistGenerationProgress.md)
 - [PlaylistGenerationSchedulesAttributes](docs/PlaylistGenerationSchedulesAttributes.md)
 - [PlaylistGenerationSchedulesCreateOperationPayload](docs/PlaylistGenerationSchedulesCreateOperationPayload.md)
 - [PlaylistGenerationSchedulesCreateOperationPayloadData](docs/PlaylistGenerationSchedulesCreateOperationPayloadData.md)
 - [PlaylistGenerationSchedulesCreateOperationPayloadDataAttributes](docs/PlaylistGenerationSchedulesCreateOperationPayloadDataAttributes.md)
 - [PlaylistGenerationSchedulesCreateOperationPayloadDataRelationships](docs/PlaylistGenerationSchedulesCreateOperationPayloadDataRelationships.md)
 - [PlaylistGenerationSchedulesCreateOperationPayloadDataRelationshipsPlaylist](docs/PlaylistGenerationSchedulesCreateOperationPayloadDataRelationshipsPlaylist.md)
 - [PlaylistGenerationSchedulesCreateOperationPayloadDataRelationshipsPlaylistData](docs/PlaylistGenerationSchedulesCreateOperationPayloadDataRelationshipsPlaylistData.md)
 - [PlaylistGenerationSchedulesCreateResource403ResponseBody](docs/PlaylistGenerationSchedulesCreateResource403ResponseBody.md)
 - [PlaylistGenerationSchedulesCreateResource403ResponseBodyErrorsInner](docs/PlaylistGenerationSchedulesCreateResource403ResponseBodyErrorsInner.md)
 - [PlaylistGenerationSchedulesCreateSingleResourceDataDocument](docs/PlaylistGenerationSchedulesCreateSingleResourceDataDocument.md)
 - [PlaylistGenerationSchedulesMultiResourceDataDocument](docs/PlaylistGenerationSchedulesMultiResourceDataDocument.md)
 - [PlaylistGenerationSchedulesPlaylistSingleRelationshipDataDocument](docs/PlaylistGenerationSchedulesPlaylistSingleRelationshipDataDocument.md)
 - [PlaylistGenerationSchedulesRelationships](docs/PlaylistGenerationSchedulesRelationships.md)
 - [PlaylistGenerationSchedulesResourceObject](docs/PlaylistGenerationSchedulesResourceObject.md)
 - [PlaylistGenerationSchedulesSingleResourceDataDocument](docs/PlaylistGenerationSchedulesSingleResourceDataDocument.md)
 - [PlaylistGenerationSchedulesUpdateOperationPayload](docs/PlaylistGenerationSchedulesUpdateOperationPayload.md)
 - [PlaylistGenerationSchedulesUpdateOperationPayloadData](docs/PlaylistGenerationSchedulesUpdateOperationPayloadData.md)
 - [PlaylistGenerationSchedulesUpdateOperationPayloadDataAttributes](docs/PlaylistGenerationSchedulesUpdateOperationPayloadDataAttributes.md)
 - [PlaylistGenerationSchedulesUpdateSingleResourceDataDocument](docs/PlaylistGenerationSchedulesUpdateSingleResourceDataDocument.md)
 - [PlaylistGenerationsAttributes](docs/PlaylistGenerationsAttributes.md)
 - [PlaylistGenerationsBaseGenerationSingleRelationshipDataDocument](docs/PlaylistGenerationsBaseGenerationSingleRelationshipDataDocument.md)
 - [PlaylistGenerationsCreateOperationPayload](docs/PlaylistGenerationsCreateOperationPayload.md)
 - [PlaylistGenerationsCreateOperationPayloadData](docs/PlaylistGenerationsCreateOperationPayloadData.md)
 - [PlaylistGenerationsCreateOperationPayloadDataAttributes](docs/PlaylistGenerationsCreateOperationPayloadDataAttributes.md)
 - [PlaylistGenerationsCreateOperationPayloadDataRelationships](docs/PlaylistGenerationsCreateOperationPayloadDataRelationships.md)
 - [PlaylistGenerationsCreateOperationPayloadDataRelationshipsBaseGeneration](docs/PlaylistGenerationsCreateOperationPayloadDataRelationshipsBaseGeneration.md)
 - [PlaylistGenerationsCreateOperationPayloadDataRelationshipsBaseGenerationData](docs/PlaylistGenerationsCreateOperationPayloadDataRelationshipsBaseGenerationData.md)
 - [PlaylistGenerationsCreateOperationPayloadDataRelationshipsPlaylist](docs/PlaylistGenerationsCreateOperationPayloadDataRelationshipsPlaylist.md)
 - [PlaylistGenerationsCreateOperationPayloadDataRelationshipsPlaylistData](docs/PlaylistGenerationsCreateOperationPayloadDataRelationshipsPlaylistData.md)
 - [PlaylistGenerationsCreateResource409ResponseBody](docs/PlaylistGenerationsCreateResource409ResponseBody.md)
 - [PlaylistGenerationsCreateResource409ResponseBodyErrorsInner](docs/PlaylistGenerationsCreateResource409ResponseBodyErrorsInner.md)
 - [PlaylistGenerationsCreateSingleResourceDataDocument](docs/PlaylistGenerationsCreateSingleResourceDataDocument.md)
 - [PlaylistGenerationsMultiResourceDataDocument](docs/PlaylistGenerationsMultiResourceDataDocument.md)
 - [PlaylistGenerationsPlaylistSingleRelationshipDataDocument](docs/PlaylistGenerationsPlaylistSingleRelationshipDataDocument.md)
 - [PlaylistGenerationsRelationships](docs/PlaylistGenerationsRelationships.md)
 - [PlaylistGenerationsResourceObject](docs/PlaylistGenerationsResourceObject.md)
 - [PlaylistGenerationsSingleResourceDataDocument](docs/PlaylistGenerationsSingleResourceDataDocument.md)
 - [PlaylistGenerationsTrackPreferencesAddMultiDataRelationshipWithResponse409ResponseBody](docs/PlaylistGenerationsTrackPreferencesAddMultiDataRelationshipWithResponse409ResponseBody.md)
 - [PlaylistGenerationsTrackPreferencesAddMultiRelationshipDataDocument](docs/PlaylistGenerationsTrackPreferencesAddMultiRelationshipDataDocument.md)
 - [PlaylistGenerationsTrackPreferencesAddMultiRelationshipDataDocumentMeta](docs/PlaylistGenerationsTrackPreferencesAddMultiRelationshipDataDocumentMeta.md)
 - [PlaylistGenerationsTrackPreferencesAddResourceIdentifier](docs/PlaylistGenerationsTrackPreferencesAddResourceIdentifier.md)
 - [PlaylistGenerationsTrackPreferencesAddResourceIdentifierMeta](docs/PlaylistGenerationsTrackPreferencesAddResourceIdentifierMeta.md)
 - [PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocument](docs/PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocument.md)
 - [PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocumentMeta](docs/PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocumentMeta.md)
 - [PlaylistGenerationsTrackPreferencesRelationshipAddOperationPayload](docs/PlaylistGenerationsTrackPreferencesRelationshipAddOperationPayload.md)
 - [PlaylistGenerationsTrackPreferencesRelationshipPayloadData](docs/PlaylistGenerationsTrackPreferencesRelationshipPayloadData.md)
 - [PlaylistGenerationsTrackPreferencesRelationshipPayloadDataMeta](docs/PlaylistGenerationsTrackPreferencesRelationshipPayloadDataMeta.md)
 - [PlaylistGenerationsTrackPreferencesRelationshipPayloadMeta](docs/PlaylistGenerationsTrackPreferencesRelationshipPayloadMeta.md)
 - [PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayload](docs/PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayload.md)
 - [PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayloadData](docs/PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayloadData.md)
 - [PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayload](docs/PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayload.md)
 - [PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayloadMeta](docs/PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayloadMeta.md)
 - [PlaylistGenerationsTrackPreferencesRemoveMultiDataRelationship409ResponseBody](docs/PlaylistGenerationsTrackPreferencesRemoveMultiDataRelationship409ResponseBody.md)
 - [PlaylistGenerationsTrackPreferencesResourceIdentifier](docs/PlaylistGenerationsTrackPreferencesResourceIdentifier.md)
 - [PlaylistGenerationsTrackPreferencesResourceIdentifierMeta](docs/PlaylistGenerationsTrackPreferencesResourceIdentifierMeta.md)
 - [PlaylistGenerationsTrackPreferencesUpdateMultiDataRelationship409ResponseBody](docs/PlaylistGenerationsTrackPreferencesUpdateMultiDataRelationship409ResponseBody.md)
 - [PlaylistGenerationsTrackPreferencesUpdateMultiRelationshipDataDocument](docs/PlaylistGenerationsTrackPreferencesUpdateMultiRelationshipDataDocument.md)
 - [PlaylistGenerationsTrackPreferencesUpdateMultiRelationshipDataDocumentMeta](docs/PlaylistGenerationsTrackPreferencesUpdateMultiRelationshipDataDocumentMeta.md)
 - [PlaylistGenerationsTrackPreferencesUpdateResourceIdentifier](docs/PlaylistGenerationsTrackPreferencesUpdateResourceIdentifier.md)
 - [PlaylistGenerationsTrackPreferencesUpdateResourceIdentifierMeta](docs/PlaylistGenerationsTrackPreferencesUpdateResourceIdentifierMeta.md)
 - [PlaylistsAttributes](docs/PlaylistsAttributes.md)
 - [PlaylistsCollaboratorProfilesMultiRelationshipDataDocument](docs/PlaylistsCollaboratorProfilesMultiRelationshipDataDocument.md)
 - [PlaylistsCollaboratorProfilesRelationshipRemoveOperationPayload](docs/PlaylistsCollaboratorProfilesRelationshipRemoveOperationPayload.md)
 - [PlaylistsCollaboratorProfilesRelationshipRemoveOperationPayloadData](docs/PlaylistsCollaboratorProfilesRelationshipRemoveOperationPayloadData.md)
 - [PlaylistsCollaboratorsMultiRelationshipDataDocument](docs/PlaylistsCollaboratorsMultiRelationshipDataDocument.md)
 - [PlaylistsCoverArtMultiRelationshipDataDocument](docs/PlaylistsCoverArtMultiRelationshipDataDocument.md)
 - [PlaylistsCoverArtRelationshipUpdateOperationPayload](docs/PlaylistsCoverArtRelationshipUpdateOperationPayload.md)
 - [PlaylistsCoverArtRelationshipUpdateOperationPayloadData](docs/PlaylistsCoverArtRelationshipUpdateOperationPayloadData.md)
 - [PlaylistsCreateOperationPayload](docs/PlaylistsCreateOperationPayload.md)
 - [PlaylistsCreateOperationPayloadData](docs/PlaylistsCreateOperationPayloadData.md)
 - [PlaylistsCreateOperationPayloadDataAttributes](docs/PlaylistsCreateOperationPayloadDataAttributes.md)
 - [PlaylistsCreateSingleResourceDataDocument](docs/PlaylistsCreateSingleResourceDataDocument.md)
 - [PlaylistsCuratorsMultiRelationshipDataDocument](docs/PlaylistsCuratorsMultiRelationshipDataDocument.md)
 - [PlaylistsItemsAddMultiDataRelationshipWithResponse409ResponseBody](docs/PlaylistsItemsAddMultiDataRelationshipWithResponse409ResponseBody.md)
 - [PlaylistsItemsAddMultiDataRelationshipWithResponse409ResponseBodyErrorsInner](docs/PlaylistsItemsAddMultiDataRelationshipWithResponse409ResponseBodyErrorsInner.md)
 - [PlaylistsItemsAddMultiRelationshipDataDocument](docs/PlaylistsItemsAddMultiRelationshipDataDocument.md)
 - [PlaylistsItemsAddMultiRelationshipDataDocumentMeta](docs/PlaylistsItemsAddMultiRelationshipDataDocumentMeta.md)
 - [PlaylistsItemsAddResourceIdentifier](docs/PlaylistsItemsAddResourceIdentifier.md)
 - [PlaylistsItemsAddResourceIdentifierMeta](docs/PlaylistsItemsAddResourceIdentifierMeta.md)
 - [PlaylistsItemsMultiRelationshipDataDocument](docs/PlaylistsItemsMultiRelationshipDataDocument.md)
 - [PlaylistsItemsRelationshipAddOperationPayload](docs/PlaylistsItemsRelationshipAddOperationPayload.md)
 - [PlaylistsItemsRelationshipAddOperationPayloadData](docs/PlaylistsItemsRelationshipAddOperationPayloadData.md)
 - [PlaylistsItemsRelationshipAddOperationPayloadDataMeta](docs/PlaylistsItemsRelationshipAddOperationPayloadDataMeta.md)
 - [PlaylistsItemsRelationshipAddOperationPayloadMeta](docs/PlaylistsItemsRelationshipAddOperationPayloadMeta.md)
 - [PlaylistsItemsRelationshipAddOperationResponseMetaSkippedItem](docs/PlaylistsItemsRelationshipAddOperationResponseMetaSkippedItem.md)
 - [PlaylistsItemsRelationshipRemoveOperationPayload](docs/PlaylistsItemsRelationshipRemoveOperationPayload.md)
 - [PlaylistsItemsRelationshipRemoveOperationPayloadData](docs/PlaylistsItemsRelationshipRemoveOperationPayloadData.md)
 - [PlaylistsItemsRelationshipRemoveOperationPayloadDataMeta](docs/PlaylistsItemsRelationshipRemoveOperationPayloadDataMeta.md)
 - [PlaylistsItemsRelationshipUpdateOperationPayload](docs/PlaylistsItemsRelationshipUpdateOperationPayload.md)
 - [PlaylistsItemsRelationshipUpdateOperationPayloadData](docs/PlaylistsItemsRelationshipUpdateOperationPayloadData.md)
 - [PlaylistsItemsRelationshipUpdateOperationPayloadDataMeta](docs/PlaylistsItemsRelationshipUpdateOperationPayloadDataMeta.md)
 - [PlaylistsItemsRelationshipUpdateOperationPayloadMeta](docs/PlaylistsItemsRelationshipUpdateOperationPayloadMeta.md)
 - [PlaylistsItemsRelationshipUpdateOperationPayloadMetaAnyOf](docs/PlaylistsItemsRelationshipUpdateOperationPayloadMetaAnyOf.md)
 - [PlaylistsItemsRelationshipUpdateOperationPayloadMetaAnyOf1](docs/PlaylistsItemsRelationshipUpdateOperationPayloadMetaAnyOf1.md)
 - [PlaylistsItemsResourceIdentifier](docs/PlaylistsItemsResourceIdentifier.md)
 - [PlaylistsItemsResourceIdentifierMeta](docs/PlaylistsItemsResourceIdentifierMeta.md)
 - [PlaylistsMultiResourceDataDocument](docs/PlaylistsMultiResourceDataDocument.md)
 - [PlaylistsOwnerProfilesMultiRelationshipDataDocument](docs/PlaylistsOwnerProfilesMultiRelationshipDataDocument.md)
 - [PlaylistsOwnersMultiRelationshipDataDocument](docs/PlaylistsOwnersMultiRelationshipDataDocument.md)
 - [PlaylistsRelationships](docs/PlaylistsRelationships.md)
 - [PlaylistsResourceObject](docs/PlaylistsResourceObject.md)
 - [PlaylistsSingleResourceDataDocument](docs/PlaylistsSingleResourceDataDocument.md)
 - [PlaylistsSuggestedCoverArtsMultiRelationshipDataDocument](docs/PlaylistsSuggestedCoverArtsMultiRelationshipDataDocument.md)
 - [PlaylistsSuggestedCoverArtsResourceIdentifier](docs/PlaylistsSuggestedCoverArtsResourceIdentifier.md)
 - [PlaylistsSuggestedCoverArtsResourceIdentifierMeta](docs/PlaylistsSuggestedCoverArtsResourceIdentifierMeta.md)
 - [PlaylistsUpdateOperationPayload](docs/PlaylistsUpdateOperationPayload.md)
 - [PlaylistsUpdateOperationPayloadData](docs/PlaylistsUpdateOperationPayloadData.md)
 - [PlaylistsUpdateOperationPayloadDataAttributes](docs/PlaylistsUpdateOperationPayloadDataAttributes.md)
 - [PlaylistsUpdateSingleResourceDataDocument](docs/PlaylistsUpdateSingleResourceDataDocument.md)
 - [PriceConfigurationsAttributes](docs/PriceConfigurationsAttributes.md)
 - [PriceConfigurationsCreateOperationPayload](docs/PriceConfigurationsCreateOperationPayload.md)
 - [PriceConfigurationsCreateOperationPayloadData](docs/PriceConfigurationsCreateOperationPayloadData.md)
 - [PriceConfigurationsCreateOperationPayloadDataAttributes](docs/PriceConfigurationsCreateOperationPayloadDataAttributes.md)
 - [PriceConfigurationsCreateOperationPayloadDataRelationships](docs/PriceConfigurationsCreateOperationPayloadDataRelationships.md)
 - [PriceConfigurationsCreateOperationPayloadDataRelationshipsSubjects](docs/PriceConfigurationsCreateOperationPayloadDataRelationshipsSubjects.md)
 - [PriceConfigurationsCreateOperationPayloadSubjects](docs/PriceConfigurationsCreateOperationPayloadSubjects.md)
 - [PriceConfigurationsCreateSingleResourceDataDocument](docs/PriceConfigurationsCreateSingleResourceDataDocument.md)
 - [PriceConfigurationsMultiResourceDataDocument](docs/PriceConfigurationsMultiResourceDataDocument.md)
 - [PriceConfigurationsResourceObject](docs/PriceConfigurationsResourceObject.md)
 - [PriceConfigurationsSingleResourceDataDocument](docs/PriceConfigurationsSingleResourceDataDocument.md)
 - [ProviderOwnersAttributes](docs/ProviderOwnersAttributes.md)
 - [ProviderOwnersMultiResourceDataDocument](docs/ProviderOwnersMultiResourceDataDocument.md)
 - [ProviderOwnersOwnersMultiRelationshipDataDocument](docs/ProviderOwnersOwnersMultiRelationshipDataDocument.md)
 - [ProviderOwnersProviderSingleRelationshipDataDocument](docs/ProviderOwnersProviderSingleRelationshipDataDocument.md)
 - [ProviderOwnersRelationships](docs/ProviderOwnersRelationships.md)
 - [ProviderOwnersResourceObject](docs/ProviderOwnersResourceObject.md)
 - [ProviderProductInfosAttributes](docs/ProviderProductInfosAttributes.md)
 - [ProviderProductInfosMultiResourceDataDocument](docs/ProviderProductInfosMultiResourceDataDocument.md)
 - [ProviderProductInfosProviderSingleRelationshipDataDocument](docs/ProviderProductInfosProviderSingleRelationshipDataDocument.md)
 - [ProviderProductInfosRelationships](docs/ProviderProductInfosRelationships.md)
 - [ProviderProductInfosResourceObject](docs/ProviderProductInfosResourceObject.md)
 - [ProviderProductInfosSubjectResourceIdentifier](docs/ProviderProductInfosSubjectResourceIdentifier.md)
 - [ProviderProductInfosSubjectResourceIdentifierMeta](docs/ProviderProductInfosSubjectResourceIdentifierMeta.md)
 - [ProviderProductInfosSubjectSingleRelationshipDataDocument](docs/ProviderProductInfosSubjectSingleRelationshipDataDocument.md)
 - [ProvidersAttributes](docs/ProvidersAttributes.md)
 - [ProvidersResourceObject](docs/ProvidersResourceObject.md)
 - [ProvidersSingleResourceDataDocument](docs/ProvidersSingleResourceDataDocument.md)
 - [PurchasesAttributes](docs/PurchasesAttributes.md)
 - [PurchasesMultiResourceDataDocument](docs/PurchasesMultiResourceDataDocument.md)
 - [PurchasesOwnersMultiRelationshipDataDocument](docs/PurchasesOwnersMultiRelationshipDataDocument.md)
 - [PurchasesRelationships](docs/PurchasesRelationships.md)
 - [PurchasesResourceObject](docs/PurchasesResourceObject.md)
 - [PurchasesSubjectResourceIdentifier](docs/PurchasesSubjectResourceIdentifier.md)
 - [PurchasesSubjectResourceIdentifierMeta](docs/PurchasesSubjectResourceIdentifierMeta.md)
 - [PurchasesSubjectSingleRelationshipDataDocument](docs/PurchasesSubjectSingleRelationshipDataDocument.md)
 - [ReactionSummariesAttributes](docs/ReactionSummariesAttributes.md)
 - [ReactionSummariesMultiResourceDataDocument](docs/ReactionSummariesMultiResourceDataDocument.md)
 - [ReactionSummariesRelationships](docs/ReactionSummariesRelationships.md)
 - [ReactionSummariesResourceObject](docs/ReactionSummariesResourceObject.md)
 - [ReactionSummariesSubjectSingleRelationshipDataDocument](docs/ReactionSummariesSubjectSingleRelationshipDataDocument.md)
 - [ReactionsAttributes](docs/ReactionsAttributes.md)
 - [ReactionsAuthorSingleRelationshipDataDocument](docs/ReactionsAuthorSingleRelationshipDataDocument.md)
 - [ReactionsCreateOperationPayload](docs/ReactionsCreateOperationPayload.md)
 - [ReactionsCreateOperationPayloadData](docs/ReactionsCreateOperationPayloadData.md)
 - [ReactionsCreateOperationPayloadDataAttributes](docs/ReactionsCreateOperationPayloadDataAttributes.md)
 - [ReactionsCreateOperationPayloadDataRelationships](docs/ReactionsCreateOperationPayloadDataRelationships.md)
 - [ReactionsCreateOperationPayloadDataRelationshipsSubject](docs/ReactionsCreateOperationPayloadDataRelationshipsSubject.md)
 - [ReactionsCreateOperationPayloadDataRelationshipsSubjectData](docs/ReactionsCreateOperationPayloadDataRelationshipsSubjectData.md)
 - [ReactionsCreateSingleResourceDataDocument](docs/ReactionsCreateSingleResourceDataDocument.md)
 - [ReactionsMultiResourceDataDocument](docs/ReactionsMultiResourceDataDocument.md)
 - [ReactionsOwnersMultiRelationshipDataDocument](docs/ReactionsOwnersMultiRelationshipDataDocument.md)
 - [ReactionsRelationships](docs/ReactionsRelationships.md)
 - [ReactionsResourceObject](docs/ReactionsResourceObject.md)
 - [ReactionsSubjectSingleRelationshipDataDocument](docs/ReactionsSubjectSingleRelationshipDataDocument.md)
 - [ReplacementOriginalIdentifier](docs/ReplacementOriginalIdentifier.md)
 - [ReplacementProvenance](docs/ReplacementProvenance.md)
 - [ResourceGrantInvitationsAttributes](docs/ResourceGrantInvitationsAttributes.md)
 - [ResourceGrantInvitationsCreateOperationPayload](docs/ResourceGrantInvitationsCreateOperationPayload.md)
 - [ResourceGrantInvitationsCreateOperationPayloadData](docs/ResourceGrantInvitationsCreateOperationPayloadData.md)
 - [ResourceGrantInvitationsCreateOperationPayloadDataAttributes](docs/ResourceGrantInvitationsCreateOperationPayloadDataAttributes.md)
 - [ResourceGrantInvitationsCreateOperationPayloadDataRelationships](docs/ResourceGrantInvitationsCreateOperationPayloadDataRelationships.md)
 - [ResourceGrantInvitationsCreateOperationPayloadDataRelationshipsSubject](docs/ResourceGrantInvitationsCreateOperationPayloadDataRelationshipsSubject.md)
 - [ResourceGrantInvitationsCreateOperationPayloadDataRelationshipsSubjectData](docs/ResourceGrantInvitationsCreateOperationPayloadDataRelationshipsSubjectData.md)
 - [ResourceGrantInvitationsCreateSingleResourceDataDocument](docs/ResourceGrantInvitationsCreateSingleResourceDataDocument.md)
 - [ResourceGrantInvitationsMultiResourceDataDocument](docs/ResourceGrantInvitationsMultiResourceDataDocument.md)
 - [ResourceGrantInvitationsOwnersMultiRelationshipDataDocument](docs/ResourceGrantInvitationsOwnersMultiRelationshipDataDocument.md)
 - [ResourceGrantInvitationsPreviewGrantSingleRelationshipDataDocument](docs/ResourceGrantInvitationsPreviewGrantSingleRelationshipDataDocument.md)
 - [ResourceGrantInvitationsRelationships](docs/ResourceGrantInvitationsRelationships.md)
 - [ResourceGrantInvitationsResourceObject](docs/ResourceGrantInvitationsResourceObject.md)
 - [ResourceGrantInvitationsSingleResourceDataDocument](docs/ResourceGrantInvitationsSingleResourceDataDocument.md)
 - [ResourceGrantInvitationsSubjectResourceIdentifier](docs/ResourceGrantInvitationsSubjectResourceIdentifier.md)
 - [ResourceGrantInvitationsSubjectResourceIdentifierMeta](docs/ResourceGrantInvitationsSubjectResourceIdentifierMeta.md)
 - [ResourceGrantInvitationsSubjectSingleRelationshipDataDocument](docs/ResourceGrantInvitationsSubjectSingleRelationshipDataDocument.md)
 - [ResourceGrantInvitationsUpdateOperationPayload](docs/ResourceGrantInvitationsUpdateOperationPayload.md)
 - [ResourceGrantInvitationsUpdateOperationPayloadData](docs/ResourceGrantInvitationsUpdateOperationPayloadData.md)
 - [ResourceGrantInvitationsUpdateOperationPayloadDataAttributes](docs/ResourceGrantInvitationsUpdateOperationPayloadDataAttributes.md)
 - [ResourceGrantInvitationsUpdateSingleResourceDataDocument](docs/ResourceGrantInvitationsUpdateSingleResourceDataDocument.md)
 - [ResourceGrantsAttributes](docs/ResourceGrantsAttributes.md)
 - [ResourceGrantsCreateOperationPayload](docs/ResourceGrantsCreateOperationPayload.md)
 - [ResourceGrantsCreateOperationPayloadData](docs/ResourceGrantsCreateOperationPayloadData.md)
 - [ResourceGrantsCreateOperationPayloadDataAttributes](docs/ResourceGrantsCreateOperationPayloadDataAttributes.md)
 - [ResourceGrantsCreateOperationPayloadDataRelationships](docs/ResourceGrantsCreateOperationPayloadDataRelationships.md)
 - [ResourceGrantsCreateOperationPayloadMeta](docs/ResourceGrantsCreateOperationPayloadMeta.md)
 - [ResourceGrantsCreateResource403ResponseBody](docs/ResourceGrantsCreateResource403ResponseBody.md)
 - [ResourceGrantsCreateResource403ResponseBodyErrorsInner](docs/ResourceGrantsCreateResource403ResponseBodyErrorsInner.md)
 - [ResourceGrantsCreateResource429ResponseBody](docs/ResourceGrantsCreateResource429ResponseBody.md)
 - [ResourceGrantsCreateResource429ResponseBodyErrorsInner](docs/ResourceGrantsCreateResource429ResponseBodyErrorsInner.md)
 - [ResourceGrantsCreateSingleResourceDataDocument](docs/ResourceGrantsCreateSingleResourceDataDocument.md)
 - [ResourceGrantsGrantee](docs/ResourceGrantsGrantee.md)
 - [ResourceGrantsGranteeLinkage](docs/ResourceGrantsGranteeLinkage.md)
 - [ResourceGrantsGranteeSingleRelationshipDataDocument](docs/ResourceGrantsGranteeSingleRelationshipDataDocument.md)
 - [ResourceGrantsInvitation](docs/ResourceGrantsInvitation.md)
 - [ResourceGrantsInvitationLinkage](docs/ResourceGrantsInvitationLinkage.md)
 - [ResourceGrantsInvitationSingleRelationshipDataDocument](docs/ResourceGrantsInvitationSingleRelationshipDataDocument.md)
 - [ResourceGrantsMultiResourceDataDocument](docs/ResourceGrantsMultiResourceDataDocument.md)
 - [ResourceGrantsRelationships](docs/ResourceGrantsRelationships.md)
 - [ResourceGrantsResourceObject](docs/ResourceGrantsResourceObject.md)
 - [ResourceGrantsSingleResourceDataDocument](docs/ResourceGrantsSingleResourceDataDocument.md)
 - [ResourceGrantsSubject](docs/ResourceGrantsSubject.md)
 - [ResourceGrantsSubjectLinkage](docs/ResourceGrantsSubjectLinkage.md)
 - [ResourceGrantsSubjectResourceIdentifier](docs/ResourceGrantsSubjectResourceIdentifier.md)
 - [ResourceGrantsSubjectResourceIdentifierMeta](docs/ResourceGrantsSubjectResourceIdentifierMeta.md)
 - [ResourceGrantsSubjectSingleRelationshipDataDocument](docs/ResourceGrantsSubjectSingleRelationshipDataDocument.md)
 - [ResourceGrantsUpdateOperationPayload](docs/ResourceGrantsUpdateOperationPayload.md)
 - [ResourceGrantsUpdateOperationPayloadData](docs/ResourceGrantsUpdateOperationPayloadData.md)
 - [ResourceGrantsUpdateOperationPayloadDataAttributes](docs/ResourceGrantsUpdateOperationPayloadDataAttributes.md)
 - [ResourceGrantsUpdateSingleResourceDataDocument](docs/ResourceGrantsUpdateSingleResourceDataDocument.md)
 - [ResourceIdentifier](docs/ResourceIdentifier.md)
 - [ResourceObjectObjectObject](docs/ResourceObjectObjectObject.md)
 - [SavedSharesAttributes](docs/SavedSharesAttributes.md)
 - [SavedSharesCreateOperationPayload](docs/SavedSharesCreateOperationPayload.md)
 - [SavedSharesCreateOperationPayloadData](docs/SavedSharesCreateOperationPayloadData.md)
 - [SavedSharesCreateOperationPayloadDataRelationships](docs/SavedSharesCreateOperationPayloadDataRelationships.md)
 - [SavedSharesCreateOperationPayloadDataRelationshipsShare](docs/SavedSharesCreateOperationPayloadDataRelationshipsShare.md)
 - [SavedSharesCreateOperationPayloadDataRelationshipsShareData](docs/SavedSharesCreateOperationPayloadDataRelationshipsShareData.md)
 - [SavedSharesCreateOperationPayloadMeta](docs/SavedSharesCreateOperationPayloadMeta.md)
 - [SavedSharesCreateResource403ResponseBody](docs/SavedSharesCreateResource403ResponseBody.md)
 - [SavedSharesCreateResource403ResponseBodyErrorsInner](docs/SavedSharesCreateResource403ResponseBodyErrorsInner.md)
 - [SavedSharesCreateResource429ResponseBody](docs/SavedSharesCreateResource429ResponseBody.md)
 - [SavedSharesCreateResource429ResponseBodyErrorsInner](docs/SavedSharesCreateResource429ResponseBodyErrorsInner.md)
 - [SavedSharesCreateSingleResourceDataDocument](docs/SavedSharesCreateSingleResourceDataDocument.md)
 - [SavedSharesResourceObject](docs/SavedSharesResourceObject.md)
 - [ScopesAttributes](docs/ScopesAttributes.md)
 - [ScopesMultiResourceDataDocument](docs/ScopesMultiResourceDataDocument.md)
 - [ScopesResourceObject](docs/ScopesResourceObject.md)
 - [SearchHistoryEntriesAttributes](docs/SearchHistoryEntriesAttributes.md)
 - [SearchHistoryEntriesResourceObject](docs/SearchHistoryEntriesResourceObject.md)
 - [SearchResultsAlbumsMultiRelationshipDataDocument](docs/SearchResultsAlbumsMultiRelationshipDataDocument.md)
 - [SearchResultsAlbumsResourceIdentifier](docs/SearchResultsAlbumsResourceIdentifier.md)
 - [SearchResultsAlbumsResourceIdentifierMeta](docs/SearchResultsAlbumsResourceIdentifierMeta.md)
 - [SearchResultsArtistsMultiRelationshipDataDocument](docs/SearchResultsArtistsMultiRelationshipDataDocument.md)
 - [SearchResultsAttributes](docs/SearchResultsAttributes.md)
 - [SearchResultsMultiResourceDataDocument](docs/SearchResultsMultiResourceDataDocument.md)
 - [SearchResultsPlaylistsMultiRelationshipDataDocument](docs/SearchResultsPlaylistsMultiRelationshipDataDocument.md)
 - [SearchResultsRelationships](docs/SearchResultsRelationships.md)
 - [SearchResultsResourceObject](docs/SearchResultsResourceObject.md)
 - [SearchResultsTopHitsMultiRelationshipDataDocument](docs/SearchResultsTopHitsMultiRelationshipDataDocument.md)
 - [SearchResultsTopHitsResourceIdentifier](docs/SearchResultsTopHitsResourceIdentifier.md)
 - [SearchResultsTopHitsResourceIdentifierMeta](docs/SearchResultsTopHitsResourceIdentifierMeta.md)
 - [SearchResultsTracksMultiRelationshipDataDocument](docs/SearchResultsTracksMultiRelationshipDataDocument.md)
 - [SearchResultsTracksResourceIdentifier](docs/SearchResultsTracksResourceIdentifier.md)
 - [SearchResultsTracksResourceIdentifierMeta](docs/SearchResultsTracksResourceIdentifierMeta.md)
 - [SearchResultsVideosMultiRelationshipDataDocument](docs/SearchResultsVideosMultiRelationshipDataDocument.md)
 - [SearchResultsVideosResourceIdentifier](docs/SearchResultsVideosResourceIdentifier.md)
 - [SearchResultsVideosResourceIdentifierMeta](docs/SearchResultsVideosResourceIdentifierMeta.md)
 - [SearchSuggestionsAttributes](docs/SearchSuggestionsAttributes.md)
 - [SearchSuggestionsDirectHitsMultiRelationshipDataDocument](docs/SearchSuggestionsDirectHitsMultiRelationshipDataDocument.md)
 - [SearchSuggestionsDirectHitsResourceIdentifier](docs/SearchSuggestionsDirectHitsResourceIdentifier.md)
 - [SearchSuggestionsDirectHitsResourceIdentifierMeta](docs/SearchSuggestionsDirectHitsResourceIdentifierMeta.md)
 - [SearchSuggestionsHighlights](docs/SearchSuggestionsHighlights.md)
 - [SearchSuggestionsHistoryMultiRelationshipDataDocument](docs/SearchSuggestionsHistoryMultiRelationshipDataDocument.md)
 - [SearchSuggestionsMultiResourceDataDocument](docs/SearchSuggestionsMultiResourceDataDocument.md)
 - [SearchSuggestionsRelationships](docs/SearchSuggestionsRelationships.md)
 - [SearchSuggestionsResourceObject](docs/SearchSuggestionsResourceObject.md)
 - [SearchSuggestionsSuggestions](docs/SearchSuggestionsSuggestions.md)
 - [SharesAttributes](docs/SharesAttributes.md)
 - [SharesCreateOperationPayload](docs/SharesCreateOperationPayload.md)
 - [SharesCreateOperationPayloadData](docs/SharesCreateOperationPayloadData.md)
 - [SharesCreateOperationPayloadDataAttributes](docs/SharesCreateOperationPayloadDataAttributes.md)
 - [SharesCreateOperationPayloadDataRelationships](docs/SharesCreateOperationPayloadDataRelationships.md)
 - [SharesCreateOperationPayloadDataRelationshipsSharedResources](docs/SharesCreateOperationPayloadDataRelationshipsSharedResources.md)
 - [SharesCreateOperationPayloadDataRelationshipsSharedResourcesData](docs/SharesCreateOperationPayloadDataRelationshipsSharedResourcesData.md)
 - [SharesCreateSingleResourceDataDocument](docs/SharesCreateSingleResourceDataDocument.md)
 - [SharesMultiResourceDataDocument](docs/SharesMultiResourceDataDocument.md)
 - [SharesOwnersMultiRelationshipDataDocument](docs/SharesOwnersMultiRelationshipDataDocument.md)
 - [SharesRelationships](docs/SharesRelationships.md)
 - [SharesResourceObject](docs/SharesResourceObject.md)
 - [SharesSharedResourcesMultiRelationshipDataDocument](docs/SharesSharedResourcesMultiRelationshipDataDocument.md)
 - [SharesSharedResourcesResourceIdentifier](docs/SharesSharedResourcesResourceIdentifier.md)
 - [SharesSharedResourcesResourceIdentifierMeta](docs/SharesSharedResourcesResourceIdentifierMeta.md)
 - [SharesSingleResourceDataDocument](docs/SharesSingleResourceDataDocument.md)
 - [SharesUpdateOperationPayload](docs/SharesUpdateOperationPayload.md)
 - [SharesUpdateOperationPayloadData](docs/SharesUpdateOperationPayloadData.md)
 - [SharesUpdateOperationPayloadDataAttributes](docs/SharesUpdateOperationPayloadDataAttributes.md)
 - [SharesUpdateSingleResourceDataDocument](docs/SharesUpdateSingleResourceDataDocument.md)
 - [SharingSummariesAttributes](docs/SharingSummariesAttributes.md)
 - [SharingSummariesMultiResourceDataDocument](docs/SharingSummariesMultiResourceDataDocument.md)
 - [SharingSummariesRelationships](docs/SharingSummariesRelationships.md)
 - [SharingSummariesResourceObject](docs/SharingSummariesResourceObject.md)
 - [SharingSummariesSubjectResourceIdentifier](docs/SharingSummariesSubjectResourceIdentifier.md)
 - [SharingSummariesSubjectResourceIdentifierMeta](docs/SharingSummariesSubjectResourceIdentifierMeta.md)
 - [SharingSummariesSubjectSingleRelationshipDataDocument](docs/SharingSummariesSubjectSingleRelationshipDataDocument.md)
 - [Site](docs/Site.md)
 - [SourceProcessing](docs/SourceProcessing.md)
 - [SquareConnectionsAttributes](docs/SquareConnectionsAttributes.md)
 - [SquareConnectionsCapability](docs/SquareConnectionsCapability.md)
 - [SquareConnectionsCreateOperationPayload](docs/SquareConnectionsCreateOperationPayload.md)
 - [SquareConnectionsCreateOperationPayloadData](docs/SquareConnectionsCreateOperationPayloadData.md)
 - [SquareConnectionsCreateOperationPayloadMeta](docs/SquareConnectionsCreateOperationPayloadMeta.md)
 - [SquareConnectionsCreateSingleResourceDataDocument](docs/SquareConnectionsCreateSingleResourceDataDocument.md)
 - [SquareConnectionsReadById403ResponseBody](docs/SquareConnectionsReadById403ResponseBody.md)
 - [SquareConnectionsRelationships](docs/SquareConnectionsRelationships.md)
 - [SquareConnectionsResourceObject](docs/SquareConnectionsResourceObject.md)
 - [SquareConnectionsSelectedSiteReadSingleDataRelationship403ResponseBody](docs/SquareConnectionsSelectedSiteReadSingleDataRelationship403ResponseBody.md)
 - [SquareConnectionsSelectedSiteRelationshipUpdateOperationPayload](docs/SquareConnectionsSelectedSiteRelationshipUpdateOperationPayload.md)
 - [SquareConnectionsSelectedSiteRelationshipUpdateOperationPayloadData](docs/SquareConnectionsSelectedSiteRelationshipUpdateOperationPayloadData.md)
 - [SquareConnectionsSelectedSiteSingleRelationshipDataDocument](docs/SquareConnectionsSelectedSiteSingleRelationshipDataDocument.md)
 - [SquareConnectionsSelectedSiteUpdateResourceIdentifier](docs/SquareConnectionsSelectedSiteUpdateResourceIdentifier.md)
 - [SquareConnectionsSelectedSiteUpdateSingleDataRelationship403ResponseBody](docs/SquareConnectionsSelectedSiteUpdateSingleDataRelationship403ResponseBody.md)
 - [SquareConnectionsSelectedSiteUpdateSingleDataRelationship409ResponseBody](docs/SquareConnectionsSelectedSiteUpdateSingleDataRelationship409ResponseBody.md)
 - [SquareConnectionsSelectedSiteUpdateSingleDataRelationship409ResponseBodyErrorsInner](docs/SquareConnectionsSelectedSiteUpdateSingleDataRelationship409ResponseBodyErrorsInner.md)
 - [SquareConnectionsSelectedSiteUpdateSingleRelationshipDataDocument](docs/SquareConnectionsSelectedSiteUpdateSingleRelationshipDataDocument.md)
 - [SquareConnectionsSingleResourceDataDocument](docs/SquareConnectionsSingleResourceDataDocument.md)
 - [SquareConnectionsSitesMultiRelationshipDataDocument](docs/SquareConnectionsSitesMultiRelationshipDataDocument.md)
 - [SquareConnectionsSitesReadMultiDataRelationship403ResponseBody](docs/SquareConnectionsSitesReadMultiDataRelationship403ResponseBody.md)
 - [SquareItemVariationPhysicalCountsAttributes](docs/SquareItemVariationPhysicalCountsAttributes.md)
 - [SquareItemVariationPhysicalCountsCreateOperationPayload](docs/SquareItemVariationPhysicalCountsCreateOperationPayload.md)
 - [SquareItemVariationPhysicalCountsCreateOperationPayloadData](docs/SquareItemVariationPhysicalCountsCreateOperationPayloadData.md)
 - [SquareItemVariationPhysicalCountsCreateOperationPayloadDataAttributes](docs/SquareItemVariationPhysicalCountsCreateOperationPayloadDataAttributes.md)
 - [SquareItemVariationPhysicalCountsCreateOperationPayloadDataRelationships](docs/SquareItemVariationPhysicalCountsCreateOperationPayloadDataRelationships.md)
 - [SquareItemVariationPhysicalCountsCreateOperationPayloadDataRelationshipsVariations](docs/SquareItemVariationPhysicalCountsCreateOperationPayloadDataRelationshipsVariations.md)
 - [SquareItemVariationPhysicalCountsCreateResource403ResponseBody](docs/SquareItemVariationPhysicalCountsCreateResource403ResponseBody.md)
 - [SquareItemVariationPhysicalCountsCreateResource409ResponseBody](docs/SquareItemVariationPhysicalCountsCreateResource409ResponseBody.md)
 - [SquareItemVariationPhysicalCountsCreateResource409ResponseBodyErrorsInner](docs/SquareItemVariationPhysicalCountsCreateResource409ResponseBodyErrorsInner.md)
 - [SquareItemVariationPhysicalCountsCreateSingleResourceDataDocument](docs/SquareItemVariationPhysicalCountsCreateSingleResourceDataDocument.md)
 - [SquareItemVariationPhysicalCountsResourceObject](docs/SquareItemVariationPhysicalCountsResourceObject.md)
 - [SquareItemVariationsArtworksMultiRelationshipDataDocument](docs/SquareItemVariationsArtworksMultiRelationshipDataDocument.md)
 - [SquareItemVariationsArtworksMultiRelationshipDataDocumentMeta](docs/SquareItemVariationsArtworksMultiRelationshipDataDocumentMeta.md)
 - [SquareItemVariationsArtworksReadMultiDataRelationship403ResponseBody](docs/SquareItemVariationsArtworksReadMultiDataRelationship403ResponseBody.md)
 - [SquareItemVariationsArtworksReadMultiDataRelationship409ResponseBody](docs/SquareItemVariationsArtworksReadMultiDataRelationship409ResponseBody.md)
 - [SquareItemVariationsArtworksReadMultiDataRelationship409ResponseBodyErrorsInner](docs/SquareItemVariationsArtworksReadMultiDataRelationship409ResponseBodyErrorsInner.md)
 - [SquareItemVariationsArtworksRelationshipUpdateOperationPayload](docs/SquareItemVariationsArtworksRelationshipUpdateOperationPayload.md)
 - [SquareItemVariationsArtworksRelationshipUpdateOperationPayloadMeta](docs/SquareItemVariationsArtworksRelationshipUpdateOperationPayloadMeta.md)
 - [SquareItemVariationsArtworksUpdateMultiDataRelationship403ResponseBody](docs/SquareItemVariationsArtworksUpdateMultiDataRelationship403ResponseBody.md)
 - [SquareItemVariationsArtworksUpdateMultiDataRelationship409ResponseBody](docs/SquareItemVariationsArtworksUpdateMultiDataRelationship409ResponseBody.md)
 - [SquareItemVariationsArtworksUpdateMultiDataRelationship409ResponseBodyErrorsInner](docs/SquareItemVariationsArtworksUpdateMultiDataRelationship409ResponseBodyErrorsInner.md)
 - [SquareItemVariationsArtworksUpdateMultiDataRelationship413ResponseBody](docs/SquareItemVariationsArtworksUpdateMultiDataRelationship413ResponseBody.md)
 - [SquareItemVariationsArtworksUpdateMultiDataRelationship413ResponseBodyErrorsInner](docs/SquareItemVariationsArtworksUpdateMultiDataRelationship413ResponseBodyErrorsInner.md)
 - [SquareItemVariationsArtworksUpdateMultiRelationshipDataDocument](docs/SquareItemVariationsArtworksUpdateMultiRelationshipDataDocument.md)
 - [SquareItemVariationsArtworksUpdateMultiRelationshipDataDocumentMeta](docs/SquareItemVariationsArtworksUpdateMultiRelationshipDataDocumentMeta.md)
 - [SquareItemVariationsArtworksUpdateResourceIdentifier](docs/SquareItemVariationsArtworksUpdateResourceIdentifier.md)
 - [SquareItemVariationsAttributes](docs/SquareItemVariationsAttributes.md)
 - [SquareItemVariationsCreateOperationPayload](docs/SquareItemVariationsCreateOperationPayload.md)
 - [SquareItemVariationsCreateOperationPayloadData](docs/SquareItemVariationsCreateOperationPayloadData.md)
 - [SquareItemVariationsCreateOperationPayloadDataAttributes](docs/SquareItemVariationsCreateOperationPayloadDataAttributes.md)
 - [SquareItemVariationsCreateOperationPayloadDataRelationships](docs/SquareItemVariationsCreateOperationPayloadDataRelationships.md)
 - [SquareItemVariationsCreateOperationPayloadDataRelationshipsItems](docs/SquareItemVariationsCreateOperationPayloadDataRelationshipsItems.md)
 - [SquareItemVariationsCreateOperationPayloadLocal](docs/SquareItemVariationsCreateOperationPayloadLocal.md)
 - [SquareItemVariationsCreateOperationPayloadLocalData](docs/SquareItemVariationsCreateOperationPayloadLocalData.md)
 - [SquareItemVariationsCreateOperationPayloadLocalDataRelationships](docs/SquareItemVariationsCreateOperationPayloadLocalDataRelationships.md)
 - [SquareItemVariationsCreateOperationPayloadLocalDataRelationshipsItems](docs/SquareItemVariationsCreateOperationPayloadLocalDataRelationshipsItems.md)
 - [SquareItemVariationsCreateOperationPayloadLocalItem](docs/SquareItemVariationsCreateOperationPayloadLocalItem.md)
 - [SquareItemVariationsCreateResource403ResponseBody](docs/SquareItemVariationsCreateResource403ResponseBody.md)
 - [SquareItemVariationsCreateResource409ResponseBody](docs/SquareItemVariationsCreateResource409ResponseBody.md)
 - [SquareItemVariationsCreateResource409ResponseBodyErrorsInner](docs/SquareItemVariationsCreateResource409ResponseBodyErrorsInner.md)
 - [SquareItemVariationsCreateSingleResourceDataDocument](docs/SquareItemVariationsCreateSingleResourceDataDocument.md)
 - [SquareItemVariationsCreateSingleResourceDataDocumentMeta](docs/SquareItemVariationsCreateSingleResourceDataDocumentMeta.md)
 - [SquareItemVariationsDeleteResource403ResponseBody](docs/SquareItemVariationsDeleteResource403ResponseBody.md)
 - [SquareItemVariationsDeleteResource409ResponseBody](docs/SquareItemVariationsDeleteResource409ResponseBody.md)
 - [SquareItemVariationsDeleteResource409ResponseBodyErrorsInner](docs/SquareItemVariationsDeleteResource409ResponseBodyErrorsInner.md)
 - [SquareItemVariationsExpectedItemRevision](docs/SquareItemVariationsExpectedItemRevision.md)
 - [SquareItemVariationsOwnersMultiRelationshipDataDocument](docs/SquareItemVariationsOwnersMultiRelationshipDataDocument.md)
 - [SquareItemVariationsReadById403ResponseBody](docs/SquareItemVariationsReadById403ResponseBody.md)
 - [SquareItemVariationsReadById409ResponseBody](docs/SquareItemVariationsReadById409ResponseBody.md)
 - [SquareItemVariationsReadById409ResponseBodyErrorsInner](docs/SquareItemVariationsReadById409ResponseBodyErrorsInner.md)
 - [SquareItemVariationsRelationships](docs/SquareItemVariationsRelationships.md)
 - [SquareItemVariationsResourceObject](docs/SquareItemVariationsResourceObject.md)
 - [SquareItemVariationsSingleResourceDataDocument](docs/SquareItemVariationsSingleResourceDataDocument.md)
 - [SquareItemVariationsUpdateOperationPayload](docs/SquareItemVariationsUpdateOperationPayload.md)
 - [SquareItemVariationsUpdateOperationPayloadData](docs/SquareItemVariationsUpdateOperationPayloadData.md)
 - [SquareItemVariationsUpdateOperationPayloadDataAttributes](docs/SquareItemVariationsUpdateOperationPayloadDataAttributes.md)
 - [SquareItemVariationsUpdateOperationPayloadMeta](docs/SquareItemVariationsUpdateOperationPayloadMeta.md)
 - [SquareItemVariationsUpdateResource403ResponseBody](docs/SquareItemVariationsUpdateResource403ResponseBody.md)
 - [SquareItemVariationsUpdateResource409ResponseBody](docs/SquareItemVariationsUpdateResource409ResponseBody.md)
 - [SquareItemVariationsUpdateResource409ResponseBodyErrorsInner](docs/SquareItemVariationsUpdateResource409ResponseBodyErrorsInner.md)
 - [SquareItemVariationsUpdateSingleResourceDataDocument](docs/SquareItemVariationsUpdateSingleResourceDataDocument.md)
 - [SquareItemsArtworksMultiRelationshipDataDocument](docs/SquareItemsArtworksMultiRelationshipDataDocument.md)
 - [SquareItemsArtworksReadMultiDataRelationship409ResponseBody](docs/SquareItemsArtworksReadMultiDataRelationship409ResponseBody.md)
 - [SquareItemsArtworksRelationshipUpdateOperationPayload](docs/SquareItemsArtworksRelationshipUpdateOperationPayload.md)
 - [SquareItemsArtworksRelationshipUpdateOperationPayloadMeta](docs/SquareItemsArtworksRelationshipUpdateOperationPayloadMeta.md)
 - [SquareItemsArtworksUpdateMultiDataRelationship403ResponseBody](docs/SquareItemsArtworksUpdateMultiDataRelationship403ResponseBody.md)
 - [SquareItemsArtworksUpdateMultiDataRelationship409ResponseBody](docs/SquareItemsArtworksUpdateMultiDataRelationship409ResponseBody.md)
 - [SquareItemsArtworksUpdateMultiDataRelationship409ResponseBodyErrorsInner](docs/SquareItemsArtworksUpdateMultiDataRelationship409ResponseBodyErrorsInner.md)
 - [SquareItemsArtworksUpdateMultiDataRelationship413ResponseBody](docs/SquareItemsArtworksUpdateMultiDataRelationship413ResponseBody.md)
 - [SquareItemsArtworksUpdateMultiRelationshipDataDocument](docs/SquareItemsArtworksUpdateMultiRelationshipDataDocument.md)
 - [SquareItemsArtworksUpdateMultiRelationshipDataDocumentMeta](docs/SquareItemsArtworksUpdateMultiRelationshipDataDocumentMeta.md)
 - [SquareItemsArtworksUpdateResourceIdentifier](docs/SquareItemsArtworksUpdateResourceIdentifier.md)
 - [SquareItemsAttributes](docs/SquareItemsAttributes.md)
 - [SquareItemsCreateOperationPayload](docs/SquareItemsCreateOperationPayload.md)
 - [SquareItemsCreateOperationPayloadData](docs/SquareItemsCreateOperationPayloadData.md)
 - [SquareItemsCreateOperationPayloadDataAttributes](docs/SquareItemsCreateOperationPayloadDataAttributes.md)
 - [SquareItemsCreateOperationPayloadDataRelationships](docs/SquareItemsCreateOperationPayloadDataRelationships.md)
 - [SquareItemsCreateOperationPayloadDataRelationshipsSites](docs/SquareItemsCreateOperationPayloadDataRelationshipsSites.md)
 - [SquareItemsDeleteResource403ResponseBody](docs/SquareItemsDeleteResource403ResponseBody.md)
 - [SquareItemsDeleteResource409ResponseBody](docs/SquareItemsDeleteResource409ResponseBody.md)
 - [SquareItemsDeleteResource409ResponseBodyErrorsInner](docs/SquareItemsDeleteResource409ResponseBodyErrorsInner.md)
 - [SquareItemsMultiResourceDataDocument](docs/SquareItemsMultiResourceDataDocument.md)
 - [SquareItemsOwnersMultiRelationshipDataDocument](docs/SquareItemsOwnersMultiRelationshipDataDocument.md)
 - [SquareItemsReadByFilter403ResponseBody](docs/SquareItemsReadByFilter403ResponseBody.md)
 - [SquareItemsReadByFilter409ResponseBody](docs/SquareItemsReadByFilter409ResponseBody.md)
 - [SquareItemsReadById403ResponseBody](docs/SquareItemsReadById403ResponseBody.md)
 - [SquareItemsReadById409ResponseBody](docs/SquareItemsReadById409ResponseBody.md)
 - [SquareItemsRelationships](docs/SquareItemsRelationships.md)
 - [SquareItemsResourceObject](docs/SquareItemsResourceObject.md)
 - [SquareItemsSingleResourceDataDocument](docs/SquareItemsSingleResourceDataDocument.md)
 - [SquareItemsUpdateOperationPayload](docs/SquareItemsUpdateOperationPayload.md)
 - [SquareItemsUpdateOperationPayloadData](docs/SquareItemsUpdateOperationPayloadData.md)
 - [SquareItemsUpdateOperationPayloadDataAttributes](docs/SquareItemsUpdateOperationPayloadDataAttributes.md)
 - [SquareItemsUpdateOperationPayloadMeta](docs/SquareItemsUpdateOperationPayloadMeta.md)
 - [SquareItemsUpdateResource403ResponseBody](docs/SquareItemsUpdateResource403ResponseBody.md)
 - [SquareItemsUpdateResource409ResponseBody](docs/SquareItemsUpdateResource409ResponseBody.md)
 - [SquareItemsUpdateSingleResourceDataDocument](docs/SquareItemsUpdateSingleResourceDataDocument.md)
 - [SquareItemsVariationsMultiRelationshipDataDocument](docs/SquareItemsVariationsMultiRelationshipDataDocument.md)
 - [SquareItemsVariationsReadMultiDataRelationship403ResponseBody](docs/SquareItemsVariationsReadMultiDataRelationship403ResponseBody.md)
 - [SquareItemsVariationsReadMultiDataRelationship409ResponseBody](docs/SquareItemsVariationsReadMultiDataRelationship409ResponseBody.md)
 - [SquareItemsVariationsRelationshipUpdateOperationPayload](docs/SquareItemsVariationsRelationshipUpdateOperationPayload.md)
 - [SquareItemsVariationsRelationshipUpdateOperationPayloadMeta](docs/SquareItemsVariationsRelationshipUpdateOperationPayloadMeta.md)
 - [SquareItemsVariationsUpdateMultiDataRelationship403ResponseBody](docs/SquareItemsVariationsUpdateMultiDataRelationship403ResponseBody.md)
 - [SquareItemsVariationsUpdateMultiDataRelationship409ResponseBody](docs/SquareItemsVariationsUpdateMultiDataRelationship409ResponseBody.md)
 - [SquareItemsVariationsUpdateMultiRelationshipDataDocument](docs/SquareItemsVariationsUpdateMultiRelationshipDataDocument.md)
 - [SquareItemsVariationsUpdateMultiRelationshipDataDocumentMeta](docs/SquareItemsVariationsUpdateMultiRelationshipDataDocumentMeta.md)
 - [SquareItemsVariationsUpdateResourceIdentifier](docs/SquareItemsVariationsUpdateResourceIdentifier.md)
 - [SquareSitesAttributes](docs/SquareSitesAttributes.md)
 - [SquareSitesItemsAddMultiDataRelationship403ResponseBody](docs/SquareSitesItemsAddMultiDataRelationship403ResponseBody.md)
 - [SquareSitesItemsAddMultiDataRelationship409ResponseBody](docs/SquareSitesItemsAddMultiDataRelationship409ResponseBody.md)
 - [SquareSitesItemsAddMultiDataRelationship409ResponseBodyErrorsInner](docs/SquareSitesItemsAddMultiDataRelationship409ResponseBodyErrorsInner.md)
 - [SquareSitesItemsMultiRelationshipDataDocument](docs/SquareSitesItemsMultiRelationshipDataDocument.md)
 - [SquareSitesItemsReadMultiDataRelationship403ResponseBody](docs/SquareSitesItemsReadMultiDataRelationship403ResponseBody.md)
 - [SquareSitesItemsReadMultiDataRelationship409ResponseBody](docs/SquareSitesItemsReadMultiDataRelationship409ResponseBody.md)
 - [SquareSitesItemsReadMultiDataRelationship409ResponseBodyErrorsInner](docs/SquareSitesItemsReadMultiDataRelationship409ResponseBodyErrorsInner.md)
 - [SquareSitesItemsRelationshipAddOperationPayload](docs/SquareSitesItemsRelationshipAddOperationPayload.md)
 - [SquareSitesItemsRelationshipAddOperationPayloadData](docs/SquareSitesItemsRelationshipAddOperationPayloadData.md)
 - [SquareSitesItemsRelationshipRemoveOperationPayload](docs/SquareSitesItemsRelationshipRemoveOperationPayload.md)
 - [SquareSitesItemsRelationshipRemoveOperationPayloadData](docs/SquareSitesItemsRelationshipRemoveOperationPayloadData.md)
 - [SquareSitesItemsRemoveMultiDataRelationship403ResponseBody](docs/SquareSitesItemsRemoveMultiDataRelationship403ResponseBody.md)
 - [SquareSitesItemsRemoveMultiDataRelationship409ResponseBody](docs/SquareSitesItemsRemoveMultiDataRelationship409ResponseBody.md)
 - [SquareSitesRelationships](docs/SquareSitesRelationships.md)
 - [SquareSitesResourceObject](docs/SquareSitesResourceObject.md)
 - [StripeConnectionsAttributes](docs/StripeConnectionsAttributes.md)
 - [StripeConnectionsCreateOperationPayload](docs/StripeConnectionsCreateOperationPayload.md)
 - [StripeConnectionsCreateOperationPayloadData](docs/StripeConnectionsCreateOperationPayloadData.md)
 - [StripeConnectionsCreateOperationPayloadDataAttributes](docs/StripeConnectionsCreateOperationPayloadDataAttributes.md)
 - [StripeConnectionsCreateOperationPayloadMeta](docs/StripeConnectionsCreateOperationPayloadMeta.md)
 - [StripeConnectionsCreateSingleResourceDataDocument](docs/StripeConnectionsCreateSingleResourceDataDocument.md)
 - [StripeConnectionsMultiResourceDataDocument](docs/StripeConnectionsMultiResourceDataDocument.md)
 - [StripeConnectionsOwnersMultiRelationshipDataDocument](docs/StripeConnectionsOwnersMultiRelationshipDataDocument.md)
 - [StripeConnectionsRelationships](docs/StripeConnectionsRelationships.md)
 - [StripeConnectionsResourceObject](docs/StripeConnectionsResourceObject.md)
 - [StripeDashboardLinksAttributes](docs/StripeDashboardLinksAttributes.md)
 - [StripeDashboardLinksMultiResourceDataDocument](docs/StripeDashboardLinksMultiResourceDataDocument.md)
 - [StripeDashboardLinksOwnersMultiRelationshipDataDocument](docs/StripeDashboardLinksOwnersMultiRelationshipDataDocument.md)
 - [StripeDashboardLinksRelationships](docs/StripeDashboardLinksRelationships.md)
 - [StripeDashboardLinksResourceObject](docs/StripeDashboardLinksResourceObject.md)
 - [StudioHomeEventTilesAttributes](docs/StudioHomeEventTilesAttributes.md)
 - [StudioHomeEventTilesResourceObject](docs/StudioHomeEventTilesResourceObject.md)
 - [StudioHomeEventTilesSingleResourceDataDocument](docs/StudioHomeEventTilesSingleResourceDataDocument.md)
 - [StudioHomeInsightTilesAttributes](docs/StudioHomeInsightTilesAttributes.md)
 - [StudioHomeInsightTilesResourceObject](docs/StudioHomeInsightTilesResourceObject.md)
 - [StudioHomeInsightTilesSingleResourceDataDocument](docs/StudioHomeInsightTilesSingleResourceDataDocument.md)
 - [StudioHomeMerchTilesAttributes](docs/StudioHomeMerchTilesAttributes.md)
 - [StudioHomeMerchTilesItemsMultiRelationshipDataDocument](docs/StudioHomeMerchTilesItemsMultiRelationshipDataDocument.md)
 - [StudioHomeMerchTilesRelationships](docs/StudioHomeMerchTilesRelationships.md)
 - [StudioHomeMerchTilesResourceObject](docs/StudioHomeMerchTilesResourceObject.md)
 - [StudioHomeMerchTilesSingleResourceDataDocument](docs/StudioHomeMerchTilesSingleResourceDataDocument.md)
 - [StudioHomeMusicTilesAttributes](docs/StudioHomeMusicTilesAttributes.md)
 - [StudioHomeMusicTilesResourceObject](docs/StudioHomeMusicTilesResourceObject.md)
 - [StudioHomeMusicTilesSingleResourceDataDocument](docs/StudioHomeMusicTilesSingleResourceDataDocument.md)
 - [SubscriptionPriceChangeDecisionsAttributes](docs/SubscriptionPriceChangeDecisionsAttributes.md)
 - [SubscriptionPriceChangeDecisionsCreateOperationPayload](docs/SubscriptionPriceChangeDecisionsCreateOperationPayload.md)
 - [SubscriptionPriceChangeDecisionsCreateOperationPayloadData](docs/SubscriptionPriceChangeDecisionsCreateOperationPayloadData.md)
 - [SubscriptionPriceChangeDecisionsCreateOperationPayloadDataAttributes](docs/SubscriptionPriceChangeDecisionsCreateOperationPayloadDataAttributes.md)
 - [SubscriptionPriceChangeDecisionsCreateOperationPayloadDataRelationships](docs/SubscriptionPriceChangeDecisionsCreateOperationPayloadDataRelationships.md)
 - [SubscriptionPriceChangeDecisionsCreateOperationPayloadDataRelationshipsPriceChange](docs/SubscriptionPriceChangeDecisionsCreateOperationPayloadDataRelationshipsPriceChange.md)
 - [SubscriptionPriceChangeDecisionsCreateOperationPayloadDataRelationshipsPriceChangeData](docs/SubscriptionPriceChangeDecisionsCreateOperationPayloadDataRelationshipsPriceChangeData.md)
 - [SubscriptionPriceChangeDecisionsCreateSingleResourceDataDocument](docs/SubscriptionPriceChangeDecisionsCreateSingleResourceDataDocument.md)
 - [SubscriptionPriceChangeDecisionsMultiResourceDataDocument](docs/SubscriptionPriceChangeDecisionsMultiResourceDataDocument.md)
 - [SubscriptionPriceChangeDecisionsPriceChangeSingleRelationshipDataDocument](docs/SubscriptionPriceChangeDecisionsPriceChangeSingleRelationshipDataDocument.md)
 - [SubscriptionPriceChangeDecisionsRelationships](docs/SubscriptionPriceChangeDecisionsRelationships.md)
 - [SubscriptionPriceChangeDecisionsResourceObject](docs/SubscriptionPriceChangeDecisionsResourceObject.md)
 - [SubscriptionPriceChangeDecisionsUpdateOperationPayload](docs/SubscriptionPriceChangeDecisionsUpdateOperationPayload.md)
 - [SubscriptionPriceChangeDecisionsUpdateOperationPayloadData](docs/SubscriptionPriceChangeDecisionsUpdateOperationPayloadData.md)
 - [SubscriptionPriceChangeDecisionsUpdateOperationPayloadDataAttributes](docs/SubscriptionPriceChangeDecisionsUpdateOperationPayloadDataAttributes.md)
 - [SubscriptionPriceChangeDecisionsUpdateSingleResourceDataDocument](docs/SubscriptionPriceChangeDecisionsUpdateSingleResourceDataDocument.md)
 - [TemporaryUserTokensCreateOperationPayload](docs/TemporaryUserTokensCreateOperationPayload.md)
 - [TemporaryUserTokensCreateOperationPayloadData](docs/TemporaryUserTokensCreateOperationPayloadData.md)
 - [TemporaryUserTokensCreateSingleResourceDataDocument](docs/TemporaryUserTokensCreateSingleResourceDataDocument.md)
 - [TemporaryUserTokensOwnersMultiRelationshipDataDocument](docs/TemporaryUserTokensOwnersMultiRelationshipDataDocument.md)
 - [TemporaryUserTokensRelationships](docs/TemporaryUserTokensRelationships.md)
 - [TemporaryUserTokensResourceObject](docs/TemporaryUserTokensResourceObject.md)
 - [TemporaryUserTokensSingleResourceDataDocument](docs/TemporaryUserTokensSingleResourceDataDocument.md)
 - [TermsAttributes](docs/TermsAttributes.md)
 - [TermsMultiResourceDataDocument](docs/TermsMultiResourceDataDocument.md)
 - [TermsResourceObject](docs/TermsResourceObject.md)
 - [TermsResourceObjectMeta](docs/TermsResourceObjectMeta.md)
 - [TermsSingleResourceDataDocument](docs/TermsSingleResourceDataDocument.md)
 - [ThirdPartyLyricsProvider](docs/ThirdPartyLyricsProvider.md)
 - [TidalLyricsProvider](docs/TidalLyricsProvider.md)
 - [TrackFilesAttributes](docs/TrackFilesAttributes.md)
 - [TrackFilesReadById403ResponseBody](docs/TrackFilesReadById403ResponseBody.md)
 - [TrackFilesReadById403ResponseBodyErrorsInner](docs/TrackFilesReadById403ResponseBodyErrorsInner.md)
 - [TrackFilesReadById404ResponseBody](docs/TrackFilesReadById404ResponseBody.md)
 - [TrackFilesReadById404ResponseBodyErrorsInner](docs/TrackFilesReadById404ResponseBodyErrorsInner.md)
 - [TrackFilesResourceObject](docs/TrackFilesResourceObject.md)
 - [TrackFilesSingleResourceDataDocument](docs/TrackFilesSingleResourceDataDocument.md)
 - [TrackInfo](docs/TrackInfo.md)
 - [TrackManifestsAttributes](docs/TrackManifestsAttributes.md)
 - [TrackManifestsReadById403ResponseBody](docs/TrackManifestsReadById403ResponseBody.md)
 - [TrackManifestsReadById404ResponseBody](docs/TrackManifestsReadById404ResponseBody.md)
 - [TrackManifestsResourceObject](docs/TrackManifestsResourceObject.md)
 - [TrackManifestsSingleResourceDataDocument](docs/TrackManifestsSingleResourceDataDocument.md)
 - [TrackSourceFilesAttributes](docs/TrackSourceFilesAttributes.md)
 - [TrackSourceFilesCommentSummarySingleRelationshipDataDocument](docs/TrackSourceFilesCommentSummarySingleRelationshipDataDocument.md)
 - [TrackSourceFilesCreateOperationPayload](docs/TrackSourceFilesCreateOperationPayload.md)
 - [TrackSourceFilesCreateOperationPayloadData](docs/TrackSourceFilesCreateOperationPayloadData.md)
 - [TrackSourceFilesCreateOperationPayloadDataAttributes](docs/TrackSourceFilesCreateOperationPayloadDataAttributes.md)
 - [TrackSourceFilesCreateOperationPayloadDataRelationships](docs/TrackSourceFilesCreateOperationPayloadDataRelationships.md)
 - [TrackSourceFilesCreateOperationPayloadDataRelationshipsTrack](docs/TrackSourceFilesCreateOperationPayloadDataRelationshipsTrack.md)
 - [TrackSourceFilesCreateOperationPayloadDataRelationshipsTrackData](docs/TrackSourceFilesCreateOperationPayloadDataRelationshipsTrackData.md)
 - [TrackSourceFilesCreateSingleResourceDataDocument](docs/TrackSourceFilesCreateSingleResourceDataDocument.md)
 - [TrackSourceFilesOwnersMultiRelationshipDataDocument](docs/TrackSourceFilesOwnersMultiRelationshipDataDocument.md)
 - [TrackSourceFilesReactionSummarySingleRelationshipDataDocument](docs/TrackSourceFilesReactionSummarySingleRelationshipDataDocument.md)
 - [TrackSourceFilesRelationships](docs/TrackSourceFilesRelationships.md)
 - [TrackSourceFilesResourceObject](docs/TrackSourceFilesResourceObject.md)
 - [TrackSourceFilesSingleResourceDataDocument](docs/TrackSourceFilesSingleResourceDataDocument.md)
 - [TrackStatisticsAttributes](docs/TrackStatisticsAttributes.md)
 - [TrackStatisticsOwnersMultiRelationshipDataDocument](docs/TrackStatisticsOwnersMultiRelationshipDataDocument.md)
 - [TrackStatisticsRelationships](docs/TrackStatisticsRelationships.md)
 - [TrackStatisticsResourceObject](docs/TrackStatisticsResourceObject.md)
 - [TrackStatisticsSingleResourceDataDocument](docs/TrackStatisticsSingleResourceDataDocument.md)
 - [TracksAlbumsMultiRelationshipDataDocument](docs/TracksAlbumsMultiRelationshipDataDocument.md)
 - [TracksAlbumsRelationshipUpdateOperationPayload](docs/TracksAlbumsRelationshipUpdateOperationPayload.md)
 - [TracksAlbumsRelationshipUpdateOperationPayloadData](docs/TracksAlbumsRelationshipUpdateOperationPayloadData.md)
 - [TracksAlbumsResourceIdentifier](docs/TracksAlbumsResourceIdentifier.md)
 - [TracksAlbumsResourceIdentifierMeta](docs/TracksAlbumsResourceIdentifierMeta.md)
 - [TracksArtistsMultiRelationshipDataDocument](docs/TracksArtistsMultiRelationshipDataDocument.md)
 - [TracksArtistsRelationshipUpdateOperationPayload](docs/TracksArtistsRelationshipUpdateOperationPayload.md)
 - [TracksArtistsRelationshipUpdateOperationPayloadData](docs/TracksArtistsRelationshipUpdateOperationPayloadData.md)
 - [TracksAttributes](docs/TracksAttributes.md)
 - [TracksCreateOperationPayload](docs/TracksCreateOperationPayload.md)
 - [TracksCreateOperationPayloadData](docs/TracksCreateOperationPayloadData.md)
 - [TracksCreateOperationPayloadDataAttributes](docs/TracksCreateOperationPayloadDataAttributes.md)
 - [TracksCreateOperationPayloadDataRelationships](docs/TracksCreateOperationPayloadDataRelationships.md)
 - [TracksCreateOperationPayloadDataRelationshipsAlbums](docs/TracksCreateOperationPayloadDataRelationshipsAlbums.md)
 - [TracksCreateOperationPayloadDataRelationshipsAlbumsData](docs/TracksCreateOperationPayloadDataRelationshipsAlbumsData.md)
 - [TracksCreateOperationPayloadDataRelationshipsArtists](docs/TracksCreateOperationPayloadDataRelationshipsArtists.md)
 - [TracksCreateOperationPayloadDataRelationshipsArtistsData](docs/TracksCreateOperationPayloadDataRelationshipsArtistsData.md)
 - [TracksCreateOperationPayloadDataRelationshipsGenres](docs/TracksCreateOperationPayloadDataRelationshipsGenres.md)
 - [TracksCreateOperationPayloadDataRelationshipsGenresData](docs/TracksCreateOperationPayloadDataRelationshipsGenresData.md)
 - [TracksCreateSingleResourceDataDocument](docs/TracksCreateSingleResourceDataDocument.md)
 - [TracksCreditsMultiRelationshipDataDocument](docs/TracksCreditsMultiRelationshipDataDocument.md)
 - [TracksDownloadSingleRelationshipDataDocument](docs/TracksDownloadSingleRelationshipDataDocument.md)
 - [TracksGenresMultiRelationshipDataDocument](docs/TracksGenresMultiRelationshipDataDocument.md)
 - [TracksLyricsMultiRelationshipDataDocument](docs/TracksLyricsMultiRelationshipDataDocument.md)
 - [TracksMetadataStatusAttributes](docs/TracksMetadataStatusAttributes.md)
 - [TracksMetadataStatusResourceObject](docs/TracksMetadataStatusResourceObject.md)
 - [TracksMetadataStatusSingleRelationshipDataDocument](docs/TracksMetadataStatusSingleRelationshipDataDocument.md)
 - [TracksMetadataStatusSingleResourceDataDocument](docs/TracksMetadataStatusSingleResourceDataDocument.md)
 - [TracksMultiResourceDataDocument](docs/TracksMultiResourceDataDocument.md)
 - [TracksOwnersMultiRelationshipDataDocument](docs/TracksOwnersMultiRelationshipDataDocument.md)
 - [TracksPriceConfigSingleRelationshipDataDocument](docs/TracksPriceConfigSingleRelationshipDataDocument.md)
 - [TracksProvidersMultiRelationshipDataDocument](docs/TracksProvidersMultiRelationshipDataDocument.md)
 - [TracksRadioMultiRelationshipDataDocument](docs/TracksRadioMultiRelationshipDataDocument.md)
 - [TracksRelationships](docs/TracksRelationships.md)
 - [TracksReplacementResourceIdentifier](docs/TracksReplacementResourceIdentifier.md)
 - [TracksReplacementResourceIdentifierMeta](docs/TracksReplacementResourceIdentifierMeta.md)
 - [TracksReplacementSingleRelationshipDataDocument](docs/TracksReplacementSingleRelationshipDataDocument.md)
 - [TracksResourceObject](docs/TracksResourceObject.md)
 - [TracksSharesMultiRelationshipDataDocument](docs/TracksSharesMultiRelationshipDataDocument.md)
 - [TracksSimilarTracksMultiRelationshipDataDocument](docs/TracksSimilarTracksMultiRelationshipDataDocument.md)
 - [TracksSimilarTracksResourceIdentifier](docs/TracksSimilarTracksResourceIdentifier.md)
 - [TracksSimilarTracksResourceIdentifierMeta](docs/TracksSimilarTracksResourceIdentifierMeta.md)
 - [TracksSingleResourceDataDocument](docs/TracksSingleResourceDataDocument.md)
 - [TracksSourceFileSingleRelationshipDataDocument](docs/TracksSourceFileSingleRelationshipDataDocument.md)
 - [TracksSuggestedTracksMultiRelationshipDataDocument](docs/TracksSuggestedTracksMultiRelationshipDataDocument.md)
 - [TracksSuggestedTracksResourceIdentifier](docs/TracksSuggestedTracksResourceIdentifier.md)
 - [TracksSuggestedTracksResourceIdentifierMeta](docs/TracksSuggestedTracksResourceIdentifierMeta.md)
 - [TracksTrackStatisticsSingleRelationshipDataDocument](docs/TracksTrackStatisticsSingleRelationshipDataDocument.md)
 - [TracksUpdateOperationPayload](docs/TracksUpdateOperationPayload.md)
 - [TracksUpdateOperationPayloadData](docs/TracksUpdateOperationPayloadData.md)
 - [TracksUpdateOperationPayloadDataAttributes](docs/TracksUpdateOperationPayloadDataAttributes.md)
 - [TracksUpdateOperationPayloadDataRelationships](docs/TracksUpdateOperationPayloadDataRelationships.md)
 - [TracksUpdateOperationPayloadDataRelationshipsGenres](docs/TracksUpdateOperationPayloadDataRelationshipsGenres.md)
 - [TracksUpdateOperationPayloadDataRelationshipsGenresData](docs/TracksUpdateOperationPayloadDataRelationshipsGenresData.md)
 - [TracksUsageRulesSingleRelationshipDataDocument](docs/TracksUsageRulesSingleRelationshipDataDocument.md)
 - [UsageRulesAttributes](docs/UsageRulesAttributes.md)
 - [UsageRulesCreateOperationPayload](docs/UsageRulesCreateOperationPayload.md)
 - [UsageRulesCreateOperationPayloadData](docs/UsageRulesCreateOperationPayloadData.md)
 - [UsageRulesCreateOperationPayloadDataAttributes](docs/UsageRulesCreateOperationPayloadDataAttributes.md)
 - [UsageRulesCreateOperationPayloadDataRelationships](docs/UsageRulesCreateOperationPayloadDataRelationships.md)
 - [UsageRulesCreateOperationPayloadDataRelationshipsSubject](docs/UsageRulesCreateOperationPayloadDataRelationshipsSubject.md)
 - [UsageRulesCreateOperationPayloadSubject](docs/UsageRulesCreateOperationPayloadSubject.md)
 - [UsageRulesCreateResource403ResponseBody](docs/UsageRulesCreateResource403ResponseBody.md)
 - [UsageRulesCreateResource403ResponseBodyErrorsInner](docs/UsageRulesCreateResource403ResponseBodyErrorsInner.md)
 - [UsageRulesCreateSingleResourceDataDocument](docs/UsageRulesCreateSingleResourceDataDocument.md)
 - [UsageRulesResourceObject](docs/UsageRulesResourceObject.md)
 - [UsageRulesSingleResourceDataDocument](docs/UsageRulesSingleResourceDataDocument.md)
 - [UserCollection](docs/UserCollection.md)
 - [UserCollectionAlbumsAttributes](docs/UserCollectionAlbumsAttributes.md)
 - [UserCollectionAlbumsItemsAddMultiDataRelationshipWithResponse409ResponseBody](docs/UserCollectionAlbumsItemsAddMultiDataRelationshipWithResponse409ResponseBody.md)
 - [UserCollectionAlbumsItemsAddMultiDataRelationshipWithResponse409ResponseBodyErrorsInner](docs/UserCollectionAlbumsItemsAddMultiDataRelationshipWithResponse409ResponseBodyErrorsInner.md)
 - [UserCollectionAlbumsItemsAddMultiRelationshipDataDocument](docs/UserCollectionAlbumsItemsAddMultiRelationshipDataDocument.md)
 - [UserCollectionAlbumsItemsAddMultiRelationshipDataDocumentMeta](docs/UserCollectionAlbumsItemsAddMultiRelationshipDataDocumentMeta.md)
 - [UserCollectionAlbumsItemsAddResourceIdentifier](docs/UserCollectionAlbumsItemsAddResourceIdentifier.md)
 - [UserCollectionAlbumsItemsAddResourceIdentifierMeta](docs/UserCollectionAlbumsItemsAddResourceIdentifierMeta.md)
 - [UserCollectionAlbumsItemsMultiRelationshipDataDocument](docs/UserCollectionAlbumsItemsMultiRelationshipDataDocument.md)
 - [UserCollectionAlbumsItemsReadMultiDataRelationship403ResponseBody](docs/UserCollectionAlbumsItemsReadMultiDataRelationship403ResponseBody.md)
 - [UserCollectionAlbumsItemsReadMultiDataRelationship403ResponseBodyErrorsInner](docs/UserCollectionAlbumsItemsReadMultiDataRelationship403ResponseBodyErrorsInner.md)
 - [UserCollectionAlbumsItemsRelationshipAddOperationPayload](docs/UserCollectionAlbumsItemsRelationshipAddOperationPayload.md)
 - [UserCollectionAlbumsItemsRelationshipAddOperationPayloadData](docs/UserCollectionAlbumsItemsRelationshipAddOperationPayloadData.md)
 - [UserCollectionAlbumsItemsRelationshipAddOperationPayloadDataMeta](docs/UserCollectionAlbumsItemsRelationshipAddOperationPayloadDataMeta.md)
 - [UserCollectionAlbumsItemsRelationshipAddOperationResponseMetaSkippedItem](docs/UserCollectionAlbumsItemsRelationshipAddOperationResponseMetaSkippedItem.md)
 - [UserCollectionAlbumsItemsRelationshipRemoveOperationPayload](docs/UserCollectionAlbumsItemsRelationshipRemoveOperationPayload.md)
 - [UserCollectionAlbumsItemsRelationshipRemoveOperationPayloadData](docs/UserCollectionAlbumsItemsRelationshipRemoveOperationPayloadData.md)
 - [UserCollectionAlbumsItemsResourceIdentifier](docs/UserCollectionAlbumsItemsResourceIdentifier.md)
 - [UserCollectionAlbumsItemsResourceIdentifierMeta](docs/UserCollectionAlbumsItemsResourceIdentifierMeta.md)
 - [UserCollectionAlbumsOwnersMultiRelationshipDataDocument](docs/UserCollectionAlbumsOwnersMultiRelationshipDataDocument.md)
 - [UserCollectionAlbumsRelationships](docs/UserCollectionAlbumsRelationships.md)
 - [UserCollectionAlbumsResourceObject](docs/UserCollectionAlbumsResourceObject.md)
 - [UserCollectionAlbumsSingleResourceDataDocument](docs/UserCollectionAlbumsSingleResourceDataDocument.md)
 - [UserCollectionArtistsAttributes](docs/UserCollectionArtistsAttributes.md)
 - [UserCollectionArtistsItemsAddMultiDataRelationshipWithResponse409ResponseBody](docs/UserCollectionArtistsItemsAddMultiDataRelationshipWithResponse409ResponseBody.md)
 - [UserCollectionArtistsItemsAddMultiRelationshipDataDocument](docs/UserCollectionArtistsItemsAddMultiRelationshipDataDocument.md)
 - [UserCollectionArtistsItemsAddMultiRelationshipDataDocumentMeta](docs/UserCollectionArtistsItemsAddMultiRelationshipDataDocumentMeta.md)
 - [UserCollectionArtistsItemsAddResourceIdentifier](docs/UserCollectionArtistsItemsAddResourceIdentifier.md)
 - [UserCollectionArtistsItemsAddResourceIdentifierMeta](docs/UserCollectionArtistsItemsAddResourceIdentifierMeta.md)
 - [UserCollectionArtistsItemsMultiRelationshipDataDocument](docs/UserCollectionArtistsItemsMultiRelationshipDataDocument.md)
 - [UserCollectionArtistsItemsReadMultiDataRelationship403ResponseBody](docs/UserCollectionArtistsItemsReadMultiDataRelationship403ResponseBody.md)
 - [UserCollectionArtistsItemsRelationshipAddOperationPayload](docs/UserCollectionArtistsItemsRelationshipAddOperationPayload.md)
 - [UserCollectionArtistsItemsRelationshipAddOperationPayloadData](docs/UserCollectionArtistsItemsRelationshipAddOperationPayloadData.md)
 - [UserCollectionArtistsItemsRelationshipAddOperationPayloadDataMeta](docs/UserCollectionArtistsItemsRelationshipAddOperationPayloadDataMeta.md)
 - [UserCollectionArtistsItemsRelationshipAddOperationResponseMetaSkippedItem](docs/UserCollectionArtistsItemsRelationshipAddOperationResponseMetaSkippedItem.md)
 - [UserCollectionArtistsItemsRelationshipRemoveOperationPayload](docs/UserCollectionArtistsItemsRelationshipRemoveOperationPayload.md)
 - [UserCollectionArtistsItemsRelationshipRemoveOperationPayloadData](docs/UserCollectionArtistsItemsRelationshipRemoveOperationPayloadData.md)
 - [UserCollectionArtistsItemsResourceIdentifier](docs/UserCollectionArtistsItemsResourceIdentifier.md)
 - [UserCollectionArtistsItemsResourceIdentifierMeta](docs/UserCollectionArtistsItemsResourceIdentifierMeta.md)
 - [UserCollectionArtistsOwnersMultiRelationshipDataDocument](docs/UserCollectionArtistsOwnersMultiRelationshipDataDocument.md)
 - [UserCollectionArtistsRelationships](docs/UserCollectionArtistsRelationships.md)
 - [UserCollectionArtistsResourceObject](docs/UserCollectionArtistsResourceObject.md)
 - [UserCollectionArtistsSingleResourceDataDocument](docs/UserCollectionArtistsSingleResourceDataDocument.md)
 - [UserCollectionFoldersAttributes](docs/UserCollectionFoldersAttributes.md)
 - [UserCollectionFoldersCreateOperationPayload](docs/UserCollectionFoldersCreateOperationPayload.md)
 - [UserCollectionFoldersCreateOperationPayloadData](docs/UserCollectionFoldersCreateOperationPayloadData.md)
 - [UserCollectionFoldersCreateOperationPayloadDataAttributes](docs/UserCollectionFoldersCreateOperationPayloadDataAttributes.md)
 - [UserCollectionFoldersCreateOperationPayloadDataRelationships](docs/UserCollectionFoldersCreateOperationPayloadDataRelationships.md)
 - [UserCollectionFoldersCreateOperationPayloadDataRelationshipsUserCollection](docs/UserCollectionFoldersCreateOperationPayloadDataRelationshipsUserCollection.md)
 - [UserCollectionFoldersCreateSingleResourceDataDocument](docs/UserCollectionFoldersCreateSingleResourceDataDocument.md)
 - [UserCollectionFoldersDeleteResource400ResponseBody](docs/UserCollectionFoldersDeleteResource400ResponseBody.md)
 - [UserCollectionFoldersDeleteResource400ResponseBodyErrorsInner](docs/UserCollectionFoldersDeleteResource400ResponseBodyErrorsInner.md)
 - [UserCollectionFoldersItemsMultiRelationshipDataDocument](docs/UserCollectionFoldersItemsMultiRelationshipDataDocument.md)
 - [UserCollectionFoldersItemsRelationshipAddOperationPayload](docs/UserCollectionFoldersItemsRelationshipAddOperationPayload.md)
 - [UserCollectionFoldersItemsRelationshipAddOperationPayloadData](docs/UserCollectionFoldersItemsRelationshipAddOperationPayloadData.md)
 - [UserCollectionFoldersItemsRelationshipRemoveOperationPayload](docs/UserCollectionFoldersItemsRelationshipRemoveOperationPayload.md)
 - [UserCollectionFoldersItemsRelationshipRemoveOperationPayloadData](docs/UserCollectionFoldersItemsRelationshipRemoveOperationPayloadData.md)
 - [UserCollectionFoldersItemsResourceIdentifier](docs/UserCollectionFoldersItemsResourceIdentifier.md)
 - [UserCollectionFoldersItemsResourceIdentifierMeta](docs/UserCollectionFoldersItemsResourceIdentifierMeta.md)
 - [UserCollectionFoldersMultiResourceDataDocument](docs/UserCollectionFoldersMultiResourceDataDocument.md)
 - [UserCollectionFoldersOwnersMultiRelationshipDataDocument](docs/UserCollectionFoldersOwnersMultiRelationshipDataDocument.md)
 - [UserCollectionFoldersRelationships](docs/UserCollectionFoldersRelationships.md)
 - [UserCollectionFoldersResourceObject](docs/UserCollectionFoldersResourceObject.md)
 - [UserCollectionFoldersSingleResourceDataDocument](docs/UserCollectionFoldersSingleResourceDataDocument.md)
 - [UserCollectionFoldersUpdateOperationPayload](docs/UserCollectionFoldersUpdateOperationPayload.md)
 - [UserCollectionFoldersUpdateOperationPayloadData](docs/UserCollectionFoldersUpdateOperationPayloadData.md)
 - [UserCollectionFoldersUpdateOperationPayloadDataAttributes](docs/UserCollectionFoldersUpdateOperationPayloadDataAttributes.md)
 - [UserCollectionFoldersUserCollectionSingleRelationshipDataDocument](docs/UserCollectionFoldersUserCollectionSingleRelationshipDataDocument.md)
 - [UserCollectionPlaylistsAttributes](docs/UserCollectionPlaylistsAttributes.md)
 - [UserCollectionPlaylistsItemsAddMultiDataRelationshipWithResponse409ResponseBody](docs/UserCollectionPlaylistsItemsAddMultiDataRelationshipWithResponse409ResponseBody.md)
 - [UserCollectionPlaylistsItemsAddMultiRelationshipDataDocument](docs/UserCollectionPlaylistsItemsAddMultiRelationshipDataDocument.md)
 - [UserCollectionPlaylistsItemsAddMultiRelationshipDataDocumentMeta](docs/UserCollectionPlaylistsItemsAddMultiRelationshipDataDocumentMeta.md)
 - [UserCollectionPlaylistsItemsAddResourceIdentifier](docs/UserCollectionPlaylistsItemsAddResourceIdentifier.md)
 - [UserCollectionPlaylistsItemsAddResourceIdentifierMeta](docs/UserCollectionPlaylistsItemsAddResourceIdentifierMeta.md)
 - [UserCollectionPlaylistsItemsMultiRelationshipDataDocument](docs/UserCollectionPlaylistsItemsMultiRelationshipDataDocument.md)
 - [UserCollectionPlaylistsItemsReadMultiDataRelationship403ResponseBody](docs/UserCollectionPlaylistsItemsReadMultiDataRelationship403ResponseBody.md)
 - [UserCollectionPlaylistsItemsRelationshipAddOperationPayload](docs/UserCollectionPlaylistsItemsRelationshipAddOperationPayload.md)
 - [UserCollectionPlaylistsItemsRelationshipAddOperationPayloadData](docs/UserCollectionPlaylistsItemsRelationshipAddOperationPayloadData.md)
 - [UserCollectionPlaylistsItemsRelationshipAddOperationPayloadDataMeta](docs/UserCollectionPlaylistsItemsRelationshipAddOperationPayloadDataMeta.md)
 - [UserCollectionPlaylistsItemsRelationshipAddOperationResponseMetaSkippedItem](docs/UserCollectionPlaylistsItemsRelationshipAddOperationResponseMetaSkippedItem.md)
 - [UserCollectionPlaylistsItemsRelationshipRemoveOperationPayload](docs/UserCollectionPlaylistsItemsRelationshipRemoveOperationPayload.md)
 - [UserCollectionPlaylistsItemsRelationshipRemoveOperationPayloadData](docs/UserCollectionPlaylistsItemsRelationshipRemoveOperationPayloadData.md)
 - [UserCollectionPlaylistsItemsResourceIdentifier](docs/UserCollectionPlaylistsItemsResourceIdentifier.md)
 - [UserCollectionPlaylistsItemsResourceIdentifierMeta](docs/UserCollectionPlaylistsItemsResourceIdentifierMeta.md)
 - [UserCollectionPlaylistsOwnersMultiRelationshipDataDocument](docs/UserCollectionPlaylistsOwnersMultiRelationshipDataDocument.md)
 - [UserCollectionPlaylistsRelationships](docs/UserCollectionPlaylistsRelationships.md)
 - [UserCollectionPlaylistsResourceObject](docs/UserCollectionPlaylistsResourceObject.md)
 - [UserCollectionPlaylistsSingleResourceDataDocument](docs/UserCollectionPlaylistsSingleResourceDataDocument.md)
 - [UserCollectionSaveForLatersAttributes](docs/UserCollectionSaveForLatersAttributes.md)
 - [UserCollectionSaveForLatersItemsAddMultiDataRelationshipWithResponse409ResponseBody](docs/UserCollectionSaveForLatersItemsAddMultiDataRelationshipWithResponse409ResponseBody.md)
 - [UserCollectionSaveForLatersItemsAddMultiRelationshipDataDocument](docs/UserCollectionSaveForLatersItemsAddMultiRelationshipDataDocument.md)
 - [UserCollectionSaveForLatersItemsAddMultiRelationshipDataDocumentMeta](docs/UserCollectionSaveForLatersItemsAddMultiRelationshipDataDocumentMeta.md)
 - [UserCollectionSaveForLatersItemsAddResourceIdentifier](docs/UserCollectionSaveForLatersItemsAddResourceIdentifier.md)
 - [UserCollectionSaveForLatersItemsAddResourceIdentifierMeta](docs/UserCollectionSaveForLatersItemsAddResourceIdentifierMeta.md)
 - [UserCollectionSaveForLatersItemsMultiRelationshipDataDocument](docs/UserCollectionSaveForLatersItemsMultiRelationshipDataDocument.md)
 - [UserCollectionSaveForLatersItemsRelationshipAddOperationPayload](docs/UserCollectionSaveForLatersItemsRelationshipAddOperationPayload.md)
 - [UserCollectionSaveForLatersItemsRelationshipAddOperationPayloadData](docs/UserCollectionSaveForLatersItemsRelationshipAddOperationPayloadData.md)
 - [UserCollectionSaveForLatersItemsRelationshipAddOperationResponseMetaSkippedItem](docs/UserCollectionSaveForLatersItemsRelationshipAddOperationResponseMetaSkippedItem.md)
 - [UserCollectionSaveForLatersItemsRelationshipRemoveOperationPayload](docs/UserCollectionSaveForLatersItemsRelationshipRemoveOperationPayload.md)
 - [UserCollectionSaveForLatersItemsRelationshipRemoveOperationPayloadData](docs/UserCollectionSaveForLatersItemsRelationshipRemoveOperationPayloadData.md)
 - [UserCollectionSaveForLatersItemsResourceIdentifier](docs/UserCollectionSaveForLatersItemsResourceIdentifier.md)
 - [UserCollectionSaveForLatersItemsResourceIdentifierMeta](docs/UserCollectionSaveForLatersItemsResourceIdentifierMeta.md)
 - [UserCollectionSaveForLatersOwnersMultiRelationshipDataDocument](docs/UserCollectionSaveForLatersOwnersMultiRelationshipDataDocument.md)
 - [UserCollectionSaveForLatersRelationships](docs/UserCollectionSaveForLatersRelationships.md)
 - [UserCollectionSaveForLatersResourceObject](docs/UserCollectionSaveForLatersResourceObject.md)
 - [UserCollectionSaveForLatersSingleResourceDataDocument](docs/UserCollectionSaveForLatersSingleResourceDataDocument.md)
 - [UserCollectionTracksAttributes](docs/UserCollectionTracksAttributes.md)
 - [UserCollectionTracksItemsAddMultiDataRelationshipWithResponse409ResponseBody](docs/UserCollectionTracksItemsAddMultiDataRelationshipWithResponse409ResponseBody.md)
 - [UserCollectionTracksItemsAddMultiRelationshipDataDocument](docs/UserCollectionTracksItemsAddMultiRelationshipDataDocument.md)
 - [UserCollectionTracksItemsAddMultiRelationshipDataDocumentMeta](docs/UserCollectionTracksItemsAddMultiRelationshipDataDocumentMeta.md)
 - [UserCollectionTracksItemsAddResourceIdentifier](docs/UserCollectionTracksItemsAddResourceIdentifier.md)
 - [UserCollectionTracksItemsAddResourceIdentifierMeta](docs/UserCollectionTracksItemsAddResourceIdentifierMeta.md)
 - [UserCollectionTracksItemsMultiRelationshipDataDocument](docs/UserCollectionTracksItemsMultiRelationshipDataDocument.md)
 - [UserCollectionTracksItemsReadMultiDataRelationship403ResponseBody](docs/UserCollectionTracksItemsReadMultiDataRelationship403ResponseBody.md)
 - [UserCollectionTracksItemsRelationshipAddOperationPayload](docs/UserCollectionTracksItemsRelationshipAddOperationPayload.md)
 - [UserCollectionTracksItemsRelationshipAddOperationPayloadData](docs/UserCollectionTracksItemsRelationshipAddOperationPayloadData.md)
 - [UserCollectionTracksItemsRelationshipAddOperationPayloadDataMeta](docs/UserCollectionTracksItemsRelationshipAddOperationPayloadDataMeta.md)
 - [UserCollectionTracksItemsRelationshipAddOperationResponseMetaSkippedItem](docs/UserCollectionTracksItemsRelationshipAddOperationResponseMetaSkippedItem.md)
 - [UserCollectionTracksItemsRelationshipRemoveOperationPayload](docs/UserCollectionTracksItemsRelationshipRemoveOperationPayload.md)
 - [UserCollectionTracksItemsRelationshipRemoveOperationPayloadData](docs/UserCollectionTracksItemsRelationshipRemoveOperationPayloadData.md)
 - [UserCollectionTracksItemsResourceIdentifier](docs/UserCollectionTracksItemsResourceIdentifier.md)
 - [UserCollectionTracksItemsResourceIdentifierMeta](docs/UserCollectionTracksItemsResourceIdentifierMeta.md)
 - [UserCollectionTracksOwnersMultiRelationshipDataDocument](docs/UserCollectionTracksOwnersMultiRelationshipDataDocument.md)
 - [UserCollectionTracksRelationships](docs/UserCollectionTracksRelationships.md)
 - [UserCollectionTracksResourceObject](docs/UserCollectionTracksResourceObject.md)
 - [UserCollectionTracksSingleResourceDataDocument](docs/UserCollectionTracksSingleResourceDataDocument.md)
 - [UserCollectionVideosAttributes](docs/UserCollectionVideosAttributes.md)
 - [UserCollectionVideosItemsAddMultiDataRelationshipWithResponse409ResponseBody](docs/UserCollectionVideosItemsAddMultiDataRelationshipWithResponse409ResponseBody.md)
 - [UserCollectionVideosItemsAddMultiRelationshipDataDocument](docs/UserCollectionVideosItemsAddMultiRelationshipDataDocument.md)
 - [UserCollectionVideosItemsAddMultiRelationshipDataDocumentMeta](docs/UserCollectionVideosItemsAddMultiRelationshipDataDocumentMeta.md)
 - [UserCollectionVideosItemsAddResourceIdentifier](docs/UserCollectionVideosItemsAddResourceIdentifier.md)
 - [UserCollectionVideosItemsAddResourceIdentifierMeta](docs/UserCollectionVideosItemsAddResourceIdentifierMeta.md)
 - [UserCollectionVideosItemsMultiRelationshipDataDocument](docs/UserCollectionVideosItemsMultiRelationshipDataDocument.md)
 - [UserCollectionVideosItemsReadMultiDataRelationship403ResponseBody](docs/UserCollectionVideosItemsReadMultiDataRelationship403ResponseBody.md)
 - [UserCollectionVideosItemsRelationshipAddOperationPayload](docs/UserCollectionVideosItemsRelationshipAddOperationPayload.md)
 - [UserCollectionVideosItemsRelationshipAddOperationPayloadData](docs/UserCollectionVideosItemsRelationshipAddOperationPayloadData.md)
 - [UserCollectionVideosItemsRelationshipAddOperationPayloadDataMeta](docs/UserCollectionVideosItemsRelationshipAddOperationPayloadDataMeta.md)
 - [UserCollectionVideosItemsRelationshipAddOperationResponseMetaSkippedItem](docs/UserCollectionVideosItemsRelationshipAddOperationResponseMetaSkippedItem.md)
 - [UserCollectionVideosItemsRelationshipRemoveOperationPayload](docs/UserCollectionVideosItemsRelationshipRemoveOperationPayload.md)
 - [UserCollectionVideosItemsRelationshipRemoveOperationPayloadData](docs/UserCollectionVideosItemsRelationshipRemoveOperationPayloadData.md)
 - [UserCollectionVideosItemsResourceIdentifier](docs/UserCollectionVideosItemsResourceIdentifier.md)
 - [UserCollectionVideosItemsResourceIdentifierMeta](docs/UserCollectionVideosItemsResourceIdentifierMeta.md)
 - [UserCollectionVideosOwnersMultiRelationshipDataDocument](docs/UserCollectionVideosOwnersMultiRelationshipDataDocument.md)
 - [UserCollectionVideosRelationships](docs/UserCollectionVideosRelationships.md)
 - [UserCollectionVideosResourceObject](docs/UserCollectionVideosResourceObject.md)
 - [UserCollectionVideosSingleResourceDataDocument](docs/UserCollectionVideosSingleResourceDataDocument.md)
 - [UserDailyMixesItemsMultiRelationshipDataDocument](docs/UserDailyMixesItemsMultiRelationshipDataDocument.md)
 - [UserDailyMixesRelationships](docs/UserDailyMixesRelationships.md)
 - [UserDailyMixesResourceObject](docs/UserDailyMixesResourceObject.md)
 - [UserDailyMixesSingleResourceDataDocument](docs/UserDailyMixesSingleResourceDataDocument.md)
 - [UserDataExportRequestsAttributes](docs/UserDataExportRequestsAttributes.md)
 - [UserDataExportRequestsCreateOperationPayload](docs/UserDataExportRequestsCreateOperationPayload.md)
 - [UserDataExportRequestsCreateOperationPayloadData](docs/UserDataExportRequestsCreateOperationPayloadData.md)
 - [UserDataExportRequestsCreateOperationPayloadDataAttributes](docs/UserDataExportRequestsCreateOperationPayloadDataAttributes.md)
 - [UserDataExportRequestsCreateSingleResourceDataDocument](docs/UserDataExportRequestsCreateSingleResourceDataDocument.md)
 - [UserDataExportRequestsResourceObject](docs/UserDataExportRequestsResourceObject.md)
 - [UserDataExportsAttributes](docs/UserDataExportsAttributes.md)
 - [UserDataExportsCreateOperationPayload](docs/UserDataExportsCreateOperationPayload.md)
 - [UserDataExportsCreateOperationPayloadData](docs/UserDataExportsCreateOperationPayloadData.md)
 - [UserDataExportsCreateOperationPayloadDataAttributes](docs/UserDataExportsCreateOperationPayloadDataAttributes.md)
 - [UserDataExportsCreateOperationPayloadMeta](docs/UserDataExportsCreateOperationPayloadMeta.md)
 - [UserDataExportsCreateResource400ResponseBody](docs/UserDataExportsCreateResource400ResponseBody.md)
 - [UserDataExportsCreateResource400ResponseBodyErrorsInner](docs/UserDataExportsCreateResource400ResponseBodyErrorsInner.md)
 - [UserDataExportsCreateResource409ResponseBody](docs/UserDataExportsCreateResource409ResponseBody.md)
 - [UserDataExportsCreateResource409ResponseBodyErrorsInner](docs/UserDataExportsCreateResource409ResponseBodyErrorsInner.md)
 - [UserDataExportsCreateSingleResourceDataDocument](docs/UserDataExportsCreateSingleResourceDataDocument.md)
 - [UserDataExportsMultiResourceDataDocument](docs/UserDataExportsMultiResourceDataDocument.md)
 - [UserDataExportsOwnersMultiRelationshipDataDocument](docs/UserDataExportsOwnersMultiRelationshipDataDocument.md)
 - [UserDataExportsRelationships](docs/UserDataExportsRelationships.md)
 - [UserDataExportsResourceObject](docs/UserDataExportsResourceObject.md)
 - [UserDataExportsSingleResourceDataDocument](docs/UserDataExportsSingleResourceDataDocument.md)
 - [UserDiscoveryMixesItemsMultiRelationshipDataDocument](docs/UserDiscoveryMixesItemsMultiRelationshipDataDocument.md)
 - [UserDiscoveryMixesRelationships](docs/UserDiscoveryMixesRelationships.md)
 - [UserDiscoveryMixesResourceObject](docs/UserDiscoveryMixesResourceObject.md)
 - [UserDiscoveryMixesSingleResourceDataDocument](docs/UserDiscoveryMixesSingleResourceDataDocument.md)
 - [UserFeedItemActivityDetails](docs/UserFeedItemActivityDetails.md)
 - [UserFeedItemAlbumFavouritedDetails](docs/UserFeedItemAlbumFavouritedDetails.md)
 - [UserFeedItemAlbumReleasedDetails](docs/UserFeedItemAlbumReleasedDetails.md)
 - [UserFeedItemAlbumSharedDetails](docs/UserFeedItemAlbumSharedDetails.md)
 - [UserFeedItemArtistFollowedDetails](docs/UserFeedItemArtistFollowedDetails.md)
 - [UserFeedItemCommentRepliedDetails](docs/UserFeedItemCommentRepliedDetails.md)
 - [UserFeedItemCopyrightFlaggedDetails](docs/UserFeedItemCopyrightFlaggedDetails.md)
 - [UserFeedItemHistoryMixReadyDetails](docs/UserFeedItemHistoryMixReadyDetails.md)
 - [UserFeedItemPlaylistUpdatedDetails](docs/UserFeedItemPlaylistUpdatedDetails.md)
 - [UserFeedItemTrackFavouritedDetails](docs/UserFeedItemTrackFavouritedDetails.md)
 - [UserFeedItemTrackPlayMilestoneDetails](docs/UserFeedItemTrackPlayMilestoneDetails.md)
 - [UserFeedItemTrackPlaylistedDetails](docs/UserFeedItemTrackPlaylistedDetails.md)
 - [UserFeedItemTrackSourceFileCommentedDetails](docs/UserFeedItemTrackSourceFileCommentedDetails.md)
 - [UserFeedItemsActorsMultiRelationshipDataDocument](docs/UserFeedItemsActorsMultiRelationshipDataDocument.md)
 - [UserFeedItemsAttributes](docs/UserFeedItemsAttributes.md)
 - [UserFeedItemsMultiResourceDataDocument](docs/UserFeedItemsMultiResourceDataDocument.md)
 - [UserFeedItemsMultiResourceDataDocumentMeta](docs/UserFeedItemsMultiResourceDataDocumentMeta.md)
 - [UserFeedItemsRelationships](docs/UserFeedItemsRelationships.md)
 - [UserFeedItemsResourceObject](docs/UserFeedItemsResourceObject.md)
 - [UserFeedItemsSubjectResourceIdentifier](docs/UserFeedItemsSubjectResourceIdentifier.md)
 - [UserFeedItemsSubjectResourceIdentifierMeta](docs/UserFeedItemsSubjectResourceIdentifierMeta.md)
 - [UserFeedItemsSubjectSingleRelationshipDataDocument](docs/UserFeedItemsSubjectSingleRelationshipDataDocument.md)
 - [UserFeedsAttributes](docs/UserFeedsAttributes.md)
 - [UserFeedsAttributesFeed](docs/UserFeedsAttributesFeed.md)
 - [UserFeedsAttributesInbox](docs/UserFeedsAttributesInbox.md)
 - [UserFeedsResourceObject](docs/UserFeedsResourceObject.md)
 - [UserFeedsSingleResourceDataDocument](docs/UserFeedsSingleResourceDataDocument.md)
 - [UserFeedsUpdateOperationPayload](docs/UserFeedsUpdateOperationPayload.md)
 - [UserFeedsUpdateOperationPayloadData](docs/UserFeedsUpdateOperationPayloadData.md)
 - [UserFeedsUpdateOperationPayloadDataAttributes](docs/UserFeedsUpdateOperationPayloadDataAttributes.md)
 - [UserFeedsUpdateOperationPayloadDataAttributesFeed](docs/UserFeedsUpdateOperationPayloadDataAttributesFeed.md)
 - [UserFeedsUpdateOperationPayloadDataAttributesInbox](docs/UserFeedsUpdateOperationPayloadDataAttributesInbox.md)
 - [UserFeedsUpdateSingleResourceDataDocument](docs/UserFeedsUpdateSingleResourceDataDocument.md)
 - [UserNewReleaseMixesItemsMultiRelationshipDataDocument](docs/UserNewReleaseMixesItemsMultiRelationshipDataDocument.md)
 - [UserNewReleaseMixesRelationships](docs/UserNewReleaseMixesRelationships.md)
 - [UserNewReleaseMixesResourceObject](docs/UserNewReleaseMixesResourceObject.md)
 - [UserNewReleaseMixesSingleResourceDataDocument](docs/UserNewReleaseMixesSingleResourceDataDocument.md)
 - [UserOfflineMixesItemsMultiRelationshipDataDocument](docs/UserOfflineMixesItemsMultiRelationshipDataDocument.md)
 - [UserOfflineMixesRelationships](docs/UserOfflineMixesRelationships.md)
 - [UserOfflineMixesResourceObject](docs/UserOfflineMixesResourceObject.md)
 - [UserOfflineMixesSingleResourceDataDocument](docs/UserOfflineMixesSingleResourceDataDocument.md)
 - [UserPlaybackStatesActivePlayerRelationshipUpdateOperationPayload](docs/UserPlaybackStatesActivePlayerRelationshipUpdateOperationPayload.md)
 - [UserPlaybackStatesActivePlayerRelationshipUpdateOperationPayloadData](docs/UserPlaybackStatesActivePlayerRelationshipUpdateOperationPayloadData.md)
 - [UserPlaybackStatesActivePlayerSingleRelationshipDataDocument](docs/UserPlaybackStatesActivePlayerSingleRelationshipDataDocument.md)
 - [UserPlaybackStatesActivePlayerUpdateResourceIdentifier](docs/UserPlaybackStatesActivePlayerUpdateResourceIdentifier.md)
 - [UserPlaybackStatesActivePlayerUpdateSingleRelationshipDataDocument](docs/UserPlaybackStatesActivePlayerUpdateSingleRelationshipDataDocument.md)
 - [UserPlaybackStatesAttributes](docs/UserPlaybackStatesAttributes.md)
 - [UserPlaybackStatesAvailablePlayersAddMultiRelationshipDataDocument](docs/UserPlaybackStatesAvailablePlayersAddMultiRelationshipDataDocument.md)
 - [UserPlaybackStatesAvailablePlayersAddResourceIdentifier](docs/UserPlaybackStatesAvailablePlayersAddResourceIdentifier.md)
 - [UserPlaybackStatesAvailablePlayersMultiRelationshipDataDocument](docs/UserPlaybackStatesAvailablePlayersMultiRelationshipDataDocument.md)
 - [UserPlaybackStatesAvailablePlayersRelationshipAddOperationPayload](docs/UserPlaybackStatesAvailablePlayersRelationshipAddOperationPayload.md)
 - [UserPlaybackStatesAvailablePlayersRelationshipOperationPayloadData](docs/UserPlaybackStatesAvailablePlayersRelationshipOperationPayloadData.md)
 - [UserPlaybackStatesAvailablePlayersRelationshipRemoveOperationPayload](docs/UserPlaybackStatesAvailablePlayersRelationshipRemoveOperationPayload.md)
 - [UserPlaybackStatesChangeEventStreamSingleRelationshipDataDocument](docs/UserPlaybackStatesChangeEventStreamSingleRelationshipDataDocument.md)
 - [UserPlaybackStatesPlayQueueRelationshipUpdateOperationPayload](docs/UserPlaybackStatesPlayQueueRelationshipUpdateOperationPayload.md)
 - [UserPlaybackStatesPlayQueueRelationshipUpdateOperationPayloadData](docs/UserPlaybackStatesPlayQueueRelationshipUpdateOperationPayloadData.md)
 - [UserPlaybackStatesPlayQueueSingleRelationshipDataDocument](docs/UserPlaybackStatesPlayQueueSingleRelationshipDataDocument.md)
 - [UserPlaybackStatesPlayQueueUpdateResourceIdentifier](docs/UserPlaybackStatesPlayQueueUpdateResourceIdentifier.md)
 - [UserPlaybackStatesPlayQueueUpdateSingleRelationshipDataDocument](docs/UserPlaybackStatesPlayQueueUpdateSingleRelationshipDataDocument.md)
 - [UserPlaybackStatesRelationships](docs/UserPlaybackStatesRelationships.md)
 - [UserPlaybackStatesResourceObject](docs/UserPlaybackStatesResourceObject.md)
 - [UserPlaybackStatesSingleResourceDataDocument](docs/UserPlaybackStatesSingleResourceDataDocument.md)
 - [UserPlaybackStatesUpdateOperationPayload](docs/UserPlaybackStatesUpdateOperationPayload.md)
 - [UserPlaybackStatesUpdateOperationPayloadData](docs/UserPlaybackStatesUpdateOperationPayloadData.md)
 - [UserPlaybackStatesUpdateOperationPayloadDataAttributes](docs/UserPlaybackStatesUpdateOperationPayloadDataAttributes.md)
 - [UserPlaybackStatesUpdateSingleResourceDataDocument](docs/UserPlaybackStatesUpdateSingleResourceDataDocument.md)
 - [UserRecommendationBlocksArtistsAddMultiDataRelationshipWithResponse409ResponseBody](docs/UserRecommendationBlocksArtistsAddMultiDataRelationshipWithResponse409ResponseBody.md)
 - [UserRecommendationBlocksArtistsAddMultiDataRelationshipWithResponse409ResponseBodyErrorsInner](docs/UserRecommendationBlocksArtistsAddMultiDataRelationshipWithResponse409ResponseBodyErrorsInner.md)
 - [UserRecommendationBlocksArtistsAddMultiRelationshipDataDocument](docs/UserRecommendationBlocksArtistsAddMultiRelationshipDataDocument.md)
 - [UserRecommendationBlocksArtistsAddResourceIdentifier](docs/UserRecommendationBlocksArtistsAddResourceIdentifier.md)
 - [UserRecommendationBlocksArtistsMultiRelationshipDataDocument](docs/UserRecommendationBlocksArtistsMultiRelationshipDataDocument.md)
 - [UserRecommendationBlocksArtistsRelationshipAddOperationPayload](docs/UserRecommendationBlocksArtistsRelationshipAddOperationPayload.md)
 - [UserRecommendationBlocksArtistsRelationshipAddOperationPayloadData](docs/UserRecommendationBlocksArtistsRelationshipAddOperationPayloadData.md)
 - [UserRecommendationBlocksArtistsRelationshipRemoveOperationPayload](docs/UserRecommendationBlocksArtistsRelationshipRemoveOperationPayload.md)
 - [UserRecommendationBlocksArtistsRelationshipRemoveOperationPayloadData](docs/UserRecommendationBlocksArtistsRelationshipRemoveOperationPayloadData.md)
 - [UserRecommendationBlocksArtistsResourceIdentifier](docs/UserRecommendationBlocksArtistsResourceIdentifier.md)
 - [UserRecommendationBlocksArtistsResourceIdentifierMeta](docs/UserRecommendationBlocksArtistsResourceIdentifierMeta.md)
 - [UserRecommendationBlocksOwnersMultiRelationshipDataDocument](docs/UserRecommendationBlocksOwnersMultiRelationshipDataDocument.md)
 - [UserRecommendationBlocksRelationships](docs/UserRecommendationBlocksRelationships.md)
 - [UserRecommendationBlocksResourceObject](docs/UserRecommendationBlocksResourceObject.md)
 - [UserRecommendationBlocksSingleResourceDataDocument](docs/UserRecommendationBlocksSingleResourceDataDocument.md)
 - [UserRecommendationBlocksTracksAddMultiDataRelationshipWithResponse409ResponseBody](docs/UserRecommendationBlocksTracksAddMultiDataRelationshipWithResponse409ResponseBody.md)
 - [UserRecommendationBlocksTracksAddMultiRelationshipDataDocument](docs/UserRecommendationBlocksTracksAddMultiRelationshipDataDocument.md)
 - [UserRecommendationBlocksTracksAddResourceIdentifier](docs/UserRecommendationBlocksTracksAddResourceIdentifier.md)
 - [UserRecommendationBlocksTracksMultiRelationshipDataDocument](docs/UserRecommendationBlocksTracksMultiRelationshipDataDocument.md)
 - [UserRecommendationBlocksTracksRelationshipAddOperationPayload](docs/UserRecommendationBlocksTracksRelationshipAddOperationPayload.md)
 - [UserRecommendationBlocksTracksRelationshipAddOperationPayloadData](docs/UserRecommendationBlocksTracksRelationshipAddOperationPayloadData.md)
 - [UserRecommendationBlocksTracksRelationshipRemoveOperationPayload](docs/UserRecommendationBlocksTracksRelationshipRemoveOperationPayload.md)
 - [UserRecommendationBlocksTracksRelationshipRemoveOperationPayloadData](docs/UserRecommendationBlocksTracksRelationshipRemoveOperationPayloadData.md)
 - [UserRecommendationBlocksTracksResourceIdentifier](docs/UserRecommendationBlocksTracksResourceIdentifier.md)
 - [UserRecommendationBlocksTracksResourceIdentifierMeta](docs/UserRecommendationBlocksTracksResourceIdentifierMeta.md)
 - [UserRecommendationBlocksVideosAddMultiDataRelationshipWithResponse409ResponseBody](docs/UserRecommendationBlocksVideosAddMultiDataRelationshipWithResponse409ResponseBody.md)
 - [UserRecommendationBlocksVideosAddMultiRelationshipDataDocument](docs/UserRecommendationBlocksVideosAddMultiRelationshipDataDocument.md)
 - [UserRecommendationBlocksVideosAddResourceIdentifier](docs/UserRecommendationBlocksVideosAddResourceIdentifier.md)
 - [UserRecommendationBlocksVideosMultiRelationshipDataDocument](docs/UserRecommendationBlocksVideosMultiRelationshipDataDocument.md)
 - [UserRecommendationBlocksVideosRelationshipAddOperationPayload](docs/UserRecommendationBlocksVideosRelationshipAddOperationPayload.md)
 - [UserRecommendationBlocksVideosRelationshipAddOperationPayloadData](docs/UserRecommendationBlocksVideosRelationshipAddOperationPayloadData.md)
 - [UserRecommendationBlocksVideosRelationshipRemoveOperationPayload](docs/UserRecommendationBlocksVideosRelationshipRemoveOperationPayload.md)
 - [UserRecommendationBlocksVideosRelationshipRemoveOperationPayloadData](docs/UserRecommendationBlocksVideosRelationshipRemoveOperationPayloadData.md)
 - [UserRecommendationBlocksVideosResourceIdentifier](docs/UserRecommendationBlocksVideosResourceIdentifier.md)
 - [UserRecommendationBlocksVideosResourceIdentifierMeta](docs/UserRecommendationBlocksVideosResourceIdentifierMeta.md)
 - [UserReportsAttributes](docs/UserReportsAttributes.md)
 - [UserReportsCreateOperationPayload](docs/UserReportsCreateOperationPayload.md)
 - [UserReportsCreateOperationPayloadData](docs/UserReportsCreateOperationPayloadData.md)
 - [UserReportsCreateOperationPayloadDataAttributes](docs/UserReportsCreateOperationPayloadDataAttributes.md)
 - [UserReportsCreateOperationPayloadDataRelationships](docs/UserReportsCreateOperationPayloadDataRelationships.md)
 - [UserReportsCreateOperationPayloadDataRelationshipsReportedResources](docs/UserReportsCreateOperationPayloadDataRelationshipsReportedResources.md)
 - [UserReportsCreateOperationPayloadDataRelationshipsReportedResourcesData](docs/UserReportsCreateOperationPayloadDataRelationshipsReportedResourcesData.md)
 - [UserReportsCreateResource403ResponseBody](docs/UserReportsCreateResource403ResponseBody.md)
 - [UserReportsCreateResource403ResponseBodyErrorsInner](docs/UserReportsCreateResource403ResponseBodyErrorsInner.md)
 - [UserReportsCreateSingleResourceDataDocument](docs/UserReportsCreateSingleResourceDataDocument.md)
 - [UserReportsResourceObject](docs/UserReportsResourceObject.md)
 - [UserSubscriptionPriceChangesAttributes](docs/UserSubscriptionPriceChangesAttributes.md)
 - [UserSubscriptionPriceChangesDecisionSingleRelationshipDataDocument](docs/UserSubscriptionPriceChangesDecisionSingleRelationshipDataDocument.md)
 - [UserSubscriptionPriceChangesMultiResourceDataDocument](docs/UserSubscriptionPriceChangesMultiResourceDataDocument.md)
 - [UserSubscriptionPriceChangesRelationships](docs/UserSubscriptionPriceChangesRelationships.md)
 - [UserSubscriptionPriceChangesResourceObject](docs/UserSubscriptionPriceChangesResourceObject.md)
 - [UsersArtistSingleRelationshipDataDocument](docs/UsersArtistSingleRelationshipDataDocument.md)
 - [UsersAttributes](docs/UsersAttributes.md)
 - [UsersRelationships](docs/UsersRelationships.md)
 - [UsersResourceObject](docs/UsersResourceObject.md)
 - [UsersSingleResourceDataDocument](docs/UsersSingleResourceDataDocument.md)
 - [Variation](docs/Variation.md)
 - [VideoManifestsAttributes](docs/VideoManifestsAttributes.md)
 - [VideoManifestsReadById403ResponseBody](docs/VideoManifestsReadById403ResponseBody.md)
 - [VideoManifestsReadById404ResponseBody](docs/VideoManifestsReadById404ResponseBody.md)
 - [VideoManifestsResourceObject](docs/VideoManifestsResourceObject.md)
 - [VideoManifestsSingleResourceDataDocument](docs/VideoManifestsSingleResourceDataDocument.md)
 - [VideosAlbumsMultiRelationshipDataDocument](docs/VideosAlbumsMultiRelationshipDataDocument.md)
 - [VideosAlbumsResourceIdentifier](docs/VideosAlbumsResourceIdentifier.md)
 - [VideosAlbumsResourceIdentifierMeta](docs/VideosAlbumsResourceIdentifierMeta.md)
 - [VideosArtistsMultiRelationshipDataDocument](docs/VideosArtistsMultiRelationshipDataDocument.md)
 - [VideosAttributes](docs/VideosAttributes.md)
 - [VideosCreditsMultiRelationshipDataDocument](docs/VideosCreditsMultiRelationshipDataDocument.md)
 - [VideosMultiResourceDataDocument](docs/VideosMultiResourceDataDocument.md)
 - [VideosProvidersMultiRelationshipDataDocument](docs/VideosProvidersMultiRelationshipDataDocument.md)
 - [VideosRelationships](docs/VideosRelationships.md)
 - [VideosReplacementResourceIdentifier](docs/VideosReplacementResourceIdentifier.md)
 - [VideosReplacementResourceIdentifierMeta](docs/VideosReplacementResourceIdentifierMeta.md)
 - [VideosReplacementSingleRelationshipDataDocument](docs/VideosReplacementSingleRelationshipDataDocument.md)
 - [VideosResourceObject](docs/VideosResourceObject.md)
 - [VideosSimilarVideosMultiRelationshipDataDocument](docs/VideosSimilarVideosMultiRelationshipDataDocument.md)
 - [VideosSimilarVideosResourceIdentifier](docs/VideosSimilarVideosResourceIdentifier.md)
 - [VideosSimilarVideosResourceIdentifierMeta](docs/VideosSimilarVideosResourceIdentifierMeta.md)
 - [VideosSingleResourceDataDocument](docs/VideosSingleResourceDataDocument.md)
 - [VideosSuggestedVideosMultiRelationshipDataDocument](docs/VideosSuggestedVideosMultiRelationshipDataDocument.md)
 - [VideosSuggestedVideosResourceIdentifier](docs/VideosSuggestedVideosResourceIdentifier.md)
 - [VideosSuggestedVideosResourceIdentifierMeta](docs/VideosSuggestedVideosResourceIdentifierMeta.md)
 - [VideosThumbnailArtMultiRelationshipDataDocument](docs/VideosThumbnailArtMultiRelationshipDataDocument.md)
 - [VideosUsageRulesSingleRelationshipDataDocument](docs/VideosUsageRulesSingleRelationshipDataDocument.md)
 - [ViewerContextsAttributes](docs/ViewerContextsAttributes.md)
 - [ViewerContextsCommentsMultiRelationshipDataDocument](docs/ViewerContextsCommentsMultiRelationshipDataDocument.md)
 - [ViewerContextsMultiResourceDataDocument](docs/ViewerContextsMultiResourceDataDocument.md)
 - [ViewerContextsReactionsMultiRelationshipDataDocument](docs/ViewerContextsReactionsMultiRelationshipDataDocument.md)
 - [ViewerContextsRelationships](docs/ViewerContextsRelationships.md)
 - [ViewerContextsResourceObject](docs/ViewerContextsResourceObject.md)
 - [ViewerContextsSingleResourceDataDocument](docs/ViewerContextsSingleResourceDataDocument.md)
 - [ViewerContextsSubjectResourceIdentifier](docs/ViewerContextsSubjectResourceIdentifier.md)
 - [ViewerContextsSubjectResourceIdentifierMeta](docs/ViewerContextsSubjectResourceIdentifierMeta.md)
 - [ViewerContextsSubjectSingleRelationshipDataDocument](docs/ViewerContextsSubjectSingleRelationshipDataDocument.md)
 - [ViewerContextsViewerSingleRelationshipDataDocument](docs/ViewerContextsViewerSingleRelationshipDataDocument.md)
 - [Waveform](docs/Waveform.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Authorization_Code_PKCE"></a>
### Authorization_Code_PKCE

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://login.tidal.com/authorize
- **Scopes**: 
 - **collection.read**: Read access to a user's \"My Collection\".
 - **collection.write**: Write access to a user's \"My Collection\".
 - **entitlements.read**: Read access to what functionality a user is entitled to access on TIDAL, such as whether they can stream music, use DJ add-ons and similar.
 - **playback**: Required to play media content and control playback.
 - **playlists.read**: Required to list playlists created by a user.
 - **playlists.write**: Write access to a user's playlists.
 - **r_usr**: Read access to all end user data
 - **recommendations.read**: Read access to a user’s personal recommendations.
 - **search.read**: Required to read personalized search results.
 - **search.write**: Required to update personalized search results, e.g. delete search history.
 - **user.read**: Read access to a user's account information, such as country and email address.
 - **w_usr**: Write user

<a id="Client_Credentials"></a>
### Client_Credentials

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: N/A


## Author




## Request headers

Header names are compared case-insensitively in all Python client libraries.
Request headers are copied; supplying `_headers` does not change the caller's dict
or the client's shared defaults. The public `_headers` argument retains its dict
validation and existing value serialization. Pydantic can coerce mappings such as HTTPX `Headers` to a dict,
combining repeated fields into a single value; `_headers` does not provide a
repeated-field or list-of-pairs API.

Precedence, from lowest to highest:

1. `_headers` (within one dict, the last inserted case variant wins).
2. Explicit OpenAPI header parameters and generated `Content-Type` (or `_content_type`).
   Generated `Accept` is added only when neither `_headers` nor explicit header
   parameters contain an `Accept` case variant.
3. `ApiClient.default_headers` (including headers set with `set_default_header`).
4. The client's `cookie` setting, for `Cookie`.
5. Authentication headers. A non-empty `_request_auth` replaces configured
   authentication for that call; `{}` retains configured authentication. Cookie
   authentication appends to the selected `Cookie` value.

This retains the existing precedence for identically spelled names and extends it
to case variants. To override a generated content type, use `_content_type`;
client defaults still take precedence over it. The winning header's spelling and
value are retained for replacements. Cookie authentication uses the canonical
`Cookie` spelling and appends its value. Values containing legitimate
comma-separated lists are not split or deduplicated. This does not remove
duplicate values inside a header or change the handling of repeated fields
supplied directly to the transport.
