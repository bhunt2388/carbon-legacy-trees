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

# ---------- hub ----------
streams = [('01', 'Voluntary Carbon Credits', ''), ('02', 'Carbon Tax Credits', 'gd'), ('03', 'Premium Hardwood Lumber', ''), ('04', 'Graphene Byproduct', 'gd')]
pts = []
for i, (n, t, g) in enumerate(streams):
    a = math.radians(-135 + i * 90)
    pts.append((50 + 37 * math.cos(a), 50 + 37 * math.sin(a), n, t, g))
spokes = ''.join('<line class="spoke %s" x1="50" y1="50" x2="%.1f" y2="%.1f"/>' % (g, x, y) for x, y, n, t, g in pts)
nodehtml = ''.join('<div class="node %s" style="left:%.1f%%;top:%.1f%%"><small>%s</small><b>%s</b></div>' % (g, x, y, n, t) for x, y, n, t, g in pts)

STATE = words("Most tree farms have one exit, sell the lumber. Phoenix Tree farms generate income across four independent channels that compound over 15 harvest cycles.", hl=("four", "compound", "15"))
MARQ = ''.join('<span>%s</span>' % t for t in ["Voluntary Carbon Credits", "Carbon Tax Credits", "Premium Hardwood Lumber", "Graphene Byproduct"] * 3)

LEGAL_HOME = ("This website is for informational purposes only and does not constitute an offer to sell or solicitation of an offer to buy any security. "
              "Carbon credit projections, harvest estimates, and revenue forecasts are illustrative. Actual results may differ. Carbon Legacy Trees LLC makes no guarantee of returns. "
              "Consult your financial, legal, and tax advisors before making any investment decision.")

I_TREE = '<path d="M12 22V12M12 12C12 12 7 9 4 4c4 1 7 4 8 8M12 12c0 0 5-3 8-8-4 1-7 4-8 8"/>'
I_DROP = '<path d="M12 2L5.5 9.5C4 11.3 4 14 6 16a8 8 0 0012 0c2-2 2-4.7.5-6.5L12 2z"/>'
I_WOOD = '<path d="M4 12h16M4 8c0 0 2-2 8-2s8 2 8 2M4 16c0 0 2 2 8 2s8-2 8-2M9 6v12M15 6v12"/>'
I_BOLT = '<path d="M13 2L4.5 13.5H12L11 22l8.5-11.5H12L13 2z"/>'
I_DNA = '<path d="M6 18L14 6M10 6h8M10 6l2 4M18 18H6"/><circle cx="12" cy="15" r="3"/>'
I_LOOP = '<path d="M4 12c0-4.4 3.6-8 8-8M20 12c0 4.4-3.6 8-8 8M12 4l-2 2 2 2M20 12l2 2-2 2M4 12L2 10l2-2"/>'
I_UP = '<polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/>'
I_COL = '<path d="M12 3v18M2 9l10-6 10 6M4 15l4-6M20 15l-4-6M2 19h8M14 19h8"/>'
I_PH = '<rect x="6" y="4" width="12" height="18" rx="2"/><path d="M9 2h6"/><path d="M12 8v8M9 12h6"/>'

body = head("Carbon Legacy Trees | Phoenix Tree Investment Platform", "", "https://www.carbonlegacytrees.com/",
    mk_meta("Carbon Legacy Trees | exclusive rights to the Phoenix Tree. 10x carbon sequestration, 15 harvest cycles, graphene byproduct. Four revenue streams per acre for investors, landowners, and carbon credit buyers.",
            "Carbon Legacy Trees | The Phoenix Tree Investment Platform",
            "The epigenetically enhanced Phoenix Tree sequesters 10x carbon, harvests 15 times, and yields graphene. Four compounding revenue streams per acre. Exclusive rights held by Carbon Legacy Trees LLC | South Dakota Phase 1 now underway.",
            "Carbon Legacy Trees | Phoenix Tree Investment Platform",
            "10x carbon sequestration. 15 harvest cycles. Graphene byproduct. Four revenue streams, one planted acre. South Dakota Phase 1 | 10,000 trees committed."))
body += nav(True)

# ---------------- HERO ----------------
body += '''
<section class="hero dk" id="top">
<div class="hero-bg"><canvas id="gl"></canvas><div id="vignette"></div><div id="flash"></div>
<div id="clock" class="clt-ui"><div id="time">--:--<span class="sec">00</span></div><div id="meta"><span id="day"></span><span class="dot"></span><span id="date"></span></div></div>
<div id="sys" class="clt-ui" aria-hidden="true"><span>CARBON&nbsp;<b>TREES</b></span><span class="pip" id="signal"></span><span><b id="gpu">GPU</b></span></div>
<div id="nowName" class="clt-ui"><div class="t"></div><div class="s"></div></div>
<nav id="dock" class="clt-ui" aria-label="Wallpaper picker"></nav>
<div id="hint" class="clt-ui"><span>Move to disturb</span></div></div>
<div class="hero-wash"></div>
<div class="orb og o1"></div><div class="orb oy o2" style="opacity:.55"></div><div class="orb og2 o3"></div><div class="gridbg"></div>
<div class="wrap">
<p class="kicker">South Dakota Launch. 10,000 Trees Committed</p>
<h1><span class="ln" style="--d:0"><span>The Tree That</span></span><span class="ln" style="--d:1"><span><em>Rewrites Carbon</em></span></span><span class="ln" style="--d:2"><span>Economics</span></span></h1>
<p class="lead rv" style="--d:3">Carbon Legacy Trees LLC holds exclusive rights to the Phoenix Tree, an epigenetically enhanced species that sequesters 10x the CO&#8322; of a conventional tree, harvests 15 times, and yields graphene as a combustion byproduct. Four compounding revenue streams on every acre planted.</p>
<div class="cta rv" style="--d:4">%s%s%s</div>
<div class="hstats rv" style="--d:5"><div class="hstat"><b>10x</b><span>CO&#8322; Sequestration</span></div><div class="hstat"><b>15</b><span>Harvest Cycles</span></div><div class="hstat"><b class="gold">4</b><span>Revenue Streams</span></div><div class="hstat"><b class="gold">100%%</b><span>Exclusive Rights</span></div></div>
</div>
<div class="scrollcue">Scroll</div>
</section>
<div class="marq dk" aria-hidden="true"><div class="track">%s</div></div>
''' % (btn('#contact', 'Buy Carbon Credits'), btn('#invest', 'Investor Access', 'gold'), btn('#land', 'Partner Your Land', 'ghost'), MARQ)

