"""
    TIDAL API

    The TIDAL API is a [JSON:API](https://jsonapi.org/)-compliant web API exposing TIDAL's music catalogue, metadata, and user functionality. Guides, authorization documentation, and API key management live at [developer.tidal.com](https://developer.tidal.com).  All endpoints exchange `application/vnd.api+json` documents per the [JSON:API specification](https://jsonapi.org/format/): [resource objects](https://jsonapi.org/format/#document-resource-objects) with `attributes` and `relationships`, [compound documents](https://jsonapi.org/format/#document-compound-documents) via `include`, and standard [error objects](https://jsonapi.org/format/#error-objects).  ### Authentication and authorization  Every request requires an OAuth 2.0 access token in the `Authorization: Bearer` header. Tokens are issued at `https://auth.tidal.com/v1/oauth2/token` via the client-credentials flow (server-to-server) or the authorization-code + PKCE flow (user context; authorize at `https://login.tidal.com/authorize`). Each endpoint documents which flows it accepts, the access tier it requires, and the scopes that apply. Scopes protect private user data: fields you are not authorized to read are redacted from the response rather than causing an error, and resources you cannot access at all behave as if they do not exist. See the [authorization guide](https://developer.tidal.com/documentation/api-sdk/api-sdk-authorization) for details.  ### Common wire types and compatibility  Each property's schema is authoritative for its allowed values, format, requiredness, nullability, and constraints. A standard defines how a value is represented; an individual schema may support only a documented subset.  - **Enums** use `UPPER_CASE_UNDERSCORE`, except JSON:API resource types, which use plural camelCase names such as `playlistGenerationSchedules`. New values can be added to any enum at any time, so treat unknown values as forward-compatible rather than errors. - **Resource IDs** are opaque strings. A few resources document well-known IDs for permanent system singleton instances; compare those IDs by exact value. Never parse, construct, or infer meaning from any other `id`, even when its current representation resembles an integer, UUID, or another recognizable value. Other properties explicitly marked with OpenAPI `format: uuid` are UUIDs. - **Dates and times** use ISO 8601. Date-times use the OpenAPI `date-time` format (`2024-05-01T12:00:00Z`), dates use `YYYY-MM-DD`, and durations use values such as `PT3M5S`. - **Recurrence frequencies** use RFC 5545 `FREQ` names such as `DAILY`, `WEEKLY`, and `MONTHLY`. The property's enum lists the frequencies that field currently supports. - **Weekdays** use `MONDAY` through `SUNDAY`. - **Time zones** use IANA Time Zone Database identifiers such as `Europe/Stockholm`, not abbreviations or raw UTC offsets for recurring civil-time schedules. - **Country codes** use ISO 3166-1 alpha-2; the shared country type also accepts `WW` for worldwide. **Locales** use IETF BCP 47 language tags such as `en-US`. - **Currencies** use ISO 4217 codes. Monetary amounts are decimal strings; each field defines its sign and precision constraints. - **Colors** use three- or six-digit hexadecimal strings (`#RGB` or `#RRGGBB`). Resource links to external URLs use JSON:API link objects with an `href` member.  ### Resource identifiers  Where supported, `filter[subject]=tracks:123` matches a related resource by type and ID; `filter[subject.id]=123` and `filter[subject.type]=tracks` match either component. Where multiple identifiers are accepted, comma-separated values match any complete pair. When a member path names a to-many relationship, at least one related resource must match; filtering does not trim that relationship. On collection and to-many relationship reads, the reserved root `self` (`filter[self]=tracks:123`) filters primary data itself. Each endpoint lists its supported filters and types.  Where supported, `me` aliases the authenticated user's dedicated resource ID for the referenced resource type. It works in paths, resource-ID filters, compact identifiers (`type:me`), resource PATCH primary IDs and standalone relationship mutation identifiers, with the same meaning as the resolved ID. Reads using the alias are `no-store`.  ### Relationships and includes  [Relationships](https://jsonapi.org/format/#document-resource-object-relationships) are returned only on request: [`include`](https://jsonapi.org/format/#fetching-includes) selects linkage and related content, while `includeLinkage` selects authorized linkage only. A relationship that was not requested is absent from the response, not empty. The full set of relationships a resource supports is documented in its schema.  For INTERNAL clients on resource GET endpoints, `includeLinkage` accepts comma-separated direct relationship names, for example `includeLinkage=subject,viewer`. It does not load related resources or add an `included` section. Nested paths and type qualifiers are unsupported. To-many linkage retains its normal pagination and relationship `next` links. Selecting the same relationship with both parameters applies full include behavior and reads the relationship once.  Request related resources in one round trip with `?include=`, a comma-separated list of dot-separated relationship paths — e.g. `include=coverArt,artists.profileArt` on an album. A nested path automatically embeds its intermediate resources: `artists.profileArt` includes the artists as well as their profile art. Include paths are always relative to the request's root resource, also on relationship endpoints. Including a relationship never changes the primary data; the related resources are added to `included`.  Include paths are validated: a path that cannot be resolved against the resources' documented relationships is rejected with `400`. Include trees are also bounded in path depth (default 3 levels) and in the total number of distinct resources they name (default 10); individual endpoints may apply different limits. Both selectors share the include-node limit, counting overlapping roots once. A request exceeding either limit is rejected with `400`, with the effective limit stated in the error.  ### Filtering, sorting, pagination  - [`filter[<memberPath>]=value`](https://jsonapi.org/format/#fetching-filtering) filters primary data by equality. Each endpoint lists its available filters; most collections require at least one. - Where explicitly documented, `filter[<memberPath>][ne]=value` negates the complete equality predicate. When the member path names a to-many relationship, no related ID may match any supplied value; a known-empty relationship matches. Operators are separate from values. Supplied comparisons combine with AND. For a required filter with multiple supported comparisons, at least one must be supplied; the parameter descriptions identify these alternatives. Unsupported operators and groups return `400`. - Where documented, `filter[<path>][<operator>]=value` applies an endpoint-defined operator, such as `filter[self][matchesQuery]`. Its meaning is described per endpoint, and it combines with other filters by AND. - [`sort=<memberPath>`](https://jsonapi.org/format/#fetching-sorting) sorts ascending, `-<memberPath>` descending (`sort=-addedAt`). Filter and sort member paths are relative to primary data. - Parameters an endpoint cannot honor are rejected with `400`: a `filter[...]` parameter the endpoint does not document (the error lists the available filters), or `sort` on an endpoint that documents no sort values. - [Pagination](https://jsonapi.org/format/#fetching-pagination) is cursor-based: responses carry `links.self` and, while more pages exist, `links.next` with an opaque `page[cursor]`. Follow `next` until absent — there are no offset or total-page parameters. Collection sizes, when available, appear as `meta.total` and may be approximate.  ### Type qualifiers  Where a relationship can contain several resource types, a path segment may be prefixed with a concrete type to scope which type's member is accessed. A playlist's `items` are `tracks` or `videos`: `GET /playlists/{id}?include=items.tracks:albums` resolves `albums` only for the items that are tracks. Qualifiers scope member access — they never filter which resources appear in a relationship — and can be chained.  The same syntax applies to `filter` and `sort` member paths on endpoints that support it; where supported, the qualified member is listed among the endpoint's documented filters and sort values. The syntax follows JSON:API proposal [json-api#1695](https://github.com/json-api/json-api/issues/1695).  ### Mutations  - [Partial updates](https://jsonapi.org/format/#crud-updating-resource-attributes) distinguish three wire states for nullable attributes: omission leaves the current value unchanged, an explicit `null` clears it, and a concrete value updates it. - Every mutation accepts an [`Idempotency-Key`](https://www.ietf.org/archive/id/draft-ietf-httpapi-idempotency-key-header-07.html) header. Keys are scoped to the client and the authenticated user. Once the original request has completed, retrying it with the same key, method, path, query and payload within one hour replays its response; a retry while it is still processing is rejected with `409`, and the same key with a different method, path, query or payload with `422`. - After a successful write, your own subsequent reads reflect the change; other clients may observe it with a delay.  ### Revisions and concurrent editing  Where supported, `attributes.revision` identifies the resource's documented aggregate state; a separately versioned relationship collection uses document `meta.revision`. Revisions are nonnegative integers that increase when covered state changes. Compare them only within the same identity and scope, preserve the exact value, and never calculate the next revision. Related content, viewer projections and independent sources are not automatically covered. Domain fields named `version`, such as a music edition, are distinct; existing endpoints retain their documented contracts.  Guarded mutations accept the observed value as top-level `meta.expectedRevision`. Each operation declares its scope and whether the precondition is required. A mismatch returns `409`; missing required input returns `400`. Refresh and reconcile after a conflict, then submit a new operation with a new idempotency key. An identical retry with the original key replays a recorded success under the idempotency contract. These revisions are not HTTP ETags.  Returned revisions describe observed snapshots, not reservations for later writes. Background changes can advance them immediately after a successful response.  ### Media resource replacements - BETA Internal only  Media resources (`tracks`, `videos`, and `albums`) can become unavailable in a country when licensing rights change. By default, TIDAL API returns the resource identifiers originally stored in a collection. This keeps ordinary reads predictable and consistent.  If a stored media resource is unavailable for the effective country, TIDAL may identify a contextually applicable alternative that is available there. Replacement is best effort, so an alternative is not always available. Replacement never changes the stored collection.  TIDAL API provides two ways to work with replacements:  1. **Inspect the `replacement` relationship.** A media resource can expose its applicable alternative through the `replacement` relationship. Include this relationship when a client needs both the original and replacement identifiers or wants to decide whether to use the replacement.  2. **Apply replacements with `replaceMedia`.** Clients can use `replaceMedia` to substitute applicable replacements directly into selected relationship data. The parameter accepts relationship paths using the same syntax as `include`. Projection affects only the response and preserves relationship order and metadata. Each identifier includes `meta.replacement` describing whether it was `ORIGINAL`, `REPLACED`, or `NOT_REPLACED`.  For example, `GET /playlists/{id}?include=items&replaceMedia=items` applies replacements to media identifiers in the playlist's `items` relationship.  ### Compression  Responses are gzip-compressed when the request includes `Accept-Encoding: gzip` (bodies over 2 KB).  ### Deprecation  Deprecated endpoints, parameters, and fields are marked `deprecated` in this specification, with the replacement noted in their description. Deprecated functionality keeps working for at least six months after being marked, and is only removed once a replacement is generally available.

    The version of the OpenAPI document: 1.10.254
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from tidal.models.albums_album_statistics_single_relationship_data_document import AlbumsAlbumStatisticsSingleRelationshipDataDocument
from tidal.models.albums_artists_multi_relationship_data_document import AlbumsArtistsMultiRelationshipDataDocument
from tidal.models.albums_artists_relationship_update_operation_payload import AlbumsArtistsRelationshipUpdateOperationPayload
from tidal.models.albums_cover_art_multi_relationship_data_document import AlbumsCoverArtMultiRelationshipDataDocument
from tidal.models.albums_cover_art_relationship_update_operation_payload import AlbumsCoverArtRelationshipUpdateOperationPayload
from tidal.models.albums_create_operation_payload import AlbumsCreateOperationPayload
from tidal.models.albums_create_single_resource_data_document import AlbumsCreateSingleResourceDataDocument
from tidal.models.albums_genres_multi_relationship_data_document import AlbumsGenresMultiRelationshipDataDocument
from tidal.models.albums_items_multi_relationship_data_document import AlbumsItemsMultiRelationshipDataDocument
from tidal.models.albums_items_relationship_update_operation_payload import AlbumsItemsRelationshipUpdateOperationPayload
from tidal.models.albums_multi_resource_data_document import AlbumsMultiResourceDataDocument
from tidal.models.albums_owners_multi_relationship_data_document import AlbumsOwnersMultiRelationshipDataDocument
from tidal.models.albums_price_config_single_relationship_data_document import AlbumsPriceConfigSingleRelationshipDataDocument
from tidal.models.albums_providers_multi_relationship_data_document import AlbumsProvidersMultiRelationshipDataDocument
from tidal.models.albums_replacement_single_relationship_data_document import AlbumsReplacementSingleRelationshipDataDocument
from tidal.models.albums_shares_multi_relationship_data_document import AlbumsSharesMultiRelationshipDataDocument
from tidal.models.albums_similar_albums_multi_relationship_data_document import AlbumsSimilarAlbumsMultiRelationshipDataDocument
from tidal.models.albums_single_resource_data_document import AlbumsSingleResourceDataDocument
from tidal.models.albums_suggested_cover_arts_multi_relationship_data_document import AlbumsSuggestedCoverArtsMultiRelationshipDataDocument
from tidal.models.albums_update_operation_payload import AlbumsUpdateOperationPayload
from tidal.models.albums_usage_rules_single_relationship_data_document import AlbumsUsageRulesSingleRelationshipDataDocument
from tidal.models.mutation_response_document import MutationResponseDocument

from tidal.api_client import ApiClient, RequestSerialized
from tidal.api_response import ApiResponse
from tidal.rest import RESTResponseType


class AlbumsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def albums_get(
        self,
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        filter_barcode_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1, strict=True)]], Field(min_length=1, max_length=20)]], Field(description="List of barcode IDs (EAN-13 or UPC-A). NOTE: Supplying more than one barcode ID will currently only return one album per barcode ID. (e.g. `196589525444`)")] = None,
        filter_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1, strict=True)]], Field(min_length=1, max_length=20)]], Field(description="List of album IDs (e.g. `251380836`)")] = None,
        filter_owners_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1, strict=True)]], Field(min_length=1, max_length=1)]], Field(description="User id. Also accepts `me`.")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: albumStatistics, artists, coverArt, genres, items, owners, priceConfig, providers, replacement, shares, similarAlbums, suggestedCoverArts, usageRules")] = None,
        include_linkage: Annotated[Optional[List[StrictStr]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        sort: Annotated[Optional[List[StrictStr]], Field(description="Values prefixed with \"-\" are sorted descending; values without it are sorted ascending.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> AlbumsMultiResourceDataDocument:
        """Get multiple albums.

        Retrieves multiple albums by available filters, or without if applicable.

        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param filter_barcode_id: List of barcode IDs (EAN-13 or UPC-A). NOTE: Supplying more than one barcode ID will currently only return one album per barcode ID. (e.g. `196589525444`)
        :type filter_barcode_id: List[str]
        :param filter_id: List of album IDs (e.g. `251380836`)
        :type filter_id: List[str]
        :param filter_owners_id: User id. Also accepts `me`.
        :type filter_owners_id: List[str]
        :param include: Include related resources. Available relationships: albumStatistics, artists, coverArt, genres, items, owners, priceConfig, providers, replacement, shares, similarAlbums, suggestedCoverArts, usageRules
        :type include: List[str]
        :param include_linkage: Comma-separated direct relationships to return as linkage only, without related content.
        :type include_linkage: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums
        :type replace_media: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param sort: Values prefixed with \"-\" are sorted descending; values without it are sorted ascending.
        :type sort: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_get_serialize(
            country_code=country_code,
            filter_barcode_id=filter_barcode_id,
            filter_id=filter_id,
            filter_owners_id=filter_owners_id,
            include=include,
            include_linkage=include_linkage,
            page_cursor=page_cursor,
            replace_media=replace_media,
            share_code=share_code,
            sort=sort,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsMultiResourceDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def albums_get_with_http_info(
        self,
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        filter_barcode_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1, strict=True)]], Field(min_length=1, max_length=20)]], Field(description="List of barcode IDs (EAN-13 or UPC-A). NOTE: Supplying more than one barcode ID will currently only return one album per barcode ID. (e.g. `196589525444`)")] = None,
        filter_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1, strict=True)]], Field(min_length=1, max_length=20)]], Field(description="List of album IDs (e.g. `251380836`)")] = None,
        filter_owners_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1, strict=True)]], Field(min_length=1, max_length=1)]], Field(description="User id. Also accepts `me`.")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: albumStatistics, artists, coverArt, genres, items, owners, priceConfig, providers, replacement, shares, similarAlbums, suggestedCoverArts, usageRules")] = None,
        include_linkage: Annotated[Optional[List[StrictStr]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        sort: Annotated[Optional[List[StrictStr]], Field(description="Values prefixed with \"-\" are sorted descending; values without it are sorted ascending.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[AlbumsMultiResourceDataDocument]:
        """Get multiple albums.

        Retrieves multiple albums by available filters, or without if applicable.

        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param filter_barcode_id: List of barcode IDs (EAN-13 or UPC-A). NOTE: Supplying more than one barcode ID will currently only return one album per barcode ID. (e.g. `196589525444`)
        :type filter_barcode_id: List[str]
        :param filter_id: List of album IDs (e.g. `251380836`)
        :type filter_id: List[str]
        :param filter_owners_id: User id. Also accepts `me`.
        :type filter_owners_id: List[str]
        :param include: Include related resources. Available relationships: albumStatistics, artists, coverArt, genres, items, owners, priceConfig, providers, replacement, shares, similarAlbums, suggestedCoverArts, usageRules
        :type include: List[str]
        :param include_linkage: Comma-separated direct relationships to return as linkage only, without related content.
        :type include_linkage: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums
        :type replace_media: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param sort: Values prefixed with \"-\" are sorted descending; values without it are sorted ascending.
        :type sort: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_get_serialize(
            country_code=country_code,
            filter_barcode_id=filter_barcode_id,
            filter_id=filter_id,
            filter_owners_id=filter_owners_id,
            include=include,
            include_linkage=include_linkage,
            page_cursor=page_cursor,
            replace_media=replace_media,
            share_code=share_code,
            sort=sort,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsMultiResourceDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def albums_get_without_preload_content(
        self,
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        filter_barcode_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1, strict=True)]], Field(min_length=1, max_length=20)]], Field(description="List of barcode IDs (EAN-13 or UPC-A). NOTE: Supplying more than one barcode ID will currently only return one album per barcode ID. (e.g. `196589525444`)")] = None,
        filter_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1, strict=True)]], Field(min_length=1, max_length=20)]], Field(description="List of album IDs (e.g. `251380836`)")] = None,
        filter_owners_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1, strict=True)]], Field(min_length=1, max_length=1)]], Field(description="User id. Also accepts `me`.")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: albumStatistics, artists, coverArt, genres, items, owners, priceConfig, providers, replacement, shares, similarAlbums, suggestedCoverArts, usageRules")] = None,
        include_linkage: Annotated[Optional[List[StrictStr]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        sort: Annotated[Optional[List[StrictStr]], Field(description="Values prefixed with \"-\" are sorted descending; values without it are sorted ascending.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get multiple albums.

        Retrieves multiple albums by available filters, or without if applicable.

        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param filter_barcode_id: List of barcode IDs (EAN-13 or UPC-A). NOTE: Supplying more than one barcode ID will currently only return one album per barcode ID. (e.g. `196589525444`)
        :type filter_barcode_id: List[str]
        :param filter_id: List of album IDs (e.g. `251380836`)
        :type filter_id: List[str]
        :param filter_owners_id: User id. Also accepts `me`.
        :type filter_owners_id: List[str]
        :param include: Include related resources. Available relationships: albumStatistics, artists, coverArt, genres, items, owners, priceConfig, providers, replacement, shares, similarAlbums, suggestedCoverArts, usageRules
        :type include: List[str]
        :param include_linkage: Comma-separated direct relationships to return as linkage only, without related content.
        :type include_linkage: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums
        :type replace_media: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param sort: Values prefixed with \"-\" are sorted descending; values without it are sorted ascending.
        :type sort: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_get_serialize(
            country_code=country_code,
            filter_barcode_id=filter_barcode_id,
            filter_id=filter_id,
            filter_owners_id=filter_owners_id,
            include=include,
            include_linkage=include_linkage,
            page_cursor=page_cursor,
            replace_media=replace_media,
            share_code=share_code,
            sort=sort,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsMultiResourceDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _albums_get_serialize(
        self,
        country_code,
        filter_barcode_id,
        filter_id,
        filter_owners_id,
        include,
        include_linkage,
        page_cursor,
        replace_media,
        share_code,
        sort,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'filter[barcodeId]': 'multi',
            'filter[id]': 'multi',
            'filter[owners.id]': 'multi',
            'include': 'multi',
            'includeLinkage': 'csv',
            'sort': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if country_code is not None:
            
            _query_params.append(('countryCode', country_code))
            
        if filter_barcode_id is not None:
            
            _query_params.append(('filter[barcodeId]', filter_barcode_id))
            
        if filter_id is not None:
            
            _query_params.append(('filter[id]', filter_id))
            
        if filter_owners_id is not None:
            
            _query_params.append(('filter[owners.id]', filter_owners_id))
            
        if include is not None:
            
            _query_params.append(('include', include))
            
        if include_linkage is not None:
            
            _query_params.append(('includeLinkage', include_linkage))
            
        if page_cursor is not None:
            
            _query_params.append(('page[cursor]', page_cursor))
            
        if replace_media is not None:
            
            _query_params.append(('replaceMedia', replace_media))
            
        if share_code is not None:
            
            _query_params.append(('shareCode', share_code))
            
        if sort is not None:
            
            _query_params.append(('sort', sort))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/albums',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def albums_id_delete(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> MutationResponseDocument:
        """Delete single album.

        Deletes existing album.

        :param id: Album id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_delete_serialize(
            id=id,
            idempotency_key=idempotency_key,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def albums_id_delete_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[MutationResponseDocument]:
        """Delete single album.

        Deletes existing album.

        :param id: Album id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_delete_serialize(
            id=id,
            idempotency_key=idempotency_key,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def albums_id_delete_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Delete single album.

        Deletes existing album.

        :param id: Album id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_delete_serialize(
            id=id,
            idempotency_key=idempotency_key,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _albums_id_delete_serialize(
        self,
        id,
        idempotency_key,
        share_code,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if share_code is not None:
            
            _query_params.append(('shareCode', share_code))
            
        # process the header parameters
        if idempotency_key is not None:
            self.api_client._set_header(_header_params, 'Idempotency-Key', idempotency_key)
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/albums/{id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def albums_id_get(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: albumStatistics, artists, coverArt, genres, items, owners, priceConfig, providers, replacement, shares, similarAlbums, suggestedCoverArts, usageRules")] = None,
        include_linkage: Annotated[Optional[List[StrictStr]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> AlbumsSingleResourceDataDocument:
        """Get single album.

        Retrieves single album by id.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: albumStatistics, artists, coverArt, genres, items, owners, priceConfig, providers, replacement, shares, similarAlbums, suggestedCoverArts, usageRules
        :type include: List[str]
        :param include_linkage: Comma-separated direct relationships to return as linkage only, without related content.
        :type include_linkage: List[str]
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums
        :type replace_media: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            include_linkage=include_linkage,
            replace_media=replace_media,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsSingleResourceDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def albums_id_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: albumStatistics, artists, coverArt, genres, items, owners, priceConfig, providers, replacement, shares, similarAlbums, suggestedCoverArts, usageRules")] = None,
        include_linkage: Annotated[Optional[List[StrictStr]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[AlbumsSingleResourceDataDocument]:
        """Get single album.

        Retrieves single album by id.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: albumStatistics, artists, coverArt, genres, items, owners, priceConfig, providers, replacement, shares, similarAlbums, suggestedCoverArts, usageRules
        :type include: List[str]
        :param include_linkage: Comma-separated direct relationships to return as linkage only, without related content.
        :type include_linkage: List[str]
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums
        :type replace_media: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            include_linkage=include_linkage,
            replace_media=replace_media,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsSingleResourceDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def albums_id_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: albumStatistics, artists, coverArt, genres, items, owners, priceConfig, providers, replacement, shares, similarAlbums, suggestedCoverArts, usageRules")] = None,
        include_linkage: Annotated[Optional[List[StrictStr]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get single album.

        Retrieves single album by id.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: albumStatistics, artists, coverArt, genres, items, owners, priceConfig, providers, replacement, shares, similarAlbums, suggestedCoverArts, usageRules
        :type include: List[str]
        :param include_linkage: Comma-separated direct relationships to return as linkage only, without related content.
        :type include_linkage: List[str]
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums
        :type replace_media: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            include_linkage=include_linkage,
            replace_media=replace_media,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsSingleResourceDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _albums_id_get_serialize(
        self,
        id,
        country_code,
        include,
        include_linkage,
        replace_media,
        share_code,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
            'includeLinkage': 'csv',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if country_code is not None:
            
            _query_params.append(('countryCode', country_code))
            
        if include is not None:
            
            _query_params.append(('include', include))
            
        if include_linkage is not None:
            
            _query_params.append(('includeLinkage', include_linkage))
            
        if replace_media is not None:
            
            _query_params.append(('replaceMedia', replace_media))
            
        if share_code is not None:
            
            _query_params.append(('shareCode', share_code))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/albums/{id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def albums_id_patch(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        albums_update_operation_payload: Optional[AlbumsUpdateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> MutationResponseDocument:
        """Update single album.

        Updates existing album. A COLLABORATOR on the album may update it; changing accessType, published or barcodeId needs OWNER.

        :param id: Album id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param albums_update_operation_payload:
        :type albums_update_operation_payload: AlbumsUpdateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_patch_serialize(
            id=id,
            idempotency_key=idempotency_key,
            share_code=share_code,
            albums_update_operation_payload=albums_update_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def albums_id_patch_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        albums_update_operation_payload: Optional[AlbumsUpdateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[MutationResponseDocument]:
        """Update single album.

        Updates existing album. A COLLABORATOR on the album may update it; changing accessType, published or barcodeId needs OWNER.

        :param id: Album id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param albums_update_operation_payload:
        :type albums_update_operation_payload: AlbumsUpdateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_patch_serialize(
            id=id,
            idempotency_key=idempotency_key,
            share_code=share_code,
            albums_update_operation_payload=albums_update_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def albums_id_patch_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        albums_update_operation_payload: Optional[AlbumsUpdateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Update single album.

        Updates existing album. A COLLABORATOR on the album may update it; changing accessType, published or barcodeId needs OWNER.

        :param id: Album id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param albums_update_operation_payload:
        :type albums_update_operation_payload: AlbumsUpdateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_patch_serialize(
            id=id,
            idempotency_key=idempotency_key,
            share_code=share_code,
            albums_update_operation_payload=albums_update_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _albums_id_patch_serialize(
        self,
        id,
        idempotency_key,
        share_code,
        albums_update_operation_payload,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if share_code is not None:
            
            _query_params.append(('shareCode', share_code))
            
        # process the header parameters
        if idempotency_key is not None:
            self.api_client._set_header(_header_params, 'Idempotency-Key', idempotency_key)
        # process the form parameters
        # process the body parameter
        if albums_update_operation_payload is not None:
            _body_params = albums_update_operation_payload


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            self.api_client._set_header(_header_params, 'Content-Type', _content_type)
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/vnd.api+json'
                    ]
                )
            )
            if _default_content_type is not None:
                self.api_client._set_header(_header_params, 'Content-Type', _default_content_type)

        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE'
        ]

        return self.api_client.param_serialize(
            method='PATCH',
            resource_path='/albums/{id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def albums_id_relationships_album_statistics_get(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: albumStatistics")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> AlbumsAlbumStatisticsSingleRelationshipDataDocument:
        """Get albumStatistics relationship (\"to-one\").

        Retrieves albumStatistics relationship.

        :param id: Album id (required)
        :type id: str
        :param include: Include related resources. Available relationships: albumStatistics
        :type include: List[str]
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_album_statistics_get_serialize(
            id=id,
            include=include,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsAlbumStatisticsSingleRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def albums_id_relationships_album_statistics_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: albumStatistics")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[AlbumsAlbumStatisticsSingleRelationshipDataDocument]:
        """Get albumStatistics relationship (\"to-one\").

        Retrieves albumStatistics relationship.

        :param id: Album id (required)
        :type id: str
        :param include: Include related resources. Available relationships: albumStatistics
        :type include: List[str]
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_album_statistics_get_serialize(
            id=id,
            include=include,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsAlbumStatisticsSingleRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def albums_id_relationships_album_statistics_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: albumStatistics")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get albumStatistics relationship (\"to-one\").

        Retrieves albumStatistics relationship.

        :param id: Album id (required)
        :type id: str
        :param include: Include related resources. Available relationships: albumStatistics
        :type include: List[str]
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_album_statistics_get_serialize(
            id=id,
            include=include,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsAlbumStatisticsSingleRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _albums_id_relationships_album_statistics_get_serialize(
        self,
        id,
        include,
        share_code,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if include is not None:
            
            _query_params.append(('include', include))
            
        if share_code is not None:
            
            _query_params.append(('shareCode', share_code))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/albums/{id}/relationships/albumStatistics',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def albums_id_relationships_artists_get(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: artists")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> AlbumsArtistsMultiRelationshipDataDocument:
        """Get artists relationship (\"to-many\").

        Retrieves artists relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: artists
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums
        :type replace_media: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_artists_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsArtistsMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def albums_id_relationships_artists_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: artists")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[AlbumsArtistsMultiRelationshipDataDocument]:
        """Get artists relationship (\"to-many\").

        Retrieves artists relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: artists
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums
        :type replace_media: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_artists_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsArtistsMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def albums_id_relationships_artists_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: artists")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get artists relationship (\"to-many\").

        Retrieves artists relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: artists
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums
        :type replace_media: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_artists_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsArtistsMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _albums_id_relationships_artists_get_serialize(
        self,
        id,
        country_code,
        include,
        page_cursor,
        replace_media,
        share_code,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if country_code is not None:
            
            _query_params.append(('countryCode', country_code))
            
        if include is not None:
            
            _query_params.append(('include', include))
            
        if page_cursor is not None:
            
            _query_params.append(('page[cursor]', page_cursor))
            
        if replace_media is not None:
            
            _query_params.append(('replaceMedia', replace_media))
            
        if share_code is not None:
            
            _query_params.append(('shareCode', share_code))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/albums/{id}/relationships/artists',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def albums_id_relationships_artists_patch(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        albums_artists_relationship_update_operation_payload: Optional[AlbumsArtistsRelationshipUpdateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> MutationResponseDocument:
        """Update artists relationship (\"to-many\").

        Sets the album's artists, replacing the current list. Artists are listed in the order given. Provide 1 to 10 distinct artists. You can add your own artist profile and the profiles of users who have owner or collaborator access to the album. Owners and collaborators can change its artists. Returns an acknowledgement.

        :param id: Album id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param albums_artists_relationship_update_operation_payload:
        :type albums_artists_relationship_update_operation_payload: AlbumsArtistsRelationshipUpdateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_artists_patch_serialize(
            id=id,
            idempotency_key=idempotency_key,
            share_code=share_code,
            albums_artists_relationship_update_operation_payload=albums_artists_relationship_update_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def albums_id_relationships_artists_patch_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        albums_artists_relationship_update_operation_payload: Optional[AlbumsArtistsRelationshipUpdateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[MutationResponseDocument]:
        """Update artists relationship (\"to-many\").

        Sets the album's artists, replacing the current list. Artists are listed in the order given. Provide 1 to 10 distinct artists. You can add your own artist profile and the profiles of users who have owner or collaborator access to the album. Owners and collaborators can change its artists. Returns an acknowledgement.

        :param id: Album id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param albums_artists_relationship_update_operation_payload:
        :type albums_artists_relationship_update_operation_payload: AlbumsArtistsRelationshipUpdateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_artists_patch_serialize(
            id=id,
            idempotency_key=idempotency_key,
            share_code=share_code,
            albums_artists_relationship_update_operation_payload=albums_artists_relationship_update_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def albums_id_relationships_artists_patch_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        albums_artists_relationship_update_operation_payload: Optional[AlbumsArtistsRelationshipUpdateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Update artists relationship (\"to-many\").

        Sets the album's artists, replacing the current list. Artists are listed in the order given. Provide 1 to 10 distinct artists. You can add your own artist profile and the profiles of users who have owner or collaborator access to the album. Owners and collaborators can change its artists. Returns an acknowledgement.

        :param id: Album id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param albums_artists_relationship_update_operation_payload:
        :type albums_artists_relationship_update_operation_payload: AlbumsArtistsRelationshipUpdateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_artists_patch_serialize(
            id=id,
            idempotency_key=idempotency_key,
            share_code=share_code,
            albums_artists_relationship_update_operation_payload=albums_artists_relationship_update_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _albums_id_relationships_artists_patch_serialize(
        self,
        id,
        idempotency_key,
        share_code,
        albums_artists_relationship_update_operation_payload,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if share_code is not None:
            
            _query_params.append(('shareCode', share_code))
            
        # process the header parameters
        if idempotency_key is not None:
            self.api_client._set_header(_header_params, 'Idempotency-Key', idempotency_key)
        # process the form parameters
        # process the body parameter
        if albums_artists_relationship_update_operation_payload is not None:
            _body_params = albums_artists_relationship_update_operation_payload


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            self.api_client._set_header(_header_params, 'Content-Type', _content_type)
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/vnd.api+json'
                    ]
                )
            )
            if _default_content_type is not None:
                self.api_client._set_header(_header_params, 'Content-Type', _default_content_type)

        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE'
        ]

        return self.api_client.param_serialize(
            method='PATCH',
            resource_path='/albums/{id}/relationships/artists',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def albums_id_relationships_cover_art_get(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: coverArt")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> AlbumsCoverArtMultiRelationshipDataDocument:
        """Get coverArt relationship (\"to-many\").

        Retrieves coverArt relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: coverArt
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_cover_art_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsCoverArtMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def albums_id_relationships_cover_art_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: coverArt")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[AlbumsCoverArtMultiRelationshipDataDocument]:
        """Get coverArt relationship (\"to-many\").

        Retrieves coverArt relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: coverArt
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_cover_art_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsCoverArtMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def albums_id_relationships_cover_art_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: coverArt")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get coverArt relationship (\"to-many\").

        Retrieves coverArt relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: coverArt
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_cover_art_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsCoverArtMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _albums_id_relationships_cover_art_get_serialize(
        self,
        id,
        country_code,
        include,
        page_cursor,
        share_code,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if country_code is not None:
            
            _query_params.append(('countryCode', country_code))
            
        if include is not None:
            
            _query_params.append(('include', include))
            
        if page_cursor is not None:
            
            _query_params.append(('page[cursor]', page_cursor))
            
        if share_code is not None:
            
            _query_params.append(('shareCode', share_code))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/albums/{id}/relationships/coverArt',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def albums_id_relationships_cover_art_patch(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        albums_cover_art_relationship_update_operation_payload: Optional[AlbumsCoverArtRelationshipUpdateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> MutationResponseDocument:
        """Update coverArt relationship (\"to-many\").

        Replaces the uploaded cover artwork selection with one attachable artwork. Empty data clears the selection. Previously attached uploaded artwork is soft-deleted unless system-managed. Returns an acknowledgement.

        :param id: Album id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param albums_cover_art_relationship_update_operation_payload:
        :type albums_cover_art_relationship_update_operation_payload: AlbumsCoverArtRelationshipUpdateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_cover_art_patch_serialize(
            id=id,
            idempotency_key=idempotency_key,
            share_code=share_code,
            albums_cover_art_relationship_update_operation_payload=albums_cover_art_relationship_update_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def albums_id_relationships_cover_art_patch_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        albums_cover_art_relationship_update_operation_payload: Optional[AlbumsCoverArtRelationshipUpdateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[MutationResponseDocument]:
        """Update coverArt relationship (\"to-many\").

        Replaces the uploaded cover artwork selection with one attachable artwork. Empty data clears the selection. Previously attached uploaded artwork is soft-deleted unless system-managed. Returns an acknowledgement.

        :param id: Album id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param albums_cover_art_relationship_update_operation_payload:
        :type albums_cover_art_relationship_update_operation_payload: AlbumsCoverArtRelationshipUpdateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_cover_art_patch_serialize(
            id=id,
            idempotency_key=idempotency_key,
            share_code=share_code,
            albums_cover_art_relationship_update_operation_payload=albums_cover_art_relationship_update_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def albums_id_relationships_cover_art_patch_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        albums_cover_art_relationship_update_operation_payload: Optional[AlbumsCoverArtRelationshipUpdateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Update coverArt relationship (\"to-many\").

        Replaces the uploaded cover artwork selection with one attachable artwork. Empty data clears the selection. Previously attached uploaded artwork is soft-deleted unless system-managed. Returns an acknowledgement.

        :param id: Album id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param albums_cover_art_relationship_update_operation_payload:
        :type albums_cover_art_relationship_update_operation_payload: AlbumsCoverArtRelationshipUpdateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_cover_art_patch_serialize(
            id=id,
            idempotency_key=idempotency_key,
            share_code=share_code,
            albums_cover_art_relationship_update_operation_payload=albums_cover_art_relationship_update_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _albums_id_relationships_cover_art_patch_serialize(
        self,
        id,
        idempotency_key,
        share_code,
        albums_cover_art_relationship_update_operation_payload,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if share_code is not None:
            
            _query_params.append(('shareCode', share_code))
            
        # process the header parameters
        if idempotency_key is not None:
            self.api_client._set_header(_header_params, 'Idempotency-Key', idempotency_key)
        # process the form parameters
        # process the body parameter
        if albums_cover_art_relationship_update_operation_payload is not None:
            _body_params = albums_cover_art_relationship_update_operation_payload


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            self.api_client._set_header(_header_params, 'Content-Type', _content_type)
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/vnd.api+json'
                    ]
                )
            )
            if _default_content_type is not None:
                self.api_client._set_header(_header_params, 'Content-Type', _default_content_type)

        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE'
        ]

        return self.api_client.param_serialize(
            method='PATCH',
            resource_path='/albums/{id}/relationships/coverArt',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def albums_id_relationships_genres_get(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: genres")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> AlbumsGenresMultiRelationshipDataDocument:
        """Get genres relationship (\"to-many\").

        Retrieves genres relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: genres
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_genres_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsGenresMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def albums_id_relationships_genres_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: genres")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[AlbumsGenresMultiRelationshipDataDocument]:
        """Get genres relationship (\"to-many\").

        Retrieves genres relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: genres
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_genres_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsGenresMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def albums_id_relationships_genres_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: genres")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get genres relationship (\"to-many\").

        Retrieves genres relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: genres
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_genres_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsGenresMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _albums_id_relationships_genres_get_serialize(
        self,
        id,
        country_code,
        include,
        page_cursor,
        share_code,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if country_code is not None:
            
            _query_params.append(('countryCode', country_code))
            
        if include is not None:
            
            _query_params.append(('include', include))
            
        if page_cursor is not None:
            
            _query_params.append(('page[cursor]', page_cursor))
            
        if share_code is not None:
            
            _query_params.append(('shareCode', share_code))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/albums/{id}/relationships/genres',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def albums_id_relationships_items_get(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: items")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> AlbumsItemsMultiRelationshipDataDocument:
        """Get items relationship (\"to-many\").

        Retrieves items relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: items
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items
        :type replace_media: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_items_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsItemsMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def albums_id_relationships_items_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: items")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[AlbumsItemsMultiRelationshipDataDocument]:
        """Get items relationship (\"to-many\").

        Retrieves items relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: items
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items
        :type replace_media: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_items_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsItemsMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def albums_id_relationships_items_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: items")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get items relationship (\"to-many\").

        Retrieves items relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: items
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items
        :type replace_media: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_items_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsItemsMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _albums_id_relationships_items_get_serialize(
        self,
        id,
        country_code,
        include,
        page_cursor,
        replace_media,
        share_code,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if country_code is not None:
            
            _query_params.append(('countryCode', country_code))
            
        if include is not None:
            
            _query_params.append(('include', include))
            
        if page_cursor is not None:
            
            _query_params.append(('page[cursor]', page_cursor))
            
        if replace_media is not None:
            
            _query_params.append(('replaceMedia', replace_media))
            
        if share_code is not None:
            
            _query_params.append(('shareCode', share_code))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/albums/{id}/relationships/items',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def albums_id_relationships_items_patch(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        albums_items_relationship_update_operation_payload: Optional[AlbumsItemsRelationshipUpdateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> MutationResponseDocument:
        """Update items relationship (\"to-many\").

        Incrementally updates one existing track's 1-based track number to meta.positionIndex. Does not replace the album's items or add or remove tracks. Empty data is rejected. A COLLABORATOR on the album may reorder. Returns an acknowledgement.

        :param id: Album id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param albums_items_relationship_update_operation_payload:
        :type albums_items_relationship_update_operation_payload: AlbumsItemsRelationshipUpdateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_items_patch_serialize(
            id=id,
            idempotency_key=idempotency_key,
            share_code=share_code,
            albums_items_relationship_update_operation_payload=albums_items_relationship_update_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def albums_id_relationships_items_patch_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        albums_items_relationship_update_operation_payload: Optional[AlbumsItemsRelationshipUpdateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[MutationResponseDocument]:
        """Update items relationship (\"to-many\").

        Incrementally updates one existing track's 1-based track number to meta.positionIndex. Does not replace the album's items or add or remove tracks. Empty data is rejected. A COLLABORATOR on the album may reorder. Returns an acknowledgement.

        :param id: Album id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param albums_items_relationship_update_operation_payload:
        :type albums_items_relationship_update_operation_payload: AlbumsItemsRelationshipUpdateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_items_patch_serialize(
            id=id,
            idempotency_key=idempotency_key,
            share_code=share_code,
            albums_items_relationship_update_operation_payload=albums_items_relationship_update_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def albums_id_relationships_items_patch_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        albums_items_relationship_update_operation_payload: Optional[AlbumsItemsRelationshipUpdateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Update items relationship (\"to-many\").

        Incrementally updates one existing track's 1-based track number to meta.positionIndex. Does not replace the album's items or add or remove tracks. Empty data is rejected. A COLLABORATOR on the album may reorder. Returns an acknowledgement.

        :param id: Album id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param albums_items_relationship_update_operation_payload:
        :type albums_items_relationship_update_operation_payload: AlbumsItemsRelationshipUpdateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_items_patch_serialize(
            id=id,
            idempotency_key=idempotency_key,
            share_code=share_code,
            albums_items_relationship_update_operation_payload=albums_items_relationship_update_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _albums_id_relationships_items_patch_serialize(
        self,
        id,
        idempotency_key,
        share_code,
        albums_items_relationship_update_operation_payload,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if share_code is not None:
            
            _query_params.append(('shareCode', share_code))
            
        # process the header parameters
        if idempotency_key is not None:
            self.api_client._set_header(_header_params, 'Idempotency-Key', idempotency_key)
        # process the form parameters
        # process the body parameter
        if albums_items_relationship_update_operation_payload is not None:
            _body_params = albums_items_relationship_update_operation_payload


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            self.api_client._set_header(_header_params, 'Content-Type', _content_type)
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/vnd.api+json'
                    ]
                )
            )
            if _default_content_type is not None:
                self.api_client._set_header(_header_params, 'Content-Type', _default_content_type)

        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE'
        ]

        return self.api_client.param_serialize(
            method='PATCH',
            resource_path='/albums/{id}/relationships/items',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def albums_id_relationships_owners_get(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: owners")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> AlbumsOwnersMultiRelationshipDataDocument:
        """Get owners relationship (\"to-many\").

        Retrieves owners relationship.

        :param id: Album id (required)
        :type id: str
        :param include: Include related resources. Available relationships: owners
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_owners_get_serialize(
            id=id,
            include=include,
            page_cursor=page_cursor,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsOwnersMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def albums_id_relationships_owners_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: owners")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[AlbumsOwnersMultiRelationshipDataDocument]:
        """Get owners relationship (\"to-many\").

        Retrieves owners relationship.

        :param id: Album id (required)
        :type id: str
        :param include: Include related resources. Available relationships: owners
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_owners_get_serialize(
            id=id,
            include=include,
            page_cursor=page_cursor,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsOwnersMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def albums_id_relationships_owners_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: owners")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get owners relationship (\"to-many\").

        Retrieves owners relationship.

        :param id: Album id (required)
        :type id: str
        :param include: Include related resources. Available relationships: owners
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_owners_get_serialize(
            id=id,
            include=include,
            page_cursor=page_cursor,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsOwnersMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _albums_id_relationships_owners_get_serialize(
        self,
        id,
        include,
        page_cursor,
        share_code,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if include is not None:
            
            _query_params.append(('include', include))
            
        if page_cursor is not None:
            
            _query_params.append(('page[cursor]', page_cursor))
            
        if share_code is not None:
            
            _query_params.append(('shareCode', share_code))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/albums/{id}/relationships/owners',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def albums_id_relationships_price_config_get(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: priceConfig")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> AlbumsPriceConfigSingleRelationshipDataDocument:
        """Get priceConfig relationship (\"to-one\").

        Retrieves priceConfig relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: priceConfig
        :type include: List[str]
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_price_config_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsPriceConfigSingleRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def albums_id_relationships_price_config_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: priceConfig")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[AlbumsPriceConfigSingleRelationshipDataDocument]:
        """Get priceConfig relationship (\"to-one\").

        Retrieves priceConfig relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: priceConfig
        :type include: List[str]
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_price_config_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsPriceConfigSingleRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def albums_id_relationships_price_config_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: priceConfig")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get priceConfig relationship (\"to-one\").

        Retrieves priceConfig relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: priceConfig
        :type include: List[str]
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_price_config_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsPriceConfigSingleRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _albums_id_relationships_price_config_get_serialize(
        self,
        id,
        country_code,
        include,
        share_code,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if country_code is not None:
            
            _query_params.append(('countryCode', country_code))
            
        if include is not None:
            
            _query_params.append(('include', include))
            
        if share_code is not None:
            
            _query_params.append(('shareCode', share_code))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/albums/{id}/relationships/priceConfig',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def albums_id_relationships_providers_get(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: providers")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> AlbumsProvidersMultiRelationshipDataDocument:
        """Get providers relationship (\"to-many\").

        Retrieves providers relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: providers
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_providers_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsProvidersMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def albums_id_relationships_providers_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: providers")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[AlbumsProvidersMultiRelationshipDataDocument]:
        """Get providers relationship (\"to-many\").

        Retrieves providers relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: providers
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_providers_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsProvidersMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def albums_id_relationships_providers_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: providers")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get providers relationship (\"to-many\").

        Retrieves providers relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: providers
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_providers_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsProvidersMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _albums_id_relationships_providers_get_serialize(
        self,
        id,
        country_code,
        include,
        page_cursor,
        share_code,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if country_code is not None:
            
            _query_params.append(('countryCode', country_code))
            
        if include is not None:
            
            _query_params.append(('include', include))
            
        if page_cursor is not None:
            
            _query_params.append(('page[cursor]', page_cursor))
            
        if share_code is not None:
            
            _query_params.append(('shareCode', share_code))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/albums/{id}/relationships/providers',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def albums_id_relationships_replacement_get(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: replacement")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: replacement")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> AlbumsReplacementSingleRelationshipDataDocument:
        """Get replacement relationship (\"to-one\").

        Retrieves replacement relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: replacement
        :type include: List[str]
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: replacement
        :type replace_media: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_replacement_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            replace_media=replace_media,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsReplacementSingleRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def albums_id_relationships_replacement_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: replacement")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: replacement")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[AlbumsReplacementSingleRelationshipDataDocument]:
        """Get replacement relationship (\"to-one\").

        Retrieves replacement relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: replacement
        :type include: List[str]
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: replacement
        :type replace_media: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_replacement_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            replace_media=replace_media,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsReplacementSingleRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def albums_id_relationships_replacement_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: replacement")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: replacement")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get replacement relationship (\"to-one\").

        Retrieves replacement relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: replacement
        :type include: List[str]
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: replacement
        :type replace_media: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_replacement_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            replace_media=replace_media,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsReplacementSingleRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _albums_id_relationships_replacement_get_serialize(
        self,
        id,
        country_code,
        include,
        replace_media,
        share_code,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if country_code is not None:
            
            _query_params.append(('countryCode', country_code))
            
        if include is not None:
            
            _query_params.append(('include', include))
            
        if replace_media is not None:
            
            _query_params.append(('replaceMedia', replace_media))
            
        if share_code is not None:
            
            _query_params.append(('shareCode', share_code))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/albums/{id}/relationships/replacement',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def albums_id_relationships_shares_get(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: shares")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: shares.sharedResources")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> AlbumsSharesMultiRelationshipDataDocument:
        """Get shares relationship (\"to-many\").

        The album's share links, active and expired, newest first.

        :param id: Album id (required)
        :type id: str
        :param include: Include related resources. Available relationships: shares
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: shares.sharedResources
        :type replace_media: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_shares_get_serialize(
            id=id,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsSharesMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def albums_id_relationships_shares_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: shares")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: shares.sharedResources")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[AlbumsSharesMultiRelationshipDataDocument]:
        """Get shares relationship (\"to-many\").

        The album's share links, active and expired, newest first.

        :param id: Album id (required)
        :type id: str
        :param include: Include related resources. Available relationships: shares
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: shares.sharedResources
        :type replace_media: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_shares_get_serialize(
            id=id,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsSharesMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def albums_id_relationships_shares_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: shares")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: shares.sharedResources")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get shares relationship (\"to-many\").

        The album's share links, active and expired, newest first.

        :param id: Album id (required)
        :type id: str
        :param include: Include related resources. Available relationships: shares
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: shares.sharedResources
        :type replace_media: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_shares_get_serialize(
            id=id,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsSharesMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _albums_id_relationships_shares_get_serialize(
        self,
        id,
        include,
        page_cursor,
        replace_media,
        share_code,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if include is not None:
            
            _query_params.append(('include', include))
            
        if page_cursor is not None:
            
            _query_params.append(('page[cursor]', page_cursor))
            
        if replace_media is not None:
            
            _query_params.append(('replaceMedia', replace_media))
            
        if share_code is not None:
            
            _query_params.append(('shareCode', share_code))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/albums/{id}/relationships/shares',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def albums_id_relationships_similar_albums_get(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: similarAlbums")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: similarAlbums")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> AlbumsSimilarAlbumsMultiRelationshipDataDocument:
        """Get similarAlbums relationship (\"to-many\").

        Retrieves similarAlbums relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: similarAlbums
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: similarAlbums
        :type replace_media: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_similar_albums_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsSimilarAlbumsMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def albums_id_relationships_similar_albums_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: similarAlbums")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: similarAlbums")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[AlbumsSimilarAlbumsMultiRelationshipDataDocument]:
        """Get similarAlbums relationship (\"to-many\").

        Retrieves similarAlbums relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: similarAlbums
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: similarAlbums
        :type replace_media: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_similar_albums_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsSimilarAlbumsMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def albums_id_relationships_similar_albums_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: similarAlbums")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: similarAlbums")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get similarAlbums relationship (\"to-many\").

        Retrieves similarAlbums relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: similarAlbums
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: similarAlbums
        :type replace_media: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_similar_albums_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsSimilarAlbumsMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _albums_id_relationships_similar_albums_get_serialize(
        self,
        id,
        country_code,
        include,
        page_cursor,
        replace_media,
        share_code,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if country_code is not None:
            
            _query_params.append(('countryCode', country_code))
            
        if include is not None:
            
            _query_params.append(('include', include))
            
        if page_cursor is not None:
            
            _query_params.append(('page[cursor]', page_cursor))
            
        if replace_media is not None:
            
            _query_params.append(('replaceMedia', replace_media))
            
        if share_code is not None:
            
            _query_params.append(('shareCode', share_code))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/albums/{id}/relationships/similarAlbums',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def albums_id_relationships_suggested_cover_arts_get(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: suggestedCoverArts")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> AlbumsSuggestedCoverArtsMultiRelationshipDataDocument:
        """Get suggestedCoverArts relationship (\"to-many\").

        Retrieves suggestedCoverArts relationship.

        :param id: Album id (required)
        :type id: str
        :param include: Include related resources. Available relationships: suggestedCoverArts
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_suggested_cover_arts_get_serialize(
            id=id,
            include=include,
            page_cursor=page_cursor,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsSuggestedCoverArtsMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def albums_id_relationships_suggested_cover_arts_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: suggestedCoverArts")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[AlbumsSuggestedCoverArtsMultiRelationshipDataDocument]:
        """Get suggestedCoverArts relationship (\"to-many\").

        Retrieves suggestedCoverArts relationship.

        :param id: Album id (required)
        :type id: str
        :param include: Include related resources. Available relationships: suggestedCoverArts
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_suggested_cover_arts_get_serialize(
            id=id,
            include=include,
            page_cursor=page_cursor,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsSuggestedCoverArtsMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def albums_id_relationships_suggested_cover_arts_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: suggestedCoverArts")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get suggestedCoverArts relationship (\"to-many\").

        Retrieves suggestedCoverArts relationship.

        :param id: Album id (required)
        :type id: str
        :param include: Include related resources. Available relationships: suggestedCoverArts
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_suggested_cover_arts_get_serialize(
            id=id,
            include=include,
            page_cursor=page_cursor,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsSuggestedCoverArtsMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _albums_id_relationships_suggested_cover_arts_get_serialize(
        self,
        id,
        include,
        page_cursor,
        share_code,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if include is not None:
            
            _query_params.append(('include', include))
            
        if page_cursor is not None:
            
            _query_params.append(('page[cursor]', page_cursor))
            
        if share_code is not None:
            
            _query_params.append(('shareCode', share_code))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/albums/{id}/relationships/suggestedCoverArts',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def albums_id_relationships_usage_rules_get(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: usageRules")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> AlbumsUsageRulesSingleRelationshipDataDocument:
        """Get usageRules relationship (\"to-one\").

        Retrieves usageRules relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: usageRules
        :type include: List[str]
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_usage_rules_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsUsageRulesSingleRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def albums_id_relationships_usage_rules_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: usageRules")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[AlbumsUsageRulesSingleRelationshipDataDocument]:
        """Get usageRules relationship (\"to-one\").

        Retrieves usageRules relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: usageRules
        :type include: List[str]
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_usage_rules_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsUsageRulesSingleRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def albums_id_relationships_usage_rules_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Album id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: usageRules")] = None,
        share_code: Annotated[Optional[StrictStr], Field(description="Share code used as a bearer credential for the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get usageRules relationship (\"to-one\").

        Retrieves usageRules relationship.

        :param id: Album id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: usageRules
        :type include: List[str]
        :param share_code: Share code used as a bearer credential for the resource.
        :type share_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_id_relationships_usage_rules_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            share_code=share_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AlbumsUsageRulesSingleRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _albums_id_relationships_usage_rules_get_serialize(
        self,
        id,
        country_code,
        include,
        share_code,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if country_code is not None:
            
            _query_params.append(('countryCode', country_code))
            
        if include is not None:
            
            _query_params.append(('include', include))
            
        if share_code is not None:
            
            _query_params.append(('shareCode', share_code))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/albums/{id}/relationships/usageRules',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def albums_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        albums_create_operation_payload: Optional[AlbumsCreateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> AlbumsCreateSingleResourceDataDocument:
        """Create single album.

        Creates an uploaded album. Album creation is not atomic with its artist assignment, so the caller must be OWNER of every listed artist; COLLABORATOR, or a role on an album, is not enough until the album exists.

        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param albums_create_operation_payload:
        :type albums_create_operation_payload: AlbumsCreateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_post_serialize(
            idempotency_key=idempotency_key,
            albums_create_operation_payload=albums_create_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "AlbumsCreateSingleResourceDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def albums_post_with_http_info(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        albums_create_operation_payload: Optional[AlbumsCreateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[AlbumsCreateSingleResourceDataDocument]:
        """Create single album.

        Creates an uploaded album. Album creation is not atomic with its artist assignment, so the caller must be OWNER of every listed artist; COLLABORATOR, or a role on an album, is not enough until the album exists.

        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param albums_create_operation_payload:
        :type albums_create_operation_payload: AlbumsCreateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_post_serialize(
            idempotency_key=idempotency_key,
            albums_create_operation_payload=albums_create_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "AlbumsCreateSingleResourceDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def albums_post_without_preload_content(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        albums_create_operation_payload: Optional[AlbumsCreateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Create single album.

        Creates an uploaded album. Album creation is not atomic with its artist assignment, so the caller must be OWNER of every listed artist; COLLABORATOR, or a role on an album, is not enough until the album exists.

        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param albums_create_operation_payload:
        :type albums_create_operation_payload: AlbumsCreateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._albums_post_serialize(
            idempotency_key=idempotency_key,
            albums_create_operation_payload=albums_create_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "AlbumsCreateSingleResourceDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _albums_post_serialize(
        self,
        idempotency_key,
        albums_create_operation_payload,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if idempotency_key is not None:
            self.api_client._set_header(_header_params, 'Idempotency-Key', idempotency_key)
        # process the form parameters
        # process the body parameter
        if albums_create_operation_payload is not None:
            _body_params = albums_create_operation_payload


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            self.api_client._set_header(_header_params, 'Content-Type', _content_type)
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/vnd.api+json'
                    ]
                )
            )
            if _default_content_type is not None:
                self.api_client._set_header(_header_params, 'Content-Type', _default_content_type)

        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/albums',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


