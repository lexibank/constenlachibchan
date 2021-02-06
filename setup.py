from setuptools import setup
import json


with open('metadata.json', encoding='utf-8') as fp:
    metadata = json.load(fp)


setup(
    name="lexibank_constenlachibchan",
    description=metadata["title"],
    license=metadata.get("license", ""),
    url=metadata.get("url", ""),
    py_modules=["lexibank_constenlachibchan"],
    include_package_data=True,
    zip_safe=False,
    entry_points={"lexibank.dataset": ["constenlachibchan=lexibank_constenlachibchan:Dataset"]},
    install_requires=["pylexibank>=2.1"],
    extras_require={"test": ["pytest-cldf"]},
)
