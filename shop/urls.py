from shop.views import home_page, GoodListView, AddGoodView, UpdateGoodView, ReturnListView, DeleteReturnView, \
    AcceptReturnView, PurchaseListView, PurchaseCreateView, ReturnCreateFrom

from django.urls import path


urlpatterns = [
    path('', GoodListView.as_view(), name='good_list'),
    # path('list/', GoodListView.as_view(), name='good_list'),
    path('add_good/', AddGoodView.as_view(), name='add_good'),
    path('update_good/<int:id>/', UpdateGoodView.as_view(), name='update_good'),
    path('return_list/', ReturnListView.as_view(), name='return_list'),
    path('delete_return/<int:pk>/', DeleteReturnView.as_view(), name='delete_return'),
    path('accept_return/<int:pk>/', AcceptReturnView.as_view(), name='accept_return'),
    path('purchase_list/', PurchaseListView.as_view(), name='purchase_list'),
    path('purchase_new/<int:pk>/', PurchaseCreateView.as_view(), name='purchase_new'),
    path('return_new/', ReturnCreateFrom.as_view(), name='return_new')
    ]
