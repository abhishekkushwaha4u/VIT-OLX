from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer


class ProductAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class SellProduct(APIView):
    params = ['name', 'price', 'description']

    def check_parameters(self, request):
        response = {}
        for i in self.params:
            if i not in request.data:
                response[i] = "{} must be properly supplied".format(i)
        if response:
            Response.status_code = 400
            return Response(response)

    def check_parameters_integrity(self, request):
        response = {}
        for i in self.params:
            if i == 'price':
                try:
                    m = float(request.data.get('price'))
                    # ToDo: Add checks for other types of constraints
                except ValueError:
                    response[i] = 'Invalid data type for price'
                    Response.status_code = 403
                    return Response(response)

    def add_product_to_market(self, request, image):
        name = request.data.get('name')
        price = request.data.get('price')
        description = request.data.get('description')
        try:
            if image:
                Product.objects.create(name=name, price=price, description=description, photo=image)
            else:
                Product.objects.create(name=name, price=price, description=description)
        except Exception as e:
            print(e)
            Response.status_code = 500
            return Response({"err": "Error adding product to the market"})

    def post(self, request):
        check = self.check_parameters(request)
        if check:
            return check

        if 'image' in request.data:
            image = request.data.get('image')
        else:
            image = ''
        integrity = self.check_parameters_integrity(request)
        if integrity:
            return integrity
        database_update = self.add_product_to_market(request, image)
        if database_update:
            return database_update

        return Response({"msg": "Successfully added to market"})








