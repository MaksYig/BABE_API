from django.contrib import admin
from django.urls import path,include
from listings.API import views as listings_api_views
from django.conf import settings
from django.conf.urls.static import static
from users.API import views as users_api_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/listings/info/<int:id>/', listings_api_views.PetListingID.as_view()),
    path('api/listings/', listings_api_views.ListingPets.as_view() ),
    path('api/listings/update/<int:id>/', listings_api_views.UpdatePet.as_view() ),
    path('api/listings/delete/<int:id>/', listings_api_views.DeletePets.as_view() ),
    path('api/listings/create/', listings_api_views.CreatePets.as_view() ),
    
    
    path('api/profiles/', users_api_views.ProfileList.as_view() ),
    path('api/user/profile/<int:id>/', users_api_views.UserProfileUpdateView.as_view() ),
    path('api/profiles/<int:user>/', users_api_views.ProfileDetails.as_view()),
    
    path('api-auth-djoser/', include('djoser.urls')),
    path('api-auth-djoser/users/', include('djoser.urls')),
    path('api-auth-djoser/', include('djoser.urls.authtoken')),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
