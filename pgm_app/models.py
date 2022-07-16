from django.db import models
# Create your models here.
class Project(models.Model):
    # Fields
    title = models.CharField(max_length=100, help_text="Titulo del Proyecto", verbose_name="Titulo")
    subtitle = models.CharField(max_length=100, help_text="Subtitulo", verbose_name="Subtitulo")
    image = models.ImageField(upload_to='media/images',blank=True, help_text="Imagen del Proyecto", verbose_name="Imagen")
    slug = models.SlugField(max_length=100, help_text="No tocar", verbose_name="Slug")
    description = models.TextField(help_text="Descripcion del Proyecto", verbose_name="Descripcion")
    date = models.DateField()
    video_url = models.CharField(max_length=200, blank=True,help_text='Url del video ', verbose_name='Video URL')
    source = models.ForeignKey('Source', on_delete=models.CASCADE,blank=True, help_text='Youtube o Vimeo o NONE si no hay video',verbose_name='Source')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, help_text='Categoria del projecto', verbose_name='Categoria')
    # Metadata
    class Meta:
        ordering = ['-date','title']
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
    # Methods
    def __str__(self):
        return f'{self.title}'
class ImageModel(models.Model):
    image = models.ImageField(upload_to='media/images', help_text='Imagen del Proyecto', verbose_name='Imagen')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, help_text='Proyecto', verbose_name='Proyecto')
    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"
    def __str__(self):
        return f'{self.image}'
class Category(models.Model):
    # Fields
    name = models.CharField(max_length=100, help_text="Nombre de la Categoria", verbose_name="Nombre")
    slug = models.SlugField(unique=True)
    # Metadata
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    # Methods
    def __str__(self):
        return f'{self.name}'
class Source(models.Model):
    #Fields
    name = models.CharField(max_length=200,db_index=True, help_text='Youtube ou Vimeo', verbose_name='Nom du site')
    def __str__(self):
        return f'{self.name}'
class NewsArticle(models.Model):
    #Fields
    img = models.ImageField(upload_to='media/images', help_text='Imagen de la noticia', verbose_name='Imagen')
    title = models.CharField(max_length=100, help_text="Titulo imagen", verbose_name="Titulo")
    date = models.DateField()
    # Metadata
    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
    # Methods
    def __str__(self):
        return f'{self.title}'