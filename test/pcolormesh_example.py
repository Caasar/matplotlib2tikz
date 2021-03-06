# -*- coding: utf-8 -*-
"""
An example of how a pcolormesh will be saved as a tikz graphic

@author: Caasar
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import cPickle as pickle
import matplotlib2tikz

def poly_kernel(x1,x2,d=2):
    """Polynom kernel"""
    return (.5*(x1.dot(x2.T)+1.0))**2

def find_bounding_box(X):
    maxv = np.max(X,0)
    minv = np.min(X,0)
    center = .5*(maxv+minv)
    rangev = .515*(maxv-minv)
    return np.c_[center-rangev,center+rangev].T

def custom_colormap():
    # build colormap
    cdict = {'red' : [(0.0,1.0,1.0),
                      (0.5,1.0,1.0),
                      (1.0,0.0,1.0)],
             'blue': [(0.0,0.0,0.0),
                      (0.5,1.0,1.0),
                      (1.0,1.0,1.0)],
             'green':[(0.0,0.0,0.0),
                      (0.5,1.0,1.0),
                      (1.0,0.0,0.0)]}
    return mpl.colors.LinearSegmentedColormap('discrmap',cdict)

def plot_modeldecision(Xdata,ydata,svs,aly,b,kernel):
    """plot a two class svm decision"""
    box = find_bounding_box(Xdata)
    x = np.linspace(box[0,0],box[1,0],128)
    y = np.linspace(box[0,1],box[1,1],128)
    
    X,Y = np.meshgrid(x,y)
    
    Xtest = np.c_[X.ravel(),Y.ravel()]
    ftest = np.dot(poly_kernel(Xtest,svs),aly)-b
    ftest.shape = 128,128
    
    ftest_scale = ftest.copy()
    ftest_scale[ftest>0] /= 2.0*ftest.max()
    ftest_scale[ftest<0] /= 2.0*abs(ftest.min())
    ftest_scale += .5
    
    plt.pcolormesh(X,Y,ftest_scale,shading='gouraud',cmap=custom_colormap())
    plt.contour(X,Y,ftest,[0.0],colors='k',linewidths=4)
    plt.contour(X,Y,ftest,[-1.0,1.0],colors='k',linewidths=2,linestyles='solid')
    plt.plot(Xdata[ydata<0,0],Xdata[ydata<0,1],'ok',markerfacecolor='r')
    plt.plot(Xdata[ydata>0,0],Xdata[ydata>0,1],'dk',markerfacecolor='b')
    

# data
data = '\x80\x02cnumpy.core.multiarray\n_reconstruct\nq\x01cnumpy\nndarray\nq\x02K\x00\x85U\x01b\x87Rq\x03(K\x01K\xc8K\x02\x86cnumpy\ndtype\nq\x04U\x02f4K\x00K\x01\x87Rq\x05(K\x03U\x01<NNNJ\xff\xff\xff\xffJ\xff\xff\xff\xffK\x00tb\x89T@\x06\x00\x00\x92\xbc\x0f\xbf\x8f_\xc4>\xc7\xb73\xbf\x10#\x0f?\x95\xd1\xc2\xbd\xc6\x9cr>\xc2N.?O\x1a*?\x0e\x8d@\xbf\xd5\xe27?qkr?-17?\x8fU\n\xbf6Xa\xbf\xa0\xb5\xe5=\r\xe9\xfb\xbe>\xe5]\xbe[\x8a\xf3>Xl\xd3\xbe\xca\x1b\xbd\xbe\xe9\xa3\xe4\xbe\xb1\xed\xec>\x1a\xd7\x8f\xbd\x06i\x1a\xbf\xc4\xea\xeb\xbd\xe8y\x0e\xbf@\x94\x99>\x063\x00\xbf\xb2X\xe5\xbe.\xaa\xb6=\xe6jU\xbee\x99\xc3>&?8\xbfk\x87r>U\xd5y>\x19\x01G\xbfk\xf6\xb4\xbe\xe7\xb9\xdc=\xc4\xe4\xc2\xbelSF\xbf\xdb\x99(\xbfJ\xc7C?\xac\xa3\x1a\xbfB\x10A=\xea\xb2\x84\xbfj\xd5u?\xf7\xcd\xd5\xbe \xad.?\xb4\x08T>G53\xbf\x94\x89 \xbfS\'\x80\xbfi=\x8e=m\x9a\xda\xbeS\tY\xbfE\xd9>?\xa8\xf1W?\xff._?\xae\x83M>\xe6?~\xbf\xb5f1\xbf\x9e\xe1\x96>\\\xc0\xd0\xbe\x18;\x89\xbfR\x030\xbf\x96\xdb\x8a>\x92\x81Y\xbf\xf9\xd2\x15>\x19\n\x1b\xbf\xf6\xb5b>\xb1J\xec\xbe\xe0X0?\xc6\xae\xf7\xbe\x94\x81\x06?\xf8\x04X\xbe\x05\xaf\xe8>(\xb2\xc9\xbd\xea\x1a\xfe>\xdc\x17\xa2\xbe\xc9,\x08>\x169">\xe4\x9bU\xbf\xa9\xaa\x03=s5V\xbfS\xe0-\xbfbq\x01>-\xcf\xd6\xbe\xea\xbe\x90\xbe_]3\xbe]Z#?\xac\xe2o>\xe17+\xbfh\xb3\x8e\xbe\xadNu\xbe\xe6l_\xbf\xfe\xa0\xea=\xca\xc1M?iy\x92?n4\x08\xbf\xdaz\x0f?\xf4\x9e\x14\xbf\xd9\xc9R?\x85v&\xbf\xe4\x16\xea>\xd24E\xbf\xf6\xb2\xad>\xd3\xe5\x9e\xbe\xc7\xa1\x7f>[\x9d\x9b>\t\x81\x7f\xbf\xd9\xd0G\xbd\x80\xa6&\xbf\xe9\x9c\t>\xac\x0f\x0b\xbf\xb1?\xf9\xbe\xb2`\xdc>>\x97%\xbf\xa4\x17\x11?#\xc4\xd2\xbeQG+?\x8d\xf1\x88>\x0c\xbeT\xbf@\x838\xbfT\xe2\xa5>\xac\x8d\x0e\xbf]\xff\x1a>\xa6M=\xbf\xaby\xa3<\x87\xb7\\?<7\x9b?\xc3d\xd7=|\xa2\xc7\xbep-\x8f>z@C\xbf\xc3\x9c\x18\xbfuZ\xe0>K\x9d\xcb>\x13\xb1:\xbf\xde\x02\xfa<\x0b\x9f\x13?\xb2\xac\x07?\x9f\xear\xbf\xa4.H\xbff\xb4\x0e\xbe\x0c\t\x96>\xed7\x10\xbfF\xa32\xbf\x8cE;>\xf6/ \xbf\x87\xa9\xc7>\x01/\x94> \xd4Y\xbf\x84\x93\xe9>=Pp\xbf\x06R\xde\xbe3\x87\x81;\xeeC\x17\xbf\t^\x83\xbf8i\x80>\x95W\xba\xbe\xe9\x93\x1d\xbf\x8d\x92\x03?\x1d6\x9f\xbeA\x95\xef>\xe3\xce&\xbf\xec\xeb3?\xd7\xd3\x17\xbfPH\xc8>\x0f\x18\xa5>\x97\x0e/\xbf\xca8)?\x867t?\xa4M\xdf=Q(\x14\xbf`G\x94>\xf3\x9e\xaf\xbea\xb8\xbe>\xa9\xec^\xbfK\x8f\x05\xbf\xa8I\xb5>\x9d\xab^?\xdc\x92K?9\xeaf>\x84C\xdd\xbe\x0c\xdd\xb7\xbe\x8bZ\xce>\xa2_\x11\xbf\x82\x0c\x87\xbf\xc5\xd6\x82\xbeWh\n\xbf\x7f\x89t?\x13\x11g?\xfa$v?\x15\x90t?\xa3.j>"\xa0\x07\xbf\xfa\xb2U\xbe\xe1\x96.?\xa9\xd2\xaa=\xf3=\x99=a\x10\x85\xbf\x16\x05\xc6\xbc\xc3*c\xbf\x96\x1c\xf0=s\xc7x=\x956D\xbf\xe6H\xbb\xbeK\xa3\xc5>\x95\xb9\x04\xbf\xefB\x0f?T"\xd9\xbe\xae\xceW\xbd\\1C\xbf+\x90W?\x16\x96\x84\xbf\xe5\x87^>\x95\x15\xef\xbee\xeb@?V\xe7\xcb>\x98\xd6\x84\xbf\xa3\xe3 \xbfGB#?v\x8b\xeb\xbe\xad\xea>>\x91\xb0\x19\xbe\xc9\xd1(\xbf7c\x03?3O6?\'\x0f\xce\xbe\xa2"\xf6=\x05E\xa6\xbe\x85tW?\x0eT<\xbf\x91`K?E<\xbb\xbe^=]?\xcb\x95a>@\xeeC\xbfOIY\xbfx\x88\xc2>\xf3\xa2\xee=T\xd7#\xbf\xe573?\xe3\xc1\x8e?\xce\x99\x08\xbf\xe2q\t?\xf2\xc0\xf7\xbe\x04\xcf\x80>\x0ea\xcd\xbe\xcfl2?YP\x8f\xbe\xc1\xc5f>T\xcc\x0f\xbfLv5?\xbc/\x1a?\xfc\xe8\x82\xbf\x10D\xb0\xbet\xcfq>D\xd2\x08\xbfH*_?\xdc]D\xbf\xd7\xae3\xbf!\xa1\xc4\xbe\xae\x1a\x19?\x81\xc6\x90?\xf1\x1cs?\xafw\x9d\xbd\x17\xb7}\xbf\xa3\n\xba\xbe\xed\xeaM?*\xa2o>\x7fv\xf0\xbe\x11\xbcH\xbf\xc0Yn>i\x16\x7f\xbf5\xc5T=\x9c\xfb\x8d\xbd\x07j\x1e\xbfw\xba+>G\x92H\xbf\x0e\x04\xd2>\x8b\x82\x89\xbf\xb0+\xdc\xbe\xf3\xa0U?o\x1a\xe7\xbe\xc1\x91\xc6>\x02\xde\x8a>\x8b\xcb/\xbf\xa2Xd?\xff\x0f\x87?\xb4\xb1u\xbeP\x81\xce>\xa55D\xbe\x94\x17\xa0>\x9a\xc9\xad=\xf8\xd4\xc3\xbeU\x0fG\xbf\x0b\x87\x16?\x08\x8b\x8e>\xa5Z1\xbf\xc16\xc0>\xc7\x13\x04\xbf\x16\xd9\xf0>\x87\xc2\x8b\xbf\x0f\xb0\xb8\xbe\x9e\x92\x01=\xe6\xae\xd9\xbe\xa6\x8f\xf0>\xcf\x15\x82\xbeylV?\x98\x90\x00?\r\xb8\t\xbf\x93b\xd7\xbe\xaf{\xdf>9\xd67>\x90V|\xbfmHB\xbf\xb1`U?\xf0\x8a\xaf=G4\x1b\xbf\x1c\xde\xda\xbd\x95\xb85\xbf\x1f\xa3[>\xde\xbb~\xbff\xe2\'>\xacUB\xbf\xcd\t\x18?J<i?\xaa#\x86\xbf\\\xf3b\xbeM\xe2\x0b?$q8?B?g\xbf3\x82\x10\xbe\x1e\xcd\xa3\xbe\xc8\x06\x86\xbe\x803E>\x908\xca\xbe_\xc3\xd2>6\xefj\xbf\x05S@\xbfv\x85\x95>"\xe6E?\xfd,\x8e?QX\xe2>\x04\rO\xbf\xcc\x88E\xbf\xe0\xd7_\xbf\x07\xb0{>5\x07\x19\xbff\xaf:>F\x0e\x08\xbfs\xab\x9e>\xf1\x0bQ?@\xa1p\xbf55\xec>_+\xd2\xbe\xc2\xe9\xab>\xe6\x9a\x16\xbf\xe2\x93@\xbf\x99\x18\r\xbf\xd0\xd17?\xee\xfa@\xbf\xdf\xcd\xd3>\x12\\\t\xbf\xf6\xa94?9?\x9d>m\x94\xfb\xbezz9>\xa8_O\xbfg\xfa\xac>\x11@\x8b\xbf\xf3\x10\xfb\xbe\xd4 ,>,\xea\xd0\xbe\xe3\x1b\xf7>\x98\x98\xb5=L\xa5\x15\xbf6\x01\x18\xbf%\xcc\xcb>\xf2\xf0\x1a\xbfh\xd6`>=\xf7\xb7>I\xf0C\xbfw>\x00\xbf\x16R\x97=\x11$9\xbfTvX\xbf^^;?vy\x82?\xec\x04\x03\xbc\x13\xc5.\xbe\xfd\xed$\xbfN\xa5\xd3>+\xc1\xbb>\x8d\x05x\xbf\x01\xc5\x9d\xbe\xcf\xe7K\xbf\xde\x8d@>v\x16\x9f\xbftbh\x01h\x02K\x00\x85U\x01b\x87Rq\x06(K\x01K\xc8\x85h\x04U\x02i8K\x00K\x01\x87Rq\x07(K\x03U\x01<NNNJ\xff\xff\xff\xffJ\xff\xff\xff\xffK\x00tb\x89T@\x06\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00tb\x86.'
Xdata, ydata = pickle.loads(data)

# define model
aly = np.array([-107.366745, -471.69812012, 73.48317719, 505.58166504])
b = 1.11400843
svs = Xdata[[  9,  99, 176, 195],:]

plot_modeldecision(Xdata,ydata,svs,aly,b,poly_kernel)
matplotlib2tikz.save('example.tikz')

