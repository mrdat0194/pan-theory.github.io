[comment]: <> (https://mrdat0194.github.io/pan-theory/)
## Welcome to My GitHub Pages

Here is my official documents for my self [editor on GitHub](https://github.com/mrdat0194/pan-theory/edit/master/index.md).

[comment]: <> (Whenever you commit to this repository, GitHub Pages will run [Jekyll]&#40;https://jekyllrb.com/&#41; to rebuild the pages in your site, from the content in your Markdown files.)

### Time Sequence

1. Long Long time ago, I started a journey by creating [Rpub](https://rpubs.com/PeterDat).

2. After working hard 'for long long time', 

*Code is organize as conda venv source for connecting with other data team to share and develop code with me*.
- Step 1: Head to and download sh file for mac: https://docs.conda.io/en/latest/miniconda.html

```
sh Miniconda3-latest-Linux-x86_64.sh
```

- Step 2: Adding to .bash_profile and run 

```
conda update conda
```

- Step 4: setup environments

```
conda create -n pan-theory python=3
conda activate pan-theory

```

- Step 5: install requirements
```
pip install -r requirements.txt
```
[comment]: <> (https://jin-zhe.github.io/guides/installing-pytorch-with-cuda-in-conda/)

**Disclaimer:** The information here may vary depending on the version you're using. Please refer to the `README.md` bundled
within the project

## Library At-A-Glance
- `main_def` &mdash; The definition that controls all the connection-wide
    - aws: working with aws
    - ggl_api: How to connect to google and edit
        - Google_spreadsheet_api: Definition 
    - info: saving results
    - models: model of sqlachemy
    - sql: connection config
    - Elasticsearch
    - Neo4j:  
    - youtube: 
- `my_functions` &mdash; My developing functions
    - google_spreadsheet_api: code to work with spreadsheet
    - open_cv_function: code to work with openCv
    - text_similarity: code to work with fuzzy word
- `helper_functions` &mdash; The helper functions define
    - tools : on-going projects




