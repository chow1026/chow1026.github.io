<!--
.. title: Matplotlib on OSX with VirtualEnv/VirtualEnvWrapper (and Pip)
.. slug: matplotlib-on-osx-virtualenv
.. date: 2016-11-14 14:17:26 UTC+08:00
.. tags: Matplotlib, OSX, VirtualEnv, VirtualEnvWrapper
.. category:
.. link:
.. description:
.. type: text
-->

I like keeping my mini projects separate, mostly under its own virtual environment set up.  I use [VirtualEnv](https://virtualenv.pypa.io/en/stable/) and [VirtualEnvWrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).  

As I am working on code for data analysis and data visualization, inevitably I need the matplotlib library.  Reading various resources online, I managed to get it to work.  And with this post, I hope to document the steps for future reference.  

My environments:      
- MacBookPro, OS macOS Sierra (10.12.1)     
- VirtualEnv v.15.0.3     
- python v.3.5.1    
- Pip v.9.0.1    

Steps:    
1. Activate the virtual environment: `workon {env}`    
2. Show pip packages: `pip3 list`    
3. Install necessary packages for data analysis and plotting: `pip install numpy scipy matplotlib pandas sympy nose`    
4. Install PyQt5: `pip install PyQt5`     
5. Modify matplotlibrc file: `nano {path to env}/lib/{pythonX.X}/site-packages/matplotlib/mpl-data/matplotlibrc`     
      - At the  top of the configurations, define backend: `backend    :   Qt5Agg`    
      - Then, define backend binding: `backend.qt5    :    PyQt5`    
      - Save file.   

You are all set now.
