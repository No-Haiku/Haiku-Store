from django import forms

class FormularioContacto(forms.Form):

    nombre= forms.CharField(label='Nombre', required=True)
    #apellido= forms.CharField(label='Apellido', required=True)
    email= forms.CharField(label='Email', required=True)
    contenido= forms.CharField(label='Contenido', required=True, widget=forms.Textarea)


    
    
    
    