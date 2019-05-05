#!/usr/bin/env python
# Triplet UHF ground state of carbon atom.

from pyscf import gto, scf
from pauxy.utils.linalg import get_orthoAO
from pauxy.utils.from_pyscf import dump_pauxy
from pauxy.estimators.greens_function import gab
import numpy

import h5py

mol = gto.Mole()
mol.basis = 'cc-pvtz'
mol.atom = (('C', 0,0,0),)
mol.spin = 2
mol.verbose = 4
mol.build()

mf = scf.UHF(mol)
mf.chkfile = 'scf.chk'
mf.kernel()
# Check if UHF solution is stable.
mf.stability()
