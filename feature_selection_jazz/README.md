# Feature Selection for Jazz Improvisation

This iPython notebook shows, how to perform different splits of the Weimar Jazz
Database according to style, epoch, artist etc.
The symbolic features extracted from the solo melody transcriptions in the WJD
are provided as data.

In order to have all required python packages available, we create a conda environment which you can use.
We recommend to install [miniconda](https://conda.io/miniconda.html) to be able to use it.

    conda env create -f environment.yml
    source activate jazzomat_experiments
    python main.py
