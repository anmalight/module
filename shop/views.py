from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import FormMixin, ModelFormMixin

from shop.forms import AddGoodForm, NewPurchaseForm, NewReturnForm
from shop.models import Good, Return, Purchase
from authentication.models import User


# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


def home_page(request, *args, **kwargs):
    return HttpResponse('True')


class AddGoodView(CreateView):
    success_url = '/'
    form_class = AddGoodForm
    template_name = 'shop/add_good.html'


class UpdateGoodView(UpdateView):
    template_name = 'shop/update_good.html'
    form_class = AddGoodForm
    success_url = '/'
    # model = Good
    queryset = Good.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Good, id=id_)


class ReturnListView(ListView):
    template_name = 'shop/return_list.html'
    model = Return
    paginate_by = 20
    context_object_name = 'posts'

    # def get(self, request, *args, **kwargs):
    #     pass

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context.update(
            {'new_return': NewReturnForm,
             'return': Return,
             'new_purchase': NewPurchaseForm
             }
        )
        return context


class DeleteReturnView(DeleteView):
    # template_name = 'delete_return.html'
    success_url = '/'
    queryset = Return.objects.all()


class AcceptReturnView(DeleteView):
    template_name = 'shop/accept_return.html'
    success_url = '/'
    model = Return
    # next_page = '/'

    def post(self, request, *args, **kwargs):
        obj = Return.objects.get(id=self.kwargs['pk'])
        number = obj.info_about_purchase.quantity_of_goods
        money = obj.info_about_purchase.info_about_good.price
        success_return_money = number*money
        success_return_good = number

        user_id = obj.info_about_purchase.info_about_customer.id
        user = User.objects.get(id=user_id)
        user.wallet += success_return_money
        user.save()

        good_id = obj.info_about_purchase.info_about_good.id
        good = Good.objects.get(id=good_id)
        good.in_stock += success_return_good
        good.save()

        obj.info_about_purchase.delete()

        return self.delete(request, *args, **kwargs)


class PurchaseListView(FormMixin, ListView):
    template_name = 'shop/purchase_list.html'
    success_url = '/purchase_list/'
    model = Purchase

    form_class = NewReturnForm
    # queryset = queryset.filter(user=self.request.user)
    paginate_by = 20
    context_object_name = 'purchase'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(info_about_customer__id=self.request.user.pk)
        # queryset = queryset.filter()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context.update(
            {'new_return': NewReturnForm,
             }
        )
        return context

    # def post(self, request, *args, **kwargs):
    #     pass


class PurchaseCreateView(CreateView):
    template_name = 'shop/purchase_create.html'
    success_url = '/'
    form_class = NewPurchaseForm
    model = Purchase

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Good, id=id_)

    # def post(self, request, *args, **kwargs):
    #     self.object = None
    #     return super().post(request, *args, **kwargs)


class ReturnCreateFrom(CreateView):
    success_url = '/purchase_list/'
    form_class = NewReturnForm
    template_name = 'shop/return_new.html'


class GoodListView(ListView):
    """ home page '/' """

    template_name = 'shop/goods_list.html'
    model = Good
    queryset = Good.objects.all()
    context_object_name = 'goods'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'new_purchase_form': NewPurchaseForm})
        return context
