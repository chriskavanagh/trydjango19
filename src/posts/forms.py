from __future__ import absolute_import
from django import forms
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit



class PostForm(forms.ModelForm):
    
    class Meta:
        fields = ('title', 'content')
        model = Post
        
        
class CrispyPostForm(PostForm):
    def __init__(self, *args, **kwargs):
        super(CrispyPostForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.layout = Layout(Fieldset('Create Or Update', 'title', 'content'),
                                              ButtonHolder(Submit('submit', 'Submit', 
                                                           css_class='btn-success')))
                                



                                
       
                                                
                                                
                                                