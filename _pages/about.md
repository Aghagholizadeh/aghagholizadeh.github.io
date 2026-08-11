---
permalink: /
title: "Welcome to the Structural Engineering and Health Monitoring (SEHM) Lab at LMU"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<p align="center">
  <img src="/images/website_welcome.png"
       alt="Overview of the Structural Engineering and Health Monitoring Laboratory"
       width="100%">
</p>

The high occupancy of urban multistory buildings, the aging of critical infrastructure, and evolving safety and sustainability expectations all demand new performance objectives for civil structures. Research at the Structural Engineering and Health Monitoring (SEHM) Lab at Loyola Marymount University focuses on developing resilient, damage-limiting structural systems and data-informed methodologies for buildings and bridges subjected to earthquakes and other natural hazards.

**SEHM Lab research integrates analytical modeling, computational simulation, and experimental validation, with emphasis on:**
- **Rocking and self-centering structural systems** for damage-limiting seismic response and retrofit of buildings and bridges  
- **Physics-based and probabilistic digital twins** for real-time structural health monitoring and condition assessment  
- **High-fidelity finite element and reduced-order modeling** to enable efficient simulation, model updating, and uncertainty quantification  

Current work in the SEHM Lab combines numerical studies with laboratory-scale and system-level investigations to better understand structural response, improve predictive capabilities, and support performance-based engineering decisions.

For more details on ongoing research activities and projects, please visit the lab’s [Research page](/research/).

---

## Featured Research

<div class="feature__wrapper">

  <div class="feature__item">
    <div class="archive__item">
      <div class="archive__item-teaser">
        <img src="/images/bridge-research.jpg"
             alt="Laboratory bridge for structural health monitoring research">
      </div>
      <div class="archive__item-body">
        <h3 class="archive__item-title">
          Structural Health Monitoring & Digital Twins
        </h3>
        <div class="archive__item-excerpt">
          <p>
            Experimental and computational methods for vibration-based structural
            health monitoring, physics-informed machine learning, and uncertainty-aware
            digital twins for infrastructure condition assessment.
          </p>
        </div>
        <p>
          <a href="/research/#structural-health-monitoring"
             class="btn btn--primary">Learn more</a>
        </p>
      </div>
    </div>
  </div>

  <div class="feature__item">
    <div class="archive__item">
      <div class="archive__item-teaser">
        <img src="/images/rocking-research.jpg"
             alt="Rocking and self-centering structural systems">
      </div>
      <div class="archive__item-body">
        <h3 class="archive__item-title">
          Earthquake Engineering & Resilient Systems
        </h3>
        <div class="archive__item-excerpt">
          <p>
            Rocking, self-centering, and damage-limiting structural systems designed
            to reduce seismic damage and improve post-earthquake functionality.
          </p>
        </div>
        <p>
          <a href="/research/#earthquake-engineering"
             class="btn btn--primary">Learn more</a>
        </p>
      </div>
    </div>
  </div>

  <div class="feature__item">
    <div class="archive__item">
      <div class="archive__item-teaser">
        <img src="/images/modeling-research.jpg"
             alt="Computational structural modeling and simulation">
      </div>
      <div class="archive__item-body">
        <h3 class="archive__item-title">
          Computational Modeling & Simulation
        </h3>
        <div class="archive__item-excerpt">
          <p>
            High-fidelity finite element modeling, reduced-order methods, model
            updating, and uncertainty quantification for efficient and reliable
            prediction of structural response.
          </p>
        </div>
        <p>
          <a href="/research/#computational-modeling"
             class="btn btn--primary">Learn more</a>
        </p>
      </div>
    </div>
  </div>

</div>

---

## Latest News

{% for post in site.posts limit:3 %}

<div class="archive__item">

  <p class="page__meta">
    {{ post.date | date: "%B %Y" }}
  </p>

  <h3 class="archive__item-title">
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
  </h3>

  <div class="archive__item-excerpt">
    {% if post.excerpt %}
      {{ post.excerpt | strip_html | truncatewords: 35 }}
    {% endif %}
  </div>

  <p>
    <a href="{{ post.url | relative_url }}">Read more &rarr;</a>
  </p>

</div>

{% endfor %}

<p style="text-align: right;">
  <a href="/news/"><strong>View all news &rarr;</strong></a>
</p>
