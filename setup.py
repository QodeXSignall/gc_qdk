from setuptools import setup


setup(
    name='gc_qdk',
    version='0.0.2',
    packages=['gc_qdk'],
    install_requires=['qdk',
                      'psycopg2'],
    url='',
    license='MIT',
    author='Arthur',
    author_email='ksmdrmvstchny@gmail.com',
    description='GCQDK - SDK для работы с API GCore Compound.',
    docs_extras = [
        'Sphinx >= 3.0.0',  # Force RTD to use >= 3.0.0
        'docutils',
        'pylons-sphinx-themes >= 1.0.8',  # Ethical Ads
        'pylons_sphinx_latesturl',
        'repoze.sphinx.autointerface',
        'sphinxcontrib-autoprogram']
)
