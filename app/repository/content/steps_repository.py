from app.models.step import Step
import markdown
from app.app_logger import logger
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.fenced_code import FencedCodeExtension


def get_steps():
    """

    :return: объект урока с метаданными и содержанием.
    """
    with open("app/content/fastapi_basics/step_01.md", "r") as f:
        md_content = f.read()
        html_content = markdown.markdown(
            md_content,
            extensions=[
                FencedCodeExtension(),  # для ``` code blocks
                CodeHiliteExtension(  # для подсветки синтаксиса
                    pygments_style="monokai",
                    noclasses=False,
                    linenums=False
                )
            ]
        )

    return Step(
            title="test",
            content=html_content
    )