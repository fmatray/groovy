"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'base.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from grappelli.dashboard import modules, Dashboard

class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard
    """

    def init_with_context(self, context):
        self.children.append(modules.Group(
            title='Application Management',
            column=1,
            collapsible=True,
            children=[
                modules.ModelList('',
                    column=1,
                    models=('appmngt.models.univers.Univers',
                            'appmngt.models.partner.Partner',
                            'appmngt.models.application.Application',
                            'appmngt.models.environment.Environment',
                            'appmngt.models.release.Release',
                            ),
                )
            ]
        ))

        self.children.append(modules.Group(
            title="Functional Management",
            column=1,
            collapsible=True,
            children=[
                modules.ModelList('',
                    column=1,
                    models=('funcmngt.models.*',),
                )
            ]
        ))
        self.children.append(modules.Group(
            title="Technical Management",
            column=1,
            collapsible=True,
            children=[
                modules.ModelList('',
                    column=1,
                    models=('techmngt.models.techflow.TechFlow',
                            'techmngt.models.asynchronous.AsynchronousFlow')),
                modules.ModelList('',
                    column=1,
                    models=(
                            'techmngt.models.server.Server',
                            'techmngt.models.network.NetworkFlow',

                            ),
                )
            ]
        ))

        self.children.append(
                modules.AppList('',
                    column=2,
                    collapsible=False,
                    models=('techmngt.models.protocol.Protocol',
                            'techmngt.models.server.ServerType',
                            )
        ))

        # append a group for "Contacts"
        self.children.append(
                modules.AppList('',
                    column=2,
                    collapsible=False,
                    models=('contactmngt.models.*',),
                )
        )
        # append a group for "Quick links"
        self.children.append(
                modules.AppList('',
                    column=2,
                    collapsible=False,
                    models=('base.models.QuickLink',),
                )
        )
        # append a group for "Administration"
        self.children.append(
                modules.AppList('',
                    column=2,
                    collapsible=False,
                    models=(

                        'django.contrib.*',),
                )
        )
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=20,
            collapsible=False,
            column=2,
        ))


