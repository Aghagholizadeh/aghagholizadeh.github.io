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

<style>
.research-cards {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1rem;
  margin: 1rem 0 2rem;
}

.research-card {
  display: block;
  text-decoration: none !important;
  color: inherit !important;
  perspective: 1000px;
}

.research-card__inner {
  position: relative;
  width: 100%;
  aspect-ratio: 4 / 5;
  transition: transform 0.65s ease;
  transform-style: preserve-3d;
}

.research-card:hover .research-card__inner,
.research-card:focus .research-card__inner,
.research-card:focus-visible .research-card__inner {
  transform: rotateY(180deg);
}

.research-card__front,
.research-card__back {
  position: absolute;
  inset: 0;
  overflow: hidden;
  border-radius: 4px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.12);
}

.research-card__front {
  background: #fff;
  display: flex;
  flex-direction: column;
}

.research-card__front img {
  width: 100%;
  height: 72%;
  object-fit: cover;
  display: block;
}

.research-card__title {
  margin: 0;
  padding: 0.8rem 0.75rem;
  font-size: 1rem;
  line-height: 1.25;
  text-align: center;
  color: #494e52;
}

.research-card__back {
  background: #494e52;
  color: #fff;
  transform: rotateY(180deg);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1.2rem;
  text-align: center;
}

.research-card__back p {
  margin: 0;
  font-size: 0.92rem;
  line-height: 1.5;
}

@media (max-width: 767px) {
  .research-cards {
    grid-template-columns: 1fr;
  }

  .research-card__inner {
    aspect-ratio: 16 / 11;
  }

  .research-card__front img {
    height: 70%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .research-card__inner {
    transition: none;
  }
}
</style>

<div class="research-cards">

  <a class="research-card"
     href="/research/#structural-health-monitoring"
     aria-label="Structural Health Monitoring and Digital Twins">
    <div class="research-card__inner">

      <div class="research-card__front">
        <img src="/images/bridge-research.jpg"
             alt="Laboratory bridge for structural health monitoring research">
        <h3 class="research-card__title">
          Structural Health Monitoring &amp; Digital Twins
        </h3>
      </div>

      <div class="research-card__back">
        <p>
          Experimental and computational methods for vibration-based structural
          health monitoring, physics-informed machine learning, and uncertainty-aware
          digital twins for infrastructure condition assessment.
        </p>
      </div>

    </div>
  </a>

  <a class="research-card"
     href="/research/#earthquake-engineering"
     aria-label="Earthquake Engineering and Resilient Systems">
    <div class="research-card__inner">

      <div class="research-card__front">
        <img src="/images/rocking-research.jpg"
             alt="Rocking and self-centering structural systems">
        <h3 class="research-card__title">
          Earthquake Engineering &amp; Resilient Systems
        </h3>
      </div>

      <div class="research-card__back">
        <p>
          Rocking, self-centering, and damage-limiting structural systems designed
          to reduce seismic damage and improve post-earthquake functionality.
        </p>
      </div>

    </div>
  </a>

  <a class="research-card"
     href="/research/#computational-modeling"
     aria-label="Computational Modeling and Simulation">
    <div class="research-card__inner">

      <div class="research-card__front">
        <img src="/images/modeling-research.jpg"
             alt="Computational structural modeling and simulation">
        <h3 class="research-card__title">
          Computational Modeling &amp; Simulation
        </h3>
      </div>

      <div class="research-card__back">
        <p>
          High-fidelity finite element modeling, reduced-order methods, model
          updating, and uncertainty quantification for efficient and reliable
          prediction of structural response.
        </p>
      </div>

    </div>
  </a>

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
