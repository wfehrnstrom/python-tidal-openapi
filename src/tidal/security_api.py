# coding: utf-8

from typing import List

from fastapi import Depends, Security  # noqa: F401
from fastapi.openapi.models import OAuthFlowImplicit, OAuthFlows  # noqa: F401
from fastapi.security import (  # noqa: F401
    HTTPAuthorizationCredentials,
    HTTPBasic,
    HTTPBasicCredentials,
    HTTPBearer,
    OAuth2,
    OAuth2AuthorizationCodeBearer,
    OAuth2PasswordBearer,
    SecurityScopes,
)
from fastapi.security.api_key import APIKeyCookie, APIKeyHeader, APIKeyQuery  # noqa: F401

from tidal.models.extra_models import TokenModel

oauth2_code = OAuth2AuthorizationCodeBearer(
    authorizationUrl="https://login.tidal.com/authorize",
    tokenUrl="https://auth.tidal.com/v1/oauth2/token",
    refreshUrl="",
    scopes={
        "collection.read": "Read access to a user&#39;s \&quot;My Collection\&quot;.",
        "collection.write": "Write access to a user&#39;s \&quot;My Collection\&quot;.",
        "entitlements.read": "Read access to what functionality a user is entitled to access on TIDAL, such as whether they can stream music, use DJ add-ons and similar.",
        "playback": "Required to play media content and control playback.",
        "playlists.read": "Required to list playlists created by a user.",
        "playlists.write": "Write access to a user&#39;s playlists.",
        "r_usr": "Read access to all end user data",
        "recommendations.read": "Read access to a user’s personal recommendations.",
        "search.read": "Required to read personalized search results.",
        "search.write": "Required to update personalized search results, e.g. delete search history.",
        "user.read": "Read access to a user&#39;s account information, such as country and email address.",
        "w_usr": "Write user",
    }
)


def get_token_Authorization_Code_PKCE(
    security_scopes: SecurityScopes, token: str = Depends(oauth2_code)
) -> TokenModel:
    """
    Validate and decode token.

    :param token Token provided by Authorization header
    :type token: str
    :return: Decoded token information or None if token is invalid
    :rtype: TokenModel | None
    """

    ...


def validate_scope_Authorization_Code_PKCE(
    required_scopes: SecurityScopes, token_scopes: List[str]
) -> bool:
    """
    Validate required scopes are included in token scope

    :param required_scopes Required scope to access called API
    :type required_scopes: List[str]
    :param token_scopes Scope present in token
    :type token_scopes: List[str]
    :return: True if access to called API is allowed
    :rtype: bool
    """

    return False



def get_token_Client_Credentials(
    security_scopes: SecurityScopes, token: str = Depends(oauth2_)
) -> TokenModel:
    """
    Validate and decode token.

    :param token Token provided by Authorization header
    :type token: str
    :return: Decoded token information or None if token is invalid
    :rtype: TokenModel | None
    """

    ...


def validate_scope_Client_Credentials(
    required_scopes: SecurityScopes, token_scopes: List[str]
) -> bool:
    """
    Validate required scopes are included in token scope

    :param required_scopes Required scope to access called API
    :type required_scopes: List[str]
    :param token_scopes Scope present in token
    :type token_scopes: List[str]
    :return: True if access to called API is allowed
    :rtype: bool
    """

    return False

