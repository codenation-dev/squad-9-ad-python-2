from datetime import datetime

from django.core.mail import send_mail

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from sales.models import Sales
from seller.models import Seller

from .models import Notification
from .serializers import NotificationSerializer

# Create your views here.


class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


@api_view(['POST'])
def check_commision(request):
    seller_id = request.data["seller"]
    amount = float(request.data["amount"])

    seller = Seller.objects.get(id=seller_id)
    notification = _send_notification_if_necessary(seller, amount)

    response = {
        "should_notify": notification is not None
    }
    return Response(response, status=status.HTTP_200_OK)


def _send_notification_if_necessary(seller, amount):
    """
    calcs seller's sales and being his average sales less than the mean,
    sends an email to the seller.
    Returns the generated and persisted notification if sending the email,
    besides returns None.
    """

    sales = _last_months_sales(seller)
    average_sale = _calc_average_sale(sales)

    if amount >= average_sale:
        return None

    _send_mail(seller, amount)

    notification = Notification(
        seller=seller,
        amount=amount,
        average_sales=average_sale,
        notification_date=datetime.now())
    notification.save()

    return notification


def _last_months_sales(seller):
    queryset = Sales.objects.all()
    seller_sales = queryset.filter(seller=seller)
    return seller_sales.order_by('-year', '-month')[:5]


def _calc_average_sale(sales):
    if not sales:
        return 0

    sorted_sales = sorted(sales, key=lambda s: s.amount)

    sales_amount_sum = 0
    mean_count = 0

    for i, sale in enumerate(sorted_sales, 1):
        sales_amount_sum += sale.amount * i
        mean_count += i

    return sales_amount_sum / mean_count


def _send_mail(seller, amount):
    data_notificacao = datetime.now().strftime('%d/%m/%Y')
    title = f"Notificação de vendas {data_notificacao}"

    from_email = "sq9p2codenation@gmail.com"
    to = [seller.email]

    message = f"""
    Olá {seller.name},
    notamos que vendas estão abaixo da média: R$ {amount}.
    """

    send_mail(title, message, from_email, to, fail_silently=False)