# ---------------- TECHNOLOGY + STATS ----------------
body += '''
<section class="sec st" id="phoenix-tree">
<div class="orb og o1" style="left:auto;right:-10%;top:-10%;opacity:.18"></div>
<div class="wrap">
<div class="split"><div><p class="kicker rv">The Technology</p><h2 class="rv" style="--d:1">Engineered by Nature.<br><em>Enhanced by Science.</em></h2></div>
<div style="padding-top:clamp(0px,3vw,46px)"><p class="lead rv" style="--d:2">Post-epigenetic modification permanently unlocks the Phoenix Tree's carbon metabolism. Not GMO. Not synthetic. A biological upgrade that compounds every advantage nature designed into a tree, available now, exclusively through Carbon Legacy Trees LLC.</p></div></div>
<div class="strip rv" style="margin-top:84px">
<div><b data-count="10000">10,000</b><span>Trees Committed. South Dakota</span></div>
<div><b data-count="10" data-suffix="x">10x</b><span>Carbon vs. Standard Trees</span></div>
<div><b class="gold" data-count="15">15</b><span>Harvest Cycles Per Tree</span></div>
<div><b data-count="2" data-suffix="yr">2yr</b><span>To Self-Sustaining Water</span></div>
<div><b class="gold" data-count="4">4</b><span>Revenue Streams Per Acre</span></div>
</div>
</div></section>
'''

# ---------------- PHASE 1 FEATURE ----------------
body += '''
<section class="sec cn"><div class="wrap">
<div class="feat">
<div class="fimg rv"><div class="bezel"><div class="imgcore"><img src="images/greenhouse.png" alt="Phoenix Tree greenhouse nursery rows" loading="lazy"></div></div></div>
<div><p class="kicker rv">Phase 1. South Dakota</p><h2 class="rv" style="--d:1;font-size:clamp(34px,4.6vw,68px)">10,000 Trees. Four Streams. <em>One Commitment.</em></h2>
<p class="lead rv" style="--d:2">The inaugural Phoenix Tree farm demonstrates scale, validates carbon measurement, and generates the first vintage of verified credits. South Dakota land economics and favorable rural tax policy make it the ideal launch market.</p>
<div class="rows rv" style="--d:3"><div><span class="l">Planting status</span><span class="v">10,000 trees committed</span></div><div><span class="l">Credits start</span><span class="v">Year 1</span></div><div><span class="l">Water independence</span><span class="v">Year 2</span></div><div><span class="l">First harvest est.</span><span class="v gd">Year 3&ndash;5</span></div></div></div>
</div></div></section>
'''

# ---------------- TREE FEATURES BENTO ----------------
body += '''
<section class="sec st" style="padding-top:clamp(40px,6vw,90px)"><div class="wrap"><div class="bento" style="margin-top:0">
%s
%s
%s
%s
%s
%s
</div></div></section>
''' % (
 bez(ic(I_TREE) + '<h3 class="lg">10x Carbon Sequestration</h3><p>Enhanced photosynthesis pathways capture and store 10 times the CO&#8322; of a standard tree. Every acre generates verified credits eligible for voluntary and compliance carbon markets.</p><div class="cstat">~1,000 lbs CO&#8322;/yr per tree vs. ~100 lbs standard</div>', 's7'),
 bez(ic(I_DROP) + '<h3>Self-Sustaining Root System</h3><p>Within 24 months roots reach sub-surface water tables with no irrigation. Zero ongoing water infrastructure cost after Year 2, dramatically lowering per-acre operating expense at scale.</p><div class="cstat">Year 2: fully irrigation-independent</div>', 's5', 1),
 bez(ic(I_WOOD) + '<h3>Premium Dense Hardwood</h3><p>Phoenix Tree lumber is among the densest commercially available hardwoods. Structural-grade yield commands premium pricing. Each of 15 harvest cycles stands alone as a meaningful revenue event.</p><div class="cstat">15 independent harvest cycles per tree</div>', 's4'),
 bez(ic(I_BOLT, 'gd') + '<h3>Graphene Combustion Byproduct</h3><p>When Phoenix Tree wood is combusted, the carbon-dense byproduct yields graphene, valued at $100&ndash;$300/kg in industrial applications. Waste becomes a premium commodity stream.</p><div class="cstat gd">Global graphene market: $1.08B+ growing 38%/yr</div>', 's4', 1),
 bez(ic(I_DNA) + "<h3>Epigenetic. Not GMO</h3><p>Post-epigenetic modification works with the tree's existing genetic expression, not foreign gene insertion. Favorable regulatory profile for USDA, EPA, and voluntary carbon registry certification programs.</p><div class=\"cstat\">Clean profile for registry certification</div>", 's4', 2),
 bez(ic(I_LOOP) + '<h3 class="lg" style="max-width:14ch">Nothing Goes to Waste</h3><p>Wood becomes lumber. Combustion becomes graphene. Sequestration becomes a credit. The credit becomes capital. The capital plants more trees. A fully closed production loop on every acre.</p><div class="loop"><div><small>01</small>Wood becomes lumber</div><div><small>02</small>Combustion becomes graphene</div><div><small>03</small>Sequestration becomes a credit</div><div><small>04</small>The credit becomes capital</div><div><small>05</small>The capital plants more trees</div></div><div class="cstat">4 revenue streams. 0 waste streams</div>', 's12')
)

