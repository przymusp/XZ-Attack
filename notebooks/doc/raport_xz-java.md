# Commits stats* All commits {len(all_commits)}
* Pure doc commits {len(all_commits) - len(non_doc_commits)}
# Lines stats
* documentation 45.00 %
* code 55.00 %

# Sankey files -> lines -> annotation

```mermaid
---
config:
  sankey:
    showValues: false
---

sankey-beta

project,src,48
src,org,48
org,tukaani,48
tukaani,xz,48
xz,[documentation],20
xz,[code],25
xz,index,3
index,[code],2
index,[documentation],1
project,__/__,8
__/__,[documentation],6
__/__,[code],2
project,maven,4
maven,__maven__,4
__maven__,[translation],4

```
