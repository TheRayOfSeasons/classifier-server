import graphene


class DoerOfActionInterface(graphene.Interface):
    created_by = graphene.Integer()
    modifed_by = graphene.Integer()


class TimeStampedInterface(graphene.Interface):
    pass