# ---------------- REVENUE: statement + hub ----------------
body += '''
<section class="sec dk" id="revenue">
<div class="orb og o1" style="top:auto;bottom:-20%%;left:-12%%"></div><div class="orb oy o2" style="opacity:.4;top:30%%"></div><div class="gridbg"></div>
<div class="wrap">
<p class="statement wide-st">%s</p>
<div class="hubwrap" style="margin-top:clamp(90px,12vw,160px)"><div><p class="kicker rv">The Business Model</p><h2 class="rv" style="--d:1">Four Revenue Streams.<br><em class="g">One Planted Acre.</em></h2>
<p class="lead rv" style="--d:2">Most tree farms have one exit, sell the lumber. Phoenix Tree farms generate income across four independent channels that compound over 15 harvest cycles. Carbon Legacy Trees holds the exclusive commercial rights to all four.</p></div>
<div class="hub rv" style="--d:2"><svg viewBox="0 0 100 100" aria-hidden="true"><circle class="ringa" cx="50" cy="50" r="27" fill="none" stroke="rgba(255,255,255,.2)" stroke-width=".25" stroke-dasharray="1 2.2"/><circle class="ringb" cx="50" cy="50" r="47" fill="none" stroke="rgba(255,255,255,.14)" stroke-width=".25" stroke-dasharray="3 3"/>%s</svg>%s<div class="hcore"><img src="images/logo-icon.png" alt="Carbon Legacy Trees Phoenix Tree mark" width="60" height="64"></div></div></div>
</div></section>
''' % (STATE, spokes, nodehtml)

# ---------------- REVENUE CARDS + TABLE ----------------
body += '''
<section class="sec cn" style="padding-top:clamp(40px,6vw,80px)"><div class="wrap">
<div class="revs" style="margin-top:0">
%s
%s
%s
%s
</div>
<div class="tblbox rv"><p class="kicker">Economics. 10,000 Tree Farm</p><h3>How the Streams Stack</h3>
<div class="tbl-wrap"><table>
<thead><tr><th>Revenue Stream</th><th>Basis</th><th>Timeline</th><th>Est. Value</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Voluntary Carbon Credits</td><td>10x sequestration &times; 10,000 trees</td><td>Year 1 onward</td><td class="gn">Recurring Annual</td><td>$6&ndash;$30/tonne; registry verified</td></tr>
<tr><td>Carbon Tax Credits</td><td>Federal / state tax attribute</td><td>Filing year eligible</td><td class="gd">Institutional sales</td><td>Discount-to-face-value model</td></tr>
<tr class="hl"><td>Hardwood Lumber. Harvest 1</td><td>Premium dense hardwood, 10,000 trees</td><td>Year 3&ndash;5 est.</td><td class="gn">Major harvest event</td><td>15 regenerative cycles</td></tr>
<tr><td>Graphene Byproduct</td><td>Combustion pathway</td><td>Concurrent with harvest</td><td class="gd">$100&ndash;$300/kg</td><td>Industrial materials market</td></tr>
<tr class="tot"><td>Combined 15-Cycle Value</td><td colspan="2">All 4 streams &times; 15 cycles &times; 10,000 trees</td><td colspan="2">Compounding multi-stream lifecycle return</td></tr>
</tbody></table></div>
<p class="fine">Projections are illustrative. Consult your financial and tax advisors before any investment decision.</p></div>
</div></section>
''' % (
 bez('<span class="rtype">Recurring</span><span class="n">01</span><h3 class="lg">Voluntary Carbon Credits</h3><p>Every Phoenix Tree acre generates verified CO&#8322; sequestration credits annually. With 10x the capture rate, a single acre produces the credit equivalent of 10 conventional acres. CLT holds exclusive rights to sell these on voluntary markets.</p><div class="rfig">$6&ndash;$30 <small>per tonne CO&#8322;, recurring annually</small></div>', 's7'),
 bez('<span class="rtype gd">Tax Strategy</span><span class="n">02</span><h3>Carbon Tax Credits</h3><p>Beyond voluntary credits, Phoenix Tree farms generate federal and state carbon tax credits. Corporations purchase these at a discount, eliminating tax exposure while funding reforestation. CLT holds exclusive origination rights.</p><div class="rfig">Immediate Tax Offset <small>sold at discount to face value</small></div><div style="margin-top:26px">%s</div>' % btn('/tax-strategy.html', 'Read the tax strategy', 'sm'), 's5', 1),
 bez('<span class="rtype">Harvest</span><span class="n">03</span><h3>Premium Hardwood Lumber</h3><p>Phoenix Tree produces extremely dense, durable hardwood. Fifteen harvest cycles from the same planting means recurring lumber revenue. Dense-grain Phoenix wood commands premium structural pricing on every harvest.</p><div class="rfig">15 Harvests <small>per tree, regenerative after each cut</small></div>', 's5'),
 bez('<span class="rtype gd">Materials</span><span class="n">04</span><h3 class="lg">Graphene Byproduct</h3><p>Combustion of Phoenix Tree wood yields graphene, one of the most valuable industrial materials on earth. As EV battery, semiconductor, and composite demand grows at 38%+ annually, this stream scales with the market.</p><div class="rfig">$100&ndash;$300/kg <small>industrial graphene market</small></div>', 's7', 1)
)

