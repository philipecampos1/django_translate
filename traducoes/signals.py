from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Traducoes
from translate import Translator


@receiver(post_save, sender=Traducoes)
def translate_frase(sender, instance, created, **kwargs):
    if created and not instance.en_gb:
        translator = Translator(from_lang='pt', to_lang='en')
        translation = translator.translate(instance.pt_br)
        instance.en_gb = translation
        instance.save(update_fields=['en_gb'])
