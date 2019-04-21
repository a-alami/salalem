import graphene  
import taskproj.taskapp.schema

class Query(taskproj.taskapp.schema.Query, graphene.ObjectType):  
    pass

schema = graphene.Schema(query=Query)
