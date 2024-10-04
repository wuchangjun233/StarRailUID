from PIL import Image
from gsuid_core.sv import SV
from gsuid_core.bot import Bot
from gsuid_core.models import Event
from gsuid_core.logger import logger
from gsuid_core.help.utils import register_help

from ..utils.sr_prefix import PREFIX
from .get_help import ICON, get_help

sv_sr_help = SV("sr帮助")


@sv_sr_help.on_fullmatch(f"{PREFIX}帮助")
async def send_help_img(bot: Bot, ev: Event):
    logger.info("开始执行[sr帮助]")
    im = await get_help()
    await bot.send(im)

register_help('StarRailUID', f'{PREFIX}帮助', Image.open(ICON))
