"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostReportingTargetAllocationsFilterBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    firm_id: typing_extensions.NotRequired[int]
    id: typing_extensions.NotRequired[int]
    name: typing_extensions.NotRequired[str]
    slug: typing_extensions.NotRequired[str]


class _SerializerPostReportingTargetAllocationsFilterBody(pydantic.BaseModel):
    """
    Serializer for PostReportingTargetAllocationsFilterBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    firm_id: typing.Optional[int] = pydantic.Field(alias="firm_id", default=None)
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    slug: typing.Optional[str] = pydantic.Field(alias="slug", default=None)
