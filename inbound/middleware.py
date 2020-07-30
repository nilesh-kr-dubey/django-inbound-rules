from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from inbound.queries import validate_inbound_rules, check_user_authentication, get_groups, get_group_inboundrules, validate_allow_all_ips, validate_ip_in_inbound_ips



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def restrict_user_middleware(get_response):

    def middleware(request):
        # Check namespace and name in InboundRules
        if not request.user.is_superuser:
            if validate_inbound_rules(path=request.path):
                user = check_user_authentication(request=request)
                if user:
                    group_ids = get_groups(user=user)
                    if group_ids:
                        inboundrules = get_group_inboundrules(group_ids=group_ids)
                        if inboundrules:
                            # passing all inboundrules
                            if validate_allow_all_ips(inboundrules_queryset=inboundrules):
                                # All IPs are allows
                                pass
                            else:
                                # Specific IPs are allows
                                ip = get_client_ip(request=request)
                                if validate_ip_in_inbound_ips(requested_ip=ip, inboundrules_queryset=inboundrules):
                                    pass
                                else:
                                    raise Http404
                        else:
                            # No inbound rules is attached to user-group
                            raise Http404
                    else:
                        raise Http404
                else:
                    raise Http404
            else:
                pass
        else:
            pass

        response = get_response(request)
        return response

    return middleware
