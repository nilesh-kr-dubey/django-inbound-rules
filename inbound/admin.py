from django.contrib import admin
from inbound.models import Rule, InboundIP

# Register your models here.


class InboundIPInline(admin.TabularInline):
    ''' Inline of Inbound Rule '''
    model = InboundIP
    readonly_fields = ['cidr']
    extra = 1


class RuleAdmin(admin.ModelAdmin):
    model = Rule
    list_display = ['name', 'namespace', 'url_name', 'group', 'allow_all', 'is_active', 'created']
    exclude = ['alias', 'slug', 'extra']
    list_filter = ['is_active', 'group', 'namespace', 'url_name']
    raw_id_fields = ['group']
    inlines = [InboundIPInline]


admin.site.register(Rule, RuleAdmin)
