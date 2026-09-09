---
layout: page
title: news
permalink: /news/
nav: true
nav_order: 5
---

<div class="sehm-news">
  <header class="news-intro">
    <p class="news-eyebrow">From the lab</p>
    <h1>News</h1>
    <p>Publications, conference presentations, student research, and other updates from the SEHM Lab.</p>
  </header>

  {% assign posts_by_year = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}
  <div class="news-archive">
    {% for year in posts_by_year %}
      <section class="news-year" aria-labelledby="news-{{ year.name }}">
        <h2 id="news-{{ year.name }}">{{ year.name }}</h2>
        <div class="news-list">
          {% for post in year.items %}
            <article class="news-card"><a href="{{ post.url | relative_url }}" aria-label="Read {{ post.title }}">
              <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%B %-d, %Y' }}</time>
              <h3>{{ post.title }}</h3>
              <p>{{ post.content | strip_html | normalize_whitespace | truncatewords: 30 }}</p>
              {% if post.tags.size > 0 %}<div class="news-tags">{% for tag in post.tags limit:3 %}<span>{{ tag | replace: '-', ' ' }}</span>{% endfor %}</div>{% endif %}
              <span class="read-more">Read update <b aria-hidden="true">→</b></span>
            </a></article>
          {% endfor %}
        </div>
      </section>
    {% endfor %}
  </div>
</div>

<style>
.sehm-news{--accent:#9f1b2e}.sehm-news h1,.sehm-news h2,.sehm-news h3{letter-spacing:-.035em}.news-intro{max-width:760px;padding:3.5rem 0 4.5rem}.news-eyebrow{color:var(--accent);font-size:.76rem;font-weight:750;letter-spacing:.12em;margin:0 0 .8rem;text-transform:uppercase}.news-intro h1{font-size:clamp(3rem,6vw,5rem);line-height:1;margin:.2rem 0 1.3rem}.news-intro>p:last-child{color:var(--global-text-color-light);font-size:clamp(1.08rem,1.7vw,1.3rem);line-height:1.65}.news-year{border-top:1px solid var(--global-divider-color);display:grid;gap:clamp(1.5rem,4vw,4rem);grid-template-columns:120px 1fr;padding:3.5rem 0}.news-year>h2{color:var(--accent);font-size:1.25rem;margin:.25rem 0}.news-list{display:grid;gap:1rem}.news-card>a{border:1px solid var(--global-divider-color);color:var(--global-text-color)!important;display:block;padding:clamp(1.35rem,3vw,2rem);text-decoration:none!important;transition:.2s}.news-card>a:hover{border-color:var(--accent);box-shadow:0 14px 36px rgba(0,0,0,.08);transform:translateY(-3px)}.news-card time{color:var(--accent);font-size:.75rem;font-weight:750;letter-spacing:.08em;text-transform:uppercase}.news-card h3{font-size:clamp(1.3rem,2.2vw,1.75rem);line-height:1.2;margin:.55rem 0 .75rem}.news-card p{color:var(--global-text-color-light);line-height:1.6;margin:0;max-width:780px}.news-tags{display:flex;flex-wrap:wrap;gap:.45rem;margin-top:1.2rem}.news-tags span{background:var(--global-card-bg-color);border-radius:999px;font-size:.68rem;font-weight:650;padding:.3rem .55rem;text-transform:capitalize}.read-more{color:var(--accent);display:inline-block;font-size:.88rem;font-weight:750;margin-top:1.2rem}.read-more b{display:inline-block;transition:.18s}.news-card>a:hover .read-more b{transform:translateX(4px)}
@media(max-width:680px){.news-intro{padding-top:2.5rem}.news-year{grid-template-columns:1fr;gap:.7rem}.news-year>h2{font-size:1rem}}
</style>
