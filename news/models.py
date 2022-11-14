from django.db import models

from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class NewsPage(Page):
    banner_title = models.CharField(max_length=100, default="News page")
    banner_image = models.ForeignKey(
        "wagtailimages.image",
        null=True, blank="False",
        on_delete=models.SET_NULL,
        related_name="+",
    )
    introduction = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("introduction"),
        FieldPanel("banner_image"),
    ]
