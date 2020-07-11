from django.contrib import admin
from django_inbound.models import InboundRule, InboundIP

# Register your models here.


class InboundIPInline(admin.TabularInline):
    ''' Inline of Inbound Rule '''
    model = InboundIP
    readonly_fields = ['cidr']
    extra = 1


class InboundRuleAdmin(admin.ModelAdmin):
    model = InboundRule
    list_display = ['name', 'namespace', 'url_name', 'group', 'allow_all', 'is_active', 'created']
    exclude = ['alias', 'slug']
    list_filter = ['is_active', 'group', 'namespace', 'url_name']
    inlines = [InboundIPInline]


admin.site.register(InboundRule, InboundRuleAdmin)
