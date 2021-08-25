from django.contrib import admin

from Usuarios.models import User

#admin.site.register(User)

class UserAdmin(admin.ModelAdmin):

	list_display= ['id','username','first_name','last_name','telefono','date_joined','last_login']	
	search_fields=['username','first_name','last_name']
	list_filter=['last_login'] 

admin.site.register(User,UserAdmin)
