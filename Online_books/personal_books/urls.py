from django.urls import path
from .views import (home, add
                    )

app_name = "personal_books"

urlpatterns = [
    path('', home, name='home'),
    path("add/", add, name='add'),
    # path('subscribe/',subscribe,name='subscribe'),
    # path('custom/',custom,name="custom")
    # path('checkout/', CheckoutView.as_view(), name='checkout'),
    # path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    # path('product/<slug>/', ItemDetailView.as_view(), name='product'),

]
