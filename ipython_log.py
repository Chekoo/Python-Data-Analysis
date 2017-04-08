# IPython log file

get_ipython().system(u'date')
thedate = get_ipython().getoutput(u'date')
thedate
a = 2 + 2
a
get_ipython().magic(u'hist')
get_ipython().magic(u'hist -g a = 2')
get_ipython().magic(u'logstart ')
get_ipython().magic(u'logoff ')
