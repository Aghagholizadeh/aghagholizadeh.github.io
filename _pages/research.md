---
layout: page
title: research
permalink: /research/
nav: true
nav_order: 3
description: Research in structural dynamics, earthquake engineering, structural health monitoring, digital twins, and computational mechanics.
---

<div class="research-page">
  <header class="research-intro">
    <p class="research-kicker">SEHM Lab · Loyola Marymount University</p>
    <h1>Research grounded in mechanics, computation, and experiment.</h1>
    <p>The SEHM Lab studies the behavior of structural systems under dynamic loading. Our work integrates analytical mechanics, laboratory and field experiments, computational modeling, system identification, and data-driven methods to advance earthquake engineering and structural health monitoring.</p>
  </header>

  <nav class="research-index" aria-label="Research areas">
    <a href="#earthquake-engineering"><span>01</span> Earthquake engineering</a>
    <a href="#structural-health-monitoring"><span>02</span> Structural health monitoring</a>
    <a href="#computational-modeling"><span>03</span> Computational modeling</a>
  </nav>

  <section class="research-feature" id="earthquake-engineering">
    <div class="research-feature__image"><img src="{{ '/assets/img/sehm/research/rocking-shear-wall.webp' | relative_url }}" alt="Rocking shear wall coupled to a moment-resisting frame"></div>
    <div class="research-feature__copy">
      <p class="research-kicker">01 · Earthquake engineering</p>
      <h2>Rocking and self-centering structural systems</h2>
      <p>Weak-story mechanisms and concentrated drift demands are recurring causes of severe damage in multistory buildings. We investigate hybrid systems that couple moment-resisting frames with stiff walls permitted to uplift and rock during earthquake excitation, promoting a more uniform distribution of deformation over the structural height.</p>
      <p>Our analytical and nonlinear numerical studies examine the dynamics of yielding frames coupled with rocking walls, the influence of wall configuration and supplemental damping, and the resulting effects on residual drift, damage, and post-earthquake functionality.</p>
    </div>
  </section>

  <section class="research-feature research-feature--reverse" id="structural-health-monitoring">
    <div class="research-feature__image"><img src="{{ '/assets/img/sehm/research/structural-health-monitoring.png' | relative_url }}" alt="Experimental structural health monitoring setup"></div>
    <div class="research-feature__copy">
      <p class="research-kicker">02 · Structural health monitoring</p>
      <h2>Physics-based digital twins and damage detection</h2>
      <p>Aging infrastructure requires reliable methods for identifying structural change and supporting condition-based decisions. We combine measured vibration response with mechanics-based models to develop digital twins capable of system identification, model updating, damage detection, and prognosis.</p>
      <p>SEHM Lab research draws on laboratory experiments and field measurements from bridges, stadiums, and energy infrastructure. Current work emphasizes physics-based vibration features, uncertainty-aware inference, and learning methods that remain connected to structural behavior.</p>
    </div>
  </section>

  <article class="research-project">
    <div>
      <p class="research-label">Current experimental platform</p>
      <h3>Digital Twin Bridge Mockup</h3>
      <p>A two-span steel bridge mockup supports research in experimental structural dynamics, reduced-order modeling, and physics-based digital twins. CNC-fabricated components, instrumented steel columns, finite element models, and experimental mode identification provide a controlled platform for real-time system identification and damage-detection studies.</p>
    </div>
    <img src="{{ '/assets/img/sehm/research/bridge-mockup.png' | relative_url }}" alt="Bridge mockup fabrication, finite element modeling, and vibration-analysis workflow">
  </article>

  <section class="research-feature" id="computational-modeling">
    <div class="research-feature__image"><img src="{{ '/assets/img/sehm/research/finite-element-modeling.png' | relative_url }}" alt="High-fidelity finite element model used for dynamic analysis"></div>
    <div class="research-feature__copy">
      <p class="research-kicker">03 · Computational modeling</p>
      <h2>High-fidelity and reduced-order structural models</h2>
      <p>Detailed finite element models can reproduce complex structural dynamics, but repeated analyses for model updating, uncertainty quantification, and inverse problems remain computationally demanding.</p>
      <p>We develop and apply substructuring and component mode synthesis methods—including Craig–Bampton reduction—to construct computationally efficient models that preserve the modes, frequency-response functions, and physical characteristics important to dynamic analysis.</p>
    </div>
  </section>

  <section class="research-secondary">
    <div class="research-secondary__heading">
      <p class="research-kicker">Extended applications</p>
      <h2>Mechanics across scales and disciplines</h2>
    </div>
    <div class="research-secondary__grid">
      <article>
        <img src="{{ '/assets/img/sehm/research/rocking-bridge-pier.png' | relative_url }}" alt="Rocking bridge pier concept with supplemental dampers">
        <div><h3>Rocking bridge piers</h3><p>We study tall, slender bridge piers that uplift and rotate above their foundations, including the use of supplemental hysteretic and viscous dampers to control dynamic response while preserving self-centering behavior.</p><p class="research-note">This work was recognized with the ASCE J. James R. Croes Medal.</p></div>
      </article>
      <article>
        <img src="{{ '/assets/img/sehm/research/rapa-nui.webp' | relative_url }}" alt="Toppled monumental stone statue at Rapa Nui">
        <div><h3>Dynamics of monumental architecture</h3><p>In collaboration with archaeologists and seismologists, we use field evidence and physics-based modeling to evaluate competing explanations for the toppling of monumental statues at Rapa Nui.</p><a href="https://www.nsf.gov/awardsearch/show-award?AWD_ID=2401213">NSF Award 2401213 →</a></div>
      </article>
    </div>
  </section>

  <section class="research-students">
    <img src="{{ '/assets/img/sehm/research/student-research.webp' | relative_url }}" alt="Students conducting structural engineering experiments in the SEHM Lab">
    <div><p class="research-kicker">Student research</p><h2>Learn by investigating real structural systems.</h2><p>Students participate in digital-twin development, experimental structural dynamics, computational modeling, and seismic-resilience projects. Motivated LMU students interested in research are encouraged to get in touch.</p><a class="research-button" href="mailto:mehrdad.aghagholizadeh@lmu.edu">Contact the lab</a></div>
  </section>
