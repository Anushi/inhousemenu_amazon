from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .views import HomePageView, FormHorizontalView, FormInlineView, PaginationView, FormWithFilesView, \
    DefaultFormView, MiscView, DefaultFormsetView, DefaultFormByFieldView, RecipeListView, RecipeDetailView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'demo.views.home', name='home'),
#     # url(r'^demo/', include('demo.foo.urls')),
#
#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#
#     # Uncomment the next line to enable the admin:
#     # url(r'^admin/', include(admin.site.urls)),
# )

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home'),
    # ex: /recipes/
    #url(r'^recipes/$', views.recipeList, name='recipeList'),
    url(r'^recipes/$', RecipeListView.as_view(), name='recipeList'),
    # ex: /recipes/5/
    url(r'^recipes/(?P<recipe_id>[0-9]+)/$', RecipeDetailView.as_view(), name='recipeDetail'),
    url(r'^formset$', DefaultFormsetView.as_view(), name='formset_default'),
    url(r'^form$', DefaultFormView.as_view(), name='form_default'),
    url(r'^form_by_field$', DefaultFormByFieldView.as_view(), name='form_by_field'),
    url(r'^form_horizontal$', FormHorizontalView.as_view(), name='form_horizontal'),
    url(r'^form_inline$', FormInlineView.as_view(), name='form_inline'),
    url(r'^form_with_files$', FormWithFilesView.as_view(), name='form_with_files'),
    url(r'^pagination$', PaginationView.as_view(), name='pagination'),
    url(r'^misc$', MiscView.as_view(), name='misc'),
)