from hotel.models import CustomerReview
from django import forms


# class AddHotelReviewForm(forms.ModelForm):
#
#     class Meta:
#         model = CustomerReview
#         fields = ["hotel_to_review", "customer", "comment", "stars"]
#
#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#
#         queryset = queryset.filter(customer=request.user)
#         return queryset


# class HotelForm(forms.ModelForm):
#     class Meta:
#         model = Hotel
#         exclude = []



# class RoomForm(forms.ModelForm):
#     class Meta:
#         model = Room
#         exclude = []

