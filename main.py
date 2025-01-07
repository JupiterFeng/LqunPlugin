from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类
import random


# 注册插件
@register(name="Dice", description="骰子模拟器", version="0.2", author="jianrenjun")
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
        if msg == "查尔斯":
            ctx.add_return("reply", ["今晚八点"])
            ctx.prevent_default()
        if msg == "机师":
            ctx.add_return("reply", ["死刑"])
            ctx.prevent_default()
        if msg == "147":
            ctx.add_return("reply", ["查尔斯来我就来"])
            ctx.prevent_default()
        if msg == "煎包":
            ctx.add_return("reply", ["147来我就来"])
            ctx.prevent_default()
        if msg == "老白":
            ctx.add_return("reply", ["兵呢？星呢？塔呢？"])
            ctx.prevent_default()
        if msg == "Licc":
            ctx.add_return("reply", ["我要波你嘴了"])
            ctx.prevent_default()
        if msg == "炸鸡":
            ctx.add_return("reply", ["够罕见"])
            ctx.prevent_default()
        if msg == "明公":
            ctx.add_return("reply", ["诈骗犯来喽"])
            ctx.prevent_default()

    # 插件卸载时触发
    def __del__(self):
        pass
