from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类
from pkg.platform.types import *
import random


# 注册插件
@register(name="LqunLanguage", description="萝群语录", version="1.0.10", author="jianrenjun")
class MyPlugin(BasePlugin):

    # 插件加载时触发
    def __init__(self, host: APIHost):
        pass

    # 异步初始化
    async def initialize(self):
        pass

    # 当收到群消息时触发
    @handler(GroupNormalMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        msg = ctx.event.text_message  # 这里的 event 即为 GroupNormalMessageReceived 的对象
        responses = {
            "查尔斯": ["今晚八点"],
            "机师": MessageChain([
                Plain("死刑"),
                Image(url="https://pic.879818327.xyz/537CB36B9205E0F434167A89A19BF711.jpg"),
            ]),
            "技师": MessageChain([
                Plain("死刑"),
                Image(url="https://pic.879818327.xyz/537CB36B9205E0F434167A89A19BF711.jpg"),
            ]),
            "147": ["查尔斯来我就来"],
            "煎包": ["147来我就来"],
            "老白": ["兵呢？星呢？塔呢？"],
            "Licc": ["我要波你嘴了"],
            "炸鸡": ["够罕见"],
            "明公": ["诈骗犯来喽"],
            "蓝枫": ["老登爆金币"],
            "肚腩": ["该重开了"],
            "千总": ["全都按法来 都完犊子了"],
            "小千": ["全都按法来 都完犊子了"],
            "小千阿姨": ["全都按法来 都完犊子了"],
            "千阿姨": ["全都按法来 都完犊子了"],
            "布衣": ["舔脚"],
            "buyi": ["舔脚"],
            "仓鼠": ["哦哈呦义父"],
            "翼瑾": ["我不玩了,求求你把钱还给我"],
            "遗精": ["我不玩了,求求你把钱还给我"],
            "吕布": ["臭外地的"],
            "老魏": ["我开凯迪拉克创你"],
            "萝莉": ["你的电脑,我来配"],
            "小麦": ["你好,我是小炮,我爱打麦"],
            "小炮": ["你好,我是小炮,我爱打麦"],
        }
        
        if msg in responses:
            ctx.add_return("reply", responses[msg])
            ctx.prevent_default()

        if msg == "下班":
            message_chain = MessageChain([
                Image(url="https://pic.879818327.xyz/A9318B287772F571E62097FE9CB462D2.jpg")
            ])
            ctx.add_return("reply", message_chain)
            ctx.prevent_default()

    # 插件卸载时触发
    def __del__(self):
        pass
