from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from fastapi_graphql.graphql.schema import schema

app = FastAPI(title="Email GraphQL API")

graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
def root():
    return {"message": "Email GraphQL API running"}