# ---------------- SEEDLING ----------------
body += '''
<section class="sec st"><div class="wrap"><div class="feat flip">
<div class="fimg rv"><div class="bezel"><div class="imgcore"><img src="images/seedling.png" alt="Phoenix Tree germinated seedling" loading="lazy"></div></div></div>
<div><p class="kicker rv">The Beginning</p><h2 class="rv" style="--d:1;font-size:clamp(34px,4.6vw,68px)">A New <em>Classification</em> of Tree</h2>
<p class="lead rv" style="--d:2">The Phoenix Tree begins as a standard seedling, then diverges entirely. Post-epigenetic modification permanently alters cellular carbon metabolism before the first leaf unfurls. What germinates is something the forestry world has never seen.</p>
<div class="rows rv" style="--d:3"><div><span class="l">Modification type</span><span class="v">Post-epigenetic, not GMO</span></div><div><span class="l">Carbon capture</span><span class="v">10x standard from Year 1</span></div><div><span class="l">Regulatory profile</span><span class="v gd">Clean, registry eligible</span></div></div></div>
</div></div></section>
'''

# ---------------- HARVEST TIMELINE ----------------
def tn(y, title, gd=False, major=False, dot=None):
    cls = 'td' + (' major' if major else '') + (' gd' if dot else '')
    return '<div class="tn rv" style="--d:%d"><div class="%s"></div><div class="y%s">%s</div><h4>%s</h4></div>' % (tn.i, cls, ' gd' if gd else '', y, title)
tnodes = []
spec = [('Y0', 'Planting + Credits Begin', False, False, False), ('Y2', 'Root Self-Water Achieved', False, False, False), ('Y3&ndash;5', 'Harvest 1 + Graphene', True, True, False),
        ('H2&ndash;H5', 'Harvests 2&ndash;5 (faster cycles)', True, True, False), ('H6&ndash;10', 'Mid-Life Harvests', True, True, False), ('H11&ndash;15', 'Final Harvest Cycles', True, True, False),
        ('Ongoing', 'Carbon Credits, full lifecycle', True, False, True)]
for i, (y, t, g, m, dt) in enumerate(spec):
    tn.i = i % 4
    tnodes.append(tn(y, t, g, m, dt))
body += '''
<section class="sec gr">
<div class="orb og2 o1" style="opacity:.28"></div><div class="orb oy o2" style="opacity:.3;top:auto;bottom:-10%%"></div><div class="gridbg"></div>
<div class="wrap">
<div class="split"><div><p class="kicker gold rv">Lifecycle Economics</p><h2 class="rv" style="--d:1">Plant Once.<br><em class="g">Harvest 15 Times.</em></h2></div>
<div style="padding-top:clamp(0px,3vw,46px)"><p class="lead rv" style="--d:2">After each harvest, the intact root system, now deep enough to access groundwater independently, drives rapid regeneration. Costs are fixed at planting. Revenue compounds across 15 cycles, with carbon credits flowing continuously throughout the entire lifecycle.</p></div></div>
<div class="tl c7">%s</div>
</div></section>
''' % ''.join(tnodes)

# ---------------- MATURE + LUMBER ----------------
body += '''
<section class="sec cn"><div class="wrap">
<div class="feat">
<div class="fimg rv"><div class="bezel"><div class="imgcore"><img src="images/mature.png" alt="Mature Phoenix Tree plantation" loading="lazy"></div></div></div>
<div><p class="kicker rv">At Full Height</p><h2 class="rv" style="--d:1;font-size:clamp(34px,4.6vw,68px)">A Living <em>Carbon Infrastructure</em></h2>
<p class="lead rv" style="--d:2">At maturity, a Phoenix Tree plantation is one of the most productive land-use configurations on earth, sequestering carbon, preparing for harvest, and standing as a documented, verifiable asset on the balance sheet of every partner involved.</p>
<div class="rows rv" style="--d:3"><div><span class="l">Sequestration rate</span><span class="v">10x conventional at maturity</span></div><div><span class="l">Wood density</span><span class="v">Structural premium grade</span></div><div><span class="l">After harvest</span><span class="v gd">Regenerates from roots</span></div></div></div>
</div>
<div class="feat flip" style="margin-top:clamp(90px,11vw,150px)">
<div class="fimg rv"><div class="bezel"><div class="imgcore"><img src="images/lumber.png" alt="Phoenix Tree premium hardwood lumber" loading="lazy"></div></div></div>
<div><p class="kicker rv">The Harvest</p><h2 class="rv" style="--d:1;font-size:clamp(34px,4.6vw,68px)">Premium Hardwood. <em>15 Times Over.</em></h2>
<p class="lead rv" style="--d:2">Phoenix Tree lumber is among the densest hardwoods commercially available. When that same wood is combusted, it yields graphene. Two premium material outcomes from a single harvest event, on a tree that grows back and does it again 14 more times.</p>
<div class="rows rv" style="--d:3"><div><span class="l">Wood grade</span><span class="v">Structural premium</span></div><div><span class="l">Combustion byproduct</span><span class="v">Graphene, $100&ndash;$300/kg</span></div><div><span class="l">Harvest cycles</span><span class="v gd">15, same root system</span></div></div></div>
</div>
</div></section>
'''

