"""MessageSvc message models.

This module is used to define message models.

:Copyright: Copyright (C) 2021-2021  cscs181
:License: AGPL-3.0 or later. See `LICENSE`_ for detail.

.. _LICENSE:
    https://github.com/cscs181/CAI/blob/master/LICENSE
"""

import abc
from typing import List
from dataclasses import dataclass

from cai.client.event import Event


@dataclass
class PrivateMessage(Event):
    seq: int
    time: int
    auto_reply: bool
    from_uin: int
    from_nick: str
    to_uin: int
    message: List["Element"]

    def type(self) -> str:
        return "private_message"


class Element(abc.ABC):
    @property
    @abc.abstractmethod
    def type(self) -> str:
        raise NotImplementedError


@dataclass
class TextElement(Element):
    content: str

    @property
    def type(self) -> str:
        return "text"


@dataclass
class FaceElement(Element):
    id: int

    @property
    def type(self) -> str:
        return "face"


@dataclass
class SmallEmojiElement(Element):
    id: int
    text: str
    # byte: bytes

    @property
    def type(self) -> str:
        return "small_emoji"


@dataclass
class PokeElement(Element):
    id: int
    name: str
    strength: int
    double_hit: int

    @property
    def type(self) -> str:
        return "poke"