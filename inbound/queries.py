import ipaddress
from django.urls import resolve
from django.contrib.auth.models import User, Group
from django.db.models import F
from datetime import datetime, timedelta
from collections import OrderedDict

from inbound.models import Rule


def validate_inbound_rules(request=None, path=None):
    if request:
        namespace = request.resolver_match.namespace
        url_name = request.resolver_match.url_name
    elif path:
        try:
            match = resolve(path)
            namespace = match.namespace
            url_name = match.url_name
        except:
            namespace = None
            url_name = None
    else:
        namespace = None
        url_name = None
    all_inbound_rules = Rule.objects.filter(is_active=True)
    combine_rule = all_inbound_rules.filter(namespace=namespace, url_name=url_name)
    if combine_rule:
        return True
    namespace_rule = all_inbound_rules.filter(namespace=namespace, url_name__isnull=True)
    if namespace_rule:
        return True
    return False


def check_user_authentication(request):
    if request.user.is_authenticated:
        try:
            user = User.objects.get(id=request.user.id)
        except:
            user = None
    else:
        user = None
    return user

def get_groups(user):
    return list(user.groups.all().values_list('id', flat=True))

def get_group_inboundrules(group_ids):
    return Rule.objects.filter(group_id__in=group_ids).filter(is_active=True)

def validate_allow_all_ips(inboundrules_queryset):
    if inboundrules_queryset.filter(allow_all=True):
        return True
    else:
        return False

# def validate_ip_in_inbound_ips(requested_ip, inboundrules_queryset):
#     '''may and may not work properly'''
#     output = False
#     for inboundrules in inboundrules_queryset:
#         all_inbound_ips = inboundrules.inboundip_set.filter(start_ip__lte=requested_ip, end_ip__gte=requested_ip)
#         if all_inbound_ips:
#             output = True
#             break
#     return output



def validate_ip_in_inbound_ips(requested_ip, inboundrules_queryset):
    output = False
    for inboundrules in inboundrules_queryset:
        all_inbound_ips = inboundrules.inboundip_set.all()
        for inbound_ip in all_inbound_ips:
            if ipaddress.ip_address(requested_ip) in ipaddress.ip_network(inbound_ip.cidr):
                output = True
                break
        if output:
            break
    return output
