# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from .models import Spec
admin.site.register(Spec)

from .models import Brand
admin.site.register(Brand)

from .models import Category
admin.site.register(Category)

from .models import Supplier
admin.site.register(Supplier)

from .models import Price
admin.site.register(Price)

from .models import Item
admin.site.register(Item)
