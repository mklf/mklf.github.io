# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1515773763.7925692
_enable_loop = True
_template_filename = 'themes/hpstr/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('pheader', context._clean_inheritance_tokens(), templateuri='post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pheader')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        pheader = _mako_get_namespace(context, 'pheader')
        parent = context.get('parent', UNDEFINED)
        post = context.get('post', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        helper = _mako_get_namespace(context, 'helper')
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        parent = context.get('parent', UNDEFINED)
        post = context.get('post', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if post.meta('keywords'):
            __M_writer('    <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('">\n')
        if post.description():
            __M_writer('    <meta name="description" content="')
            __M_writer(str(post.description()))
            __M_writer('">\n')
        __M_writer('    <meta name="author" content="')
        __M_writer(str(post.author()))
        __M_writer('">\n')
        if post.prev_post:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(post.prev_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.prev_post.title())))
            __M_writer('" type="text/html">\n')
        if post.next_post:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(post.next_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.next_post.title())))
            __M_writer('" type="text/html">\n')
        if post.is_draft:
            __M_writer('        <meta name="robots" content="noindex">\n')
        __M_writer('    <link href="/assets/css/colorbox.css" rel="stylesheet" type="text/css">\n<script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.min.js"></script>\n    <script src="/assets/js/jquery.colorbox-min.js"></script>\n    ')
        __M_writer(str(helper.open_graph_metadata(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.meta_translations(post)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        def content():
            return render_content(context)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        helper = _mako_get_namespace(context, 'helper')
        pheader = _mako_get_namespace(context, 'pheader')
        __M_writer = context.writer()
        __M_writer('\n<article class="post-')
        __M_writer(str(post.meta('type')))
        __M_writer(' h-entry hentry postpage" itemscope="itemscope" itemtype="http://schema.org/Article">\n    ')
        __M_writer(str(pheader.html_post_header()))
        __M_writer('\n    <div class="e-content entry-content" itemprop="articleBody text">\n    ')
        __M_writer(str(post.text()))
        __M_writer('\n    </div>\n    <aside class="postpromonav">\n    <nav>\n    ')
        __M_writer(str(helper.html_tags(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.html_pager(post)))
        __M_writer('\n    </nav>\n    </aside>\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('        <section class="comments">\n        ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer('\n        </section>\n')
        __M_writer('    \n    <script type="text/javascript" src="//cdn.bootcss.com/mathjax/2.6.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML"> </script>\n    ')
        __M_writer(str(mathjax_config))
        __M_writer('\n\n</article>\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/hpstr/templates/post.tmpl", "uri": "post.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "35": 0, "51": 2, "52": 3, "53": 4, "54": 5, "59": 31, "64": 56, "70": 7, "79": 7, "80": 8, "81": 8, "82": 9, "83": 10, "84": 10, "85": 10, "86": 12, "87": 13, "88": 13, "89": 13, "90": 15, "91": 15, "92": 15, "93": 16, "94": 17, "95": 17, "96": 17, "97": 17, "98": 17, "99": 19, "100": 20, "101": 20, "102": 20, "103": 20, "104": 20, "105": 22, "106": 23, "107": 25, "108": 28, "109": 28, "110": 29, "111": 29, "112": 30, "113": 30, "119": 33, "131": 33, "132": 34, "133": 34, "134": 35, "135": 35, "136": 37, "137": 37, "138": 41, "139": 41, "140": 42, "141": 42, "142": 45, "143": 46, "144": 47, "145": 47, "146": 50, "147": 52, "148": 52, "149": 55, "150": 55, "156": 150}}
__M_END_METADATA
"""
