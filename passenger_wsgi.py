import sys, os

INTERP = os.path.join(os.getcwd(), '/virtualenv/repositories/nahor_cf/3.7/bin/python')
sys.path.append(INTERP)


from nahor import app as application