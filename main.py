from typing import Literal
from utils.logger import logger
from exchange_index_list import IndexData
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

ORIGINS_LIST = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS_LIST,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"data": "The main page will be implemented later!"}


@app.get("/index/{exchange_index_name}")
async def get_index_list(exchange_index_name: Literal["NSENifty", "BSESensex"]):
    try:
        logger.info(f"Exchange and Index:{exchange_index_name}")
        index_data = IndexData(index_name=exchange_index_name).get_index_data()
        logger.info(f"Index Data Length:{len(index_data)}")
        return {"data": index_data}
    except Exception as exp:
        logger.exception(exp)
        raise HTTPException(status_code=400, detail="Index List Not Found")


@app.get("/index/{exchange_index_name}/company/{company_name}")
async def get_company_index_data(
    exchange_index_name: Literal["NSENifty", "BSESensex"],
    company_name: str
):
    try:
        logger.info(f"Exchange and Index:{exchange_index_name}::Company Name:{company_name}")
        index_data = IndexData(index_name=exchange_index_name).get_index_data()
        logger.info(f"Index Data:{index_data}")
        matching_companies = []
        for company_data in index_data:
            if company_name.lower() in company_data["companyName"].lower():
                logger.info(f"CompanyName: {company_data['companyName']}")
                matching_companies.append(company_data)
        return {"data": matching_companies}
    except Exception as exp:
        logger.exception(exp)
        raise HTTPException(status_code=400, detail="Unable to find company in index")
