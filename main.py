from fastapi import FastAPI
from sqlalchemy import text
from app.controllers.product_controller import router as product_router
from app.controllers.categoria_controller import router as categoria_router
from app.controllers.subcategory_controller import router as subcategory_router
from app.controllers.role_controller import router as role_router
from app.controllers.user_controller import router as user_router
from app.controllers.order_controller import router as order_router
from app.controllers.cart_controller import router as cart_router
from app.controllers.question_controller import router as question_router
from app.controllers.review_controller import router as review_router
from app.connection.database import Base, database

import uvicorn

from app.utils.jwt_middleware import JWTMiddleware
from app.utils.openapi_schema import custom_openapi

app = FastAPI()
app.openapi = lambda: custom_openapi(app)
app.include_router(product_router)
app.include_router(categoria_router)
app.include_router(subcategory_router)
app.include_router(role_router)
app.include_router(user_router)
app.include_router(order_router)
app.include_router(cart_router)
app.include_router(question_router)
app.include_router(review_router)
Base.metadata.create_all(bind=database.engine)  # Criar tabelas no banco de dados
app.add_middleware(JWTMiddleware)

@app.get("/")

def read_root():
    return {"Hello": "World"}

def startup():
    with database.get_session() as db:
        try:
            sql_script = """
                DO
                $$
                DECLARE
                    table_name RECORD;
                BEGIN
                    -- Para cada tabela no schema especificado
                    FOR table_name IN
                        SELECT tablename
                        FROM pg_tables
                        WHERE schemaname = 'public'
                    LOOP
                        -- Gerar e executar o comando de exclusão da tabela
                        EXECUTE 'DROP TABLE public.' || table_name.tablename || ' CASCADE';
                    END LOOP;
                END
                $$;
            """
            db.execute(text(sql_script))
            db.commit()

            # configure_mappers()
            # Base.metadata.create_all(bind=ConnectionPool.get_engine())

            # with open("./resources/script.sql", "r", encoding="utf-8") as file:
            #     sql_file_content = file.read()
            # queries = sql_file_content.split(";")
            # for query in queries:
            #     query.replace("\n", "")
            #     if query.strip():
            #         db.execute(text(query))
            # db.commit()

        finally:
            db.close()

def main():
    # startup()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
if __name__ == "__main__":
    main()
