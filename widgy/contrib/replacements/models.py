from django.contrib.sites.models import Site
from django.core.validators import RegexValidator
from fusionbox.behaviors import Timestampable, Publishable
from django.db.models import CharField, ForeignKey

no_curlies_validator = RegexValidator(r'^[^\{\}]+$',
        message='The replacement tag may not contain "}" or "{"')


class Replacement(Timestampable, Publishable):
    """
    """
    site = ForeignKey(Site, related_name='replacements')
    tag = CharField(max_length=255,
            validators=[no_curlies_validator],
            help_text=u'When this text is encountered \
            anywhere on site surrounded by {{ }}, it will be replaced with \
            the replacement text.')

    class Meta:
        verbose_name = 'replacement'
        verbose_name_plural = 'replacements'
        ordering = ('tag',)
