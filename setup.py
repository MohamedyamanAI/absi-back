from setuptools import setup, find_packages

setup(
    name="youtoon_absi",
    version="1.1",
    packages=find_packages(where="src") + ['tools.ayat_time_stamps'],
    package_dir={"": "src"},
    include_package_data=True,
)