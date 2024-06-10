# Commits stats* All commits {len(all_commits)}
* Pure doc commits {len(all_commits) - len(non_doc_commits)}
# Lines stats
* documentation 97.10 %
* code 2.90 %

# Sankey files -> lines -> annotation

```mermaid
---
config:
  sankey:
    showValues: false
---

sankey-beta

project,__/__,32
__/__,[documentation],32
project,linux,20
linux,include,2
include,_linux,2
linux,[documentation],2
project,userspace,17
userspace,__userspace__,17
__userspace__,[documentation],15
__userspace__,[code],2
linux,Documentation,16
Documentation,[documentation],16
linux,lib,2
lib,xz,2
xz,[documentation],2

```
