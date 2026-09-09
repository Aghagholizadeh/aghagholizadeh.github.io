---
layout: page
title:
permalink: /
nav: true
nav_title: home
nav_order: 1
---

<div class="sehm-home">
  <section class="sehm-hero">
    <div>
      <img class="sehm-logo" src="{{ '/assets/img/sehm/sehm-lockup.png' | relative_url }}" alt="Structural Engineering and Health Monitoring Laboratory">
      <p class="sehm-eyebrow">Loyola Marymount University · Los Angeles</p>
      <h1>Engineering resilient structures through mechanics, sensing, and data.</h1>
      <p class="sehm-lead">The SEHM Lab investigates the dynamic behavior of structures through engineering mechanics, experimental testing, computational modeling, and data-driven analysis, with applications to earthquake engineering, structural health monitoring, and resilient infrastructure.</p>
      <div class="sehm-actions">
        <a class="sehm-button primary" href="{{ '/research/' | relative_url }}">Explore our research</a>
        <a class="sehm-button" href="{{ '/people/' | relative_url }}">Meet the team</a>
      </div>
    </div>
    <figure class="sehm-visual">
      <img src="{{ '/assets/img/sehm/lab-overview.jpg' | relative_url }}" alt="SEHM laboratory research overview">
    </figure>
  </section>

  <section class="sehm-section">
    <div class="sehm-heading">
      <p class="sehm-eyebrow">Research themes</p>
      <h2>From structural response to informed decisions</h2>
    </div>
    <div class="sehm-grid">
      <a class="sehm-card" href="{{ '/research/#structural-health-monitoring' | relative_url }}">
        <img src="{{ '/assets/img/sehm/bridge-research.jpg' | relative_url }}" alt="Instrumented bridge used for structural health monitoring research">
        <div><span>01</span><h3>Structural Health Monitoring &amp; Digital Twins</h3><p>Physics-informed sensing, machine learning, and uncertainty-aware models for infrastructure assessment.</p></div>
      </a>
      <a class="sehm-card" href="{{ '/research/#earthquake-engineering' | relative_url }}">
        <img src="{{ '/assets/img/sehm/rocking-research.jpg' | relative_url }}" alt="Rocking structural system research">
        <div><span>02</span><h3>Earthquake Engineering &amp; Resilient Systems</h3><p>Rocking and self-centering systems that reduce seismic damage and improve recovery.</p></div>
      </a>
      <a class="sehm-card" href="{{ '/research/#computational-modeling' | relative_url }}">
        <img src="{{ '/assets/img/sehm/modeling-research.jpg' | relative_url }}" alt="Computational structural models">
        <div><span>03</span><h3>Computational Modeling &amp; Simulation</h3><p>High-fidelity and reduced-order models for efficient, reliable prediction of structural response.</p></div>
      </a>
    </div>
  </section>

  <section class="sehm-profile">
    <img src="{{ '/assets/img/sehm/mehrdad-aghagholizadeh.jpg' | relative_url }}" alt="Mehrdad Aghagholizadeh">
    <div>
      <p class="sehm-eyebrow">Lab director</p>
      <h2>Mehrdad Aghagholizadeh, <span class="sehm-credentials">Ph.D., P.E.</span></h2>
      <p>Assistant Professor of Structural Engineering at Loyola Marymount University. His research connects experimental mechanics, computational simulation, and structural health monitoring to advance resilient civil infrastructure.</p>
      <a class="sehm-text-link" href="{{ '/people/' | relative_url }}">People at SEHM <span aria-hidden="true">→</span></a>
    </div>
  </section>

  <section class="sehm-section sehm-split">
    <div><p class="sehm-eyebrow">Recent work</p><h2>Publications</h2><p>Research findings in earthquake engineering, structural health monitoring, computational mechanics, and resilient structural systems.</p><a class="sehm-text-link" href="{{ '/publications/' | relative_url }}">View publications <span aria-hidden="true">→</span></a></div>
    <div><p class="sehm-eyebrow">From the lab</p><h2>Latest news</h2><p>Conference presentations, new publications, student research, and updates from the SEHM Lab.</p><a class="sehm-text-link" href="{{ '/news/' | relative_url }}">Read lab news <span aria-hidden="true">→</span></a></div>
  </section>

  <section class="sehm-academic-profiles" aria-labelledby="academic-profiles-title">
    <div>
      <p class="sehm-eyebrow">Connect</p>
      <h2 id="academic-profiles-title">Academic profiles</h2>
    </div>
    <div class="sehm-profile-links">{% social_links %}</div>
  </section>
</div>

