from enum import Enum
from ..models import DakaUser


class UserInfo(Enum):
    users = DakaUser.objects.filter(enable=True).all().values()
    
    vpn = False # 经过VPN，默认为不经过
    auto_vpn = False # 若上项设置为不经过，当学校封网时，自动切换为经过VPN
