from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import astrbot.api.message_components as Comp

@register("Zenless Zone Zore", "LK", "一个简单的 Fairy 插件", "1.0.0")
class FairyPlugin(Star):
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

    @filter.command("image") # 注册一个 /image 指令，接收 text 参数。
    async def on_aiocqhttp(self, event: AstrMessageEvent, text: str):
        url = await self.text_to_image(text) # text_to_image() 是 Star 类的一个方法。
        # path = await self.text_to_image(text, return_url = False) # 如果你想保存图片到本地
        yield event.image_result(url)

    @filter.command("fakechat")
    async def fakechat(self, event: AstrMessageEvent, uin: int, name: str, text: str):
        from astrbot.api.message_components import Node, Plain, Image
        node = Node(
            uin=uin, name=name, content=[Plain(text)]
        )
        node2 = Node(uin=uin, name=name, content=[Plain("测试")])
        yield event.chain_result([node, node2])

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
        pass