<style>
.sehm-home{--accent:#9f1b2e}.sehm-home h1,.sehm-home h2,.sehm-home h3{letter-spacing:-.035em}.sehm-hero{display:grid;grid-template-columns:minmax(0,1.02fr) minmax(360px,.98fr);gap:clamp(2.5rem,6vw,6rem);align-items:center;min-height:66vh;padding:4.5rem 0 5.5rem}.sehm-logo{width:min(340px,78%);max-height:105px;object-fit:contain;object-position:left center;margin-bottom:2.25rem}.sehm-eyebrow{color:var(--accent);font-size:.76rem;font-weight:700;letter-spacing:.12em;margin:0 0 .85rem;text-transform:uppercase}.sehm-hero h1{font-size:clamp(2.45rem,5vw,4.65rem);line-height:.98;margin:0 0 1.6rem}.sehm-lead{font-size:clamp(1.05rem,1.7vw,1.28rem);line-height:1.65}.sehm-actions{display:flex;flex-wrap:wrap;gap:.8rem;margin-top:2.1rem}.sehm-button{border:1px solid var(--global-divider-color);border-radius:999px;color:var(--global-text-color)!important;display:inline-flex;font-weight:650;padding:.78rem 1.25rem;text-decoration:none!important;transition:.18s}.sehm-button:hover{border-color:var(--accent);transform:translateY(-2px)}.sehm-button.primary{background:var(--accent);border-color:var(--accent);color:#fff!important}.sehm-visual{margin:0;position:relative}.sehm-visual:before{background:var(--accent);content:"";height:54%;left:-14px;position:absolute;top:-14px;width:44%;z-index:-1}.sehm-visual img{aspect-ratio:4/5;border-radius:2px;box-shadow:0 26px 70px rgba(0,0,0,.16);object-fit:cover;width:100%}.sehm-section{border-top:1px solid var(--global-divider-color);padding:5.25rem 0}.sehm-heading{max-width:720px;margin-bottom:2.25rem}.sehm-section h2{font-size:clamp(1.85rem,3vw,2.65rem);line-height:1.1}.sehm-profile h2{font-size:clamp(1.75rem,2.5vw,2.25rem);line-height:1.12}.sehm-credentials{white-space:nowrap}.sehm-grid{display:grid;gap:1.25rem;grid-template-columns:repeat(3,1fr)}.sehm-card{border:1px solid var(--global-divider-color);color:var(--global-text-color)!important;overflow:hidden;text-decoration:none!important;transition:.2s}.sehm-card:hover{box-shadow:0 20px 45px rgba(0,0,0,.11);transform:translateY(-5px)}.sehm-card>img{aspect-ratio:4/3;object-fit:cover;width:100%}.sehm-card>div{padding:1.35rem 1.35rem 1.55rem}.sehm-card span{color:var(--accent);font-size:.72rem;font-weight:750;letter-spacing:.12em}.sehm-card h3{font-size:1.22rem;line-height:1.2;margin:.55rem 0 .75rem}.sehm-card p{color:var(--global-text-color-light);font-size:.94rem;line-height:1.55;margin:0}.sehm-profile{align-items:center;background:color-mix(in srgb,var(--global-card-bg-color) 82%,var(--accent) 18%);display:grid;gap:clamp(2rem,5vw,4.5rem);grid-template-columns:minmax(220px,.62fr) 1.38fr;margin:1.5rem 0 5.5rem;padding:clamp(2rem,5vw,4.5rem)}.sehm-profile>img{aspect-ratio:1;border-radius:50%;object-fit:cover;width:100%}.sehm-profile p:not(.sehm-eyebrow){font-size:1.05rem;line-height:1.7}.sehm-text-link{color:var(--accent)!important;font-weight:700;text-decoration:none!important}.sehm-text-link span{display:inline-block;transition:.18s}.sehm-text-link:hover span{transform:translateX(4px)}.sehm-split{display:grid;gap:clamp(2rem,7vw,7rem);grid-template-columns:repeat(2,1fr)}.sehm-academic-profiles{align-items:center;border-top:1px solid var(--global-divider-color);display:flex;justify-content:space-between;padding:3.25rem 0 1.25rem}.sehm-academic-profiles h2{font-size:1.45rem;margin:0}.sehm-profile-links{font-size:3.75rem;line-height:1;text-align:right}.sehm-profile-links a{display:inline-block;margin-left:1.4rem;transition:transform .18s ease}.sehm-profile-links a:hover{transform:translateY(-3px)}html[data-theme=dark] .sehm-logo{filter:invert(1);mix-blend-mode:screen}
@media(max-width:800px){.sehm-hero{grid-template-columns:1fr;min-height:auto;padding:3rem 0 4rem}.sehm-visual img{aspect-ratio:16/10}.sehm-grid{grid-template-columns:1fr}.sehm-profile{grid-template-columns:1fr}.sehm-profile>img{max-width:220px}}@media(max-width:560px){.sehm-hero h1{font-size:2.55rem}.sehm-split{grid-template-columns:1fr}.sehm-academic-profiles{align-items:flex-start;flex-direction:column;gap:1.25rem}.sehm-profile-links{font-size:3.2rem;text-align:left}.sehm-profile-links a{margin:0 1.25rem 0 0}}
</style>
