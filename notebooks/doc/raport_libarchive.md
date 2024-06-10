# Commits stats* All commits {len(all_commits)}
* Pure doc commits {len(all_commits) - len(non_doc_commits)}
# Lines stats
* code 40.25 %
* documentation 42.10 %
* test 17.65 %

# Sankey files -> lines -> annotation

```mermaid
---
config:
  sankey:
    showValues: false
---

sankey-beta

project,libarchive,799
libarchive,test,694
test,[test],366
project,test_utils,2
test_utils,__test_utils__,2
__test_utils__,[test],2
libarchive,__libarchive__,105
__libarchive__,[documentation],13
__libarchive__,[code],90
test,[documentation],328
__libarchive__,[translation],2
project,tar,7
tar,__tar__,7
__tar__,[code],7
project,__/__,2
__/__,[code],2

```
