import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
import build_home_lib as L

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
btn, bez, head = L.btn, L.bez, L.head

LEGAL = ("This page is for informational purposes only and does not constitute legal, tax, or investment advice. Tax strategies described are based on current IRS law (OBBBA 2025) and require individual CPA review. "
         "&sect;168(k)(5) specified plant election eligibility should be confirmed with a qualified tax professional for your specific situation. Carbon credit valuations are market estimates and are not guaranteed.")

meta = ('<meta name="description" content="How Carbon Legacy Trees investors capture immediate tax value via &sect;168(k)(5) specified plant election, plus the full creative tax stack.">\n')
b = head("Tax Strategy | Carbon Legacy Trees", "", "https://www.carbonlegacytrees.com/tax-strategy.html", meta)
b += nav(False, 'Tax Strategy')

def stat(val, cnt, lbl, gold=False, pre='', suf=''):
    return '<div class="hstat"><b%s data-count="%s" data-prefix="%s" data-suffix="%s">%s</b><span>%s</span></div>' % (' class="gold"' if gold else '', cnt, pre, suf, val, lbl)

b += '''
<section class="hero thero dk" id="top">
<div class="hero-bg"></div>
<div class="orb og o1"></div><div class="orb oy o2" style="opacity:.55"></div><div class="orb og2 o3"></div><div class="gridbg"></div>
<img class="hwm" src="images/logo-icon.png" alt="" aria-hidden="true">
<div class="wrap">
<p class="kicker">Investor Tax Strategy. OBBBA 2025</p>
<h1><span class="ln" style="--d:0"><span>The Tax Play That Makes</span></span><span class="ln" style="--d:1"><span>Your Investment Work</span></span><span class="ln" style="--d:2"><span><em>Twice.</em></span></span></h1>
<p class="lead rv" style="--d:3">Two IRS-confirmed strategies, &sect;168(k)(5) Specified Plant Election and the full tax leverage stack, let you capture hundreds of thousands in tax value the same year you invest. Before the first carbon credit is ever sold.</p>
<div class="cta rv" style="--d:4">%s%s</div>
<div class="hstats rv" style="--d:5">%s%s%s%s</div>
</div></section>
''' % (btn('/#contact', 'Schedule a Call', 'gold'), btn('#anchor', 'See the math', 'ghost'),
       stat('100%', 100, 'Bonus Dep.. Year 1', False, '', '%'), stat('$259K+', 259, 'Tax Savings on $700K Plant Cost', True, '$', 'K+'),
       stat('15', 15, 'Harvest Cycles Per Tree'), stat('$350K+', 350, 'Combined Year 1 Tax Stack', True, '$', 'K+'))

# anchor
def step(i, t):
    return '<li><b class="i">%d</b><span>%s</span></li>' % (i, t)
b += '''
<section class="sec st" id="anchor"><div class="orb og o1" style="left:auto;right:-12%%;opacity:.16"></div><div class="wrap">
<div class="split"><div><p class="kicker gold rv">The Anchor Play, &sect;168(k)(5)</p><h2 class="rv" style="--d:1;font-size:clamp(34px,4.8vw,72px)">Specified Plant Election: <em class="g">100%% Deduction</em> the Year You Plant</h2></div>
<div style="padding-top:clamp(0px,3vw,46px)"><p class="lead rv" style="--d:2">Under the One Big Beautiful Bill Act (signed July 4, 2025), Congress permanently restored 100%% bonus depreciation under &sect;168(k). For investors in Carbon Legacy Trees, this unlocks a specific election that changes the entire return profile of the investment.</p></div></div>
<div class="anchor-two">
<div class="bezel rv"><div class="core2"><span class="ptag gd">The Legal Basis</span><h3>What Is a &quot;Specified Plant&quot;?</h3>
<p>IRC &sect;168(k)(5)(B) defines a specified plant as: <span class="quote">&quot;(i) any tree or vine which bears fruits or nuts, and (ii) any other plant which will have more than one crop or yield.&quot;</span></p>
<p>Carbon Legacy Trees are regenerative. The root system survives every harvest and produces <strong style="color:var(--gl)">15 harvest cycles</strong> per tree. By statute, any plant producing more than one yield qualifies as a specified plant.</p>
<div class="callout"><strong>Confirmed:</strong> 15-cycle regenerative harvest satisfies the &sect;168(k)(5)(B)(ii) multi-yield requirement. CPA-verified.</div></div></div>
<div class="bezel rv" style="--d:1"><div class="core2"><span class="ptag">How the Election Works</span><h3>Deduction in Year of Planting</h3>
<ol class="steps4">%s%s%s%s</ol></div></div>
</div></div></section>
''' % (step(1, 'Trees are planted on project land (all 2025&ndash;2026 plantings qualify).'),
       step(2, "Investor's CPA attaches a &sect;168(k)(5) election statement to the timely-filed tax return for the planting year."),
       step(3, '<strong>100% of the tree planting cost</strong> is deducted in the year of planting, not depreciated over years. Full deduction, Year 1.'),
       step(4, 'Trees continue growing, generating carbon credits, lumber, and graphene, with zero remaining depreciation basis to recapture.'))

