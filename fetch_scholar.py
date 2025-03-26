from scholarly import scholarly

# Replace with your actual Google Scholar ID
scholar_id = "Nt-tWzsAAAAJ"

# Fetch your Google Scholar profile
author = scholarly.fill(scholarly.search_author_id(scholar_id))
 
# Prepare markdown content
md_content = "# 📚 Publications\n\n"
for pub in author['publications']:
    pub_filled = scholarly.fill(pub)
    title = pub_filled.get('bib', {}).get('title', 'N/A')
    authors = pub_filled.get('bib', {}).get('author', 'N/A')
    journal = pub_filled.get('bib', {}).get('journal', '')
    year = pub_filled.get('bib', {}).get('pub_year', '')
    citedby = pub_filled.get('num_citations', 0)

    md_content += f"- **{title}**, {authors}. *{journal}*, {year}. (Cited by: {citedby})\n"

# Write publications to markdown file
# with open("publications.md", "w", encoding="utf-8") as file:
 with open("publications/index.md", "w", encoding="utf-8") as file:
    file.write(md_content)
