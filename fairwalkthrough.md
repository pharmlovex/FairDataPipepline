<h1 style="text-align: center;">FAIR DATA PIPELINE </h1>
<div style="text-align: justify;">
The FAIR Data Pipeline is intended to enable tracking of provenance of <a href="https://doi.org/10.1038/sdata.2016.18">FAIR</a> (findable, accessible, interoperable and reusable) data. This provides full tracking of a Project from data collection to the final results, including all the steps along the way. Each piece of data or analysis in the Project created in the Project will be tagged and bundled together. 
It follows the <a href="https://www.researchobject.org/">Research Object Crate</a> schema to package your research data with its metadata. This will aid in gathering your data and analysis when you are producing a paper and make your experimental data more accessible to other researchers using the system. 

The Fair Data Pipeline can be used locally on your laptop for your own Projects, or at a shared level where all the Institute/College's Projects can be stored and accessed.

The FAIR Data Pipeline is not restricted to data produced by yourself or colleges as it can bundle data from papers and tag them into your own projects.
How FAIR Data Pipeline works

The FAIR Data Pipeline system will track your Project by creating a registry which will hold the objects belonging to your project; data, code, plots, documentation, links to papers etc. The FAIR Data Pipeline provides command line tools for setting up and controlling your registry and API's to add to your code to talk to your registry. The registry can be viewed via a webpage, where you can see the providence and metadata of the objects in your Project. It also will allow you to download objects, for example the figures that will go into your paper.

</div>
<div>
The APIs allow you to link to the registry using the following languages:

- Python

- R

- C++

- Julia

- Java

Configuration files are created during set up. These configurations files allow you to define all the parameters, for example your Orchid ID, and run your workflow code.

The documentation for the command line tools, APIs and configuration files can be found in their own pages. For first time users, we suggest following the tutorials below to get an understanding of the pipeline.

Security

GitHub/GitLab is used to securely authorise users access to a registry.

Minimum Computational requirements

FAIRDataPipeline is a light weight OS agnostic resource.

Familiarity with the following will be beneficial:

- GitHub/GitLab

- Command line tools

- Conda/Python environments

</div>

## Install fair

```sh
pip install fair-cli
```

## Setup

### Step 1: Initialize fair cli

```sh
fair init
```

### NB: fair set up an interactive session to capture project metadata

```md
-----------------
{P : prompt}
{D : description}
{R : possible response}
-----------------

P=> Local Registry Port [8000]:
D=> Confirm your port. if you are happy with port 8000 else change it to suit you
R=> choose default; press enter

---

p=> Remote API URL [https://data.fairdatapipeline.org/api/]:
D=> Confirm your remote API URL. choose default or change it to suit you
R=> add your fair registry eg: https://test-data.fairdatapipeline.org/api/

---

p=> Remote Data Storage Root [https://test-data.fairdatapipeline.org/data/]:  
D=> This validates your remote fair registry for data storage.
R=> choose default; press enter

---

p=> Remote API Token:
D=> This authenticates your permission to the fair registry
R=> Enter token from your fair registry

---

p=> Default Data Store [/home/jovyan/.fair/data/]:
D=> Validates the local data store
R=> press Enter

---

p=> Email (optional) []:
D=> Add your email.
R=> Add your email

---

p=> User ID system (GITHUB/GITLAB/ORCID/ROR/GRID/None) [GITHUB]:
D=> Fair registry user identifier
R=> choose prefered platform for identification

---

p=> Default output namespace [it will add your name here]:
D=> Confirm your name
R=> Leave blank if your happy with the default

---

p=> Default input namespace [it will add your name here]:
D=> Confirm your name
R=> Leave blank if name is correct; press enter

---

P=> GitHub Username:
D=> add ur github user name
R=> Add your github username

---

p=> Local Git repository [/home/jovyan/work/FairDataPipepline]:  
D=> Validate local repo
R=> Choose default by leaving it blank

---

P=> Git remote name [origin]:
D=> Validates remote name
R=> Choose default by leaving it blank

---

P=> Remote API URL [https://test-data.fairdatapipeline.org/api/]:
D=> Validate API URL
R=> Choose default by leaving it blank

---

P=> Remote API Token File [/home/jovyan/.fair/cli/remotetoken.txt]:
D=> Validate API Token file
R=> Choose default by leaving it blank

---

P=> Default output namespace [it will add your name here]:  
D=> Validate output namespace
R=> Choose default by leaving it blank

---

P=> Default input namespace [it will add your name here]:
D=> Validate input namespace
R=> Choose default by leaving it blank
```

## Fair

### Step 2: Create a configuration file

```yaml
# config.yaml

run_metadata:
  default_input_namespace: ImageProcessing
  default_output_namespace: ImageProcessing
  description: Project description
  script: python main.py
  remote_repo: https://github.com/ImageProcessing/FairDataPipepline

register:
- namespace: ImageProcessing
  full_name: Scientist
  website: https://github.com/ImageProcessing

- external_object: image/data
  namespace_name: ImageProcessing
  root: https://github.com/ImageProcessing/raw/main/image
  path: single_frame_image.tif
  title: Single Frame Image
  description: Image Analysis
  identifier: https://doi.org/10.1038/wS92-020-0856-2
  file_type: tif
  release_date: 2021-09-20T12:00
  version: "1.0.0"
  primary: "false"

write:
- data_product: image/results/image_analysis
  description: Image Morphology results
  file_type: csv

- data_product: image/results/image_mask
  description: Image Mask
  file_type: tiff


```
