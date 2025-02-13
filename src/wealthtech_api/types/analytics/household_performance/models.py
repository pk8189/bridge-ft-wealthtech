"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class PostAnalyticsHouseholdPerformanceResponseItemFive(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_balance: typing.Optional[float] = pydantic.Field(
        alias="current_balance", default=None
    )
    entity_id: typing.Optional[int] = pydantic.Field(alias="entity_id", default=None)
    net_return: typing.Optional[float] = pydantic.Field(
        alias="net_return", default=None
    )


class PostAnalyticsHouseholdPerformanceResponseItemItd(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_balance: typing.Optional[float] = pydantic.Field(
        alias="current_balance", default=None
    )
    entity_id: typing.Optional[int] = pydantic.Field(alias="entity_id", default=None)
    net_return: typing.Optional[float] = pydantic.Field(
        alias="net_return", default=None
    )


class PostAnalyticsHouseholdPerformanceResponseItemItda(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_balance: typing.Optional[float] = pydantic.Field(
        alias="current_balance", default=None
    )
    entity_id: typing.Optional[int] = pydantic.Field(alias="entity_id", default=None)
    net_return: typing.Optional[float] = pydantic.Field(
        alias="net_return", default=None
    )


class PostAnalyticsHouseholdPerformanceResponseItemMtd(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_balance: typing.Optional[float] = pydantic.Field(
        alias="current_balance", default=None
    )
    entity_id: typing.Optional[int] = pydantic.Field(alias="entity_id", default=None)
    net_return: typing.Optional[float] = pydantic.Field(
        alias="net_return", default=None
    )


class PostAnalyticsHouseholdPerformanceResponseItemOne(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_balance: typing.Optional[float] = pydantic.Field(
        alias="current_balance", default=None
    )
    entity_id: typing.Optional[int] = pydantic.Field(alias="entity_id", default=None)
    net_return: typing.Optional[float] = pydantic.Field(
        alias="net_return", default=None
    )


class PostAnalyticsHouseholdPerformanceResponseItemQtd(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_balance: typing.Optional[float] = pydantic.Field(
        alias="current_balance", default=None
    )
    entity_id: typing.Optional[int] = pydantic.Field(alias="entity_id", default=None)
    net_return: typing.Optional[float] = pydantic.Field(
        alias="net_return", default=None
    )


class PostAnalyticsHouseholdPerformanceResponseItemThree(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_balance: typing.Optional[float] = pydantic.Field(
        alias="current_balance", default=None
    )
    entity_id: typing.Optional[int] = pydantic.Field(alias="entity_id", default=None)
    net_return: typing.Optional[float] = pydantic.Field(
        alias="net_return", default=None
    )


class PostAnalyticsHouseholdPerformanceResponseItemYtd(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    current_balance: typing.Optional[float] = pydantic.Field(
        alias="current_balance", default=None
    )
    entity_id: typing.Optional[int] = pydantic.Field(alias="entity_id", default=None)
    net_return: typing.Optional[float] = pydantic.Field(
        alias="net_return", default=None
    )


class PostAnalyticsHouseholdPerformanceResponseItem(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    five: typing.Optional[PostAnalyticsHouseholdPerformanceResponseItemFive] = (
        pydantic.Field(alias="five", default=None)
    )
    itd: typing.Optional[PostAnalyticsHouseholdPerformanceResponseItemItd] = (
        pydantic.Field(alias="itd", default=None)
    )
    itda: typing.Optional[PostAnalyticsHouseholdPerformanceResponseItemItda] = (
        pydantic.Field(alias="itda", default=None)
    )
    mtd: typing.Optional[PostAnalyticsHouseholdPerformanceResponseItemMtd] = (
        pydantic.Field(alias="mtd", default=None)
    )
    one: typing.Optional[PostAnalyticsHouseholdPerformanceResponseItemOne] = (
        pydantic.Field(alias="one", default=None)
    )
    qtd: typing.Optional[PostAnalyticsHouseholdPerformanceResponseItemQtd] = (
        pydantic.Field(alias="qtd", default=None)
    )
    three: typing.Optional[PostAnalyticsHouseholdPerformanceResponseItemThree] = (
        pydantic.Field(alias="three", default=None)
    )
    ytd: typing.Optional[PostAnalyticsHouseholdPerformanceResponseItemYtd] = (
        pydantic.Field(alias="ytd", default=None)
    )
