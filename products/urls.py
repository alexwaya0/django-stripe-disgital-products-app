from django.urls import path

from .views import CreateStripeCheckoutSessionView, StripeWebhookView, CancelView, SuccessView

from .views import (ProductDetailView, ProductListView,)

app_name = "products"

urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product-detail"),

    path("create-checkout-session/<int:pk>/", CreateStripeCheckoutSessionView.as_view(), name="create-checkout-session",),

    path("success/", SuccessView.as_view(), name="success"),
    path("cancel/", CancelView.as_view(), name="cancel"),

    path("webhooks/stripe/", StripeWebhookView.as_view(), name="stripe-webhook"),


]