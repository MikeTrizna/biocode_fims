============
Biocode FIMS
============


.. image:: https://img.shields.io/pypi/v/biocode_fims.svg
        :target: https://pypi.python.org/pypi/biocode_fims

.. image:: https://img.shields.io/travis/MikeTrizna/biocode_fims.svg
        :target: https://travis-ci.org/MikeTrizna/biocode_fims

.. image:: https://readthedocs.org/projects/biocode-fims/badge/?version=latest
        :target: https://biocode-fims.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/MikeTrizna/biocode_fims/shield.svg
     :target: https://pyup.io/repos/github/MikeTrizna/biocode_fims/
     :alt: Updates


A Python client for accessing data from the `Biocode FIMS <http://www.biscicol.org/>`_ database.


* Free software: MIT license
* Documentation: https://biocode-fims.readthedocs.io.


Installation
------------

.. code-block:: python

	pip install biocode_fims

Basic Usage
-----------

Returning a list of all *public* Projects in the Biocode FIMS.

.. code-block:: python

	>>> import biocode_fims
	>>> all_projects = biocode_fims.list_projects()
	>>> print(all_projects)
	{
	  "Barcode of Wildlife Nigeria": 10,
	  "Amphibian Disease": 26,
	  "SI Barcoding CBOL": 12,
	  "Hawaii Dimensions": 3,
	  "University and Jepson Herbaria": 22,
	  "Barcode of Wildlife Nepal": 23,
	  "Barcode of Wildlife Kenya": 8,
	  "New York Botanical Garden": 28,
	  "Barcode of Wildlife Proficiency Testing": 24,
	  "Barcode of Wildlife Mexico": 9,
	  "Barcode of Wildlife South Africa": 11,
	  "Barcode of Wildlife Training": 5
	}

Return the first 4 datasets in the "SI Barcoding CBOL" project (project id: 12).

.. code-block:: python

	>>> import biocode_fims
	>>> all_sibn_datasets = biocode_fims.list_datasets(12)
	>>> print(all_sibn_datasets[:4])
	['Brazil_Ants_A', 'Brazil_Ants_B', 'Brazil_Ants_C', 'Brazil_Ants_D']

Grab the contents of the dataset "DJBirds_P01".

.. code-block:: python

	>>> import biocode_fims
	>>> contents = biocode_fims.dataset_contents(12,['DJBirds_P01'])
	>>> print(len(contents))
	83

To do something useful with the dataset contents, it's best of load them into a Pandas DataFrame.

TODO
----

* Get testing implemented correctly
* Expand to API endpoints behind OAuth

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

