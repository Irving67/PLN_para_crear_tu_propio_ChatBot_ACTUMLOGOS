from IPython.display import display, HTML


def header_str(a_str, n=80):
    """Returns a string formatted as a header."""
    return '{{:=^{:d}}}'.format(n).format(' ' + a_str + ' ')


def header_html(astr, level=1):
    """Returns a string formatted as a HTML header."""
    html_code = '<h{}>{}</h{}>'.format(level, astr, level)
    return display(HTML(html_code))
