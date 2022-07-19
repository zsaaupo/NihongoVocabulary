from django.urls import path
from .views import choice, english_list, all_forms, basic_form_list, present_positive_list, past_positive_list, present_negative_list, past_negative_list, present_continuous_list, past_continuous_list, te_from_list, note

urlpatterns = [

    # root urls
    path('', choice),

    # url for note
    path('note/', note),

    # urls for verb form's list
    path('english/', english_list),
    path('basic_form/', basic_form_list),
    path('present_positive/', present_positive_list),
    path('present_negative/', present_negative_list),
    path('past_negative/', past_negative_list),
    path('past_positive/', past_positive_list),
    path('present_continuous/', present_continuous_list),
    path('past_continuous/', past_continuous_list),
    path('te_from/', te_from_list),

    # urls for all form
    path('forms/<str:get_id>/', all_forms),
]