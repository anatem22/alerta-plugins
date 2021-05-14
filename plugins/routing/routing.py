#def rules(alert, plugins):
#    if alert.severity in ['critical', 'major']:
#        return [plugins['telegram']]
#    else:
#        return [plugins['rocketchat']]
"""
Example Routing Rules Plugin - Customer-based Escalation/Notification
Use different notification paths for different customers. ie. PagerDuty
for Tier 1 customers, Slack for Tier 2 and nothing for Tier 3 customers.
"""

TIER_ONE_CUSTOMERS = [
    'critical',
    'major'
]

TIER_TWO_CUSTOMERS = [
    'minor',
    'warning'
]


def rules(alert, plugins):

    if alert.group in TIER_ONE_CUSTOMERS:
        return [
            plugins['telegram']
        ]
    elif alert.group in TIER_TWO_CUSTOMERS:
        return [
            plugins['rocketchat']
        ]
    else:
        return [
            plugins['reject']
        ]
