"""
URL configuration for aicraft project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from aicraft.views import (
    ProductSize, ProductSite, Product,
    Payment, Pattern, Company,
    Comment, Category, Address, AdminGroup, AdminUser
)

router = routers.DefaultRouter()
router.register(r'users', AdminUser.UserViewSet)
router.register(r'groups', AdminGroup.GroupViewSet)
router.register(r'product-sizes', ProductSize.ProductSizeViewSet)
router.register(r'product-sites', ProductSite.ProductSiteViewSet)
router.register(r'products', Product.ProductViewSet)
router.register(r'payments', Payment.PaymentViewSet)
router.register(r'patterns', Pattern.PatternViewSet)
router.register(r'companies', Company.CompanyViewSet)
router.register(r'comments', Comment.CommentViewSet)
router.register(r'categories', Category.CategoryViewSet)
router.register(r'addresses', Address.AddressViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += router.urls


# router = SimpleRouter()
#
# router.register(r'users', AdminUser.UserViewSet, basename='user')
# router.register(r'groups', AdminGroup.GroupViewSet, basename='group')
# router.register(r'product-sizes', ProductSize.ProductSizeViewSet, basename='product-size')
# router.register(r'product-sites', ProductSite.ProductSiteViewSet, basename='product-site')
# router.register(r'products', Product.ProductViewSet, basename='product')
# router.register(r'payments', Payment.PaymentViewSet, basename='payment')
# router.register(r'patterns', Pattern.PatternViewSet, basename='pattern')
# router.register(r'companies', Company.CompanyViewSet, basename='company')
# router.register(r'comments', Comment.CommentViewSet, basename='comment')
# router.register(r'categories', Category.CategoryViewSet, basename='category')
# router.register(r'addresses', Address.AddressViewSet, basename='address')
#
# urlpatterns = [
#     # path('api/', include(router.urls)),
#     # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#
#     path('product-sizes/<int:pk>/create/', ProductSize.ProductSizeViewSet.as_view({'post': 'create'}),
#          name='product-size-create'),
#     path('product-sizes/<int:pk>/update/', ProductSize.ProductSizeViewSet.as_view({'put': 'update'}),
#          name='product-size-update'),
#     path('product-sizes/<int:pk>/partial-update/', ProductSize.ProductSizeViewSet.as_view({'patch': 'partial_update'}),
#          name='product-size-partial-update'),
#     path('product-sizes/<int:pk>/delete/', ProductSize.ProductSizeViewSet.as_view({'delete': 'destroy'}),
#          name='product-size-delete'),
#
#     path('product-sites/<int:pk>/create/', ProductSite.ProductSiteViewSet.as_view({'post': 'create'}),
#          name='product-site-create'),
#     path('product-sites/<int:pk>/update/', ProductSite.ProductSiteViewSet.as_view({'put': 'update'}),
#          name='product-site-update'),
#     path('product-sites/<int:pk>/partial-update/', ProductSite.ProductSiteViewSet.as_view({'patch': 'partial_update'}),
#          name='product-site-partial-update'),
#     path('product-sites/<int:pk>/delete/', ProductSite.ProductSiteViewSet.as_view({'delete': 'destroy'}),
#          name='product-site-delete'),
#
#     path('products/<int:pk>/create/', Product.ProductViewSet.as_view({'post': 'create'}), name='product-create'),
#     path('products/<int:pk>/update/', Product.ProductViewSet.as_view({'put': 'update'}), name='product-update'),
#     path('products/<int:pk>/partial-update/', Product.ProductViewSet.as_view({'patch': 'partial_update'}),
#          name='product-partial-update'),
#     path('products/<int:pk>/delete/', Product.ProductViewSet.as_view({'delete': 'destroy'}), name='product-delete'),
#
#     path('payments/<int:pk>/create/', Payment.PaymentViewSet.as_view({'post': 'create'}), name='payment-create'),
#     path('payments/<int:pk>/update/', Payment.PaymentViewSet.as_view({'put': 'update'}), name='payment-update'),
#     path('payments/<int:pk>/partial-update/', Payment.PaymentViewSet.as_view({'patch': 'partial_update'}),
#          name='payment-partial-update'),
#     path('payments/<int:pk>/delete/', Payment.PaymentViewSet.as_view({'delete': 'destroy'}), name='payment-delete'),
#
#     path('patterns/<int:pk>/create/', Pattern.PatternViewSet.as_view({'post': 'create'}), name='pattern-create'),
#     path('patterns/<int:pk>/update/', Pattern.PatternViewSet.as_view({'put': 'update'}), name='pattern-update'),
#     path('patterns/<int:pk>/partial-update/', Pattern.PatternViewSet.as_view({'patch': 'partial_update'}),
#          name='pattern-partial-update'),
#     path('patterns/<int:pk>/delete/', Pattern.PatternViewSet.as_view({'delete': 'destroy'}), name='pattern-delete'),
#
#     path('companies/<int:pk>/create/', Company.CompanyViewSet.as_view({'post': 'create'}), name='company-create'),
#     path('companies/<int:pk>/update/', Company.CompanyViewSet.as_view({'put': 'update'}), name='company-update'),
#     path('companies/<int:pk>/partial-update/', Company.CompanyViewSet.as_view({'patch': 'partial_update'}),
#          name='company-partial-update'),
#     path('companies/<int:pk>/delete/', Company.CompanyViewSet.as_view({'delete': 'destroy'}), name='company-delete'),
#
#     path('comments/<int:pk>/create/', Comment.CommentViewSet.as_view({'post': 'create'}), name='comment-create'),
#     path('comments/<int:pk>/update/', Comment.CommentViewSet.as_view({'put': 'update'}), name='comment-update'),
#     path('comments/<int:pk>/partial-update/', Comment.CommentViewSet.as_view({'patch': 'partial_update'}),
#          name='comment-partial-update'),
#     path('comments/<int:pk>/delete/', Comment.CommentViewSet.as_view({'delete': 'destroy'}), name='comment-delete'),
#
#     path('categories/<int:pk>/create/', Category.CategoryViewSet.as_view({'post': 'create'}), name='category-create'),
#     path('categories/<int:pk>/update/', Category.CategoryViewSet.as_view({'put': 'update'}), name='category-update'),
#     path('categories/<int:pk>/partial-update/', Category.CategoryViewSet.as_view({'patch': 'partial_update'}),
#          name='category-partial-update'),
#     path('categories/<int:pk>/delete/', Category.CategoryViewSet.as_view({'delete': 'destroy'}),
#          name='category-delete'),
#
#     path('addresses/<int:pk>/create/', Address.AddressViewSet.as_view({'post': 'create'}), name='address-create'),
#     path('addresses/<int:pk>/update/', Address.AddressViewSet.as_view({'put': 'update'}), name='address-update'),
#     path('addresses/<int:pk>/partial-update/', Address.AddressViewSet.as_view({'patch': 'partial_update'}),
#          name='address-partial-update'),
#     path('addresses/<int:pk>/delete/', Address.AddressViewSet.as_view({'delete': 'destroy'}), name='address-delete'),
# ]
# urlpatterns += router.urls
