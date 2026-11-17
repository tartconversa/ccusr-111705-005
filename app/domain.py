"""限时快闪的报名窗口和门店状态监测：目录卡片既有数据约定。"""
import re

def interpret_card(item):
    parts = item['summary'].split(' · ', 1)
    if len(parts) != 2:
        raise ValueError('卡片摘要格式无效')
    condition, observation = parts
    found = re.fullmatch(r"(?P<amount>待开放|可报名|候补)", observation)
    if not found:
        raise ValueError('卡片状态未识别')
    amount = found.group('amount')
    return {'kind': 'popup', 'identity': item['id'], 'condition': condition, 'registration': observation, 'state': int(amount) if amount.isdigit() else amount}
