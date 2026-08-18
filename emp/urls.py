# from django.templatetags import media
# from django.conf.urls.static import static
# from django.urls import path

# from Employee import settings
# from .views import delete_emp, emp_home, add_emp , update_emp

# urlpatterns = [
#     path('', emp_home, name='home'),
#     path('add_emp/', add_emp, name='add_emp'),
#     path('delete_emp/<int:id>/', delete_emp, name='delete_emp'),
#     path('update_emp/<int:id>/', update_emp, name='update_emp')
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import delete_emp, emp_home, add_emp, update_emp, Testimonials,Feedback


urlpatterns = [
    path('', emp_home, name='home'),
    path('add_emp/', add_emp, name='add_emp'),
    path('delete_emp/<int:id>/', delete_emp, name='delete_emp'),
    path('update_emp/<int:id>/', update_emp, name='update_emp'),
    path('testimonials/', Testimonials, name='testimonials'),
    path('feedback/', Feedback, name='feedback'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)