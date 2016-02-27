from __future__ import absolute_import
from django import forms
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import FormActions    # for bootstrap 3 (replaces Buttonholder)



class PostForm(forms.ModelForm):
    
    class Meta:
        fields = ('title', 'content')
        model = Post
        
        
class CrispyPostForm(PostForm):
    
    def __init__(self, *args, **kwargs):
        super(CrispyPostForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.layout = Layout(Fieldset('Create Or Update', 'title', 'content'),
                                              FormActions(Submit('submit', 'Submit', 
                                                           css_class='btn-success')))
                                                           
                                                           
                                                           
 

free_food_choices = (
    ('donuts', 'Donuts'),
    ('crab rangoon', 'Crab Rangoon'),
    ('sushi', 'Sushi')
)

order_type = (
    ('pickup', 'PickUp'),
    ('delivery', 'Delivery')
)

 
class FoodForm(forms.Form):
    name = forms.CharField(label='Your name')
    address = forms.CharField(required=False)
    type = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=order_type, help_text='Select one.')
                                                                            
    email = forms.EmailField(help_text='A valid email address, please.')
    phone = forms.IntegerField(help_text='Ex: 5409897947')
    comment = forms.CharField(widget=forms.Textarea, max_length=100, help_text='100 characters max.')
    coupon = forms.MultipleChoiceField(required=False,
                                        widget=forms.CheckboxSelectMultiple, 
                                        choices=free_food_choices,
                                        help_text='Donuts-$15 or more, Crab Rangoon-$20 or more, Sushi Roll-$30 or more.')
    
                                 
    
                                



                                
       
                                                
                                                
                                                