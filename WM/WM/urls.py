"""
URL configuration for Global project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
#################index############
    path('admin/', admin.site.urls),
    path('index',views.index),
    path('about',views.about),
    path('services',views.services),
    path('login',views.login),
    path('register',views.user_r),
    path('logout',views.logout),

 #############admin#############


    path('admin',views.admin),
    path('send_reply/<int:complaint>',views.send_reply),
    path('send_reply_post/<int:id>',views.send_reply_post),
    path('U-profile',views.user_view),
    path('adviewcomplaint', views.viewcom),
    path('Addwaste', views.add_W),
    path('display_W', views.display_W),
    path('upd/<int:id>', views.update),
    path('update/<int:id>', views.update_view),
    path('del/<int:id>', views.delete),
    path('W-profile', views.worker_view),
    path('delete/<int:id>',views.delete1),
    path('bio/<int:id>', views.bio),
    path('bio1/<int:id>', views.bio1),
    path('approve/<int:id>',views.approve),
    path('approved',views.approved),
   path('admin_vieworders',views.admin_vieworders),
    path('admin_pass/<int:sts>',views.admin_pass),

###############user################
    path('user',views.user),
    path('viewprofile',views.view_profile),
    path('edit',views.edit_view),
    path('edit1',views.edit_profile),
    path('complaint',views.complaint),
    path('complaint_view',views.complaint_view),
    path('viewcomplaint',views.viewcomplaint),
    path('add',views.display),
    path('booking/<int:id>',views.booking),
    path('payment/<int:price>', views.payment),
    path('order_view', views.view_orders),

    ###############worker###################
    path('worker',views.worker),
    path('worker-r',views.worker_r),
    path('profile_view',views.profile_view),
    path('worker_management',views.worker_management),
    path('delivery_status/<sts>',views.delivery_status),
    path('edit2',views.edit_view1),
    path('edit3',views.Wedit_profile),
#     path('contacts',views.contacts),

    #################forgot############3
path('forgot_password', views.forgot_password, name="forgot"),
    path('reset/<token>', views.reset_password, name='reset_password'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)