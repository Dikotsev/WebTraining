

from django import forms


from WebTraining.properties.models import Properties, Image


class BootstrapFormMixin:
    def __init__(self):
        self.fields = None

    def _init_bootstrap(self):
        for (_, field) in self.fields.items():
            field.widget.attrs = {
                'form': 'form',
            }


class PropertiesForms(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = Properties
        fields = ['name', 'description', 'price']


class ImageForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self._init_bootstrap()

    class Meta:
        model = Image
        fields = '__all__'




class AddProperty(forms.Form):
    pass


class DeleteProperty(forms.Form):
    pass


class UpdateProperty(PropertiesForms, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()
    pass
