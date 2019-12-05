
from django.forms import ModelForm
from .models import Squirrel
 
class ArticleForm(ModelForm): 
    class Meta:
        model = Squirrel  
        fields = '__all__'
