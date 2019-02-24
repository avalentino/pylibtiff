import pytest
from tempfile import mktemp
import atexit
import numpy as np

lt = pytest.importorskip('libtiff.libtiff_ctypes')
from libtiff import TIFFimage
    
def test_issue69():
    itype = np.uint32
    image = np.array([[[1,2,3], [4,5,6]]], itype)
    fn = mktemp('issue69.tif')
    tif = TIFFimage(image)
    tif.write_file(fn)
    del tif
    tif = lt.TIFF3D.open(fn)
    tif.close()
