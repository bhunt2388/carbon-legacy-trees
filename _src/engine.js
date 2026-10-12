  (function(){
    'use strict';

    var WALLPAPERS = [
      { key:'mercury',  name:'Canopy',   kind:'Fresh Water',   sw:'linear-gradient(135deg,#0a1f2e,#1a7fa0 55%,#a8dff0)' },
      { key:'nebula',   name:'Carbon',   kind:'Deep Field',    sw:'linear-gradient(135deg,#0a0f24,#1e8f78 50%,#c8a8d8)' },
      { key:'lattice',  name:'Roots',    kind:'Living Lattice',sw:'linear-gradient(135deg,#091017,#1f8f78 60%,#d8b15a)' },
      { key:'velocity', name:'Graphene', kind:'Lightfold',     sw:'linear-gradient(135deg,#070b16,#5aa0ff 60%,#f0c66a)' },
      { key:'silk',     name:'Credits',  kind:'Caustic Drift', sw:'linear-gradient(135deg,#0a1018,#1a6f5e 55%,#e6cf8a)' }
    ];

    /* single mode — only compile mercury for performance */
    var SINGLE_MODE = true;

    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    /* ---------------- WebGL ---------------- */
    var canvas = document.getElementById('gl');
    var gl = canvas.getContext('webgl', { antialias:false, alpha:false, preserveDrawingBuffer:true, powerPreference:'high-performance' })
          || canvas.getContext('experimental-webgl');
    if(!gl){ canvas.style.display='none'; return; }

    var VERT = 'attribute vec2 p; void main(){ gl_Position = vec4(p,0.0,1.0); }';

    function compile(type, src){
      var s = gl.createShader(type);
      gl.shaderSource(s, src);
      gl.compileShader(s);
      if(!gl.getShaderParameter(s, gl.COMPILE_STATUS)){
        console.error('shader error:', gl.getShaderInfoLog(s), '\n', src);
        return null;
      }
      return s;
    }
    function buildProgram(fragMain){
      var vs = compile(gl.VERTEX_SHADER, VERT);
      var fs = compile(gl.FRAGMENT_SHADER, window.SHADER_COMMON + fragMain);
      if(!vs || !fs) return null;
      var p = gl.createProgram();
      gl.attachShader(p, vs); gl.attachShader(p, fs);
      gl.bindAttribLocation(p, 0, 'p');
      gl.linkProgram(p);
      if(!gl.getProgramParameter(p, gl.LINK_STATUS)){ console.error('link error:', gl.getProgramInfoLog(p)); return null; }
      return p;
    }

    // fullscreen triangle
    var buf = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buf);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1, 3,-1, -1,3]), gl.STATIC_DRAW);
    gl.enableVertexAttribArray(0);
    gl.vertexAttribPointer(0, 2, gl.FLOAT, false, 0, 0);

    var programs = {}, uniforms = {};
    WALLPAPERS.forEach(function(w){
      if(SINGLE_MODE && w.key !== 'mercury') return;  /* skip unused shaders */
      var prog = buildProgram(window.SHADERS[w.key]);
      programs[w.key] = prog;
      if(prog){
        uniforms[w.key] = {
          time:   gl.getUniformLocation(prog, 'u_time'),
          res:    gl.getUniformLocation(prog, 'u_res'),
          mouse:  gl.getUniformLocation(prog, 'u_mouse'),
          mDown:  gl.getUniformLocation(prog, 'u_mDown'),
          ripple: gl.getUniformLocation(prog, 'u_ripple[0]')
        };
      }
    });

    /* Mobile/low-power GPUs pay a much higher per-pixel cost for this shader than
       desktop — cap DPR harder on coarse-pointer (touch) devices so we don't render
       at full retina density on phones. */
    var isMobile = window.matchMedia('(pointer: coarse)').matches;
    var MAX_DPR = isMobile ? 1.25 : 2;

    var dpr = Math.min(window.devicePixelRatio || 1, MAX_DPR);
    var W = 1, H = 1;
    function resize(){
      dpr = Math.min(window.devicePixelRatio || 1, MAX_DPR);
      var hero = canvas.closest('section') || canvas.parentElement;
      W = Math.floor((hero ? hero.offsetWidth  : window.innerWidth)  * dpr);
      H = Math.floor((hero ? hero.offsetHeight : window.innerHeight) * dpr);
      canvas.width = W; canvas.height = H;
      gl.viewport(0, 0, W, H);
    }
    window.addEventListener('resize', resize);
    resize();

    /* Hard FPS cap — don't rely solely on the browser to throttle a hidden/
       backgrounded tab. Some mobile WebViews keep pumping rAF at full rate even
       when the tab is backgrounded or the device is under multitasking pressure,
       which is what was pegging the whole phone's GPU. Also cut real render cost
       (not just simulated speed) under prefers-reduced-motion. */
    var TARGET_FPS = isMobile ? 30 : 60;
    if (reduceMotion) TARGET_FPS = 15;
    var FRAME_MIN_MS = 1000 / TARGET_FPS;
    var lastFrameTime = 0;
    var rafHandle = null;
    var paused = false;

    document.addEventListener('visibilitychange', function(){
      if (document.hidden) {
        paused = true;
        if (rafHandle) { cancelAnimationFrame(rafHandle); rafHandle = null; }
      } else if (paused) {
        paused = false;
        lastFrameTime = 0;
        rafHandle = requestAnimationFrame(frame);
      }
    });

    /* ---------------- interaction state ---------------- */
    // mouse in framebuffer px, y-up
    var tgt = { x: W*0.5, y: H*0.5 };
    var cur = { x: W*0.5, y: H*0.5 };
    var down = 0, downTarget = 0;

    /* scope pointer events to the hero section only */
    var heroEl = canvas.closest('section') || canvas.parentElement;
    function setPointer(clientX, clientY){
      var rect = canvas.getBoundingClientRect();
      tgt.x = (clientX - rect.left) * dpr;
      tgt.y = H - (clientY - rect.top) * dpr;   // flip to y-up
    }
    heroEl.addEventListener('pointermove', function(e){ setPointer(e.clientX, e.clientY); }, { passive:true });

    // ripples: 6 slots, each [x, y, t0]; z packed as age at draw time
    var ripple = new Float32Array(18);
    for(var i=0;i<6;i++) ripple[i*3+2] = -1;
    var rT0 = [-1,-1,-1,-1,-1,-1];
    var rNext = 0;
    function addRipple(clientX, clientY){
      var rect = canvas.getBoundingClientRect();
      var x = (clientX - rect.left) * dpr;
      var y = H - (clientY - rect.top) * dpr;
      ripple[rNext*3+0] = x;
      ripple[rNext*3+1] = y;
      rT0[rNext] = nowSec();
      rNext = (rNext + 1) % 6;
    }
    heroEl.addEventListener('pointerdown', function(e){
      if(e.target.closest('.clt-ui')) return;
      downTarget = 1;
      setPointer(e.clientX, e.clientY);
      cur.x = tgt.x; cur.y = tgt.y;
      addRipple(e.clientX, e.clientY);
    });
    heroEl.addEventListener('pointerup', function(){ downTarget = 0; });
    heroEl.addEventListener('pointercancel', function(){ downTarget = 0; });

    /* ---------------- selection ---------------- */
    var current = 0;
    var saved = +localStorage.getItem('carbon_trees_wallpaper');
    if(!isNaN(saved) && saved >= 0 && saved < WALLPAPERS.length) current = saved;

    var flash = document.getElementById('flash');
    var nowName = document.getElementById('nowName');
    var nameTimer = null;
    function select(idx, announce){
      current = (idx + WALLPAPERS.length) % WALLPAPERS.length;
      localStorage.setItem('carbon_trees_wallpaper', current);
      [].forEach.call(document.querySelectorAll('.tile'), function(t, i){
        t.classList.toggle('active', i === current);
        t.setAttribute('aria-selected', i === current ? 'true' : 'false');
      });
      flash.classList.add('on');
      setTimeout(function(){ flash.classList.remove('on'); }, 90);
      if(announce){
        var w = WALLPAPERS[current];
        nowName.querySelector('.t').textContent = w.name;
        nowName.querySelector('.s').textContent = w.kind;
        nowName.classList.add('show');
        clearTimeout(nameTimer);
        nameTimer = setTimeout(function(){ nowName.classList.remove('show'); }, 1700);
      }
    }

    // build dock
    var dock = document.getElementById('dock');
    WALLPAPERS.forEach(function(w, i){
      var tile = document.createElement('button');
      tile.className = 'tile';
      tile.type = 'button';
      tile.setAttribute('role', 'tab');
      tile.setAttribute('aria-label', w.name + ', ' + w.kind);
      tile.innerHTML =
        '<span class="sw" style="background:'+w.sw+'"></span>' +
        '<span class="lab"><span class="n">'+w.name+'</span><span class="k">'+w.kind+'</span></span>' +
        '<span class="idx">'+(i+1)+'</span>';
      tile.addEventListener('click', function(){ select(i, true); });
      dock.appendChild(tile);
    });

    window.addEventListener('keydown', function(e){
      if(e.target && /^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName)) return;
      if(e.key >= '1' && e.key <= '5'){ select(+e.key - 1, true); }
      else if(e.key === 'ArrowRight'){ select(current + 1, true); }
      else if(e.key === 'ArrowLeft'){ select(current - 1, true); }
    });

    /* ---------------- clock ---------------- */
    var timeEl = document.getElementById('time'),
        dayEl = document.getElementById('day'),
        dateEl = document.getElementById('date');
    function tick(){
      var d = new Date();
      var hh = String(d.getHours()).padStart(2,'0');
      var mm = String(d.getMinutes()).padStart(2,'0');
      var ss = String(d.getSeconds()).padStart(2,'0');
      timeEl.innerHTML = hh + ':' + mm + '<span class="sec">' + ss + '</span>';
      dayEl.textContent = d.toLocaleDateString(undefined, { weekday:'long' });
      dateEl.textContent = d.toLocaleDateString(undefined, { month:'long', day:'numeric' });
    }
    tick(); setInterval(tick, 1000);

    // fake signal bars + gpu label for OS flavor
    (function(){
      var sig = document.getElementById('signal');
      [7,11,15,19].forEach(function(h){
        var b = document.createElement('span'); b.className = 'bar'; b.style.height = h + 'px';
        sig.appendChild(b);
      });
      try{
        var dbg = gl.getExtension('WEBGL_debug_renderer_info');
        var r = dbg ? gl.getParameter(dbg.UNMASKED_RENDERER_WEBGL) : '';
        document.getElementById('gpu').textContent = r ? r.split(/[(,]/)[0].trim().slice(0,18) : 'GPU';
      }catch(e){ document.getElementById('gpu').textContent = 'GPU'; }
    })();

    /* ---------------- render loop ---------------- */
    var t0 = performance.now();
    var __frames = 0;
    function nowSec(){ return (performance.now() - t0) / 1000; }
    var timeScale = reduceMotion ? 0.22 : 1.0;

    function frame(timestamp){
      // FPS cap — skip work if we're being asked to render faster than TARGET_FPS
      if (timestamp && lastFrameTime && (timestamp - lastFrameTime) < FRAME_MIN_MS) {
        rafHandle = requestAnimationFrame(frame);
        return;
      }
      lastFrameTime = timestamp || performance.now();

      var w = WALLPAPERS[current];
      var prog = programs[w.key], u = uniforms[w.key];

      // smoothing
      cur.x += (tgt.x - cur.x) * 0.12;
      cur.y += (tgt.y - cur.y) * 0.12;
      down  += (downTarget - down) * 0.18;

      // update ripple ages
      var ns = nowSec();
      for(var i=0;i<6;i++){
        if(rT0[i] < 0){ ripple[i*3+2] = -1; continue; }
        var age = ns - rT0[i];
        if(age > 3.2){ rT0[i] = -1; ripple[i*3+2] = -1; }
        else ripple[i*3+2] = age;
      }

      if(prog){
        gl.useProgram(prog);
        gl.uniform1f(u.time, (__ovr!=null?__ovr:ns) * timeScale);
        gl.uniform2f(u.res, W, H);
        gl.uniform2f(u.mouse, cur.x, cur.y);
        gl.uniform1f(u.mDown, down);
        if(u.ripple) gl.uniform3fv(u.ripple, ripple);
        gl.drawArrays(gl.TRIANGLES, 0, 3);
      }
      if (!paused) rafHandle = requestAnimationFrame(frame);
      __frames++;
    }

    select(current, false);
    frame(); // draw first frame synchronously (rAF is paused while hidden)

    // debug hook
    window.__step = function(t){ if(t!=null){ __ovr = t; } frame(); };
    var __ovr = null;
    window.__dbg = function(){
      var w = WALLPAPERS[current];
      return {
        prog: !!programs[w.key],
        link: programs[w.key] ? gl.getProgramParameter(programs[w.key], gl.LINK_STATUS) : null,
        glerr: gl.getError(),
        size: [W,H],
        frames: __frames
      };
    };
  })();