# math / stack
def srow(d, lab, sub, bar, fig, cls):
    w, bg, fg, txt = bar
    return ('<div class="srow" style="--d:%d"><div class="lab"><strong>%s</strong><span>%s</span></div><div class="sbar"><i style="width:%s;background:%s;color:%s;--d:%d">%s</i></div><div class="sval %s">%s</div></div>'
            % (d, lab, sub, w, bg, fg, d, txt, cls, fig))
def snote(t, extra=''):
    return '<p class="snote">%s</p>' % t
b += '''
<section class="sec dk" id="math"><div class="orb og o1" style="top:auto;bottom:-20%%;left:-10%%"></div><div class="orb oy o2" style="opacity:.35"></div><div class="gridbg"></div>
<div class="wrap">
<p class="kicker gold rv">The Math, $1M Investment Example</p>
<h2 class="rv" style="--d:1;max-width:16ch">How $1M invested produces <em class="g">$350K+</em> in Year 1 tax value</h2>
<div class="stack rv">
<div class="srow head"><span>Strategy</span><span>Deduction / Credit Value</span><span style="text-align:right">Tax Saved @ 37%%</span></div>
%s
%s
%s
%s
%s
<div class="srow total" style="--d:5"><div class="lab"><strong>COMBINED YEAR 1 TAX VALUE</strong></div><div class="sbar"><i style="width:100%%;background:linear-gradient(90deg,#B88A22,#146B3A);color:#fff;font-weight:700;--d:5">$1,000,000 invested &rarr; tax value</i></div><div class="sval gd">$385&ndash;400K</div></div>
</div>
<div class="note gold rv" style="margin-top:34px"><strong style="color:var(--goldl)">Net result:</strong> A $1M investment generates $385&ndash;400K in tax savings in Year 1 alone, before a single carbon credit is sold. The trees keep growing. Carbon credits begin at Month 18. All 15 harvest cycles and all future appreciation remain on the table.</div>
</div></section>
''' % (
 srow(0, '&sect;168(k)(5) Specified Plant Deduction', '100% of tree planting cost. Year 1', ('70%', 'linear-gradient(90deg,#B88A22,#d4a83a)', '#1E2428', '$700,000 deduction'), '<strong>$259,000</strong>', 'gd') + snote('Assumes $700K of the $1M investment is allocable to tree planting costs (as documented in partnership allocation). CPA confirms exact allocation.'),
 srow(1, '&sect;168(k) Bonus Dep.. Infrastructure', 'Irrigation, roads, monitoring equipment. 100% Year 1', ('20%', 'linear-gradient(90deg,#146B3A,#2f9a5c)', '#fff', '$200K'), '<strong>$74,000</strong>', 'gn') + snote('Cost segregation study ($5K) accelerates infrastructure into 5&ndash;15 year MACRS property, all eligible for 100% first-year expensing.'),
 srow(2, '&sect;194 Reforestation Deduction', '$10K/project &times; 10 projects, immediate', ('10%', 'rgba(110,232,162,.55)', '#fff', '$100K'), '<strong>$37,000</strong>', 'gn') + snote('Deductible in the year of planting via Form T. Remaining reforestation costs amortized over 84 months.'),
 srow(3, '&sect;48 Solar ITC', '30% credit on solar installation, actual tax credit', ('3%', '#5fa4de', '#fff', ''), '<strong>$15&ndash;30K</strong>', 'bl') + snote('The one true IRS tax credit available. 30% of solar equipment cost dollar-for-dollar off tax owed. Applies to irrigation pumps, monitoring stations, and any grid-tied or off-grid solar on project land.'),
 '')

