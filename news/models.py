from django.db import models

from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    StreamFieldPanel,
    PageChooserPanel,
)
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from django.db import models

from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet


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


class ArticlePage(Page):
    headline = models.CharField(max_length=100, default="Headline")
    main_image = models.ForeignKey(
        "wagtailimages.image",
        null=True, blank="False",
        on_delete=models.SET_NULL,
        related_name="+",
    )
    article_body = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("headline"),
        FieldPanel("main_image"),
        FieldPanel("article_body"),
        MultiFieldPanel([
            InlinePanel("article_authors", label="Author",
                        min_num=1, max_num=4)
        ], heading="Author(s)")
    ]


class ArticleAuthor(models.Model):
    """Article author for snippets"""
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    image = models.ForeignKey(
        "wagtailimages.image", on_delete=models.SET_NULL, null=True, blank=False, related_name="+")

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                FieldPanel("position"),
                FieldPanel("image"),
            ],
            heading="Name and image",
        ),
        MultiFieldPanel(
            [
                FieldPanel("website"),
            ],
            heading="Links")
    ]

    def __str__(self):
        """String representation of this class"""
        return self.name

    class Meta:
        verbose_name = "Article Author"
        verbose_name_plural = "Article Authors"


register_snippet(ArticleAuthor)


class ArticleAuthorOrderable(Orderable):
    """Allows us to select one or more blog authors from snippets."""
    page = ParentalKey("news.ArticlePage", related_name="article_authors", )
    author = models.ForeignKey(
        "news.ArticleAuthor",
        on_delete=models.CASCADE,
    )
    panels = [
        SnippetChooserPanel("author"),
    ]