# ---------------- AUDIENCE ----------------
def rowhtml(rows):
    return ''.join('<div><span class="l">%s</span><span class="v %s">%s</span></div>' % (l, c, v) for l, v, c in rows)
def pts_(items):
    return '<ul class="points">' + ''.join('<li>%s</li>' % i for i in items) + '</ul>'

inv_rows = [('Initial Phase', 'South Dakota. 10,000 Trees', ''), ('Revenue Start', 'Year 1 (Carbon Credits)', 'gn'), ('First Harvest Est.', 'Year 3&ndash;5', ''), ('Total Harvest Cycles', '15 per tree', ''),
            ('Water Independence', 'Year 2', ''), ('Revenue Streams', '4 (credits, tax, lumber, graphene)', 'gd'), ('Exclusive Rights', 'Carbon Legacy Trees LLC', ''), ('Use of Funds', 'Planting + Scale Expansion', '')]
land_rows = [('Capital Required', 'None. CLT plants + operates', 'gn'), ('Land Types', 'Rural, ag, grassland, marginal', ''), ('Min. Parcel Size', '50 acres', ''), ('Credit Revenue Share', 'Negotiated per deal', ''),
             ('Lumber Revenue Share', 'Negotiated per deal', ''), ('Water After Y2', 'Self-sustaining, no cost', 'gn'), ('Target Regions', 'Midwest, Plains, Mountain West', ''), ('Land Enhancement', 'Carbon-registered asset', 'gd')]
cr_rows = [('Credit Type 1', 'Voluntary Market (VCM)', ''), ('Credit Type 2', 'Carbon Tax Credits', 'gd'), ('VCM Price Range', '$6&ndash;$30 / tonne CO&#8322;', ''), ('Sequestration Rate', '10x standard trees', 'gn'),
           ('Documentation', 'Full registry package', ''), ('Use Case', 'ESG, compliance, tax offset', ''), ('Exclusivity', 'Carbon Legacy Trees LLC', 'gd')]

def pane(pid, active, kicker, kid, h3, lead, points, btnhtml, title, rows):
    return ('<div class="pane%s" id="pane-%s"><div class="aud"><div class="bezel"><div class="core2"><p class="kicker"%s>%s</p><h3>%s</h3><p class="lead" style="max-width:none">%s</p>%s%s</div></div>'
            '<div class="bezel"><div class="core2"><div class="boxt">%s</div><div class="rows" style="margin-top:14px">%s</div></div></div></div></div>'
            % (' active' if active else '', pid, (' id="%s"' % kid) if kid else '', kicker, h3, lead, pts_(points), btnhtml, title, rowhtml(rows)))

body += '''
<section class="sec st" id="land" data-land-section="true"><span id="invest" style="position:absolute;top:0;visibility:hidden"></span>
<div class="wrap">
<p class="kicker rv">Who We Work With</p><h2 class="rv" style="--d:1;max-width:14ch">Three Ways to <em>Participate</em></h2>
<p class="lead rv" style="--d:2">Carbon Legacy Trees serves investors who want multi-stream carbon asset exposure, landowners seeking returns from idle acreage, and corporations needing carbon credit and tax solutions.</p>
<div class="tabs rv" role="tablist"><button class="tab active" data-pane="investors" role="tab" aria-selected="true">Investors</button><button class="tab" data-pane="land" role="tab" aria-selected="false">Land Partners</button><button class="tab" data-pane="credits" role="tab" aria-selected="false">Credit Buyers</button></div>
%s
%s
%s
</div></section>
''' % (
 pane('investors', True, 'Investor Access Open', None, 'Finance the Future of Carbon Agriculture',
      'Capital invested today plants trees that generate four independent revenue streams for 15 harvest cycles, with carbon credit income starting Year 1 and lumber income beginning at first harvest.',
      ['Investment finances planting, irrigation setup, and operations through Year 2 self-sufficiency threshold', 'Carbon credit revenue begins Year 1, partial offset to operating cost during establishment',
       'First harvest event (est. Year 3&ndash;5) generates significant lumber and graphene revenue', '15 total harvest cycles, each faster than the last as root systems mature',
       'Exclusive commercial rights to all four revenue streams held by Carbon Legacy Trees LLC', 'South Dakota Phase 1 provides proof-of-scale before national expansion'],
      btn('#contact', 'Request Investment Deck', 'gold'), 'Investment Highlights', inv_rows),
 pane('land', False, 'Land Partner Program', None, 'Turn Idle Land into a Producing Asset',
      'Own rural acreage with minimal yield? CLT plants, operates, and manages, you receive revenue share on carbon credits and harvest events with zero capital requirement.',
      ['No capital required. CLT provides trees, planting, and all operations', 'After Year 2, zero irrigation or infrastructure burden, trees self-water',
       'Revenue share on voluntary and tax carbon credits generated by your acreage', 'Revenue share on hardwood lumber from all 15 harvest cycles',
       'Land value appreciates as a documented, certified carbon sequestration site', 'Ideal parcels: 50&ndash;5,000+ acres, Midwest / Great Plains / Mountain West'],
      btn('#contact', 'Inquire About Your Land'), 'Land Partner Terms', land_rows),
 pane('credits', False, 'Credits Now Available', 'credits', 'Carbon Credit Solutions for Corporations &amp; Advisors',
      'CLT is the exclusive originator of Phoenix Tree carbon credits and tax attributes. We sell both voluntary market credits and federal tax attributes, letting your organization address climate commitments and tax liability simultaneously.',
      ['Voluntary credits: verified sequestration for ESG reporting and corporate climate commitments', 'Tax credits: transferable federal attributes applicable against corporate tax liability',
       'Purchase at a discount to face value, maximize your carbon ROI', '10x sequestration rate means exceptional credit quality per dollar spent',
       'Full documentation provided: registry certificates, sequestration data, disclosure support'],
      btn('#contact', 'Inquire About Credits'), 'Credit Snapshot', cr_rows)
)

