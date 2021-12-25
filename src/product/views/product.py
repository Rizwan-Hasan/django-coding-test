from django.views import generic

from product.models import Product, Variant


class CreateProductView(generic.TemplateView):
    template_name = "products/create.html"

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values("id", "title")
        context["product"] = True
        context["variants"] = list(variants.all())
        return context


class ListProductView(generic.TemplateView):
    template_name = "products/list.html"

    def get_context_data(self, **kwargs):
        context = super(ListProductView, self).get_context_data(**kwargs)
        products = Product.objects
        context["product"] = True
        context["products"] = list(products.all())
        print(products.all())
        return context
