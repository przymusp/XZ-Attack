# Commits stats* All commits {len(all_commits)}
* Pure doc commits {len(all_commits) - len(non_doc_commits)}
# Lines stats
* code 15.82 %
* documentation 84.18 %

# Sankey files -> lines -> annotation

```mermaid
---
config:
  sankey:
    showValues: false
---

sankey-beta

project,src,5795
src,xz,1706
xz,[code],1179
xz,[documentation],527
project,po,16413
po,__po__,16413
__po__,[translation],16413
project,__/__,2583
__/__,[documentation],1671
__/__,[code],912
src,liblzma,3893
liblzma,api,1697
api,lzma,1690
lzma,[documentation],2122
api,[documentation],7
liblzma,common,200
common,[documentation],150
common,[code],98
project,tests,4987
tests,__tests__,4936
__tests__,[test],3165
__tests__,[documentation],1771
project,doc,78
doc,logo,11
logo,[documentation],11
project,build-aux,491
build-aux,__build-aux__,491
__build-aux__,[code],421
project,m4,1
m4,__m4__,1
__m4__,[code],1
liblzma,check,779
check,[documentation],632
src,common,48
liblzma,lzma,842
lzma,[code],410
check,[code],147
project,.github,758
.github,workflows,721
workflows,[documentation],123
workflows,[code],598
project,lib,1716
lib,__lib__,1716
__lib__,[documentation],953
__lib__,[code],763
__build-aux__,[documentation],70
liblzma,lz,78
lz,[code],51
lz,[documentation],27
project,po4a,62136
po4a,__po4a__,62136
__po4a__,[translation],62136
liblzma,simple,206
simple,[documentation],71
simple,[code],135
src,scripts,2
scripts,[code],2
.github,__.github__,37
__.github__,[documentation],37
doc,__doc__,49
__doc__,[documentation],49
project,windows,3
windows,__windows__,3
__windows__,[documentation],3
liblzma,[documentation],4
liblzma,[code],4
liblzma,rangecoder,83
rangecoder,[documentation],83
project,dos,8
dos,__dos__,8
__dos__,[documentation],8
tests,ossfuzz,51
ossfuzz,[documentation],23
ossfuzz,[test],28
src,xzdec,146
xzdec,[documentation],80
xzdec,[code],66
project,cmake,5
cmake,__cmake__,5
__cmake__,[code],5
doc,examples,18
examples,[documentation],18

```