# six plays
def play(n, tag, tcls, title, irc, body_, rows, feat=False, span='s4'):
    r = ''.join('<div class="prow%s"><span>%s</span><span>%s</span></div>' % (' hi' if hi else '', a, c) for a, c, hi in rows)
    return bez('<div class="ghost-n">%d</div><span class="ptag %s">%s</span><h3 class="%s">%s</h3><div class="pirc">%s</div><p>%s</p><div class="prows">%s</div>' % (n, tcls, tag, 'lg' if feat else '', title, irc, body_, r), span, n % 3)
PL = [
 play(1, 'Highest Impact. Year 1', 'gd', '&sect;168(k)(5) Specified Plant. 100% Bonus Depreciation', 'IRC &sect;168(k)(5)(B)(ii) &middot; OBBBA July 4, 2025',
      'NF Trees produce 15 regenerative harvest cycles, satisfying the &quot;more than one yield&quot; requirement for specified plant status. 100% of tree planting costs deducted in the tax year of planting. No phaseout. Permanent law under OBBBA. Elect via &sect;168(k)(5) statement attached to timely filed return.',
      [('On $700K planting cost', '$700,000 deduction', 0), ('Tax savings @ 37%', '$259,000 Year 1', 1), ('Requires', 'CPA election statement', 0), ('Cost to execute', '~$2K CPA time', 0), ('Law basis', 'Confirmed per OBBBA 2025', 0)], True, 's8 r2'),
 play(2, 'High Impact. Year 1', '', '&sect;168(k) Bonus Dep. on Infrastructure', 'IRC &sect;168(k) &middot; 100% first-year. OBBBA permanent',
      'Irrigation systems, access roads, monitoring equipment, fencing, and processing equipment all qualify for 100% first-year expensing. A cost segregation study ($5K) reclassifies assets into 5&ndash;15 year MACRS property to maximize the first-year deduction on every dollar of infrastructure spend.',
      [('On $200K infrastructure', '$200,000 deduction', 0), ('Tax savings @ 37%', '$74,000 Year 1', 1), ('&sect;179 stack', 'Up to $1.22M equipment expensing', 0), ('Cost seg study', '~$5K, pays 15x in Year 1', 0)], False, 's4'),
 play(3, 'Year 1. Minimal Cost', '', '&sect;194 Reforestation Deduction', 'IRC &sect;194 &middot; $10K/project immediate + 84-month amortization',
      'Available to all partners in the year of planting. $10,000 immediate deduction per qualified timber property. Remaining reforestation costs amortized over 84 months with no dollar limit. File Form T with your return. Applies to all 10 current projects simultaneously.',
      [('10 projects &times; $10K', '$100,000 Year 1', 0), ('Tax savings @ 37%', '$37,000 Year 1', 1), ('Remainder', 'Amortized 84 months', 0), ('Filing', 'Form T + Schedule C/F', 0)], False, 's4'),
 play(4, 'Year 1. Actual Tax Credit', 'bl', '&sect;48 Investment Tax Credit. Solar', 'IRC &sect;48 &middot; 30% of solar equipment cost &middot; dollar-for-dollar credit',
      'The only direct IRS tax credit (not deduction) available to the project. 30% of the cost of solar equipment, irrigation pump motors, remote monitoring power, off-grid stations, reduces your tax owed dollar-for-dollar. Not a deduction. A credit. On a $100K solar install: $30K off your tax bill.',
      [('Credit rate', '30% of qualifying solar cost', 0), ('On $100K solar', '$30,000 off tax owed, directly', 1), ('Difference from deduction', 'Dollar-for-dollar vs. rate-adjusted', 0), ('Stackable with', 'All other plays above', 0)], False, 's4'),
 play(5, 'Ongoing. Harvest Stage', 'gd', '&sect;631(b) Capital Gains + Timber Depletion', 'IRC &sect;631(b) &middot; IRC &sect;611 depletion allowance',
      'When trees are harvested (Yr 7&ndash;10 and 15 subsequent cycles), &sect;631(b) treats standing timber sale proceeds as long-term capital gains, not ordinary income. Save 17%+ vs. ordinary income rate on every harvest dollar. Layer the timber depletion allowance on top to further reduce taxable income at each harvest event.',
      [('Ordinary income rate', '37%', 0), ('LTCG rate (&sect;631b)', '20%, save 17 cents per dollar', 1), ('On $500K harvest', '$85,000 saved vs. ordinary income', 0), ('Depletion allowance', 'Additional offset at each of 15 cycles', 0)], False, 's4'),
 play(6, 'Long-Term. Zero Tax on Upside', 'gd', 'Rural Qualified Opportunity Fund (QROF)', 'IRC &sect;1400Z-2 &middot; OBBBA permanent extension &middot; 30% rural step-up',
      'If project sites are in designated rural Qualified Opportunity Zones (new designations Jan 2027), investing via a Qualified Rural Opportunity Fund gives investors: deferred capital gains on invested amount, 30% basis step-up after 5 years, and complete exclusion of all appreciation after 10 years. All carbon credit income growth and appreciation, zero federal tax events at exit.',
      [('Gain deferral', 'Until year 5 from investment', 0), ('Rural step-up', '30% of deferred gain eliminated', 1), ('10-year benefit', 'Zero tax on all appreciation', 0), ('Check eligibility', 'MI, ID, CO, MT, TX project sites', 0)], False, 's8'),
]
b += '''
<section class="sec cn" id="plays"><div class="wrap">
<div class="split"><div><p class="kicker rv">The Full Tax Stack. 6 Plays</p><h2 class="rv" style="--d:1;font-size:clamp(34px,4.8vw,72px)">Every Lever Available to Carbon Legacy Trees <em>Investors</em></h2></div>
<div style="padding-top:clamp(0px,3vw,46px)"><p class="lead rv" style="--d:2">Ranked by Year 1 impact. Plays 1&ndash;4 stack in the same tax year. Plays 5&ndash;6 compound over time.</p></div></div>
<div class="bento">%s</div>
</div></section>
''' % '\n'.join(PL)

