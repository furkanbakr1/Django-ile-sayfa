from django.contrib import admin

from .models import Article,Comment
# Register your models here.

admin.site.register(Comment)

@admin.register(Article)   
class ArticleAdmin(admin.ModelAdmin):  #admin panelini özelliştirmek için oluşturduğum class

    list_display = ["title","author","created_date"] # sadece başlığın değil diğerlerini de gösterebilmek için.

    list_display_links = ["title","created_date"]  # link ekliyor.

    search_fields = ["title"] # başlığa göre arama yapmak için.

    list_filter = ["created_date"] # tarih süzgeçine göre filtreliyor.
    
    class Meta: #Article modeliyle ArticleAdmin i birleştirmek için kullanılan class içindeki class. Django öneriyor.
        model = Article