# ---------------- PROCESS ----------------
def ps(n, t, b, d):
    return '<div class="ps rv" style="--d:%d"><div class="psn">%s</div><h4>%s</h4><p>%s</p></div>' % (d, n, t, b)
body += '''
<section class="sec dk">
<div class="orb og o1" style="left:auto;right:-14%%;top:-10%%;opacity:.8"></div><div class="gridbg"></div>
<div class="wrap">
<div class="split"><div><p class="kicker rv">The Process</p><h2 class="rv" style="--d:1">From Bare Land to <em>Four Revenue Streams</em></h2></div>
<div style="padding-top:clamp(0px,3vw,46px)"><p class="lead rv" style="--d:2">CLT manages every step, planting, irrigation, registry certification, harvest coordination, and credit sales. Partners provide land or capital. CLT provides everything else.</p></div></div>
<div class="proc">%s</div>
</div></section>
''' % ''.join([
 ps('01', 'Site Assessment &amp; Agreement', 'CLT evaluates land characteristics, soil, water depth, and sun exposure. Deal structure, revenue share, and all rights to the four revenue streams are finalized before a single tree goes in the ground.', 0),
 ps('02', 'Planting &amp; Establishment', 'Phoenix Trees are planted at optimized density. Initial irrigation is active for Years 0&ndash;2. Carbon sequestration and registry baseline measurements begin immediately on Day 1.', 1),
 ps('03', 'Annual Carbon Credit Issuance', 'Each year, CLT submits verified sequestration data to registered VCM registries. Credits are certified, serialized, and made available for sale. Revenue distributed per agreement.', 2),
 ps('04', 'Harvest, Graphene &amp; Regeneration', 'At maturity, CLT coordinates harvest of dense Phoenix hardwood. Lumber sold at premium rates. A portion goes through the combustion/graphene pathway. Trees regenerate. Cycle repeats up to 15 times.', 3)])

# ---------------- ABOUT ----------------
def pc(n, t, b, d):
    return bez('<span class="pnum">%s</span><div class="pt">%s</div><p>%s</p>' % (n, t, b), '', d)
body += '''
<section class="sec st" id="about"><div class="wrap">
<p class="kicker rv">Who We Are</p><h2 class="rv" style="--d:1">We Don't Extract.<br>We <em>Partner.</em></h2>
<p class="mlead rv">At Carbon Legacy Trees, we believe the earth does not need to be conquered. <em>It needs to be understood.</em></p>
<div class="mbody rv">
<p>The Phoenix Tree is not an invention. It is a revelation, a living organism whose full potential had simply never been unlocked. When we plant one, we are not taking from the ground. <strong>We are entering into an agreement with it.</strong> The tree gives us carbon sequestration, dense hardwood, fifteen harvests, and graphene from its very combustion. In return, we give it water, land, protection, and permanence. That is not agriculture. That is partnership.</p>
<p>This principle extends to every relationship we build. When a landowner opens their acreage to us, they are not leasing ground, they are joining a living enterprise that pays them across decades, enhances the value of their property, and leaves their land more productive than they found it. When an investor backs a Phoenix Tree farm, they are not buying exposure to a single commodity, they are planting four revenue streams that compound across fifteen harvest cycles.</p>
<p><strong>Every party at our table wins. Not as a strategy. As a requirement.</strong> We do not structure deals where one side captures the value and another absorbs the cost. The win-win-win is not a tagline for us, it is the test every deal must pass before we shake hands on it.</p>
<p class="mclose">We are building a company that honors the land, its partners, and the people who believed in it first. This is what a legacy looks like.</p>
</div>
<div class="distilled rv"><div class="bezel"><div class="core2"><p>Carbon Legacy Trees exists to honor the full potential of the earth and the people who steward it. We plant trees that sequester carbon, harvest premium hardwood, and yield graphene, and we structure every deal so the investor, the landowner, the buyer, and the land itself all come out ahead. True abundance is not extracted. It is grown, shared, and replanted.</p></div></div></div>
<div style="margin-top:clamp(80px,10vw,130px)"><p class="kicker rv">Founding Principles</p><h3 class="big rv" style="margin-top:22px;max-width:18ch">Five Commitments We Don't Negotiate On</h3></div>
<div class="bento" style="margin-top:56px">
%s
</div>
</div></section>
''' % '\n'.join([
 pc('01. The Earth', 'The Earth Is a Partner, Not a Resource', 'We plant with the intent to leave every acre more productive, more documented, and more valuable than we found it. The Phoenix Tree does not deplete the land. It deepens it.', 0).replace('class="bezel rv ', 'class="bezel rv s4 ', 1),
 pc('02. Relationships', 'Every Relationship Must Produce a Real Return for Every Party', "We do not do deals where one side wins at another's expense. Landowners, investors, credit buyers, and the land itself all walk away ahead. If a structure can't deliver that, we rebuild it.", 1).replace('class="bezel rv ', 'class="bezel rv s4 ', 1),
 pc('03. Time Horizon', 'We Build for Legacy, Not Liquidity Events', 'A Phoenix Tree planted today is still harvesting in a generation. We think in decades. We build infrastructure that outlasts the deal that funded it, because real value does not peak at exit.', 2).replace('class="bezel rv ', 'class="bezel rv s4 ', 1),
 pc('04. Full Use', 'What the Earth Creates, We Refuse to Waste', 'Wood becomes lumber. Combustion becomes graphene. Sequestration becomes a credit. The credit becomes capital. The capital plants more trees. Nothing the Phoenix Tree produces goes unused.', 0).replace('class="bezel rv ', 'class="bezel rv s6 ', 1),
 pc('05. Integrity', 'Integrity Is the Only Asset That Cannot Be Harvested and Replanted', 'Our word is the foundation every partner stands on. We say what we mean, document what we commit, and deliver what we promise, or we tell you why before you find out on your own.', 1).replace('class="bezel rv ', 'class="bezel rv s6 ', 1)])

