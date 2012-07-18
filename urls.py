from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('preview.views',
    #(r'^catalog/$','views.home'),
    (r'^catalog/$','home'),
    (r'^catalog/about/','about'),
    (r'^catalog/privacy/','privacy'),
    (r'^catalog/projects/','projects'),
    (r'^catalog/contacts/','contacts'),
    (r'^accounts/', include('accounts.urls')),
    (r'^accounts/',include('django.contrib.auth.urls')),
    #(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    
    # Example:
    # (r'^iStore/', include('iStore.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
urlpatterns+=patterns('',
     (r'^search/',include('search.urls')),
     (r'^comment/product/add','comments.views.addComments'),
     (r'^admin/', include(admin.site.urls)),
     (r'^cart/',include('cart.urls')),
     (r'^',include('catalog.urls')),
     (r'rating/$','rate.views.addRating'),
     (r'^checkout/$','checkout.views.check_out'),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() #this serves static files and media files.
    #in case media is not served correctly
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    )

handler404 = 'iStore.views.file_not_found_404'
