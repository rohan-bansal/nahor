import graphene

import shortener.schema


class Query(shortener.schema.Query, graphene.ObjectType):
    pass

class Mutation(shortener.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)