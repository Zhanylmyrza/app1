# # from django.db.models import Q
# from goods.models import Product
# from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector


# def q_search(query):

#     if query.isdigit() and len(query) <= 5:
#         return Product.objects.filter(id=int(query))

#     vector = SearchVector("name", "description")
#     query = SearchQuery("query")

#     return (
#         Product.objects.annotate(rank=SearchRank(vector, query))
#         .filter(rank__gt=0)
#         .order_by("-rank")
#     )

#     # return Product.objects.filter(description__search=query)
#     # keywords = [word for word in query.split() if len(word) > 2]
#     # q_objects = Q()

#     # for token in keywords:
#     #     q_objects |= Q(description__icontains=token)
#     #     q_objects |= Q(name__icontains=token)

#     # return Product.objects.filter(q_objects)


from goods.models import Product
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector


def q_search(query):
    # Проверка, является ли query числом и не превышает 5 символов
    if query.isdigit() and len(query) <= 5:
        return Product.objects.filter(id=int(query))

    # Создание вектора и запроса для поиска
    vector = SearchVector("name", "description")
    search_query = SearchQuery(query)  # Используйте реальный текст запроса

    return (
        Product.objects.annotate(rank=SearchRank(vector, search_query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )
