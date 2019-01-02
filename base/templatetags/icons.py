from django import template

register = template.Library()


@register.filter
def get_icon(label):
    icons = {
        "about": "fas fa-info-circle",
        "actions": "fas fa-hand-spock",
        "add": "fas fa-plus",
        "admin": "fas fa-unlock-alt",
        "application": "fas fa-mobile-alt",
        "async. flow": "far fa-file",
        "batch": "fas fa-sync-alt",
        "change password": "fas fa-key",
        "comment": "far fa-comment",
        "create": "far fa-edit",
        "csv": "fas fa-file-csv",
        "delete": "far fa-trash-alt",
        "disconnect": "fas fa-stop",
        "edit": "far fa-edit",
        "environment": "fas fa-leaf",
        "export": "fas fa-file-export",
        "filter": "fas fa-filter",
        "functional flow": "fas fa-stream",
        "history": "fas fa-history",
        "let me in": "fas fa-play",
        "network": "fas fa-network-wired",
        "partner": "fas fa-hands-helping",
        "release": "fas fa-code-branch",
        "requester": "fas fa-sign-out-alt",
        "receiver": "fas fa-sign-in-alt",
        "server": "fas fa-server",
        "sub functional flows":"fas fa-arrows-alt-h",
        "submit": "far fa-edit",
        "univers": "fas fa-globe",
        "uri": "fas fa-cloud",
        "view": "far fa-eye",
        "xls": "fas fa-file-excel",
    }
    label = label.lower()

    if label in icons:
        return icons[label]
    if label[:-1] in icons:
        return icons[label[:-1]]
    if label[:-2] in icons:
        return icons[label[:-2]]
    return None
