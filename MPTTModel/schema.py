import graphene
import graphQL.schema


class Query(graphQL.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
