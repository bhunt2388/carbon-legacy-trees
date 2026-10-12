# Shared design system for Carbon Legacy Trees (home + tax strategy).
# Mechanics adapted from the Kreative Brands build system, re-tokenized to the CLT brand kit.
# Palette ratios per kit: ~70% stone/white, 15% navy, 8% green, 4% slate/black, 3% gold.

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17L17 7M8 7h9v9"/></svg>'

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..800;1,400..700&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">')

CSS = r"""
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{--navy:#0B2545;--navy2:#0F2F57;--navy0:#071A33;--green:#146B3A;--greend:#0C3B22;--greend2:#11492B;--gold:#B88A22;--goldl:#D4A83A;--stone:#F7F5F0;--canopy:#EEF0EC;--slate:#334155;--ink:#1E2428;--leaf:#6ee8a2;
--serif:'Playfair Display',Georgia,'Times New Roman',serif;--sans:'Inter',system-ui,-apple-system,sans-serif;--mono:'JetBrains Mono',ui-monospace,Menlo,monospace;--ease:cubic-bezier(.32,.72,0,1)}
html{background:var(--navy);color:var(--ink);font-family:var(--sans);-webkit-font-smoothing:antialiased;scroll-behavior:smooth;scroll-padding-top:96px}
body{background:var(--stone);color:var(--ink);overflow-x:hidden;font-size:16px;line-height:1.6}
a{color:inherit}
img{max-width:100%}
::selection{background:var(--green);color:#fff}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:90;opacity:.045;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible{outline:2px solid var(--green);outline-offset:3px}
.dk a:focus-visible,.gr a:focus-visible,nav a:focus-visible,nav button:focus-visible,footer a:focus-visible,.dk button:focus-visible{outline-color:var(--leaf)}
.wrap{max-width:1240px;margin:0 auto;padding:0 32px;position:relative}
/* surfaces */
.st{--bg:var(--stone);--bg2:#fff;--fg:var(--ink);--mute:var(--slate);--line:rgba(11,37,69,.16);--card:rgba(11,37,69,.045);--acc:var(--green);--gl:#7a5608;--chip:var(--green);--chipfg:#fff;--btnbg:var(--navy);--btnfg:#fff}
.cn{--bg:var(--canopy);--bg2:#fff;--fg:var(--ink);--mute:var(--slate);--line:rgba(11,37,69,.14);--card:rgba(11,37,69,.05);--acc:var(--green);--gl:#8a6210;--chip:var(--green);--chipfg:#fff;--btnbg:var(--navy);--btnfg:#fff}
.dk{--bg:var(--navy);--bg2:var(--navy2);--fg:#fff;--mute:rgba(255,255,255,.7);--line:rgba(255,255,255,.14);--card:rgba(255,255,255,.04);--acc:var(--leaf);--gl:var(--goldl);--chip:var(--green);--chipfg:#fff;--btnbg:var(--stone);--btnfg:var(--navy)}
.gr{--bg:var(--greend);--bg2:var(--greend2);--fg:#fff;--mute:rgba(255,255,255,.72);--line:rgba(255,255,255,.16);--card:rgba(255,255,255,.05);--acc:var(--leaf);--gl:var(--goldl);--chip:var(--goldl);--chipfg:var(--navy);--btnbg:var(--stone);--btnfg:var(--navy)}
.sec{position:relative;background:var(--bg);color:var(--fg);padding:clamp(72px,9vw,128px) 0;overflow:hidden}
.sec.tight{padding-top:0}
.sec>.wrap{z-index:2}
/* kicker: plain ruled editorial label, no container */
.kicker{display:flex;align-items:center;gap:14px;font-family:var(--mono);font-size:11.5px;font-weight:500;letter-spacing:.18em;text-transform:uppercase;color:var(--mute);margin:0}
.kicker::before{content:"";width:34px;height:2px;background:var(--acc);flex:none}
.kicker.gold::before{background:var(--gl)}
/* nav */
nav.nav{position:fixed;top:16px;left:50%;transform:translateX(-50%);z-index:80;width:min(1240px,calc(100% - 28px));border-radius:20px;background:rgba(11,37,69,.78);backdrop-filter:blur(18px) saturate(1.4);-webkit-backdrop-filter:blur(18px) saturate(1.4);border:1px solid rgba(255,255,255,.14);color:#fff;box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 18px 50px -20px rgba(7,26,51,.6);transition:background .6s var(--ease)}
nav.nav.scrolled{background:rgba(11,37,69,.94)}
nav .in{display:flex;align-items:center;justify-content:space-between;gap:18px;padding:8px 8px 8px 20px}
.mark{display:flex;align-items:center;gap:12px;text-decoration:none;color:#fff;font-family:var(--serif);font-size:19px;font-weight:500;letter-spacing:-.005em;white-space:nowrap}
.mark img{height:34px;width:auto;filter:brightness(0) invert(1);display:block}
nav .links{display:flex;gap:24px;align-items:center;list-style:none}
nav .links a.t{font-size:13px;text-decoration:none;color:rgba(255,255,255,.7);transition:color .5s var(--ease);white-space:nowrap}
nav .links a.t:hover,nav .links a.t.act{color:#fff}
nav .links a.t.act{box-shadow:0 2px 0 var(--leaf);padding-bottom:3px}
.nav-toggle{display:none;width:44px;height:44px;border-radius:12px;border:1px solid rgba(255,255,255,.18);background:rgba(255,255,255,.06);cursor:pointer;position:relative;color:#fff}
.nav-toggle span{position:absolute;left:13px;right:13px;height:2px;border-radius:2px;background:#fff;transition:transform .5s var(--ease),opacity .3s}
.nav-toggle span:nth-child(1){top:16px}.nav-toggle span:nth-child(2){top:21px}.nav-toggle span:nth-child(3){top:26px}
nav.menu-open .nav-toggle span:nth-child(1){transform:translateY(5px) rotate(45deg)}
nav.menu-open .nav-toggle span:nth-child(2){opacity:0}
nav.menu-open .nav-toggle span:nth-child(3){transform:translateY(-5px) rotate(-45deg)}
#progress-bar{position:fixed;top:0;left:0;height:2px;width:0;background:linear-gradient(90deg,var(--green),var(--leaf));z-index:95}
/* buttons: label + nested rounded-square chip */
.btn{display:inline-flex;align-items:center;gap:14px;background:var(--btnbg);color:var(--btnfg)!important;padding:8px 8px 8px 24px;border-radius:14px;font-family:var(--sans);font-weight:600;font-size:14px;text-decoration:none;border:none;cursor:pointer;transition:transform .6s var(--ease),background .6s var(--ease),box-shadow .6s var(--ease);will-change:transform}
.btn .ic{width:36px;height:36px;border-radius:9px;background:var(--chip);color:var(--chipfg);display:grid;place-items:center;flex:none;transition:transform .6s var(--ease)}
.btn .ic svg{width:15px;height:15px}
.btn:hover .ic{transform:translate(3px,-2px) scale(1.06)}
.btn:active{transform:scale(.98)}
.btn.sm{padding:6px 6px 6px 18px;font-size:13px}.btn.sm .ic{width:30px;height:30px}
.btn.gold{--chip:var(--gold);--chipfg:#fff}
.dk .btn.gold,.gr .btn.gold{--chip:var(--goldl);--chipfg:var(--navy)}
.btn.ghost{background:transparent;color:var(--fg)!important;box-shadow:inset 0 0 0 1px var(--line);padding-right:24px}
.btn.ghost:hover{background:var(--card)}
.nav-cta{--btnbg:var(--stone);--btnfg:var(--navy);--chip:var(--green);--chipfg:#fff}
button.btn[type=submit]{width:100%;justify-content:space-between}
button.btn:disabled{opacity:.7;cursor:not-allowed}
/* reveal: blur-up with stagger, visible when JS fails */
.js .rv{opacity:0;transform:translateY(46px);filter:blur(10px);transition:opacity 1.1s var(--ease),transform 1.1s var(--ease),filter 1.1s var(--ease);transition-delay:calc(var(--d,0)*90ms)}
.js .rv.on{opacity:1;transform:none;filter:none}
/* ambient layer */
.orb{position:absolute;border-radius:50%;filter:blur(90px);will-change:transform;pointer-events:none;z-index:1}
.og{background:radial-gradient(circle,rgba(20,107,58,.7),transparent 65%)}
.og2{background:radial-gradient(circle,rgba(110,232,162,.32),transparent 65%)}
.oy{background:radial-gradient(circle,rgba(184,138,34,.34),transparent 65%)}
.ob{background:radial-gradient(circle,rgba(30,90,170,.4),transparent 65%)}
.o1{width:60vw;height:60vw;max-width:760px;max-height:760px;left:-14%;top:-20%;animation:fl1 16s var(--ease) infinite alternate}
.o2{width:50vw;height:50vw;max-width:640px;max-height:640px;right:-10%;top:12%;animation:fl2 19s var(--ease) infinite alternate}
.o3{width:38vw;height:38vw;max-width:480px;max-height:480px;left:38%;bottom:-24%;animation:fl1 22s var(--ease) infinite alternate-reverse}
@keyframes fl1{to{transform:translate3d(8vw,6vh,0) scale(1.18)}}
@keyframes fl2{to{transform:translate3d(-9vw,8vh,0) scale(1.12)}}
.gridbg{position:absolute;inset:0;z-index:1;pointer-events:none;background-image:linear-gradient(var(--line) 1px,transparent 1px),linear-gradient(90deg,var(--line) 1px,transparent 1px);background-size:72px 72px;opacity:.55;-webkit-mask-image:radial-gradient(ellipse 70% 60% at 50% 40%,#000,transparent 75%);mask-image:radial-gradient(ellipse 70% 60% at 50% 40%,#000,transparent 75%)}
.cn .orb,.st .orb{filter:blur(100px);opacity:.5}
/* hero */
.hero{position:relative;min-height:100svh;display:flex;flex-direction:column;justify-content:center;overflow:hidden;padding:112px 0 72px;background:var(--navy);color:#fff}
.hero-bg{position:absolute;inset:0;z-index:0;background:var(--navy)}
#gl{position:absolute;inset:0;width:100%;height:100%;display:block}
.hero-wash{position:absolute;inset:0;z-index:1;pointer-events:none;background:linear-gradient(100deg,rgba(11,37,69,.94) 0%,rgba(11,37,69,.8) 46%,rgba(11,37,69,.34) 100%),linear-gradient(0deg,var(--navy) 0%,transparent 28%)}
#vignette{position:absolute;inset:0;pointer-events:none;background:radial-gradient(120% 120% at 50% 38%,transparent 52%,rgba(0,0,0,.38) 100%);z-index:2}
#flash{position:absolute;inset:0;pointer-events:none;z-index:2;background:#05070d;opacity:0;transition:opacity .42s ease}
#flash.on{opacity:.55;transition:opacity .08s ease}
.clt-ui{display:none!important}
.hero .orb,.hero .gridbg{z-index:2}
.hero .wrap{z-index:4}
.hwm{position:absolute;right:-4%;top:50%;width:min(44vw,620px);height:auto;transform:translateY(-52%);opacity:.07;filter:brightness(0) invert(1);pointer-events:none;z-index:3;animation:kf 14s var(--ease) infinite alternate}
@keyframes kf{to{transform:translateY(-56%) rotate(2.5deg)}}
.hero .kicker{color:rgba(255,255,255,.78)}
.hero .kicker::before{background:var(--leaf)}
h1,h2,h3,h4{font-family:var(--serif);font-weight:500}
h1{font-size:clamp(42px,min(9vw,10.5vh),128px);line-height:.94;letter-spacing:-.03em;margin:26px 0 30px;max-width:11.5em}
h1 .ln{display:block;overflow:hidden;padding-bottom:.1em;margin-bottom:-.04em}
h1 .ln span{display:block}
.js h1 .ln span{transform:translateY(112%);transition:transform 1.4s var(--ease);transition-delay:calc(var(--d,0)*120ms + 200ms)}
.js.on-load h1 .ln span,.on-load h1 .ln span{transform:none}
h1 em{font-style:italic;font-weight:500;background:linear-gradient(100deg,#B88A22,#E3BE5C 55%,#B88A22);-webkit-background-clip:text;background-clip:text;color:transparent;padding-right:.08em}
.lead{font-size:clamp(17px,1.5vw,20px);line-height:1.65;color:var(--mute);max-width:62ch}
.hero .lead{color:rgba(255,255,255,.8);max-width:70ch}
.cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:34px}
.hero .rv{transition-delay:calc(var(--d,0)*110ms + 500ms)}
.js .on-load .hero .rv,.on-load .hero .rv{opacity:1;transform:none;filter:none}
.hero .btn.ghost{box-shadow:inset 0 0 0 1px rgba(255,255,255,.4);background:rgba(11,37,69,.35)}
.hstats{display:grid;grid-template-columns:repeat(4,1fr);margin-top:clamp(28px,5vh,56px);border-top:1px solid rgba(255,255,255,.18)}
.hstat{padding:22px 24px 0 0;position:relative}
.hstat+.hstat{padding-left:24px;border-left:1px solid rgba(255,255,255,.12)}
.hstat b{display:block;font-family:var(--serif);font-weight:500;font-size:clamp(34px,4.2vw,60px);line-height:1;letter-spacing:-.02em;color:#fff}
.hstat b.gold{color:var(--goldl)}
.hstat span{display:block;margin-top:10px;font-family:var(--mono);font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.8)}
.scrollcue{position:absolute;left:32px;bottom:34px;z-index:4;font-family:var(--mono);font-size:10px;letter-spacing:.24em;text-transform:uppercase;color:rgba(255,255,255,.6);display:flex;align-items:center;gap:12px}
.scrollcue::after{content:"";width:46px;height:1px;background:linear-gradient(90deg,#fff,transparent);transform-origin:left;animation:cue 2.4s var(--ease) infinite}
@keyframes cue{0%{transform:scaleX(0)}60%{transform:scaleX(1);opacity:1}100%{transform:scaleX(1);opacity:0}}
/* marquee */
.marq{background:var(--navy0);border-block:1px solid rgba(255,255,255,.12);overflow:hidden;padding:30px 0;color:#fff;position:relative;z-index:3}
.track{display:flex;gap:56px;width:max-content;animation:mq 46s linear infinite}
.track span{font-family:var(--serif);font-weight:500;font-style:italic;font-size:clamp(30px,4vw,56px);letter-spacing:-.015em;white-space:nowrap;display:flex;align-items:center;gap:56px}
.track span::after{content:"";width:44px;height:2px;background:var(--goldl);flex:none}
@keyframes mq{to{transform:translateX(-50%)}}
/* headings */
h2{font-size:clamp(36px,5.6vw,88px);line-height:1.02;letter-spacing:-.025em;margin:22px 0 26px;text-wrap:balance}
h2 em{font-style:italic;color:var(--acc)}
h2 em.g{color:var(--gl)}
.big{font-family:var(--serif);font-weight:500;font-size:clamp(30px,4.6vw,66px);line-height:1.08;letter-spacing:-.02em}
/* scroll-lit statement */
.statement{font-family:var(--serif);font-weight:500;font-size:clamp(26px,3.5vw,52px);line-height:1.18;letter-spacing:-.015em;max-width:30ch}
.statement .w{color:color-mix(in srgb,var(--fg) 20%,transparent);transition:color .9s var(--ease)}
.statement .w.on{color:var(--fg)}
.statement .w.hl.on{color:var(--acc);font-style:italic}
.wide-st{max-width:28ch}
/* split + stats strip */
.split{display:grid;grid-template-columns:5fr 7fr;gap:72px;align-items:start}
.strip{display:grid;grid-template-columns:repeat(5,1fr);border-block:1px solid var(--line)}
.strip>div{padding:38px 26px 34px 0}
.strip>div+div{padding-left:26px;border-left:1px solid var(--line)}
.strip b{display:block;font-family:var(--serif);font-weight:500;font-size:clamp(40px,5.2vw,78px);line-height:1;letter-spacing:-.03em;color:var(--fg)}
.strip b.gold{color:var(--gl)}
.strip span{display:block;margin-top:14px;font-family:var(--mono);font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--mute);line-height:1.6}
/* bezel + bento */
.bezel{padding:7px;border-radius:2rem;background:var(--card);border:1px solid var(--line)}
.core2{border-radius:calc(2rem - 7px);background:var(--bg2);box-shadow:inset 0 1px 1px rgba(255,255,255,.14);padding:34px;height:100%;position:relative;overflow:hidden}
.st .core2,.cn .core2{box-shadow:inset 0 1px 1px #fff,0 1px 2px rgba(11,37,69,.05)}
.core2::before{content:"";position:absolute;inset:0;background:radial-gradient(420px circle at var(--mx,50%) var(--my,-30%),color-mix(in srgb,var(--acc) 22%,transparent),transparent 60%);opacity:0;transition:opacity .6s var(--ease);pointer-events:none}
.bezel:hover .core2::before{opacity:1}
.bento{display:grid;grid-template-columns:repeat(12,1fr);gap:16px;margin-top:64px}
.s3{grid-column:span 3}.s4{grid-column:span 4}.s5{grid-column:span 5}.s6{grid-column:span 6}.s7{grid-column:span 7}.s8{grid-column:span 8}.s12{grid-column:span 12}
.r2{grid-row:span 2}
.core2 .n{font-family:var(--mono);font-size:11px;letter-spacing:.2em;color:var(--acc);margin-bottom:22px;display:block;text-transform:uppercase}
.st .core2 .n,.cn .core2 .n{color:var(--green)}
.core2 h3{font-size:clamp(24px,2.5vw,36px);line-height:1.08;margin-bottom:14px;letter-spacing:-.015em}
.core2 h3.lg{font-size:clamp(30px,3.6vw,52px)}
.core2 p{font-size:15px;line-height:1.7;color:var(--mute);max-width:52ch}
.core2 p+p{margin-top:14px}
.cstat{margin-top:26px;padding-top:16px;border-top:1px solid var(--line);font-family:var(--mono);font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--fg);line-height:1.6}
.cstat.gd{color:var(--gl)}
.core2 .ico{width:46px;height:46px;border-radius:12px;display:grid;place-items:center;background:var(--card);box-shadow:inset 0 0 0 1px var(--line);margin-bottom:24px;color:var(--acc)}
.st .core2 .ico,.cn .core2 .ico{color:var(--green)}
.core2 .ico.gd{color:var(--gl)}
.core2 .ico svg{width:22px;height:22px}
.loop{display:grid;grid-template-columns:repeat(5,1fr);gap:0;margin-top:30px;border:1px solid var(--line);border-radius:18px;overflow:hidden}
.loop div{padding:18px 18px;font-family:var(--serif);font-weight:500;font-size:19px;line-height:1.2;border-left:1px solid var(--line)}
.loop div:first-child{border-left:0}
.loop div small{display:block;font-family:var(--mono);font-size:10px;letter-spacing:.18em;color:var(--acc);margin-bottom:8px;font-weight:400}
.st .loop small,.cn .loop small{color:var(--green)}
/* feature (image) */
.feat{display:grid;grid-template-columns:7fr 5fr;gap:56px;align-items:center}
.feat.flip{grid-template-columns:5fr 7fr}
.feat.flip .fimg{order:2}
.fimg{position:relative}
.fimg .bezel{padding:8px;border-radius:2.2rem}
.fimg .imgcore{border-radius:calc(2.2rem - 8px);overflow:hidden;box-shadow:inset 0 1px 1px rgba(255,255,255,.2);aspect-ratio:16/10;background:var(--navy)}
.fimg img{width:100%;height:100%;object-fit:cover;display:block;transform:scale(1.08);transition:transform 1.6s var(--ease)}
.fimg:hover img{transform:scale(1.14)}
.fimg .tag{position:absolute;left:28px;bottom:28px;font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;color:#fff;text-shadow:0 1px 12px rgba(0,0,0,.6)}
.rows{margin-top:34px;border-top:1px solid var(--line)}
.rows>div{display:flex;justify-content:space-between;gap:20px;align-items:baseline;padding:14px 0;border-bottom:1px solid var(--line)}
.rows .l{font-family:var(--mono);font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--mute)}
.rows .v{font-family:var(--serif);font-weight:500;font-size:19px;text-align:right;color:var(--fg)}
.rows .v.gd{color:var(--gl)}.rows .v.gn{color:var(--acc)}
.st .rows .v.gn,.cn .rows .v.gn{color:var(--green)}
/* hub diagram */
.hubwrap{display:grid;grid-template-columns:1fr 1.05fr;gap:64px;align-items:center}
.hub{position:relative;width:100%;max-width:600px;aspect-ratio:1;margin:0 auto}
.hub svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.hub .spoke{stroke:rgba(110,232,162,.7);stroke-width:.28;stroke-dasharray:1.2 1.6;animation:flow 3s linear infinite}
.hub .spoke.gd{stroke:rgba(212,168,58,.8)}
@keyframes flow{to{stroke-dashoffset:-5.6}}
.hub .ringa{transform-origin:50% 50%;animation:spin 60s linear infinite}
.hub .ringb{transform-origin:50% 50%;animation:spin 90s linear infinite reverse}
@keyframes spin{to{transform:rotate(360deg)}}
.hcore{position:absolute;left:50%;top:50%;width:27%;aspect-ratio:1;transform:translate(-50%,-50%);border-radius:50%;display:grid;place-items:center;background:radial-gradient(circle at 30% 25%,#1a8a4c,#146B3A 58%,#0C3B22);box-shadow:0 0 0 10px rgba(110,232,162,.1),0 0 90px rgba(20,107,58,.7);animation:pulse 4s var(--ease) infinite}
.hcore img{width:62%;height:auto;display:block;filter:brightness(0) invert(1)}
@keyframes pulse{50%{box-shadow:0 0 0 18px rgba(110,232,162,.06),0 0 120px rgba(20,107,58,.9)}}
.node{position:absolute;transform:translate(-50%,-50%);padding:11px 16px;border-radius:14px;background:rgba(15,47,87,.88);border:1px solid rgba(255,255,255,.18);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);transition:transform .6s var(--ease),border-color .6s var(--ease);width:max-content;max-width:42%}
.node:hover{transform:translate(-50%,-50%) scale(1.06);border-color:var(--leaf)}
.node small{display:block;font-family:var(--mono);font-size:10px;letter-spacing:.2em;color:var(--leaf);margin-bottom:4px}
.node.gd small{color:var(--goldl)}
.node b{display:block;font-family:var(--serif);font-weight:500;font-size:clamp(13px,1.35vw,17px);line-height:1.15;color:#fff}
/* revenue cards */
.revs{display:grid;grid-template-columns:repeat(12,1fr);gap:16px;margin-top:84px}
.rfig{margin-top:26px;font-family:var(--serif);font-weight:500;font-size:clamp(26px,2.8vw,40px);line-height:1.05;letter-spacing:-.02em;color:var(--fg)}
.rfig small{display:block;margin-top:8px;font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--mute);font-weight:400}
.rtype{position:absolute;top:34px;right:34px;font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;color:var(--mute)}
.rtype.gd{color:var(--gl)}
/* table */
.tblbox{margin-top:70px}
.tblbox h3{font-size:clamp(26px,3vw,40px);margin:18px 0 26px;letter-spacing:-.02em}
.tbl-wrap{overflow-x:auto;border-radius:1.6rem;border:1px solid var(--line);background:var(--card);padding:7px;-webkit-overflow-scrolling:touch}
.tbl-wrap table{width:100%;min-width:780px;border-collapse:separate;border-spacing:0;background:var(--bg2);border-radius:calc(1.6rem - 7px);overflow:hidden;box-shadow:inset 0 1px 1px rgba(255,255,255,.14)}
.tbl-wrap th{font-family:var(--mono);font-weight:500;font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;text-align:left;padding:18px 20px;color:var(--mute);border-bottom:1px solid var(--line);white-space:nowrap}
.tbl-wrap td{padding:17px 20px;font-size:14.5px;line-height:1.5;border-bottom:1px solid var(--line);color:var(--fg);vertical-align:top}
.tbl-wrap tr:last-child td{border-bottom:0}
.tbl-wrap td:first-child{font-family:var(--serif);font-weight:500;font-size:16.5px}
.tbl-wrap td.gn{color:var(--acc)}.tbl-wrap td.gd{color:var(--gl)}
.tbl-wrap tr.hl td{background:color-mix(in srgb,var(--acc) 9%,transparent)}
.tbl-wrap tr.tot td{font-family:var(--serif);font-weight:500;font-size:17px;border-top:1px solid var(--line);background:color-mix(in srgb,var(--gl) 12%,transparent)}
.nil{display:inline-block;width:18px;height:2px;background:var(--mute);vertical-align:middle;opacity:.6}
.fine{font-size:12.5px;line-height:1.7;color:var(--mute);margin-top:16px;max-width:80ch}
.note{margin-top:22px;padding:18px 22px;border-radius:16px;border:1px solid var(--line);background:var(--card);font-size:13.5px;line-height:1.7;color:var(--mute)}
.note.gold{border-color:color-mix(in srgb,var(--gl) 55%,transparent)}
/* timeline */
.tl{position:relative;margin-top:84px;display:grid;gap:0}
.tl::before{content:"";position:absolute;left:0;right:0;top:9px;height:1px;background:var(--line)}
.tl::after{content:"";position:absolute;left:0;top:9px;height:2px;width:100%;background:linear-gradient(90deg,var(--green),var(--gl));transform:scaleX(0);transform-origin:left;transition:transform 2.6s var(--ease) .3s}
.dk .tl::after,.gr .tl::after{background:linear-gradient(90deg,var(--leaf),var(--goldl))}
.tl.on::after{transform:scaleX(1)}
.tl.c7{grid-template-columns:repeat(7,1fr)}
.tl.c8{grid-template-columns:repeat(8,1fr)}
.tn{position:relative;padding-right:14px}
.td{width:19px;height:19px;border-radius:6px;background:var(--bg);border:2px solid var(--acc);position:relative;z-index:2;margin-bottom:26px;transition:transform .6s var(--ease)}
.st .td,.cn .td{border-color:var(--green)}
.td.major{background:var(--acc);transform:rotate(45deg)}
.st .td.major,.cn .td.major{background:var(--green)}
.td.gd{border-color:var(--gl);background:var(--gl)}
.tn .y{font-family:var(--mono);font-size:13px;letter-spacing:.14em;color:var(--acc);text-transform:uppercase;margin-bottom:8px}
.st .tn .y,.cn .tn .y{color:var(--green)}
.tn .y.gd{color:var(--gl)}
.tn h4{font-family:var(--serif);font-weight:500;font-size:22px;line-height:1.2;letter-spacing:-.01em;margin-bottom:8px}
.tn p{font-size:13.5px;line-height:1.6;color:var(--mute)}
.tn .tv{font-family:var(--serif);font-weight:500;font-size:17px;line-height:1.25;margin-top:10px;color:var(--acc)}
.st .tn .tv,.cn .tn .tv{color:var(--green)}
.tn .tv.gd{color:var(--gl)}
/* process */
.proc{display:grid;grid-template-columns:repeat(4,1fr);gap:0;margin-top:70px;position:relative}
.proc::before{content:"";position:absolute;left:0;right:0;top:27px;height:1px;background:var(--line)}
.proc::after{content:"";position:absolute;left:0;top:27px;height:2px;width:100%;background:var(--green);transform:scaleX(0);transform-origin:left;transition:transform 2.4s var(--ease) .3s}
.proc.on::after{transform:scaleX(1)}
.ps{position:relative;padding-right:28px}
.psn{width:55px;height:55px;border-radius:14px;background:var(--bg);border:1px solid var(--line);display:grid;place-items:center;font-family:var(--mono);font-size:13px;position:relative;z-index:2;margin-bottom:26px;color:var(--acc);box-shadow:0 0 0 6px var(--bg)}
.ps h4{font-size:25px;line-height:1.15;margin-bottom:12px;letter-spacing:-.015em}
.ps p{font-size:15px;line-height:1.7;color:var(--mute)}
/* audience tabs */
.tabs{display:inline-flex;gap:6px;margin:54px 0 30px;padding:6px;border-radius:18px;background:var(--card);border:1px solid var(--line);flex-wrap:wrap}
.tab{font-family:var(--sans);font-weight:600;font-size:14px;padding:12px 22px;border-radius:12px;border:0;background:transparent;color:var(--mute);cursor:pointer;transition:background .5s var(--ease),color .5s var(--ease)}
.tab:hover{color:var(--fg)}
.tab.active{background:var(--navy);color:#fff;box-shadow:inset 0 1px 0 rgba(255,255,255,.14)}
.pane{display:none}
.pane.active{display:block;animation:paneIn .8s var(--ease)}
@keyframes paneIn{from{opacity:0;transform:translateY(18px);filter:blur(6px)}to{opacity:1;transform:none;filter:none}}
.aud{display:grid;grid-template-columns:7fr 5fr;gap:16px}
.aud h3{font-size:clamp(28px,3.4vw,48px);line-height:1.05;letter-spacing:-.02em;margin:20px 0 18px}
.points{list-style:none;margin:28px 0 34px;border-top:1px solid var(--line)}
.points li{position:relative;padding:14px 0 14px 34px;border-bottom:1px solid var(--line);font-size:15px;line-height:1.6;color:var(--ink)}
.points li::before{content:"";position:absolute;left:0;top:25px;width:18px;height:2px;background:var(--green)}
.boxt{font-family:var(--mono);font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--green);margin-bottom:8px}
.pane .rows{margin-top:10px}
/* about */
.mlead{font-family:var(--serif);font-weight:500;font-size:clamp(30px,4.6vw,68px);line-height:1.06;letter-spacing:-.025em;max-width:20ch;margin-top:44px}
.mlead em{color:var(--green)}
.mbody{display:grid;grid-template-columns:1fr 1fr;gap:28px 64px;margin-top:64px}
.mbody p{font-size:16.5px;line-height:1.8;color:var(--slate)}
.mbody p strong{color:var(--ink);font-weight:600}
.mbody p.mclose{font-family:var(--serif);font-weight:500;font-size:clamp(22px,2.2vw,30px);line-height:1.3;color:var(--ink);grid-column:1/-1;max-width:34ch}
.distilled{margin-top:70px}
.distilled .core2{padding:clamp(28px,4vw,56px)}
.distilled p{font-family:var(--serif);font-weight:500;font-size:clamp(20px,2.3vw,32px);line-height:1.35;color:#fff;max-width:46ch;letter-spacing:-.01em}
.distilled .core2{background:var(--navy);box-shadow:inset 0 1px 1px rgba(255,255,255,.14)}
.distilled .bezel{background:rgba(11,37,69,.08)}
.pnum{font-family:var(--mono);font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--green);margin-bottom:20px;display:block}
.core2 .pt{font-family:var(--serif);font-weight:500;font-size:clamp(20px,1.9vw,26px);line-height:1.18;letter-spacing:-.01em;margin-bottom:12px;color:var(--fg)}
/* closing statement */
.closing{padding:clamp(110px,15vw,210px) 0}
.closing .sub{margin-top:44px;font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--mute);line-height:1.8;max-width:70ch}
/* contact */
.two{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:start}
.cinfo{margin-top:38px;border-top:1px solid var(--line)}
.cinfo div{display:flex;align-items:center;gap:16px;padding:16px 0;border-bottom:1px solid var(--line);font-size:16px}
.cinfo svg{width:20px;height:20px;color:var(--green);flex:none}
.formin{padding:36px}
.formhead{font-family:var(--serif);font-weight:500;font-size:clamp(26px,2.6vw,36px);line-height:1.1;letter-spacing:-.015em;margin-bottom:8px}
.formsub{font-size:14.5px;color:var(--mute);margin-bottom:26px}
form{display:flex;flex-direction:column;gap:18px}
label.l{font-family:var(--mono);font-size:10px;letter-spacing:.22em;text-transform:uppercase;color:var(--mute);display:block;margin-bottom:8px}
input[type=text],input[type=tel],input[type=email],select,textarea{width:100%;background:var(--stone);border:1px solid var(--line);padding:14px 16px;font-family:var(--sans);font-size:15px;color:var(--ink);outline:none;border-radius:14px;transition:border-color .5s var(--ease),background .5s var(--ease);-webkit-appearance:none;appearance:none}
select{background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' fill='none' stroke='%23334155' stroke-width='1.6'%3E%3Cpath d='M1 1.5l5 5 5-5'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 16px center;padding-right:40px}
input:focus,select:focus,textarea:focus{border-color:var(--green);background:#fff}
textarea{min-height:120px;resize:vertical}
.row{display:grid;grid-template-columns:1fr 1fr;gap:16px}
/* network (our companies) */
.net-k{display:flex;align-items:center;gap:14px;font-family:var(--mono);font-size:11.5px;font-weight:500;letter-spacing:.18em;text-transform:uppercase;color:var(--mute)}
.net-k::before{content:"";width:34px;height:2px;background:var(--green);flex:none}
.net-top{display:grid;grid-template-columns:7fr 5fr;gap:0 64px;align-items:end;margin-bottom:56px}
.net-top h2{margin:22px 0 0;font-size:clamp(34px,4.8vw,70px)}
.net-top p{color:var(--slate);font-size:17px;line-height:1.7;max-width:40ch}
.net-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:16px}
.net-grid .bezel{grid-column:span 2;padding:7px;border-radius:2rem;background:var(--card);border:1px solid var(--line);transition:transform .6s var(--ease)}
.net-grid .bezel:nth-child(1),.net-grid .bezel:nth-child(2){grid-column:span 3}
.net-grid .bezel:hover{transform:translateY(-4px)}
.net-card{display:flex;flex-direction:column;gap:12px;height:100%;padding:32px;border-radius:calc(2rem - 7px);background:#fff;color:var(--navy);text-decoration:none;position:relative;overflow:hidden;box-shadow:inset 0 1px 1px #fff,0 1px 2px rgba(11,37,69,.05)}
.net-card::before{content:"";position:absolute;inset:0;background:radial-gradient(420px circle at var(--mx,50%) var(--my,-30%),rgba(20,107,58,.14),transparent 60%);opacity:0;transition:opacity .6s var(--ease);pointer-events:none}
.net-grid .bezel:hover .net-card::before{opacity:1}
.net-card:focus-visible{outline:2px solid var(--green);outline-offset:2px}
.net-n{font-family:var(--mono);font-size:11px;letter-spacing:.2em;color:var(--green)}
.net-name{font-family:var(--serif);font-weight:500;font-size:clamp(24px,2.4vw,34px);line-height:1.1;letter-spacing:-.015em;color:var(--navy)}
.net-desc{font-size:15px;line-height:1.7;color:var(--slate);max-width:44ch}
.net-go{margin-top:auto;padding-top:22px;display:flex;align-items:center;justify-content:space-between;font-size:14px;font-weight:600;color:var(--navy)}
.net-go::after{content:"";width:34px;height:34px;border-radius:9px;background:var(--green) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M7 17L17 7M8 7h9v9'/%3E%3C/svg%3E") center/15px no-repeat;transition:transform .6s var(--ease)}
.net-card:hover .net-go::after{transform:translate(3px,-2px) scale(1.06)}
/* footer */
footer.foot{background:var(--navy);color:rgba(255,255,255,.72);padding:96px 0 40px;position:relative;overflow:hidden}
footer .grid{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:48px;margin-bottom:56px;position:relative;z-index:2}
footer .brand img{height:64px;width:auto;max-width:240px;object-fit:contain;filter:brightness(0) invert(1);display:block;margin-bottom:20px}
footer .brand p{font-size:14.5px;line-height:1.75;max-width:38ch;color:rgba(255,255,255,.7)}
footer h4{font-family:var(--mono);font-weight:500;font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;color:#fff;margin-bottom:18px}
footer ul{list-style:none;display:grid;gap:11px}
footer ul a{font-size:14px;color:rgba(255,255,255,.66);text-decoration:none;transition:color .5s var(--ease)}
footer ul a:hover{color:var(--leaf)}
footer .bot{padding-top:26px;border-top:1px solid rgba(255,255,255,.14);display:flex;flex-wrap:wrap;justify-content:space-between;gap:12px;position:relative;z-index:2}
footer .bot p{font-size:12.5px;color:rgba(255,255,255,.55)}
footer .legal{font-size:12px;line-height:1.8;color:rgba(255,255,255,.5);margin-top:14px;max-width:110ch;position:relative;z-index:2}
/* tax page */
.thero{padding:128px 0 90px}
.thero h1{font-size:clamp(38px,min(7.2vw,12.5vh),104px);max-width:none}
.thero h1 .ln{white-space:nowrap}
@media(max-width:700px){.thero h1 .ln{white-space:normal}.thero h1{font-size:clamp(36px,10vw,60px)}}
.stack{margin-top:50px}
.srow{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1.5fr) minmax(0,.7fr);gap:28px;align-items:center;padding:22px 0;border-top:1px solid var(--line)}
.srow.head{padding:0 0 14px;border-top:0;font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--mute)}
.srow .lab strong{font-family:var(--serif);font-weight:500;font-size:19px;line-height:1.2;display:block;margin-bottom:4px;color:var(--fg)}
.srow .lab span{font-size:13px;color:var(--mute);line-height:1.5}
.sbar{height:46px;border-radius:12px;background:var(--card);box-shadow:inset 0 0 0 1px var(--line);overflow:hidden}
.sbar i{display:flex;align-items:center;height:100%;padding:0 16px;font-style:normal;font-family:var(--mono);font-size:12px;font-weight:500;letter-spacing:.04em;white-space:nowrap;border-radius:12px;transform-origin:left;transform:scaleX(0);transition:transform 1.8s var(--ease) calc(var(--d,0)*140ms + 300ms);overflow:hidden}
.stack.on .sbar i{transform:scaleX(1)}
.sval{text-align:right;font-family:var(--serif);font-weight:500;font-size:clamp(22px,2.2vw,30px);letter-spacing:-.02em}
.sval.gd{color:var(--gl)}.sval.gn{color:var(--acc)}.sval.bl{color:#8fc0ec}
.st .sval.gn,.cn .sval.gn{color:var(--green)}.st .sval.bl,.cn .sval.bl{color:#1d5a96}
.snote{font-size:13px;line-height:1.7;color:var(--mute);padding:0 0 22px;max-width:72ch}
.srow.total{border-top:2px solid var(--fg);margin-top:8px}
.srow.total .sval{font-size:clamp(26px,3vw,42px)}
.plays{margin-top:70px}
.ghost-n{position:absolute;right:26px;top:6px;font-family:var(--serif);font-weight:500;font-size:150px;line-height:1;color:var(--fg);opacity:.06;pointer-events:none;letter-spacing:-.04em}
.ptag{font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;color:var(--acc);display:block;margin-bottom:18px}
.st .ptag,.cn .ptag{color:var(--green)}
.ptag.gd{color:var(--gl)}.ptag.bl{color:#1d5a96}
.pirc{font-family:var(--mono);font-size:11px;letter-spacing:.08em;color:var(--mute);margin:-4px 0 16px;line-height:1.6}
.prow{display:flex;justify-content:space-between;gap:18px;padding:11px 0;border-top:1px solid var(--line);font-size:13.5px;line-height:1.5}
.prow span:first-child{color:var(--mute)}
.prow span:last-child{text-align:right;color:var(--fg);font-weight:500}
.prow.hi span:last-child{color:var(--gl);font-family:var(--serif);font-size:17px}
.prows{margin-top:26px}
.anchor-two{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:64px}
.steps4{list-style:none;display:grid;gap:0;margin-top:6px}
.steps4 li{display:grid;grid-template-columns:34px 1fr;gap:16px;padding:14px 0;border-top:1px solid var(--line);font-size:14.5px;line-height:1.65;color:var(--mute)}
.steps4 li b.i{font-family:var(--mono);font-size:11px;color:var(--green);width:30px;height:30px;border-radius:8px;box-shadow:inset 0 0 0 1px var(--line);display:grid;place-items:center;font-weight:500}
.steps4 li strong{color:var(--ink)}
.quote{font-style:italic;color:var(--ink)}
.callout{margin-top:22px;padding:16px 18px;border-radius:14px;background:rgba(184,138,34,.1);box-shadow:inset 0 0 0 1px rgba(184,138,34,.35);font-size:14px;line-height:1.65;color:var(--slate)}
.callout strong{color:#8a6210}
/* responsive */
@media(max-width:1100px){
 nav .links{position:absolute;top:calc(100% + 8px);left:0;right:0;flex-direction:column;align-items:stretch;gap:0;padding:12px 18px 18px;border-radius:20px;background:rgba(11,37,69,.97);backdrop-filter:blur(18px);border:1px solid rgba(255,255,255,.14);opacity:0;pointer-events:none;transform:translateY(-8px);transition:opacity .4s var(--ease),transform .5s var(--ease)}
 nav.menu-open .links{opacity:1;pointer-events:auto;transform:none}
 nav .links li{border-bottom:1px solid rgba(255,255,255,.1)}
 nav .links li:last-child{border:0;padding-top:14px}
 nav .links a.t{display:block;padding:14px 0;font-size:16px}
 nav .links a.t.act{box-shadow:none;color:var(--leaf)}
 .nav-toggle{display:block}
 .nav-cta-d{display:none}
}
@media(max-width:1100px){
 .tl.c7,.tl.c8{grid-template-columns:1fr;gap:34px;margin-top:60px;padding-left:38px}
 .tl::before{left:9px;right:auto;top:0;bottom:0;width:1px;height:auto}
 .tl::after{left:9px;top:0;width:2px;height:100%;transform:scaleY(0);transform-origin:top;background:linear-gradient(180deg,var(--green),var(--gl))}
 .dk .tl::after,.gr .tl::after{background:linear-gradient(180deg,var(--leaf),var(--goldl))}
 .tl.on::after{transform:scaleY(1)}
 .td{position:absolute;left:-38px;top:2px;margin:0}
 .td.major{transform:rotate(45deg)}
 .tn{padding-right:0}
}
@media(max-width:900px){
 .wrap{padding:0 22px}
 .split,.hubwrap,.feat,.feat.flip,.aud,.two,.net-top,.anchor-two,.mbody{grid-template-columns:1fr;gap:38px}
 .feat.flip .fimg{order:0}
 .bento,.revs{grid-template-columns:1fr;margin-top:48px}
 .s3,.s4,.s5,.s6,.s7,.s8,.s12{grid-column:auto}.r2{grid-row:auto}
 .strip{grid-template-columns:1fr 1fr}
 .strip>div{padding:28px 14px 26px 0}
 .strip>div:nth-child(odd){padding-left:0;border-left:0}
 .strip>div:nth-child(even){padding-left:20px;border-left:1px solid var(--line)}
 .strip>div:nth-child(n+3){border-top:1px solid var(--line)}
 .strip>div:last-child{grid-column:1/-1;border-left:0;padding-left:0}
 .hstats{grid-template-columns:1fr 1fr;margin-top:48px}
 .hstat:nth-child(3){padding-left:0;border-left:0}
 .hstat:nth-child(n+3){margin-top:22px;border-top:1px solid rgba(255,255,255,.12)}
 .hstat+.hstat{padding-left:20px}
 .hstat:nth-child(3){padding-left:0}
 .hero{padding:124px 0 130px}
 .core2,.formin{padding:26px}
 .loop{grid-template-columns:1fr 1fr}.loop div{border-left:0;border-top:1px solid var(--line)}.loop div:first-child{border-top:0}
 .proc{grid-template-columns:1fr;gap:38px;margin-top:50px;padding-left:0}
 .proc::before,.proc::after{display:none}
 .net-grid{grid-template-columns:1fr}
 .net-grid .bezel,.net-grid .bezel:nth-child(1),.net-grid .bezel:nth-child(2){grid-column:auto}
 footer .grid{grid-template-columns:1fr 1fr}
 .row{grid-template-columns:1fr}
 .srow{grid-template-columns:1fr;gap:12px}
 .srow.head{display:none}
 .sval{text-align:left}
 .hub{max-width:460px}
 .node{padding:8px 11px;border-radius:12px}
 .rtype{position:static;display:block;margin-bottom:16px}
 .scrollcue{display:none}
 .ghost-n{font-size:110px}
 .tabs{display:flex;width:100%}
 .tab{flex:1 1 auto;padding:12px 10px;font-size:13px}
}
@media(max-width:560px){
 footer .grid{grid-template-columns:1fr}
 .mark span{font-size:16px}
 .cta .btn{width:100%;justify-content:space-between}
 .cta .btn.ghost{justify-content:space-between}
 .hstat span{font-size:9.5px}
 .strip b{font-size:42px}
 .tbl-wrap td{padding:14px 14px}
}
@media(max-width:380px){.mark span{display:none}}
@media(prefers-reduced-motion:reduce){
 html{scroll-behavior:auto}
 .js .rv{opacity:1!important;transform:none!important;filter:none!important;transition:none!important}
 .js h1 .ln span{transform:none!important;transition:none!important}
 *,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}
 .statement .w{color:var(--fg)!important}
 .tl::after,.proc::after{transform:none!important}
 .sbar i{transform:none!important}
 .track{animation:none}
}
"""

