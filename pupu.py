#coding:L1
d,m='',0
t=['y�x�w�v�vSJ�v�v�w�hNN�fPP�cSQ�cSP�]^J�Y�V�T�S�R�Q�P�P�OSIUI�OPIJHOHJH�O�P�P�P�N�M�LdHMH�KVLQM�J�J�J�J�K�L�M�N�O�R�V�','L1']
for c in bytearray(*t[0:(str!=bytes)+1]):
 d+=c%70*" *"[m];m=(m+1)%2
 if c>140:print(d);d=''