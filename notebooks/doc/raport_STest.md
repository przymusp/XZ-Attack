# Commits stats* All commits {len(all_commits)}
* Pure doc commits {len(all_commits) - len(non_doc_commits)}
# Lines stats
* documentation 26.18 %
* code 73.82 %

# Sankey files -> lines -> annotation

```mermaid
---
config:
  sankey:
    showValues: false
---

sankey-beta

project,src,2615
src,__src__,2615
__src__,[documentation],575
__src__,[test],2040
project,__/__,223
__/__,[documentation],223
project,tests,401
tests,__tests__,401
__tests__,[documentation],50
__tests__,[test],351

```
