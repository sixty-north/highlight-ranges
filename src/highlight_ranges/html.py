import pkg_resources


def get_html(css, div):
    template = pkg_resources.resource_string(
        'highlight_ranges', 'data/template.html')
    return template.decode().format(css=css, code=div)
