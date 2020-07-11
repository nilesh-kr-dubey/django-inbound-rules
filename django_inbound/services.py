
def get_resolved_urls(url_patterns, namespace=None):
    url_patterns_resolved = []
    for entry in url_patterns:
        if hasattr(entry, 'url_patterns'):
            if namespace:
                if entry.namespace == namespace:
                    # url_patterns_resolved += get_resolved_urls(
                    #     entry.url_patterns, namespace=namespace)
                    url_patterns_resolved += get_resolved_urls(
                        entry.url_patterns)
            else:
                url_patterns_resolved += get_resolved_urls(
                    entry.url_patterns)

        else:
            if entry.name is not None:
                url_patterns_resolved.append(entry.name)
    return url_patterns_resolved