# ---------------- CLOSING PULL QUOTE ----------------
body += '''
<section class="sec gr closing">
<div class="orb og2 o1" style="opacity:.3"></div><div class="orb oy o2" style="opacity:.34"></div><div class="gridbg"></div>
<div class="wrap">
<p class="big rv" style="font-size:clamp(32px,5.6vw,84px);line-height:1.04;max-width:20ch">We are building the most efficient carbon sequestration infrastructure on earth, and giving investors, landowners, and corporations <em style="color:var(--goldl)">a piece of every dollar it generates.</em></p>
<p class="sub rv" style="--d:2">Carbon Legacy Trees LLC. South Dakota, 2025. 10,000 trees committed. Exclusive Phoenix Tree commercial rights.</p>
</div></section>
'''

# ---------------- WHY NOW ----------------
body += '''
<section class="sec cn"><div class="wrap">
<div class="split"><div><p class="kicker rv">Market Timing</p><h2 class="rv" style="--d:1;font-size:clamp(34px,4.8vw,72px)">The Carbon Market Is Entering Its <em>Institutional Phase</em></h2></div>
<div style="padding-top:clamp(0px,3vw,46px)"><p class="lead rv" style="--d:2">Voluntary carbon markets transacted $535M in 2025. Corporate net-zero pledges are creating sustained demand for high-quality credits. Transferable tax credits made carbon a tax strategy. And graphene supply chains are being built right now.</p></div></div>
<div class="bento" style="margin-top:64px">
%s
%s
%s
</div></div></section>
''' % (
 bez(ic(I_UP) + '<h3>VCM Growing Demand</h3><p>Voluntary carbon credit issuances grew 8% year-over-year in 2025. Corporate ESG mandates are pushing institutional buyers who demand high-quality, well-documented sequestration credits into the market.</p><div class="cstat">$535M VCM market value. 2025</div>', 's4'),
 bez(ic(I_COL, 'gd') + '<h3>Transferable Tax Credits</h3><p>Congressional authorization of transferable credits opened a new buyer class: CFOs who want to eliminate tax liability at a discount. Carbon tax credits are no longer just a climate tool, they are a corporate finance tool.</p><div class="cstat gd">Buy $1 of tax elimination for less than $1</div>', 's4', 1),
 bez(ic(I_PH, 'gd') + '<h3>Graphene Demand Surge</h3><p>Graphene applications in EV batteries, semiconductors, and composites are driving the global market toward $1.08B+ at 38% annual growth. Phoenix Tree combustion positions CLT to supply into this fast-growing demand.</p><div class="cstat gd">$1.08B+ global graphene market. 38% CAGR</div>', 's4', 2))

