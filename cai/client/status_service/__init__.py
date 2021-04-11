"""StatSvc Related SDK.

This module is used to build and handle status service related packet.

:Copyright: Copyright (C) 2021-2021  cscs181
:License: AGPL-3.0 or later. See `LICENSE`_ for detail.

.. _LICENSE:
    https://github.com/cscs181/CAI/blob/master/LICENSE
"""

from enum import Enum, IntEnum
from typing import Union, Optional, TYPE_CHECKING

from jce import types

from .jce import SvcReqRegister
from cai.utils.binary import Packet
from cai.settings.device import get_device
from cai.settings.protocol import get_protocol
from cai.utils.jce import RequestPacketVersion3
from cai.pb.oicq.cmd0x769_pb2 import ConfigSeq, ReqBody
from .event import SvcRegisterResponse, RegisterSuccess, RegisterFail
from cai.client.packet import CSsoBodyPacket, CSsoDataPacket, IncomingPacket

if TYPE_CHECKING:
    from cai.client import Client

DEVICE = get_device()
APK_INFO = get_protocol()


class OnlineStatus(IntEnum):
    """
    Note:
        Source: mqq.app.AppRuntime
    """

    Unknown = 0
    """未知"""
    Online = 11
    """我在线上"""
    Offline = 21
    """离线"""
    Away = 31
    """离开"""
    Invisible = 41
    """隐身"""
    Busy = 50
    """忙碌"""
    Qme = 60
    """Q 我吧"""
    Dnd = 70
    """请勿打扰"""
    ReceiveOfflineMsg = 95
    """离线但接收消息"""

    @classmethod
    def _missing_(cls, value: int) -> "OnlineStatus":
        return OnlineStatus.Unknown


class RegPushReason(str, Enum):
    """
    Note:
        Source: com.tencent.mobileqq.msf.core.push.RegPushReason
    """

    MsfBoot = "msfBoot"
    AppRegister = "appRegister"
    Unknown = "unknown"
    MsfHeartTimeTooLong = "msfHeartTimeTooLong"
    MsfByNetChange = "msfByNetChange"
    ServerPush = "serverPush"
    FillRegProxy = "fillRegProxy"
    CreateDefaultRegInfo = "createDefaultRegInfo"
    SetOnlineStatus = "setOnlineStatus"


# register
def encode_register(
    seq: int,
    session_id: bytes,
    ksid: bytes,
    uin: int,
    tgt: bytes,
    d2: bytes,
    d2key: bytes,
    bid: int,
    status: Union[int, OnlineStatus],
    reg_push_reason: Union[str, RegPushReason],
    battery_status: Optional[int] = None,
    is_power_connected: bool = False,
) -> Packet:
    """Build status service register packet.

    Called in ``com.tencent.mobileqq.msf.core.push.e.a``.

    command name: ``StatSvc.register``

    Note:
        Source: com.tencent.mobileqq.msf.core.push.e.a

    Args:
        seq (int): Packet sequence.
        session_id (bytes): Session ID.
        ksid (bytes): KSID of client.
        uin (int): User QQ number.
        tgt (bytes): Siginfo tgt.
        d2 (bytes): Siginfo d2.
        d2key (bytes): Siginfo d2 key.
        bid (int): register bid. login: 1 | 2 | 4, other: 0.
        status (Union[int, OnlineStatus]): Online status.
        reg_push_reason (Union[str, RegPushReason]): Reg push reason.
        battery_status (Optional[int], optional): Battery capacity.
            Defaults to None.
        is_power_connected (bool, optional): Is power connected to phone.
            Defaults to False.

    Returns:
        Packet: Register packet.
    """
    COMMAND_NAME = "StatSvc.register"
    SUB_APP_ID = APK_INFO.sub_app_id

    assert (
        battery_status is None or 0 <= battery_status <= 100
    ), "Battery Capacity Error!"

    svc = SvcReqRegister(
        uin=uin,
        bid=bid,
        status=int(status),
        ios_version=DEVICE.version.sdk,
        nettype=bytes([1]),
        reg_type=bytes(1)
        if reg_push_reason in (RegPushReason.AppRegister)
        else bytes([1]),
        guid=DEVICE.guid,
        dev_name=DEVICE.model,
        dev_type=DEVICE.model,
        os_version=DEVICE.version.release,
        large_seq=0,
        vendor_name=DEVICE.vendor_name,
        vendor_os_name=DEVICE.vendor_os_name,
        b769_req=ReqBody(
            config_list=[
                ConfigSeq(type=46, version=0),
                ConfigSeq(type=283, version=0),
            ]
        ).SerializeToString(),
        is_set_status=False,
        set_mute=False,
        ext_online_status=1000 if battery_status is None else -1,
        battery_status=0
        if battery_status is None
        else battery_status | (128 if is_power_connected else 0),
    )
    payload = SvcReqRegister.to_bytes(0, svc)
    req_packet = RequestPacketVersion3(
        servant_name="PushService",
        func_name="SvcReqRegister",
        data=types.MAP({types.STRING("SvcReqRegister"): types.BYTES(payload)}),
    ).encode()
    sso_packet = CSsoBodyPacket.build(
        seq,
        SUB_APP_ID,
        COMMAND_NAME,
        DEVICE.imei,
        session_id,
        ksid,
        body=req_packet,
        extra_data=tgt,
    )
    packet = CSsoDataPacket.build(uin, 1, sso_packet, key=d2key, extra_data=d2)
    return packet


async def handle_register_response(
    client: "Client", packet: IncomingPacket
) -> SvcRegisterResponse:
    response = SvcRegisterResponse.decode_response(
        packet.uin,
        packet.seq,
        packet.ret_code,
        packet.command_name,
        packet.data,
    )
    if isinstance(response, RegisterSuccess):
        client._heartbeat_interval = response.response.hello_interval
        client._status = OnlineStatus(response.response.status)
    return response


__all__ = [
    "encode_register",
    "handle_register_response",
    "OnlineStatus",
    "RegPushReason",
    "SvcRegisterResponse",
    "RegisterSuccess",
    "RegisterFail",
]
