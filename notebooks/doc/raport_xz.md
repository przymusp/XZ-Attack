# Commits stats* All commits {len(all_commits)}
* Pure doc commits {len(all_commits) - len(non_doc_commits)}
# Lines stats
* code 14.17 %
* documentation 85.83 %

# Sankey files -> lines -> annotation

```mermaid
---
config:
  sankey:
    showValues: false
---

sankey-beta

project,src,7245
src,xz,1745
xz,[code],1185
xz,[documentation],560
project,po,16413
po,__po__,16413
__po__,[translation],16413
project,__/__,5504
__/__,[code],3817
__/__,[documentation],1687
src,xzdec,158
xzdec,[documentation],87
xzdec,[code],71
src,liblzma,5280
liblzma,api,1707
api,lzma,1700
lzma,[documentation],2129
api,[documentation],7
liblzma,common,200
common,[documentation],157
common,[code],99
project,tests,7277
tests,__tests__,7128
__tests__,[test],4397
__tests__,[documentation],2731
project,doc,78
doc,logo,11
logo,[documentation],11
project,doxygen,137
doxygen,__doxygen__,137
__doxygen__,[code],137
project,build-aux,663
build-aux,__build-aux__,663
__build-aux__,[code],555
project,m4,98
m4,__m4__,98
__m4__,[code],98
liblzma,check,1636
check,[documentation],1219
src,common,56
liblzma,lzma,845
lzma,[code],416
check,[code],417
project,.github,801
.github,workflows,764
workflows,[documentation],139
workflows,[code],625
project,lib,1924
lib,__lib__,1924
__lib__,[documentation],1161
__lib__,[code],763
__build-aux__,[documentation],108
liblzma,lz,78
lz,[code],51
lz,[documentation],27
project,po4a,51099
po4a,__po4a__,51099
__po4a__,[translation],51099
liblzma,simple,701
simple,[code],145
simple,[documentation],556
project,windows,11
windows,vs2013,2
vs2013,[code],2
windows,vs2017,2
vs2017,[code],2
windows,vs2019,2
vs2019,[code],2
src,scripts,6
scripts,[code],6
.github,__.github__,37
__.github__,[documentation],37
doc,__doc__,49
__doc__,[documentation],49
windows,__windows__,5
__windows__,[documentation],3
liblzma,[documentation],4
liblzma,[code],26
tests,files,27
files,[test],27
liblzma,rangecoder,83
rangecoder,[documentation],83
project,dos,8
dos,__dos__,8
__dos__,[documentation],8
__windows__,[code],2
tests,ossfuzz,122
ossfuzz,[test],37
ossfuzz,config,35
config,[test],35
ossfuzz,[documentation],50
project,cmake,5
cmake,__cmake__,5
__cmake__,[code],5
doc,examples,18
examples,[documentation],18

```
