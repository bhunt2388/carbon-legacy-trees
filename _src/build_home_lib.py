import math, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import *

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

def words(s, hl=()):
    return ' '.join('<span class="w%s">%s</span>' % (' hl' if w.strip('.,') in hl else '', w) for w in s.split())

def split_css(css):
    a = css.index('/* network (our companies) */')
    b = css.index('/* footer */')
    mob='@media(max-width:900px){.net-top{grid-template-columns:1fr;gap:28px}.net-grid{grid-template-columns:1fr}.net-grid .bezel,.net-grid .bezel:nth-child(1),.net-grid .bezel:nth-child(2){grid-column:auto}}\n'
    return css[:a] + css[b:], css[a:b] + mob

def head(title, desc, canon, extra_meta, net=True):
    main, netcss = split_css(CSS)
    return ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width,initial-scale=1.0">\n'
            '<meta name="theme-color" content="#0B2545">\n'
            + extra_meta +
            '<link rel="canonical" href="%s">\n<link rel="icon" type="image/png" href="images/logo-icon.png">\n<link rel="apple-touch-icon" href="images/logo-icon.png">\n'
            '<title>%s</title>\n%s\n<script>document.documentElement.classList.add("js")</script>\n<style>%s</style>\n<style id="net-css">%s</style>\n</head>\n<body>\n'
            % (canon, title, FONTS, main, netcss))

def mk_meta(desc, ogtitle, ogdesc, twtitle, twdesc):
    return ('<meta name="description" content="%s">\n'
            '<meta property="og:type" content="website">\n<meta property="og:url" content="https://www.carbonlegacytrees.com">\n<meta property="og:site_name" content="Carbon Legacy Trees">\n'
            '<meta property="og:title" content="%s">\n<meta property="og:description" content="%s">\n'
            '<meta property="og:image" content="https://www.carbonlegacytrees.com/images/mature.png">\n<meta property="og:image:width" content="1024">\n<meta property="og:image:height" content="576">\n'
            '<meta property="og:image:alt" content="Phoenix Tree plantation | Carbon Legacy Trees">\n<meta name="twitter:card" content="summary_large_image">\n'
            '<meta name="twitter:title" content="%s">\n<meta name="twitter:description" content="%s">\n'
            '<meta name="twitter:image" content="https://www.carbonlegacytrees.com/images/mature.png">\n<meta name="twitter:image:alt" content="Phoenix Tree plantation | Carbon Legacy Trees">\n'
            % (desc, ogtitle, ogdesc, twtitle, twdesc))

def ic(path, cls=''):
    return '<span class="ico %s"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg></span>' % (cls, path)

def btn(href, label, cls=''):
    return '<a class="btn %s" href="%s">%s<span class="ic">%s</span></a>' % (cls, href, label, ARROW)

def bez(inner, cls='', d=0):
    return '<div class="bezel rv %s" style="--d:%d"><div class="core2">%s</div></div>' % (cls, d, inner)

