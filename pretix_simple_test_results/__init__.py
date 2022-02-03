from django.utils.translation import gettext_lazy

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")

__version__ = "1.0.0"


class PluginApp(PluginConfig):
    name = "pretix_simple_test_results"
    verbose_name = "Simple Test Results"

    class PretixPluginMeta:
        name = gettext_lazy("Simple Test Results")
        author = "pretix"
        description = gettext_lazy("Simple test result sending")
        visible = True
        version = __version__
        category = "FEATURE"
        compatibility = "pretix>=2.7.0"

    def ready(self):
        from . import signals  # NOQA


default_app_config = "pretix_simple_test_results.PluginApp"
