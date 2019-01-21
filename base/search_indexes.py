from appmngt.models.application import Application
from appmngt.models.environment import Environment
from appmngt.models.partner import Partner
from appmngt.models.release import Release
from appmngt.models.univers import Univers
from haystack import indexes
from funcmngt.models.funcflow import FuncFlow
from funcmngt.models.funcflow import FuncFlow
from funcmngt.models.subfuncflow import SubFuncFlow
from funcmngt.models.subfuncflow import SubFuncFlow
from techmngt.models.asynchronous import AsynchronousFlow
from techmngt.models.batch import BatchFlow
from techmngt.models.network import NetworkFlow
from techmngt.models.server import Server
from techmngt.models.uri import URIFlow


class BaseMixin(indexes.SearchIndex, indexes.Indexable):
    name = indexes.CharField(model_attr='name')
    description = indexes.CharField(model_attr='description')
    comment = indexes.CharField(model_attr='comment')
    text = indexes.CharField(document=True)

    def get_model(self):
        return self.Meta.model

    class Meta:
        model = None

# APP MNGT
class ApplicationIndex(BaseMixin):
    class Meta:
        model = Application


class EnvironmentIndex(BaseMixin):
    class Meta:
        model = Environment


class PartnerIndex(BaseMixin):
    class Meta:
        model = Partner


class ReleaseIndex(BaseMixin):
    class Meta:
        model = Release


class UniversIndex(BaseMixin):
    class Meta:
        model = Univers


# Func Mngt
class FuncFlowIndex(BaseMixin):
    class Meta:
        model = FuncFlow


class SubFuncFlowIndex(BaseMixin):
    class Meta:
        model = SubFuncFlow


# Tech MNGT

class AsynchronousFlowIndex(BaseMixin):
    class Meta:
        model = AsynchronousFlow


class BatchFlowIndex(BaseMixin):
    class Meta:
        model = BatchFlow


class NetworkFlowIndex(BaseMixin):
    class Meta:
        model = NetworkFlow


class ServerIndex(BaseMixin):
    class Meta:
        model = Server


class URIFlowIndex(BaseMixin):
    class Meta:
        model = URIFlow
