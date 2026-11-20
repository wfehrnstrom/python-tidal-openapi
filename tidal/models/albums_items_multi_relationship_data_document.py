# coding: utf-8

"""
    TIDAL API

    The TIDAL API is a [JSON:API](https://jsonapi.org/)-compliant web API exposing TIDAL's music catalogue, metadata, and user functionality. Guides, authorization documentation, and API key management live at [developer.tidal.com](https://developer.tidal.com).  All endpoints exchange `application/vnd.api+json` documents per the [JSON:API specification](https://jsonapi.org/format/): [resource objects](https://jsonapi.org/format/#document-resource-objects) with `attributes` and `relationships`, [compound documents](https://jsonapi.org/format/#document-compound-documents) via `include`, and standard [error objects](https://jsonapi.org/format/#error-objects).  ### Authentication and authorization  Every request requires an OAuth 2.0 access token in the `Authorization: Bearer` header. Tokens are issued at `https://auth.tidal.com/v1/oauth2/token` via the client-credentials flow (server-to-server) or the authorization-code + PKCE flow (user context; authorize at `https://login.tidal.com/authorize`). Each endpoint documents which flows it accepts, the access tier it requires, and the scopes that apply. Scopes protect private user data: fields you are not authorized to read are redacted from the response rather than causing an error, and resources you cannot access at all behave as if they do not exist. See the [authorization guide](https://developer.tidal.com/documentation/api-sdk/api-sdk-authorization) for details.  ### Common wire types and compatibility  Each property's schema is authoritative for its allowed values, format, requiredness, nullability, and constraints. A standard defines how a value is represented; an individual schema may support only a documented subset.  - **Enums** use `UPPER_CASE_UNDERSCORE`, except JSON:API resource types, which use plural camelCase names such as `playlistGenerationSchedules`. New values can be added to any enum at any time, so treat unknown values as forward-compatible rather than errors. - **Resource IDs** are opaque strings. A few resources document well-known IDs for permanent system singleton instances; compare those IDs by exact value. Never parse, construct, or infer meaning from any other `id`, even when its current representation resembles an integer, UUID, or another recognizable value. Other properties explicitly marked with OpenAPI `format: uuid` are UUIDs. - **Dates and times** use ISO 8601. Date-times use the OpenAPI `date-time` format (`2024-05-01T12:00:00Z`), dates use `YYYY-MM-DD`, and durations use values such as `PT3M5S`. - **Recurrence frequencies** use RFC 5545 `FREQ` names such as `DAILY`, `WEEKLY`, and `MONTHLY`. The property's enum lists the frequencies that field currently supports. - **Weekdays** use `MONDAY` through `SUNDAY`. - **Time zones** use IANA Time Zone Database identifiers such as `Europe/Stockholm`, not abbreviations or raw UTC offsets for recurring civil-time schedules. - **Country codes** use ISO 3166-1 alpha-2; the shared country type also accepts `WW` for worldwide. **Locales** use IETF BCP 47 language tags such as `en-US`. - **Currencies** use ISO 4217 codes. Monetary amounts are decimal strings; each field defines its sign and precision constraints. - **Colors** use three- or six-digit hexadecimal strings (`#RGB` or `#RRGGBB`). Resource links to external URLs use JSON:API link objects with an `href` member.  ### Resource identifiers  Where supported, `filter[subject]=tracks:123` matches a related resource by type and ID; `filter[subject.id]=123` and `filter[subject.type]=tracks` match either component. Where multiple identifiers are accepted, comma-separated values match any complete pair. When a member path names a to-many relationship, at least one related resource must match; filtering does not trim that relationship. On collection and to-many relationship reads, the reserved root `self` (`filter[self]=tracks:123`) filters primary data itself. Each endpoint lists its supported filters and types.  Where supported, `me` aliases the authenticated user's dedicated resource ID for the referenced resource type. It works in paths, resource-ID filters, compact identifiers (`type:me`), resource PATCH primary IDs and standalone relationship mutation identifiers, with the same meaning as the resolved ID. Reads using the alias are `no-store`.  ### Relationships and includes  [Relationships](https://jsonapi.org/format/#document-resource-object-relationships) are returned only on request: [`include`](https://jsonapi.org/format/#fetching-includes) selects linkage and related content, while `includeLinkage` selects authorized linkage only. A relationship that was not requested is absent from the response, not empty. The full set of relationships a resource supports is documented in its schema.  For INTERNAL clients on resource GET endpoints, `includeLinkage` accepts comma-separated direct relationship names, for example `includeLinkage=subject,viewer`. It does not load related resources or add an `included` section. Nested paths and type qualifiers are unsupported. To-many linkage retains its normal pagination and relationship `next` links. Selecting the same relationship with both parameters applies full include behavior and reads the relationship once.  Request related resources in one round trip with `?include=`, a comma-separated list of dot-separated relationship paths — e.g. `include=coverArt,artists.profileArt` on an album. A nested path automatically embeds its intermediate resources: `artists.profileArt` includes the artists as well as their profile art. Include paths are always relative to the request's root resource, also on relationship endpoints. Including a relationship never changes the primary data; the related resources are added to `included`.  Include paths are validated: a path that cannot be resolved against the resources' documented relationships is rejected with `400`. Include trees are also bounded in path depth (default 3 levels) and in the total number of distinct resources they name (default 10); individual endpoints may apply different limits. Both selectors share the include-node limit, counting overlapping roots once. A request exceeding either limit is rejected with `400`, with the effective limit stated in the error.  ### Filtering, sorting, pagination  - [`filter[<memberPath>]=value`](https://jsonapi.org/format/#fetching-filtering) filters primary data by equality. Each endpoint lists its available filters; most collections require at least one. - Where explicitly documented, `filter[<memberPath>][ne]=value` negates the complete equality predicate. When the member path names a to-many relationship, no related ID may match any supplied value; a known-empty relationship matches. Operators are separate from values. Supplied comparisons combine with AND. For a required filter with multiple supported comparisons, at least one must be supplied; the parameter descriptions identify these alternatives. Unsupported operators and groups return `400`. - Where documented, `filter[<path>][<operator>]=value` applies an endpoint-defined operator, such as `filter[self][matchesQuery]`. Its meaning is described per endpoint, and it combines with other filters by AND. - [`sort=<memberPath>`](https://jsonapi.org/format/#fetching-sorting) sorts ascending, `-<memberPath>` descending (`sort=-addedAt`). Filter and sort member paths are relative to primary data. - Parameters an endpoint cannot honor are rejected with `400`: a `filter[...]` parameter the endpoint does not document (the error lists the available filters), or `sort` on an endpoint that documents no sort values. - [Pagination](https://jsonapi.org/format/#fetching-pagination) is cursor-based: responses carry `links.self` and, while more pages exist, `links.next` with an opaque `page[cursor]`. Follow `next` until absent — there are no offset or total-page parameters. Collection sizes, when available, appear as `meta.total` and may be approximate.  ### Type qualifiers  Where a relationship can contain several resource types, a path segment may be prefixed with a concrete type to scope which type's member is accessed. A playlist's `items` are `tracks` or `videos`: `GET /playlists/{id}?include=items.tracks:albums` resolves `albums` only for the items that are tracks. Qualifiers scope member access — they never filter which resources appear in a relationship — and can be chained.  The same syntax applies to `filter` and `sort` member paths on endpoints that support it; where supported, the qualified member is listed among the endpoint's documented filters and sort values. The syntax follows JSON:API proposal [json-api#1695](https://github.com/json-api/json-api/issues/1695).  ### Mutations  - [Partial updates](https://jsonapi.org/format/#crud-updating-resource-attributes) distinguish three wire states for nullable attributes: omission leaves the current value unchanged, an explicit `null` clears it, and a concrete value updates it. - Every mutation accepts an [`Idempotency-Key`](https://www.ietf.org/archive/id/draft-ietf-httpapi-idempotency-key-header-07.html) header. Keys are scoped to the client and the authenticated user. Once the original request has completed, retrying it with the same key, method, path, query and payload within one hour replays its response; a retry while it is still processing is rejected with `409`, and the same key with a different method, path, query or payload with `422`. - After a successful write, your own subsequent reads reflect the change; other clients may observe it with a delay.  ### Revisions and concurrent editing  Where supported, `attributes.revision` identifies the resource's documented aggregate state; a separately versioned relationship collection uses document `meta.revision`. Revisions are nonnegative integers that increase when covered state changes. Compare them only within the same identity and scope, preserve the exact value, and never calculate the next revision. Related content, viewer projections and independent sources are not automatically covered. Domain fields named `version`, such as a music edition, are distinct; existing endpoints retain their documented contracts.  Guarded mutations accept the observed value as top-level `meta.expectedRevision`. Each operation declares its scope and whether the precondition is required. A mismatch returns `409`; missing required input returns `400`. Refresh and reconcile after a conflict, then submit a new operation with a new idempotency key. An identical retry with the original key replays a recorded success under the idempotency contract. These revisions are not HTTP ETags.  Returned revisions describe observed snapshots, not reservations for later writes. Background changes can advance them immediately after a successful response.  ### Media resource replacements - BETA Internal only  Media resources (`tracks`, `videos`, and `albums`) can become unavailable in a country when licensing rights change. By default, TIDAL API returns the resource identifiers originally stored in a collection. This keeps ordinary reads predictable and consistent.  If a stored media resource is unavailable for the effective country, TIDAL may identify a contextually applicable alternative that is available there. Replacement is best effort, so an alternative is not always available. Replacement never changes the stored collection.  TIDAL API provides two ways to work with replacements:  1. **Inspect the `replacement` relationship.** A media resource can expose its applicable alternative through the `replacement` relationship. Include this relationship when a client needs both the original and replacement identifiers or wants to decide whether to use the replacement.  2. **Apply replacements with `replaceMedia`.** Clients can use `replaceMedia` to substitute applicable replacements directly into selected relationship data. The parameter accepts relationship paths using the same syntax as `include`. Projection affects only the response and preserves relationship order and metadata. Each identifier includes `meta.replacement` describing whether it was `ORIGINAL`, `REPLACED`, or `NOT_REPLACED`.  For example, `GET /playlists/{id}?include=items&replaceMedia=items` applies replacements to media identifiers in the playlist's `items` relationship.  ### Compression  Responses are gzip-compressed when the request includes `Accept-Encoding: gzip` (bodies over 2 KB).  ### Deprecation  Deprecated endpoints, parameters, and fields are marked `deprecated` in this specification, with the replacement noted in their description. Deprecated functionality keeps working for at least six months after being marked, and is only removed once a replacement is generally available.

    The version of the OpenAPI document: 1.10.254
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from tidal.models.albums_items_resource_identifier import AlbumsItemsResourceIdentifier
from tidal.models.links import Links
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AlbumsItemsMultiRelationshipDataDocument(BaseModel):
    """
    Target resource types: `tracks`, `videos`.
    """ # noqa: E501
    data: Optional[List[AlbumsItemsResourceIdentifier]] = None
    included: Optional[List[IncludedInner]] = None
    links: Links
    __properties: ClassVar[List[str]] = ["data", "included", "links"]

    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(to_jsonable_python(self.to_dict()))

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AlbumsItemsMultiRelationshipDataDocument from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item_data in self.data:
                _items.append(_item_data.to_dict() if _item_data is not None else None)
            _dict['data'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in included (list)
        _items = []
        if self.included:
            for _item_included in self.included:
                _items.append(_item_included.to_dict() if _item_included is not None else None)
            _dict['included'] = _items
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AlbumsItemsMultiRelationshipDataDocument from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "data": [AlbumsItemsResourceIdentifier.from_dict(_item) for _item in obj["data"]] if obj.get("data") is not None else None,
            "included": [IncludedInner.from_dict(_item) for _item in obj["included"]] if obj.get("included") is not None else None,
            "links": Links.from_dict(obj["links"]) if obj.get("links") is not None else None
        })
        return _obj

from tidal.models.included_inner import IncludedInner
# TODO: Rewrite to not use raise_errors
AlbumsItemsMultiRelationshipDataDocument.model_rebuild(raise_errors=False)

