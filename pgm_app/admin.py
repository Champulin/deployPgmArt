from django.contrib import admin
from .models import Project, Category, Source, ImageModel
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    pass
    list_display = ('title', 'date', 'category', 'source')
    list_filter = ('date', 'category', 'source')
    search_fields = ('title', 'description')
    ordering = ['-date', 'title']
    date_hierarchy = 'date'
    fieldsets = (
        (None, {
            'fields': ('title','subtitle', 'description', 'image', 'date', 'video_url',  'source', 'category', 'slug')
        }),
    )
    prepopulated_fields = {'slug': ('title',)}
class CategoryAdmin(admin.ModelAdmin):
    pass
    list_display = ('name', 'id')
    search_fields = ('name',)
    ordering=['-id']
    fieldsets = (
        (None, {
            'fields': ('name','slug')
        }),
    )
    prepopulated_fields = {'slug': ('name',)}
class SourceAdmin(admin.ModelAdmin):
    pass
    list_display = ('name','id')
    search_fields = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
    )
class ImageModelAdmin(admin.ModelAdmin):
    pass
    list_display = ('image', 'project')
    search_fields = ('image',)
    fieldsets = (
        (None, {
            'fields': ('image', 'project')
        }),
    )
admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(ImageModel, ImageModelAdmin)