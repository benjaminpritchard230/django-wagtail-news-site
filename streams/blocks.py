"""Streamfields"""
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add additional text")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title and Text"


class CardBlock(blocks.StructBlock):
    """Cards with image text and button"""
    title = blocks.CharBlock(required=True, help_text="Add your title")
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False,
                 help_text="Button page will be used first.")),
            ]
        )
    )

    class Meta:
        template = "streams/card_block.html"
        icon = "edit"
        label = "Cards"


class RichTextBlock(blocks.RichTextBlock):
    """Richtext block with all features"""
    class Meta:
        # template = "streams/rich_text_block.html"
        icon = "edit"
        label = "Full Richtext"


class SimpleRichTextBlock(blocks.RichTextBlock):
    """Richtext without all the features"""
    class Meta:
        template = "streams/rich_text_block.html"
        icon = "edit"
        label = "Simple Richtext"

    def __init__(
        self,
        required=True,
        help_text=None,
        editor="default",
        features=None,
        max_length=None,
        validators=(),
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.features = ["bold"]
