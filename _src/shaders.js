// Shader wallpapers — fragment shader sources.
// Each entry is a fragment-shader main(); the COMMON prelude (uniforms + helpers)
// is prepended by the engine. Coordinate space helper toP() returns
// aspect-corrected centered coords (y in roughly -0.5..0.5).

window.SHADER_COMMON = `
precision highp float;
uniform float u_time;
uniform vec2  u_res;
uniform vec2  u_mouse;   // framebuffer px, y-up
uniform float u_mDown;   // 0..1 pressed
uniform vec3  u_ripple[6]; // xy = px (y-up), z = age secs (<0 inactive)

vec2 toP(vec2 px){ return (px - 0.5*u_res)/u_res.y; }

float hash21(vec2 p){
  p = fract(p*vec2(123.34, 456.21));
  p += dot(p, p+45.32);
  return fract(p.x*p.y);
}
vec2 hash22(vec2 p){
  vec3 a = fract(vec3(p.xyx)*vec3(123.34, 234.34, 345.65));
  a += dot(a, a+34.45);
  return fract(vec2(a.x*a.y, a.y*a.z));
}
float vnoise(vec2 p){
  vec2 i = floor(p), f = fract(p);
  vec2 u = f*f*(3.0-2.0*f);
  float a = hash21(i), b = hash21(i+vec2(1,0));
  float c = hash21(i+vec2(0,1)), d = hash21(i+vec2(1,1));
  return mix(mix(a,b,u.x), mix(c,d,u.x), u.y);
}
float fbm(vec2 p){
  float s = 0.0, a = 0.5;
  mat2 m = mat2(1.6, 1.2, -1.2, 1.6);
  for(int i=0;i<5;i++){ s += a*vnoise(p); p = m*p; a *= 0.5; }
  return s;
}
vec3 pal(float t, vec3 a, vec3 b, vec3 c, vec3 d){
  return a + b*cos(6.28318*(c*t + d));
}
// oscillating ring field from active click ripples
float ripples(vec2 p){
  float s = 0.0;
  for(int i=0;i<6;i++){
    if(u_ripple[i].z < 0.0) continue;
    vec2 rp = toP(u_ripple[i].xy);
    float age = u_ripple[i].z;
    float d = length(p - rp);
    float radius = age*0.9;
    float ring = sin((d - radius)*26.0);
    float env = exp(-age*2.2) * exp(-pow((d - radius)*5.0, 2.0));
    s += ring*env;
  }
  return s;
}
// summed inward "speed" from ripples (for warp shader)
float rippleBurst(vec2 p){
  float s = 0.0;
  for(int i=0;i<6;i++){
    if(u_ripple[i].z < 0.0) continue;
    s += exp(-u_ripple[i].z*1.6);
  }
  return s;
}
`;

window.SHADERS = {};

