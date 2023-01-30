from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .bs_controller import RootIndex


app = FastAPI()


@app.get("/")
async def root(text: str = '', filetype: str = ''):
    ret = []
    if text != '' and filetype != '':
      ri = RootIndex(text, filetype)
      ret = ri.create_results()

    return JSONResponse(content=ret)
