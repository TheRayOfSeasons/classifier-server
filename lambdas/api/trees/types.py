import graphene

from database import DATABASE_CONNECTION

from .services import TREE_SERVICE


class Tree(graphene.ObjectType):
    """
    """

    name = graphene.String()

    def resolve_name(root, info):
        return TREE_SERVICE.retrieve_values('name')
