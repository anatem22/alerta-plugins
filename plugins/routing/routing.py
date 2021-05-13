def rules(alert, plugins):
    if alert.severity in ['critical', 'major']:
        return [plugins[telegram'], plugins['pagerduty']]
    else:
        return [plugins['rocketchat']]

