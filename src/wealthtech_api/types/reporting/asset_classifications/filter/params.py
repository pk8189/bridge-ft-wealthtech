"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostReportingAssetClassificationsFilterBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    class_tag_id: typing_extensions.NotRequired[int]
    created_by_user_id: typing_extensions.NotRequired[int]
    firm_id: typing_extensions.NotRequired[int]
    id: typing_extensions.NotRequired[int]
    security_id: typing_extensions.NotRequired[int]


class _SerializerPostReportingAssetClassificationsFilterBody(pydantic.BaseModel):
    """
    Serializer for PostReportingAssetClassificationsFilterBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    class_tag_id: typing.Optional[int] = pydantic.Field(
        alias="class_tag_id", default=None
    )
    created_by_user_id: typing.Optional[int] = pydantic.Field(
        alias="created_by_user_id", default=None
    )
    firm_id: typing.Optional[int] = pydantic.Field(alias="firm_id", default=None)
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    security_id: typing.Optional[int] = pydantic.Field(
        alias="security_id", default=None
    )