def nav(home, active=None):
    p = '' if home else '/'
    brand = '#top' if home else '/'
    items = [('About', p + '#about'), ('The Tree', p + '#phoenix-tree'), ('Revenue', p + '#revenue'),
             ('Invest', p + '#invest'), ('Land Partners', p + '#land'), ('Credits', p + '#credits'),
             ('Tax Strategy', '/tax-strategy.html')]
    lis = ''.join('<li><a class="t%s" href="%s">%s</a></li>' % (' act' if n == active else '', h, n) for n, h in items)
    lis += '<li><a class="btn sm nav-cta" href="%s#contact">Get Started<span class="ic">%s</span></a></li>' % (p, ARROW)
    return ('<div id="progress-bar"></div>\n<nav class="nav" id="main-nav"><div class="in">'
            '<a href="%s" class="mark"><img src="images/logo-icon.png" alt="Carbon Legacy Trees"><span>Carbon Legacy Trees</span></a>'
            '<button class="nav-toggle" id="navToggle" type="button" aria-label="Menu" aria-expanded="false" aria-controls="navLinks"><span></span><span></span><span></span></button>'
            '<ul class="links" id="navLinks">%s</ul></div></nav>' % (brand, lis))

def footer(home, legal):
    p = '' if home else '/'
    return ('<footer class="foot dk"><div class="orb og o2" style="opacity:.35"></div><div class="wrap">'
            '<div class="grid"><div class="brand"><img src="images/logo-primary.png" alt="Carbon Legacy Trees">'
            '<p>Exclusive commercial rights to the Phoenix Tree, an epigenetically enhanced species generating four revenue streams per acre: carbon credits, tax credits, premium hardwood, and graphene.</p></div>'
            '<div><h4>The Tree</h4><ul>'
            '<li><a href="%(p)s#phoenix-tree">Phoenix Tree Science</a></li><li><a href="%(p)s#phoenix-tree">10x Carbon Capture</a></li><li><a href="%(p)s#phoenix-tree">Self-Water System</a></li><li><a href="%(p)s#phoenix-tree">15 Harvest Cycles</a></li><li><a href="%(p)s#phoenix-tree">Graphene Byproduct</a></li></ul></div>'
            '<div><h4>Revenue</h4><ul>'
            '<li><a href="%(p)s#revenue">Voluntary Credits</a></li><li><a href="%(p)s#revenue">Carbon Tax Credits</a></li><li><a href="%(p)s#revenue">Premium Lumber</a></li><li><a href="%(p)s#revenue">Graphene Stream</a></li></ul></div>'
            '<div><h4>Participate</h4><ul>'
            '<li><a href="%(p)s#invest">Investor Access</a></li><li><a href="%(p)s#land">Land Partners</a></li><li><a href="%(p)s#credits">Buy Credits</a></li><li><a href="/tax-strategy.html">Tax Strategy</a></li><li><a href="%(p)s#contact">Contact Us</a></li></ul></div></div>'
            '<div class="bot"><p>&copy; 2026 Carbon Legacy Trees LLC. All rights reserved. Exclusive Phoenix Tree commercial rights holder.</p><p>South Dakota Phase 1. National expansion ongoing</p></div>'
            '<p class="legal">%(legal)s</p></div></footer>') % {'p': p, 'legal': legal}

