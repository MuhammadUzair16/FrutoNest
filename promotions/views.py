from django.shortcuts import render
from django.utils import timezone
from .models import Deal  # Import the Deal model

def deal_of_the_month(request):
    current_date = timezone.now().date()
    deal = Deal.objects.filter(start_date__lte=current_date, end_date__gte=current_date).first()

    if not deal:
        deal = {
            'name': 'No Deal',
            'description': 'There is no deal available for this month.',
            'end_date': current_date
        }

    return render(request, 'home.html', {'deal': deal})
