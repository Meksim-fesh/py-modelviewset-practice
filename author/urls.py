from django.urls import path

from author import views


author_list = views.AuthorViewSet.as_view(
    actions={
        "get": "list",
        "post": "create",
    }
)

author_detail = views.AuthorViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)


urlpatterns = [
    path("authors/", author_list, name="manage-list"),
    path("authors/<int:pk>/", author_detail, name="author-detail"),
]

app_name = "author"
