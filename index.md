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
- `adHoc` &mdash; As an analyst, there is always adhoc.
    - For reproducible result, adHoc can use notebook to test and implement beforehand SQL flow.
    
    
- `main_def` &mdash; The definition that controls all the connection-wide
    - aws: working with aws
    - ggl_api: How to connect to google and edit
        - Google_spreadsheet_api: Definition 
    - info: saving results
    - models: model of sqlachemy
    - sql: connection config
    - Elasticsearch: connect and test with database
    - Neo4j:  connect and test with database
    - youtube: Some functions use with youtube content
    
- `my_functions` &mdash; My developing functions
    - google_spreadsheet_api: code to work with spreadsheet
    - open_cv_function: code to work with openCv
    - text_similarity: code to work with fuzzy word
    
- `helper_functions` &mdash; The helper functions define
    - tools : on-going projects

- `datastructure` &mdash; The helper functions define
    - tools : on-going projects

## License

The theme is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).


[comment]: <> (```markdown)

[comment]: <> (Syntax highlighted code block)

[comment]: <> (# Header 1)

[comment]: <> (## Header 2)

[comment]: <> (### Header 3)

[comment]: <> (- Bulleted)

[comment]: <> (- List)

[comment]: <> (1. Numbered)

[comment]: <> (2. List)

[comment]: <> (**Bold** and _Italic_ and `Code` text)

[comment]: <> ([Link]&#40;url&#41; and ![Image]&#40;src&#41;)

[comment]: <> (```)

[comment]: <> (For more details see [GitHub Flavored Markdown]&#40;https://guides.github.com/features/mastering-markdown/&#41;)

[comment]: <> (### Jekyll Themes)

[comment]: <> (Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings]&#40;https://github.com/mrdat0194/pan-theory/settings&#41;. The name of this theme is saved in the Jekyll `_config.yml` configuration file.)

[comment]: <> (### Support or Contact)

[comment]: <> (Having trouble with Pages? Check out our [documentation]&#40;https://help.github.com/categories/github-pages-basics/&#41; or [contact support]&#40;https://github.com/contact&#41; and we’ll help you sort it out.)




