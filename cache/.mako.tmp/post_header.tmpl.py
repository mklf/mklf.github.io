# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1515773763.826528
_enable_loop = True
_template_filename = 'themes/hpstr/templates/post_header.tmpl'
_template_uri = 'post_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_title', 'html_translations', 'html_sourcelink', 'html_post_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if title and not post.meta('hidetitle'):
            __M_writer('    <h1 class="p-name entry-title" itemprop="headline name"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(post.translated_to) > 1:
            __M_writer('        <div class="metadata posttranslations translations">\n            <h3 class="posttranslations-intro">')
            __M_writer(str(messages("Also available in:")))
            __M_writer('</h3>\n')
            for langname in translations.keys():
                if langname != lang and post.is_translation_available(langname):
                    __M_writer('                <p><a href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('" rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('">')
                    __M_writer(str(messages("LANGUAGE", langname)))
                    __M_writer('</a></p>\n')
            __M_writer('        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if show_sourcelink:
            __M_writer('        <span class="sourceline"><a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a></span>&nbsp;&nbsp;&middot;&nbsp;&nbsp;\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_post_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def html_sourcelink():
            return render_html_sourcelink(context)
        keysite_has_comments = context.get('keysite_has_comments', UNDEFINED)
        def html_title():
            return render_html_title(context)
        def html_translations(post):
            return render_html_translations(context,post)
        post = context.get('post', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        __M_writer = context.writer()
        __M_writer('\n    <header>\n        <div class="entry-meta">\n            <span class="dateline"><a href="')
        __M_writer(str(post.permalink()))
        __M_writer('" rel="bookmark"><time class="published dt-published" datetime="')
        __M_writer(str(post.date.isoformat()))
        __M_writer('" itemprop="datePublished" title="')
        __M_writer(str(post.formatted_date(date_format)))
        __M_writer('">')
        __M_writer(str(post.formatted_date(date_format)))
        __M_writer('</time></a></span>&nbsp;&nbsp;&middot;&nbsp;&nbsp;\n            <span class="byline author vcard">')
        __M_writer(str(post.author()))
        __M_writer('</span>&nbsp;&nbsp;&middot;&nbsp;&nbsp;\n')
        if not post.meta('nocomments') and keysite_has_comments:
            __M_writer('                <!--<span class="commentline">')
            __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
            __M_writer('</span>&nbsp;&nbsp;&middot;&nbsp;&nbsp; -->\n')
        __M_writer('            ')
        __M_writer(str(html_sourcelink()))
        __M_writer('\n')
        if post.meta('link'):
            __M_writer("                    <span><a href='")
            __M_writer(str(post.meta('link')))
            __M_writer("'>")
            __M_writer(str(messages("Original site")))
            __M_writer('</a></span>&nbsp;&nbsp;&middot;&nbsp;&nbsp;\n')
        if post.description():
            __M_writer('                <meta name="description" itemprop="description" content="')
            __M_writer(str(post.description()))
            __M_writer('">\n')
        __M_writer('        </div>\n        ')
        __M_writer(str(html_translations(post)))
        __M_writer('\n    ')
        __M_writer(str(html_title()))
        __M_writer('\n    </header>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/hpstr/templates/post_header.tmpl", "uri": "post_header.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 0, "34": 2, "35": 3, "36": 9, "37": 22, "38": 28, "39": 49, "45": 5, "51": 5, "52": 6, "53": 7, "54": 7, "55": 7, "56": 7, "57": 7, "63": 11, "71": 11, "72": 12, "73": 13, "74": 14, "75": 14, "76": 15, "77": 16, "78": 17, "79": 17, "80": 17, "81": 17, "82": 17, "83": 17, "84": 17, "85": 20, "91": 24, "98": 24, "99": 25, "100": 26, "101": 26, "102": 26, "103": 26, "104": 26, "110": 30, "125": 30, "126": 33, "127": 33, "128": 33, "129": 33, "130": 33, "131": 33, "132": 33, "133": 33, "134": 34, "135": 34, "136": 35, "137": 36, "138": 36, "139": 36, "140": 38, "141": 38, "142": 38, "143": 39, "144": 40, "145": 40, "146": 40, "147": 40, "148": 40, "149": 42, "150": 43, "151": 43, "152": 43, "153": 45, "154": 46, "155": 46, "156": 47, "157": 47, "163": 157}}
__M_END_METADATA
"""
