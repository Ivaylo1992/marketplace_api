from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from marketplace_api.api.models import Product
from django.core.cache import cache


@receiver([post_save, post_delete], sender=Product)
def individual_product_cache(sender, instance, **kwargs):
    print('Clearing product cache')

    cache.delete_pattern('*product_list*')