# timeline
def tn(i, y, t, v, cls, big):
    c = 'td' + (' major' if big else '') + (' gd' if cls == 'gd' else '')
    yc = ' gd' if cls == 'gd' else ''
    return '<div class="tn rv" style="--d:%d"><div class="%s"></div><div class="y%s">%s</div><h4>%s</h4><div class="tv%s">%s</div></div>' % (i % 4, c, yc, y, t, yc, v)
TL = [('Day 1', 'Plant + Elect', '$385&ndash;400K<br>tax value', 'gd', True), ('Mo. 1&ndash;6', 'Offtake LOI<br>+ Registry', '$300&ndash;500K<br>advance', 'g', False),
      ('Mo. 6&ndash;18', 'Forward Sale<br>Yr 2&ndash;5 credits', '$990K&ndash;1.25M<br>upfront', 'g', False), ('Mo. 18', 'First VCUs<br>Issued', '$83&ndash;217K/yr<br>recurring', 'g', True),
      ('Yr 2&ndash;5', 'Credits Grow<br>+15&ndash;18%/yr', '$83&ndash;374K<br>per year', 'g', False), ('Yr 7&ndash;10', 'First Harvest<br>Event', 'Lumber +<br>Graphene +<br>Biochar $164/t', 'gd', True),
      ('Yr 10+', 'QOZ Exit<br>(if applicable)', 'Zero tax on<br>all upside', 'g', True), ('Yr 7&ndash;50+', '15 Harvest Cycles<br>+ Annual Credits', 'Perpetual<br>income stack', 'gd', False)]
