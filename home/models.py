from django.db import models

from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet


class HomePage(Page):
    banner_title = models.CharField(max_length=100, default="Homepage")

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
    ]