# ---------------- CONTACT ----------------
IC_BLD = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L6 10h3l-3 6h4v4h4v-4h4l-3-6h3L12 2z"/></svg>'
IC_PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2C8.7 2 6 4.7 6 8c0 5 6 12 6 12s6-7 6-12c0-3.3-2.7-6-6-6z"/><circle cx="12" cy="8" r="2"/></svg>'
IC_ML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 7l10 7 10-7"/></svg>'
IC_LK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="10" width="14" height="10" rx="2"/><path d="M8 10V7a4 4 0 018 0v3"/></svg>'
body += '''
<section class="sec st" id="contact"><div class="orb og o1" style="left:auto;right:-10%%;opacity:.16"></div>
<div class="wrap"><div class="two">
<div><p class="kicker rv">Get Involved</p><h2 class="rv" style="--d:1">Ready to Plant<br><em>Your Stake?</em></h2>
<p class="lead rv" style="--d:2;max-width:none">Whether you own land, have capital to deploy, need carbon credits for ESG compliance, or want to offset corporate tax liability. Carbon Legacy Trees has a structure for you.</p>
<div class="cinfo rv" style="--d:3"><div>%s<span>Carbon Legacy Trees LLC</span></div><div>%s<span>South Dakota Phase 1. National Expansion</span></div><div>%s<span>contact@carbonlegacytrees.com</span></div><div>%s<span>All inquiries are confidential</span></div></div></div>
<div class="bezel rv" style="--d:2"><div class="core2 formin"><div class="formhead">Start the Conversation</div><div class="formsub">Select your interest and we'll respond within 24 hours.</div>
<form onsubmit="handleSubmit(event)">
<input type="hidden" name="_subject" value="Carbon Legacy Trees - New Inquiry"><input type="hidden" name="source" value="carbonlegacytrees.com">
<div class="row"><div><label class="l" for="f1">First Name</label><input id="f1" type="text" name="first_name" placeholder="First" required autocomplete="given-name"></div><div><label class="l" for="f2">Last Name</label><input id="f2" type="text" name="last_name" placeholder="Last" required autocomplete="family-name"></div></div>
<div><label class="l" for="f3">Email</label><input id="f3" type="email" name="email" placeholder="you@company.com" required autocomplete="email"></div>
<div><label class="l" for="f4">Phone</label><input id="f4" type="tel" name="phone" placeholder="+1 (555) 000-0000" autocomplete="tel"></div>
<div><label class="l" for="f5">I Am Interested In</label><select id="f5" name="interest" required><option value="" disabled selected>Select your interest...</option><option>Investing, financing tree plantings</option><option>Land Partnership. I have acreage available</option><option>Voluntary Carbon Credits. ESG / climate</option><option>Carbon Tax Credits, corporate tax offset</option><option>Graphene / Lumber off-take partnership</option><option>General inquiry</option></select></div>
<div><label class="l" for="f6">Tell Us More</label><textarea id="f6" name="message" placeholder="Investment size, acreage, credit volume, or questions..."></textarea></div>
<button type="submit" class="btn" id="form-btn">Send Inquiry<span class="ic">%s</span></button>
</form></div></div>
</div></div></section>
''' % (IC_BLD, IC_PIN, IC_ML, IC_LK, ARROW)

# ---------------- NETWORK ----------------
NET = [('https://majorshuntergroup.com', 'Majors Hunter Group', 'Private holding and investment company. Land, real estate, structured credit, hospitality and strategic capital.'),
       ('https://www.brysonhunter.com', 'Bryson Hunter Enterprises', 'Private investment platform across real estate, carbon credits, tax mediation, private equity and life sciences.'),
       ('https://www.thekreativebrands.com', 'Kreative Brands', 'Sales, marketing and fulfillment infrastructure behind a portfolio of brands.'),
       ('https://blackrivercompanies.com', 'Black River Investments', 'Private capital partnership focused on creative financing, deal structuring, land rights and bridge lending.'),
       ('https://www.roicfo.com', 'ROI CFO', 'Tax and financial strategy delivered through family offices, advisors and accounting firms.')]
cards = ''.join('<div class="bezel rv" style="--d:%d"><a class="net-card" href="%s" rel="noopener"><span class="net-n">0%d</span><span class="net-name">%s</span><span class="net-desc">%s</span><span class="net-go" aria-hidden="true">Visit site</span></a></div>' % (i % 3, h, i + 1, n, d) for i, (h, n, d) in enumerate(NET))
body += ('<section class="net sec cn" id="network" aria-labelledby="net-h" style="background:var(--canopy)"><div class="wrap"><div class="net-top"><div><span class="net-k rv">Our companies</span>'
         '<h2 id="net-h" class="rv" style="--d:1">One group of companies, each built for its own job.</h2></div><p class="rv" style="--d:2">A family of sister companies. Each operates under its own brand and serves its own clients.</p></div>'
         '<div class="net-grid">%s</div></div></section>\n' % cards)

body += footer(True, LEGAL_HOME)

# ---------------- SCRIPTS ----------------
FORM_JS = r"""<script>
function handleSubmit(e) {
  e.preventDefault();
  const btn = document.getElementById('form-btn');
  const form = e.target;
  const data = Object.fromEntries(new FormData(form));
  const label = btn.innerHTML;
  btn.textContent = 'Sending...';
  btn.disabled = true;
  fetch('https://formspree.io/f/xdarooko', {
    method: 'POST',
    headers: {'Content-Type': 'application/json', 'Accept': 'application/json'},
    body: JSON.stringify(data)
  })
  .then(r => r.json())
  .then(d => {
    if(d.ok) {
      btn.textContent = 'Received. We will be in touch within 24 hours';
      form.reset();
    } else {
      btn.textContent = 'Error. Please email bryson@roicfo.com directly';
      btn.disabled = false;
    }
  })
  .catch(() => {
    btn.textContent = 'Error. Please email bryson@roicfo.com directly';
    btn.disabled = false;
  });
}
</script>"""
sh = open(os.path.join(HERE, 'shaders.js')).read().replace('\u2014', '-')
en = open(os.path.join(HERE, 'engine.js')).read().replace('\u2014', '-')
body += FORM_JS + '\n' + FX + '\n<!-- Carbon Trees WebGL hero engine -->\n<script>\n' + sh + '\n</script>\n<script>\n' + en + '\n</script>\n</body>\n</html>\n'
open(os.path.join(ROOT, 'index.html'), 'w').write(body)
print('index.html', len(body))
