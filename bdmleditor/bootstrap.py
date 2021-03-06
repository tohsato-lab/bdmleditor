import h5py
import sys
import numpy as np


def data_load(hdfpath, object_id):
    with h5py.File(hdfpath, 'r') as f:
        data = []
        data.append(f[object_id][()])
        # Todo 抽象化
        dimension = f['data/scaleUnit']['dimension'].astype(np.str)
        f.close()
    return data, dimensional_judge(dimension[0])


def dimensional_judge(dimension):
    if '3D' in dimension:
        return '3D'
    elif '2D' in dimension:
        return '2D'
    else:
        sys.exit("didn't know the dimensions.")


def objectdef_load(hdfpath):
    with h5py.File(hdfpath, 'r') as f:
        objectdef_list = f['data/objectDef']['oID']
        f.close()
    return objectdef_list
