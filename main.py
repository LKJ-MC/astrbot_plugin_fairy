from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import astrbot.api.message_components as Comp

@register("Zenless Zone Zore", "LK", "一个简单的 Fairy 插件", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""
        pass

    @filter.command("zzz")
    async def zzz(self, event: AstrMessageEvent):
        user_name = event.get_sender_name()
        message_chain = event.get_messages()
        logger.info(message_chain)
        yield event.plain_result(f"你好, {user_name}, 绝区零登顶！")

    @filter.command("esu")
    async def esu(self, event: AstrMessageEvent):
        chain = [
            Comp.At(qq=event.get_sender_id()),  # At 消息发送者
            Comp.Plain("来看这个图："),
            Comp.Image.fromFileSystem(
                r"D:\Project\AstrBot\data\plugins\astrbot_plugin_fairy\logo.png"
            ),  # 从本地文件目录发送图片
            Comp.Plain("这是一个图片。"),
        ]
        yield event.chain_result(chain)

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
        pass
