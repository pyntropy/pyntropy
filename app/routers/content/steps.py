from fastapi import APIRouter, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

import os
from pathlib import Path
import markdown
import logging


log_file = '/app/app.log'

if os.path.exists(log_file):
    os.remove(log_file)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app/app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix='/modules/{module_id}')
templates = Jinja2Templates(directory="app/templates")


@ router.get("/steps/{step_id}")
async def get_step(module_id: str, step_id: str, request: Request):
    file_path = Path(f'./app/content/modules/{module_id}/{step_id}.md')

    with open(file_path, 'r') as f:
        logger.info(f.read())

    if not file_path.exists():
        logger.error(f"Step not found: {file_path}")
        raise HTTPException(status_code=404, detail="Step not found")

    try:
        raw_content = file_path.read_text(encoding='utf-8')
        logger.info('ewe')
        html_content = markdown.markdown(raw_content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading step: {str(e)}")

    return templates.TemplateResponse(
        "steps/step.html",
        {"request": request,
         "content": html_content,
         "module": module_id,
         "step": step_id
         }
    )
