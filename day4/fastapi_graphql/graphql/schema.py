import strawberry
from fastapi_graphql.services.email_service import send_email

@strawberry.type
class Query:
    @strawberry.field
    def health(self) -> str:
        return "GraphQL API is running"


@strawberry.type
class Mutation:

    @strawberry.mutation
    def sendEmail(
        self,
        to_email: str,
        subject: str,
        body: str
    ) -> str:
        send_email(to_email, subject, body)
        return "Email sent successfully"

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)
