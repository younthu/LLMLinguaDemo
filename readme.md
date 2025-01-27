1. `conda create --name fireman_ai python=3.10`
1. `conda activate fireman_ai`
1. `pip install -r requirements.txt`
1. `uvicorn main:app --reload`
1. http://127.0.0.1:8000/docs, FastAPI 默认的 Swagger UI.
1. http://127.0.0.1:8000/redoc, Redoc 是一个开源工具，用于将 OpenAPI 规范（以前称为 Swagger 规范）转换为美观、交互式且易于阅读的 API 文档。