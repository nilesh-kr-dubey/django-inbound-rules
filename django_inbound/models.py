import ipaddress
from datetime import datetime
from django.db import models
from django.urls import reverse, get_resolver, get_urlconf
from django.utils.text import slugify
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError

from django_inbound.services import get_resolved_urls


class InboundRule(models.Model):
    '''
        Model of Inbound Rule
    '''
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, null=True, blank=True)
    slug = models.CharField(max_length=100, null=True, blank=True)
    namespace = models.CharField(max_length=100, null=True, blank=True)
    url_name = models.CharField(max_length=100, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    allow_all = models.BooleanField(default=False, help_text='Allow all User', verbose_name='Allow all IP\'s')
    is_active = models.BooleanField(default=True)
    extra = models.TextField(null=True, blank=True)
    created = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = 'Inbound Rule'
        verbose_name_plural = 'Inbound Rules'

    def __str__(self):
        return self.name

    def clean(self, *args, **kwargs):
        if not self.namespace:
            raise ValidationError({'namespace': "Please provide data"})
        else:
            url_resolver = get_resolver(get_urlconf())
            all_namespace = list(url_resolver.namespace_dict.keys())
            if self.namespace not in all_namespace:
                raise ValidationError({'namespace': "Invalid namesapce"})
        if self.url_name and self.namespace:
            # path = '{0}:{1}'.format(self.namespace, self.url_name)
            # try:
            #     path = reverse(path)
            # except:
            #     raise ValidationError({'namespace': "Invalid namesapce", 'url_name': "Invalid url name"})
            patterns = get_resolver().url_patterns
            corrosponding_urls = get_resolved_urls(url_patterns=patterns, namespace=self.namespace)
            if self.url_name not in corrosponding_urls:
                raise ValidationError({'url_name': "Invalid url name"})
        super(InboundRule, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(InboundRule, self).save(*args, **kwargs)


class InboundIP(models.Model):
    '''
        Model of Inbound IP
    '''
    inbound_rule = models.ForeignKey(InboundRule, on_delete=models.CASCADE)
    start_ip = models.GenericIPAddressField()
    end_ip = models.GenericIPAddressField(null=True, blank=True, help_text='For Single or specific IP, Leave it Blank')
    cidr = models.CharField(max_length=20, null=True, blank=True, help_text='CIDR Block', verbose_name='CIDR')
    created = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = 'Inbound IP'
        verbose_name_plural = 'Inbound IPs'

    def __str__(self):
        return self.inbound_rule.name

    def clean(self, *args, **kwargs):
        start_ip = self.start_ip
        if not self.end_ip:
            end_ip = self.start_ip
        else:
            end_ip = self.end_ip
        startip = ipaddress.IPv4Address(start_ip)
        endip = ipaddress.IPv4Address(end_ip)
        try:
            all_blocks = [ipaddr for ipaddr in ipaddress.summarize_address_range(startip, endip)]
            if not all_blocks:
                raise ValidationError('Invalid Range')
        except:
            raise ValidationError({'start_ip': "Invalid range", 'end_ip': "Invalid Range"})
        if len(all_blocks) > 1:
            raise ValidationError({'start_ip': "Provide range for single CIDR", 'end_ip': "Provide range for single CIDR"})
        super(InboundIP, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.end_ip:
            self.end_ip = self.start_ip
        if self.start_ip and self.end_ip:
            startip = ipaddress.IPv4Address(self.start_ip)
            endip = ipaddress.IPv4Address(self.end_ip)
            all_blocks = [ipaddr for ipaddr in ipaddress.summarize_address_range(startip, endip)]
            if all_blocks:
                all_blocks = all_blocks[0]
                self.cidr = all_blocks.compressed
        super(InboundIP, self).save(*args, **kwargs)
