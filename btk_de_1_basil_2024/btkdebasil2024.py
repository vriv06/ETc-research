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
    par.thetaWP = 0.060 #Vol. Soil Water Content, Wilting point (FAO-56, table 19, loamy sand substrat 5)
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
    irr.addevent(2024, 123, 1.264, 1.00)
    irr.addevent(2024, 124, 18.92, 1.00)
    irr.addevent(2024, 128, 6.767, 1.00)
    irr.addevent(2024, 130, 3.667, 1.00)
    irr.addevent(2024, 131, 3.896, 1.00)
    irr.addevent(2024, 132, 5.498, 1.00)
    irr.addevent(2024, 133, 6.668, 1.00)
    irr.addevent(2024, 134, 6.542, 1.00)
    irr.addevent(2024, 135, 4.73, 1.00)
    irr.addevent(2024, 136, 6.918, 1.00)
    irr.addevent(2024, 137, 2.854, 1.00)
    irr.addevent(2024, 138, 5.228, 1.00)
    irr.addevent(2024, 139, 1.312, 1.00)
    irr.addevent(2024, 140, 4.8, 1.00)
    irr.addevent(2024, 141, 4.578, 1.00)
    irr.addevent(2024, 142, 6.40, 1.00)
    irr.addevent(2024, 143, 1.457, 1.00)
    irr.addevent(2024, 144, 6.103, 1.00)
    irr.addevent(2024, 145, 3.965, 1.00)
    irr.savefile(os.path.join(module_dir,'btkdebasil2024.irr'))
    irr.loadfile(os.path.join(module_dir,'btkdebasil2024.irr'))
   

    #Run the model
    mdl = fao.Model('2024-102','2024-145', par, wth, irr=irr, aq_Ks=True,
                    comment = 'btk 2024 basil trial')
    mdl.run()
    print(mdl)
    mdl.savefile(os.path.join(module_dir,'btkdebasil2024.out'))
    mdl.savesums(os.path.join(module_dir,'btkdebasil2024.sum'))

if __name__ == '__main__':
    run()
