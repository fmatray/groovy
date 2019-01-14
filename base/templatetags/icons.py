from django import template

from appmngt.models.application import Application
from appmngt.models.environment import Environment
from appmngt.models.partner import Partner
from appmngt.models.release import Release
from appmngt.models.univers import Univers
from funcmngt.models.funcflow import FuncFlow
from funcmngt.models.subfuncflow import SubFuncFlow
from techmngt.models.asynchronous import AsynchronousFlow
from techmngt.models.batch import BatchFlow
from techmngt.models.network import NetworkFlow
from techmngt.models.server import Server
from techmngt.models.uri import URIFlow
from contactmngt.models import Team, Person
register = template.Library()


@register.filter
def get_model_icon(label):
    models = [Application, Environment, Partner, Release, Univers,
              FuncFlow, SubFuncFlow,
              AsynchronousFlow, BatchFlow, NetworkFlow, URIFlow, Server,
              Team, Person]
    for model in models:
        if label.lower() == model.__name__.lower():
            return model.icon
    return None

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
        "contact": "far fa-address-book",
        "create": "far fa-edit",
        "delete": "far fa-trash-alt",
        "disconnect": "fas fa-stop",
        "edit": "far fa-edit",
        "environment": "fas fa-leaf",
        "export": "fas fa-file-export",
        "filter": "fas fa-filter",
        "functional flow": "fas fa-stream",
        "history": "fas fa-history",
        "output flow": "fas fa-sign-out-alt",
        "input flow": "fas fa-sign-in-alt",
        "let me in": "fas fa-play",
        "network": "fas fa-network-wired",
        "network flow": "fas fa-network-wired",
        "partner": "fas fa-hands-helping",
        "release": "fas fa-code-branch",
        "requester": "fas fa-sign-out-alt",
        "receiver": "fas fa-sign-in-alt",
        "server": "fas fa-server",
        "source server": "fas fa-sign-out-alt",
        "destination server": "fas fa-sign-in-alt",
        "sub functional flow": "fas fa-arrows-alt-h",
        "submit": "far fa-edit",
        "techincal flow": "fas fa-wrench",
        "univers": "fas fa-globe",
        "uri": "fas fa-cloud",
        "view": "far fa-eye",
        "team": "fas fa-users",
        "person": "fas fa-user"
    }

    label = label.lower()
    if label in icons:
        return icons[label]
    if label[:-1] in icons:
        return icons[label[:-1]]
    if label[:-2] in icons:
        return icons[label[:-2]]
    return None