FX = r"""<script>
(function(){
var d=document,reduce=matchMedia('(prefers-reduced-motion:reduce)').matches,rt=d.documentElement;
requestAnimationFrame(function(){setTimeout(function(){rt.classList.add('on-load')},60)});
/* nav: scrolled state, progress bar, mobile menu */
var nv=d.getElementById('main-nav'),bar=d.getElementById('progress-bar');
function onScroll(){var h=d.documentElement;if(nv)nv.classList.toggle('scrolled',scrollY>50);if(bar)bar.style.width=(h.scrollTop/Math.max(1,h.scrollHeight-h.clientHeight)*100)+'%'}
addEventListener('scroll',onScroll,{passive:true});onScroll();
var tg=d.getElementById('navToggle'),lk=d.getElementById('navLinks');
if(tg&&lk){function setM(o){nv.classList.toggle('menu-open',o);tg.setAttribute('aria-expanded',o?'true':'false')}
 tg.addEventListener('click',function(){setM(!nv.classList.contains('menu-open'))});
 lk.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){setM(false)})});
 addEventListener('keydown',function(e){if(e.key==='Escape')setM(false)});
 addEventListener('resize',function(){if(innerWidth>1100)setM(false)})}
/* blur-up reveals with stagger */
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}})},{threshold:.12,rootMargin:'0px 0px -6% 0px'});
d.querySelectorAll('.rv,.tl,.proc,.stack,.statement .w').forEach(function(el){io.observe(el)});
setTimeout(function(){d.querySelectorAll('.rv:not(.on),.tl:not(.on),.proc:not(.on),.stack:not(.on)').forEach(function(e){if(e.getBoundingClientRect().top<innerHeight*1.2)e.classList.add('on')})},2500);
/* scroll-driven statements: each word lights up */
var sts=[].slice.call(d.querySelectorAll('.statement'));
function so(){sts.forEach(function(st){var ws=st.querySelectorAll('.w'),r=st.getBoundingClientRect(),h=innerHeight;var p=Math.min(1,Math.max(0,(h*.85-r.top)/(r.height+h*.35)));var n=Math.round(p*ws.length);ws.forEach(function(w,i){w.classList.toggle('on',i<n)})})}
if(sts.length){var tk=false;addEventListener('scroll',function(){if(!tk){tk=true;requestAnimationFrame(function(){so();tk=false})}},{passive:true});so()}
/* count-up */
function ease(t){return 1-Math.pow(2,-10*t)}
function countUp(el){var t=parseFloat(el.dataset.count),sx=el.dataset.suffix||'',px=el.dataset.prefix||'',dur=t>=1000?2000:1200,sv=t>=1000?t-8:(t>=100?Math.round(t*.35):0),t0=Date.now();
 (function tick(){var p=Math.min((Date.now()-t0)/dur,1),v=sv+(t-sv)*ease(p);el.textContent=px+Math.round(v).toLocaleString()+sx;if(p<1)requestAnimationFrame(tick);else el.textContent=px+t.toLocaleString()+sx})()}
if(!reduce){var co=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;co.unobserve(e.target);countUp(e.target)})},{threshold:.5});d.querySelectorAll('[data-count]').forEach(function(el){co.observe(el)})}
/* audience tabs */
function tab(name){d.querySelectorAll('.tab').forEach(function(t){var a=t.dataset.pane===name;t.classList.toggle('active',a);t.setAttribute('aria-selected',a?'true':'false')});d.querySelectorAll('.pane').forEach(function(p){p.classList.toggle('active',p.id==='pane-'+name)})}
d.querySelectorAll('.tab').forEach(function(t){t.addEventListener('click',function(){tab(t.dataset.pane)})});
var map={'#land':'land','#invest':'investors','#credits':'credits'};
d.querySelectorAll('a[href="#land"],a[href="#invest"],a[href="#credits"],a[href="/#land"],a[href="/#invest"],a[href="/#credits"]').forEach(function(a){a.addEventListener('click',function(e){var h=a.getAttribute('href').replace('/','');if(!d.querySelector('.tab'))return;e.preventDefault();tab(map[h]);setTimeout(function(){var s=d.getElementById('land');if(!s)return;var top=s.getBoundingClientRect().top+scrollY-80;scrollTo({top:top,behavior:reduce?'auto':'smooth'})},30)})});
if(!reduce){
 /* magnetic buttons */
 d.querySelectorAll('.btn:not(button)').forEach(function(b){b.addEventListener('pointermove',function(e){var r=b.getBoundingClientRect();b.style.transform='translate('+((e.clientX-r.left-r.width/2)*.18)+'px,'+((e.clientY-r.top-r.height/2)*.28)+'px)'});b.addEventListener('pointerleave',function(){b.style.transform=''})});
 /* cursor spotlight on bezel cards */
 d.querySelectorAll('.bezel').forEach(function(c){var k=c.querySelector('.core2,.net-card');if(!k)return;c.addEventListener('pointermove',function(e){var r=c.getBoundingClientRect();k.style.setProperty('--mx',(e.clientX-r.left)+'px');k.style.setProperty('--my',(e.clientY-r.top)+'px')})});
 /* hero pointer parallax */
 var h=d.querySelector('.hero');if(h){var o=h.querySelectorAll('.orb'),wm=h.querySelector('.hwm');h.addEventListener('pointermove',function(e){var x=e.clientX/innerWidth-.5,y=e.clientY/innerHeight-.5;o.forEach(function(el,i){el.style.translate=(x*(30+i*24))+'px '+(y*(24+i*18))+'px'});if(wm)wm.style.translate=(x*-26)+'px '+(y*-18)+'px'})}
}
})();
</script>"""