/* ---------- 1. MERCURY — fresh water surface ---------- */
window.SHADERS.mercury = `
float H(vec2 p){
  float t = u_time*0.10;
  /* layered wave interference — shallow water feel */
  vec2 q = vec2(fbm(p*2.2 + t*0.8), fbm(p*2.2 + vec2(4.1,1.8) - t*0.6));
  float h = fbm(p*3.0 + q*1.4 + t*0.45);
  /* gentle ripple rings from a second fbm pass */
  float r2 = fbm(p*5.5 - t*1.1 + vec2(2.3,0.7))*0.35;
  h = h*0.65 + r2*0.35;
  /* cursor depression — water disturbed by hand */
  vec2 m = toP(u_mouse);
  float md = length(p - m);
  h -= exp(-md*md*6.0)*(0.28 + 0.22*u_mDown);
  h += ripples(p)*0.18;
  return h;
}
void main(){
  vec2 p = toP(gl_FragCoord.xy);
  /* compute surface normal via height-field gradient */
  float e = 0.0018;
  float hx = H(p+vec2(e,0.0)) - H(p-vec2(e,0.0));
  float hy = H(p+vec2(0.0,e)) - H(p-vec2(0.0,e));
  vec3 n = normalize(vec3(-hx*1.6, -hy*1.6, e*3.5));
  vec3 vdir = vec3(0.0, 0.0, 1.0);
  vec3 rd = reflect(-vdir, n);

  /* sky reflection — pale daylight sky above water */
  float yy = rd.y*0.5 + 0.5;
  vec3 skyHigh = vec3(0.52, 0.78, 0.92);   /* bright sky blue */
  vec3 skyHor  = vec3(0.20, 0.50, 0.72);   /* horizon blue */
  vec3 skyDeep = vec3(0.04, 0.14, 0.32);   /* deep water below */
  vec3 sky = mix(skyDeep, skyHor, smoothstep(-0.2, 0.4, yy));
  sky = mix(sky, skyHigh, smoothstep(0.35, 1.0, yy));
  vec3 col = sky;

  /* Fresnel — water is highly reflective at grazing angles */
  float fres = pow(1.0 - max(dot(n, vdir), 0.0), 2.8);
  col = mix(col, skyHigh, fres*0.55);

  /* subsurface scatter — water depth teal/cyan */
  float h0 = H(p);
  vec3 waterDeep = vec3(0.02, 0.18, 0.28);
  vec3 waterShallow = vec3(0.08, 0.44, 0.55);
  vec3 sub = mix(waterDeep, waterShallow, smoothstep(0.2, 0.75, h0));
  col = mix(sub, col, 0.55 + fres*0.35);

  /* caustic sparkles — brightest where surface curves to focus light */
  float caustic = pow(max(0.0, 1.0 - length(vec2(hx,hy))*18.0), 2.4);
  col += vec3(0.75, 0.92, 1.0) * caustic * 0.55;

  /* specular sun highlight */
  vec3 L = normalize(vec3(0.4, 0.65, 0.70));
  float spec = pow(max(dot(rd, L), 0.0), 64.0);
  col += vec3(1.0, 0.98, 0.94) * spec * 0.80;

  /* subtle warm-gold glint from sun angle */
  float glint = pow(max(dot(rd, normalize(vec3(0.7,0.5,0.55))), 0.0), 110.0);
  col += vec3(1.0, 0.88, 0.55) * glint * 0.5;

  /* edge vignette */
  col *= 1.0 - 0.20*dot(p,p);

  gl_FragColor = vec4(col, 1.0);
}
`;

/* ---------- 2. NEBULA — deep field plasma ---------- */
window.SHADERS.nebula = `
void main(){
  vec2 p = toP(gl_FragCoord.xy)*1.25;
  vec2 m = toP(u_mouse)*1.25;
  float t = u_time*0.06;

  // swirl space around cursor (gravity well)
  vec2 d = p - m; float r = length(d);
  float ang = exp(-r*1.4)*2.6*(1.0 + 0.7*u_mDown);
  float ca = cos(ang), sa = sin(ang);
  vec2 ps = m + mat2(ca,-sa,sa,ca)*d;

  vec2 q  = vec2(fbm(ps + t), fbm(ps + vec2(3.1,1.7) - t));
  vec2 rr = vec2(fbm(ps + q*2.0 + t*0.5), fbm(ps + q*2.0 + vec2(8.3) - t*0.4));
  float f = fbm(ps + rr*2.2);
  f += ripples(p)*0.22;

  // bright filament structure from the warped field
  float fil = pow(smoothstep(0.42, 0.78, f), 2.0);

  vec3 deep   = vec3(0.015, 0.02, 0.065);
  vec3 violet = vec3(0.30, 0.16, 0.52);
  vec3 teal   = vec3(0.08, 0.46, 0.58);
  vec3 col = deep;
  col = mix(col, violet, smoothstep(0.28, 0.72, f));
  col = mix(col, teal, fil*0.85);
  col += vec3(0.85, 0.95, 1.0) * pow(fil, 3.0) * 0.45;   // hot cores

  // cursor: a glowing nebula heart
  col += vec3(0.18, 0.52, 0.62) * exp(-r*2.8) * 0.9;
  col += vec3(0.9, 0.85, 1.0)  * exp(-r*9.0) * 0.5;

  // sparse stars
  vec2 sg = toP(gl_FragCoord.xy)*150.0;
  vec2 sid = floor(sg);
  float star = step(0.992, hash21(sid));
  float tw = 0.6 + 0.4*sin(u_time*3.0 + hash21(sid+5.0)*30.0);
  col += star*tw*vec3(0.85, 0.92, 1.0)*0.9;

  gl_FragColor = vec4(col, 1.0);
}
`;

