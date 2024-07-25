"""
########################################################################
The btkdebasil2024.py module contains a function to setup and run pyfao56
for the treatment in a 2024 basil greenhouse study at
Hohenheim, Germany.  The savefile and loadfile routines for Parameters,
Weather, and Irrigation classes are also tested.

The btkdebasil2024.py module contains the following:
    run - function to setup and run pyfao56 for the
    treatment in a 2024 basil greenhouse study at Hohenheim, Germany

03/11/2024 Scripts developed for running pyfao56 for 2024 basil data
########################################################################
"""

import pyfao56 as fao
import os

def run():
    """Setup and run pyfao56 for a 2024 basil greenhouse study"""

    #Get the module directory
    module_dir = os.path.dirname(os.path.abspath(__file__))

    #Specify the model parameters
    par = fao.Parameters(comment = '2024 Basil')
    par.Kcbini = 0.40 #mint parameters 
    par.Kcbmid = 1.10 #mint parameters 
    par.Kcbend = 1.05 #mint parameters 
    par.Lini = 15 #based on literature for basil plant development
    par.Ldev = 30 #based on literature for basil plant development
    par.Lmid = 20 #based on literature for basil plant development
    par.Lend = 20 #based on literature for basil plant development
    par.hini = 0.036 #Initial Height in m (3.6cm overall as of may 3 2024, experiment start)
    par.hmax = 0.8 #maximum Height in m 
    par.thetaFC = 0.14 #Vol. Soil Water Content, Field Capacity (FAO-56, table 19, loamy sand substrat 5)
    par.thetaWP = 0.150 #Vol. Soil Water Content, Wilting point (FAO-56, table 19, loamy sand substrat 5)
    par.theta0 = 0.000 #Initial volume soil water content
    par.Zrini = 0.035 #Initial root depth, as of may 3 2024 (experiment start)
    par.Zrmax = 0.0840 # maximum root depth (m), 8.4 cm because of the pot height
    par.pbase = 0.40
    par.Ze = 0.1143
    par.REW = 8.0
    par.savefile(os.path.join(module_dir,'btkdebasil2024.par'))
    par.loadfile(os.path.join(module_dir,'btkdebasil2024.par'))

    #Specify the weather data
    wth = fao.Weather(comment = '2024 basil')
    wth.loadfile(os.path.join(module_dir,'transformed_weather_data.wth'))
    wth.savefile(os.path.join(module_dir,'transformed_weather_data.wth'))
    wth.loadfile(os.path.join(module_dir,'transformed_weather_data.wth'))

    #Specify the irrigation schedule
    """
    Atributes
    -------
        index - Year and day of year as string ('yyyy-ddd')
        columns - ['Depth','fw']
            Depth - Irrigation depth (mm)
            fw - fraction of soil surface wetted (FAO-56 Table 20)
            
    Methods
    -------
    savefile(filepath='pyfao56.irr')
        Save irrigation data to a file
    loadfile(filepath='pyfao56.irr')
        Load irrigation data from a file
    addevent(year,doy,depth,fw)
        Add an irrigation event to self.idata
    customload()
        Users can override for custom loading of irrigation data.
    """
    irr = fao.Irrigation(comment = '2024 basil')
    irr.addevent(2024, 189, 2.800, 0.30)
    irr.addevent(2024, 190, 3.284, 0.30)
    irr.addevent(2024, 191, 4.975, 0.30)
    irr.addevent(2024, 192, 5.317, 0.30)
    irr.addevent(2024, 193, 4.200, 0.30)
    irr.addevent(2024, 194, 3.855, 0.30)
    irr.addevent(2024, 195, 3.385, 0.30)
    irr.addevent(2024, 196, 3.640, 0.30)
    irr.addevent(2024, 197, 4.810, 0.30)
    irr.addevent(2024, 198, 5.529, 0.30)
    irr.addevent(2024, 199, 5.361, 0.30)
    irr.addevent(2024, 200, 53.00, 0.30)
    irr.addevent(2024, 201, 7.52, 0.30)
    irr.addevent(2024, 202, 5.50, 0.30)
    irr.addevent(2024, 203, 6.07, 0.30)
    irr.addevent(2024, 204, 4.14, 0.30)
    irr.addevent(2024, 205, 4.56, 0.30)
    irr.addevent(2024, 206, 4.52, 0.30)
    irr.savefile(os.path.join(module_dir,'btkdebasil2024.irr'))
    irr.loadfile(os.path.join(module_dir,'btkdebasil2024.irr'))
   

    #Run the model
    mdl = fao.Model('2024-158','2024-206', par, wth, irr=irr, aq_Ks=True,
                    comment = 'btk DE 2024 basil trial 2')
    mdl.run()
    print(mdl)
    mdl.savefile(os.path.join(module_dir,'btkdebasil2024.out'))
    mdl.savesums(os.path.join(module_dir,'btkdebasil2024.sum'))

if __name__ == '__main__':
    run()
