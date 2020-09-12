def filter_resolved_urls(url_patterns, namespace=None):
    filtered_content = []
    for entry in url_patterns:
        if namespace:
            if hasattr(entry, 'url_patterns'):
                if entry.namespace == namespace:
                    filtered_content.append(entry)
        else:
            if not hasattr(entry, 'url_patterns'):
                filtered_content.append(entry)
    return filtered_content

def resolved_urls(filtered_content):
    req_urls = []
    for entry in filtered_content:
        if hasattr(entry, 'url_patterns'):
            for sub_entry in entry.url_patterns:
                if sub_entry.name is not None:
                    req_urls.append(sub_entry.name)
        else:
           if entry.name is not None:
                req_urls.append(entry.name)
    return req_urls

def get_resolved_urls(url_patterns, namespace=None):
    filtered_content = filter_resolved_urls(url_patterns=url_patterns, namespace=namespace)
    output = resolved_urls(filtered_content=filtered_content)
    return output
