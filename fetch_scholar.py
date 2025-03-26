from scholarly import scholarly

scholar_id = "Nt-tWzsAAAAJ"

author = scholarly.fill(scholarly.search_author_id(scholar_id))

#md_content = "# 📚 Publications\n\n"
md_content = "_Updated automatically from [Google Scholar](https://scholar.google.com/citations?user=Nt-tWzsAAAAJ)._\n\n"

for pub in author['publications']:
    pub_filled = scholarly.fill(pub)
    title = pub_filled.get('bib', {}).get('title', 'N/A')
    authors = pub_filled.get('bib', {}).get('author', 'N/A')
    journal = pub_filled.get('bib', {}).get('journal', '')
    year = pub_filled.get('bib', {}).get('pub_year', '')
    citedby = pub_filled.get('num_citations', 0)

    md_content += f"- **{title}**, {authors}. *{journal}*, {year}. (Cited by: {citedby})\n"

with open("list-of-publications.md", "w", encoding="utf-8") as file:
    file.write(md_content)
