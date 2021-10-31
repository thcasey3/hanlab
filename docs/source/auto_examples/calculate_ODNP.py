# %% [markdown]
"""
calculate ODNP
==============

This example demonstrates how to use the odnp module

"""
# %%

# %% [markdown]
# First import the odnp module of hanlab, dnplab, and numpy,
import dnplab
from hanlab import odnp
import numpy as np

# %%

# %% [markdown]
# To use the odnp module first create a dictionary with the necessary inputs. You may use odnp with DNPLab by creating a workspace and assinging the inputs dictionary to the key **'hydration_inputs'**. For example, start by defining the inputs dictionary,

Enhancements = [] # list of signal enhancements
Enhancement_powers = [] # list of powers in Watts corresponding to Enhancements
T1s = [] # list of T1 values in seconds
T1_powers = [] # list of powers in Watts corresponding to T1s

inputs = {
          'E_array' : np.array(Enhancements),
          'E_powers' : np.array(Enhancement_powers),
          'T1_array' : np.array(T1s),
          'T1_powers' : np.array(T1_powers),
          'T10': 2.0, # T1 measured with power=0
          'T100': 2.5, # T1 measured with SL=0 and power=0
          'spin_C': 100, # spin concentration in micromolar
          'field': 350, # magnetic field in mT
          'smax_model': 'tethered', # choice of smax model
          'interpolate_method': 'second_order' # choice of interpolation method
          }
# %%

# %% [markdown]
# Now you can either create a workspace and add the dictionary under the key **'hydration_inputs'**,
workspace = dnplab.create_workspace('hydration_inputs', inputs)
# %%

# %% [markdown]
# Or add to an existing workspace,
workspace.add('hydration_inputs', inputs)
# %%

# %% [markdown]
# In rare cases the bulk water or second order T1 interpolation constants may need to be altered. This is not necessary for the odnp module to operate, but if needed this can be done by adding the dictionary **'hydration_constants'** to the workspace. For example,
constants = {
             'ksigma_bulk': 95.4, # bulk ksigma value
             'krho_bulk': 353.4, # bulk krho value
             'klow_bulk': 366, # bulk klow value
             'tcorr_bulk': 54, # bulk tcorr value
             'D_H2O': 2.3e-9, # bulk water diffusivity
             'D_SL': 4.1e-10, # diffusivity of spin probe in bulk water
             'delta_T1_water': 1, # change in water proton T1 due to microwaves
             'T1_water': 2.5, # T1 of bulk water protons
             'macro_C': 100, # concentration of macromolecule in uM
             }

workspace.add('hydration_constants', constants)
# %%

# %% [markdown]
# Next, pass the workspace to odnp.hydration to perform calculations using,
hydration_results = odnp.hydration(workspace)
# %%

# %% [markdown]
# or operate in-place with:
odnp.hydration(workspace)
# %%


# %% [markdown]
# For use without creating a DNPLab workspace simply skip the above steps and pass the dictionaries to odnp directly,
hydration_results = odnp.hydration(inputs=inputs, constants=constants)
# %%