/* ---------- 3. LATTICE — living crystal voronoi ---------- */
window.SHADERS.lattice = `
void main(){
  vec2 p = toP(gl_FragCoord.xy);
  vec2 m = toP(u_mouse);
  float t = u_time*0.25;
  float scale = 4.5;
  vec2 g = p*scale;
  vec2 ii = floor(g), f = fract(g);

  float d1 = 8.0, d2 = 8.0;
  vec2 id1 = vec2(0.0);
  for(int y=-1;y<=1;y++){
    for(int x=-1;x<=1;x++){
      vec2 o = vec2(float(x), float(y));
      vec2 rnd = hash22(ii + o);
      vec2 pt = o + 0.5 + 0.42*sin(t + 6.28318*rnd);
      vec2 diff = pt - f;
      float dd = dot(diff, diff);
      if(dd < d1){ d2 = d1; d1 = dd; id1 = ii + o; }
      else if(dd < d2){ d2 = dd; }
    }
  }
  d1 = sqrt(d1); d2 = sqrt(d2);
  float border = d2 - d1;

  float md = length(p - m);
  float ml = exp(-md*2.2);                 // cursor light pool
  float rip = ripples(p);
  float edge = smoothstep(0.18, 0.0, border);

  float cid = hash21(id1);
  vec3 cellA = mix(vec3(0.035,0.06,0.11), vec3(0.05,0.11,0.10), cid);
  vec3 col = cellA*(0.45 + 0.55*d1);

  vec3 edgeCol = mix(vec3(0.20,0.72,0.62), vec3(0.86,0.66,0.26), step(0.5, fract(cid*7.0)));
  col += edgeCol*edge*(0.45 + 1.4*ml + 0.7*abs(rip));

  col += vec3(0.14,0.5,0.5)*ml*0.45;
  col *= 1.0 - 0.18*dot(p,p);
  gl_FragColor = vec4(col, 1.0);
}
`;

/* ---------- 4. VELOCITY — hyperspace lightfold ---------- */
window.SHADERS.velocity = `
void main(){
  vec2 p = toP(gl_FragCoord.xy);
  vec2 m = toP(u_mouse);
  vec2 c = m*0.7;                          // vanishing point steers with cursor
  vec2 d = p - c;
  float a = atan(d.y, d.x);
  float r = length(d);

  float speed = 0.55 + 1.6*u_mDown + 1.2*rippleBurst(p);
  float z = u_time*speed + 0.5/(r + 0.04);

  // thin, crisp light streaks: high angular frequency, stretched along radius
  float s1 = fbm(vec2(a*5.0, z*1.2));
  float s2 = fbm(vec2(a*5.0 + 9.0, z*1.2 + 0.4));   // 2nd sample -> motion-blur feel
  float streak = max(s1, s2);
  streak = pow(smoothstep(0.5, 0.92, streak), 1.4);
  float depth = smoothstep(0.0, 0.22, r);
  float bright = streak*depth;

  vec3 col = vec3(0.012, 0.02, 0.05);
  col += mix(vec3(0.18,0.42,0.95), vec3(0.62,0.85,1.0), streak) * bright * 1.5;
  col += vec3(0.5,0.72,1.0) * exp(-r*5.5) * 0.8;                 // core flash
  col += vec3(0.95,0.74,0.34) * pow(streak,4.0) * depth * 0.5;   // gold sparks
  col *= 1.0 - 0.15*dot(p,p);
  gl_FragColor = vec4(col, 1.0);
}
`;

/* ---------- 5. SILK — caustic drift ---------- */
window.SHADERS.silk = `
void main(){
  vec2 p = toP(gl_FragCoord.xy);
  vec2 m = toP(u_mouse);
  float t = u_time*0.2;

  vec2 q = p;
  for(int i=0;i<4;i++){
    float fi = float(i);
    vec2 pull = (m - q)*exp(-length(m-q)*1.8)*0.25*(1.0 + u_mDown);
    q += pull;
    q += 0.28*vec2(sin(q.y*3.0 + t + fi), cos(q.x*3.0 - t + fi))/(fi + 1.0);
  }
  float v = 0.5 + 0.5*sin(q.x*3.0 + q.y*3.0 + t*2.0);
  v += ripples(p)*0.3;

  float md = length(p - m);
  float light = exp(-md*md*1.6);
  float caustic = pow(max(v,0.0), 3.0);

  vec3 col = mix(vec3(0.05,0.08,0.15), vec3(0.10,0.36,0.31), clamp(v,0.0,1.0));
  col += vec3(0.90,0.80,0.50)*caustic*0.4;       // gold caustic glints
  col += vec3(0.55,0.80,0.90)*light*0.55;        // cursor light
  col *= 1.0 - 0.16*dot(p,p);
  gl_FragColor = vec4(col, 1.0);
}
`;