tl = ''.join(tn(i, *t) for i, t in enumerate(TL))
TBL = [('hl', 'Year 1', '&sect;168(k)(5) Specified Plant Deduction', '100% bonus dep on tree cost', '$185K saved', '$259K saved', 'Deduction, offsets any income'),
       ('hl', 'Year 1', 'Infrastructure Bonus Dep + &sect;194 + &sect;48', '&sect;168(k), &sect;194, solar ITC', '$90K saved', '$126K saved', 'Deduction + actual credit'),
       ('', 'Mo. 1&ndash;6', 'Offtake advance payment', '10-yr corporate buyer deal', '$300K cash', '$500K cash', 'Ordinary income when received'),
       ('', 'Mo. 6&ndash;18', 'Forward pre-issuance credit sale', 'Verra ex-ante sale', '$990K cash', '$1.25M cash', 'Ordinary income (spread over delivery)'),
       ('', 'Mo. 18+', 'Annual VCM ARR credits. Yr 1', 'Verra VCU issuance', '$83K/yr', '$217K/yr', 'Ordinary income'),
       ('', 'Yr 2&ndash;5', 'Annual credits, growing +15&ndash;18%/yr', 'Compounding canopy', '$570K total', '$1.48M total', 'Ordinary income'),
       ('hl', 'Yr 7&ndash;10', 'First harvest: lumber + graphene + biochar CDR', '&sect;631(b) + Puro.earth CDR', 'Significant', 'Significant', 'LTCG rate (&sect;631b) + depletion offset'),
       ('', 'Yr 10+', 'QOZ exit gain exclusion', 'Rural QROF &sect;1400Z-2', '<span class="nil"></span>', '100% exclusion', 'Zero federal tax on appreciation'),
       ('tot', 'Year 1 Combined', 'Tax savings + offtake + forward sale', 'All plays stacked', '$1.56M', '$2.13M', 'On a $1M investment')]
rows = ''.join('<tr class="%s">%s</tr>' % (r[0], ''.join('<td>%s</td>' % c for c in r[1:])) for r in TBL)
b += '''
<section class="sec gr" id="return"><div class="orb og2 o1" style="opacity:.28"></div><div class="orb oy o2" style="opacity:.3;top:auto;bottom:-10%%"></div><div class="gridbg"></div>
<div class="wrap">
<div class="split"><div><p class="kicker gold rv">The Full Return Picture</p><h2 class="rv" style="--d:1">How $1M Compounds <em class="g">From Day One</em></h2></div>
<div style="padding-top:clamp(0px,3vw,46px)"><p class="lead rv" style="--d:2">Tax savings, carbon credits, and harvest events layered across a 10-year horizon. Every stream compounds independently.</p></div></div>
<div class="tl c8">%s</div>
<div class="tbl-wrap rv" style="margin-top:80px"><table>
<thead><tr><th>When</th><th>Income/Value Stream</th><th>Mechanism</th><th>Conservative</th><th>Base Case</th><th>Tax Treatment</th></tr></thead>
<tbody>%s</tbody></table></div>
<div class="note gold rv">Year 1 combined assumes the forward credit sale ($990K&ndash;$1.25M upfront) closes within the first 18 months post-planting, which requires Verra registration. Tax savings are realized in the planting tax year regardless. All projections are estimates; actual results depend on individual tax situation, project scale, and market conditions.</div>
</div></section>
''' % (tl, rows)

b += '''
<section class="sec st closing"><div class="orb og o1" style="left:auto;right:-12%%;opacity:.16"></div><div class="wrap">
<p class="kicker gold rv">Ready to Invest</p>
<h2 class="rv" style="--d:1;font-size:clamp(34px,5.6vw,84px);max-width:16ch">Talk to Our Team About the Tax Strategy for <em>Your Situation</em></h2>
<p class="lead rv" style="--d:2">Every investor's tax picture is different. We work with your CPA to document the &sect;168(k)(5) election properly, identify your applicable QOZ projects, and structure the investment to maximize Year 1 value.</p>
<div class="cta rv" style="--d:3">%s%s</div>
</div></section>
''' % (btn('/#contact', 'Schedule a Call', 'gold'), btn('/#invest', 'Learn About Investing', 'ghost'))

b += footer(False, LEGAL) + '\n' + FX + '\n</body>\n</html>\n'
open(os.path.join(ROOT, 'tax-strategy.html'), 'w').write(b)
print('tax', len(b))