</div>

<style>
.research-page{--accent:#9f1b2e}.research-page h1,.research-page h2,.research-page h3{letter-spacing:-.035em}.research-intro{max-width:860px;padding:4.5rem 0 3rem}.research-intro h1{font-size:clamp(2.7rem,5.6vw,5.2rem);line-height:.98;margin:.5rem 0 1.6rem}.research-intro>p:last-child{color:var(--global-text-color-light);font-size:clamp(1.05rem,1.7vw,1.3rem);line-height:1.7;max-width:790px}.research-kicker,.research-label{color:var(--accent);font-size:.75rem;font-weight:750;letter-spacing:.12em;text-transform:uppercase}.research-index{border-bottom:1px solid var(--global-divider-color);border-top:1px solid var(--global-divider-color);display:grid;grid-template-columns:repeat(3,1fr);margin-bottom:6rem}.research-index a{color:var(--global-text-color)!important;font-weight:650;padding:1.25rem .75rem 1.25rem 0;text-decoration:none!important}.research-index span{color:var(--accent);font-size:.72rem;margin-right:.45rem}.research-feature{align-items:center;display:grid;gap:clamp(2.5rem,7vw,7rem);grid-template-columns:minmax(0,.95fr) minmax(0,1.05fr);padding:1rem 0 7rem;scroll-margin-top:6rem}.research-feature--reverse .research-feature__image{order:2}.research-feature__image{position:relative}.research-feature__image:after{border:1px solid var(--accent);content:"";height:100%;left:14px;position:absolute;top:14px;width:100%;z-index:-1}.research-feature__image img{aspect-ratio:4/3;background:#fff;object-fit:cover;width:100%}.research-feature__copy h2,.research-secondary h2,.research-students h2{font-size:clamp(2rem,3.7vw,3.25rem);line-height:1.05;margin:.75rem 0 1.35rem}.research-feature__copy p{font-size:1.02rem;line-height:1.72}.research-project{align-items:center;background:color-mix(in srgb,var(--global-card-bg-color) 84%,var(--accent) 16%);display:grid;gap:3rem;grid-template-columns:.9fr 1.1fr;margin:0 0 7rem;padding:clamp(2rem,5vw,4rem)}.research-project h3{font-size:2rem;margin:.5rem 0 1rem}.research-project p{line-height:1.7}.research-project img{background:#fff;width:100%}.research-secondary{border-top:1px solid var(--global-divider-color);padding:5rem 0 6rem}.research-secondary__heading{max-width:700px;margin-bottom:2.5rem}.research-secondary__grid{display:grid;gap:1.5rem;grid-template-columns:repeat(2,1fr)}.research-secondary article{border:1px solid var(--global-divider-color)}.research-secondary article>img{aspect-ratio:16/10;background:#fff;object-fit:cover;width:100%}.research-secondary article>div{padding:1.6rem}.research-secondary h3{font-size:1.55rem;margin:0 0 1rem}.research-secondary article p{line-height:1.65}.research-secondary article a{color:var(--accent)!important;font-weight:700;text-decoration:none!important}.research-note{color:var(--global-text-color-light);font-size:.9rem;font-style:italic}.research-students{align-items:center;border-top:1px solid var(--global-divider-color);display:grid;gap:clamp(2.5rem,7vw,7rem);grid-template-columns:.9fr 1.1fr;padding:6rem 0 3rem}.research-students>img{aspect-ratio:4/3;object-fit:cover;width:100%}.research-students p:not(.research-kicker){font-size:1.05rem;line-height:1.7}.research-button{background:var(--accent);border-radius:999px;color:#fff!important;display:inline-flex;font-weight:700;margin-top:1rem;padding:.75rem 1.2rem;text-decoration:none!important}
@media(max-width:800px){.research-index{grid-template-columns:1fr;margin-bottom:4rem}.research-index a{border-bottom:1px solid var(--global-divider-color)}.research-feature,.research-project,.research-students{grid-template-columns:1fr}.research-feature--reverse .research-feature__image{order:0}.research-feature{padding-bottom:5rem}.research-secondary__grid{grid-template-columns:1fr}}
</style>
