The bottom line. Follow your Nose, or our Nose. Write-run-love tests :fist:.

##Setup

###Fork, Clone, Setup Your Version of the Plotly Python API

First, you'll need to *get* our project. This is the appropriate *clone* command (if you're unfamiliar with this process, https://help.github.com/articles/fork-a-repo):

**DO THIS (in the directory where you want the repo to live)**

```bash
git clone https://github.com/plotly/python-api.git
```

###Submodules

Second, this project uses git submodules! There both helpful and, at times, difficult to work with. The good news is you probably don't need to think about them! Just run the following shell command to make sure that your local repo is wired properly:

**DO THIS (run this command in your new `plotly-api` directory)**

```bash
make setup_subs
```

That's going to initialize the submodules we use in this project, update them so that they're synced to the proper commit, and copy files to the appropriate locations in your local repo.

Here's what you need to know: changes to any files inside the following directories **will get overwritten**. These are synced with the submodules, if you need to change functionality there, you will need to make a pull request in the appropriate sub project repository.
- chunked_requests
- graph_reference
- mplexporter

Additionally, there are some project shortcuts that live in the `makefile` file. You can read all about this in the `make_instructions.txt` file. OR, just run:

```bash
make readme
```

###Making a Development Branch

Third, *don't* work in the `master` branch. As soon as you get your master branch ready, run:

**DO THIS (but change the branch name)**
```bash
git checkout -b my-dev-branch
```

... where you should give your branch a more descriptive name than `my-dev-branch`

###Pull Request When Ready

Once you've made your changes (and hopefully written some tests...), make that pull request!

##Suggestions

###Local Python
Setting up Python versions that *don't* require you to use `sudo` is a good idea. In addition, the core Python on your machine may not be the Python that we've developed in! Here are some nice guides for Mac, Windows, and Linux: 
- http://docs.python-guide.org/en/latest/starting/install/osx/
- http://docs.python-guide.org/en/latest/starting/install/win/
- http://docs.python-guide.org/en/latest/starting/install/linux/

###Virtualenv
Virtualenv is a way to create Python environments on your machine that know nothing about one another. This is really helpful for ironing out dependency-problems arising from different versions of packages. Here's a nice guide on how to do this: http://docs.python-guide.org/en/latest/dev/virtualenvs/

###Alter Your PYTHONPATH
The PYTHONPATH variable in your shell tells Python where to look for modules. Since you'll be developing, it'll be a pain to need to *install* Python every time you need to test some functionality (or at least ensure you're running code from the right directory...). You can easily make this change from a shell:

```bash
export PYTHONPATH="/path/to/local/repo:$PYTHONPATH"
```

Note, that's non-permanent. When you close the shell, that variable definition disappears. Also, `path/to/local/repo` is *your* specific repository path (e.g., `/Users/andrew/projects/python-api`).

###Why?

Now you can run the following code and be guaranteed to have a working development version that you can make changes to on-the-fly, test, and be confident will not break on other's machines!

```bash
pip install -r requirements.txt
pip install -r optional-requirements.txt
export PYTHONPATH="/path/to/local/repo:$PYTHONPATH"
```

##Dependencies

There's a short list of core dependencies you'll need installed in your Python environment to have any sort of fun with Plotly's Python API (see `requirements.txt`). Additionally, you're likely to have even more fun if you install some other requirements (see `optional-requirements.txt`). 

###Dependencies and Virtualenv

If you decided to follow the suggestion about about the Virtualenv *and* you've run `source bin/activate` within your new virtualenv directory to activate it--you can run the following to install the core dependencies:

```bash
pip install -r requirements.txt
```

To install the optional dependencies:

```bash
pip install -r optional-requirements.txt
```

##Testing

Our API uses Nose to run tests. (https://nose.readthedocs.org/en/latest/)

###Running Tests

Since our tests cover *all* the functionality, to prevent tons of errors from showing up and having to parse through a messy output, you'll need to install `optional-requirements.txt` as explained above.

After you've done that, go ahead and follow (y)our Nose!

```bash
nosetests -w plotly/tests
```

Or for more *verbose* output:

```bash
nosetests -w plotly/tests -v
```

Either of those will run *every* test we've written for the Python API. You can get more granular by running something like:

```bash
nosetests -w plotly/tests/test_plotly
```

... or even more granular by running something like:

```bash
nosetests plotly/tests/test_plotly/test_plot.py
```

###Writing Tests

You're *strongly* encouraged to write tests that check your added functionality. 

When you write a new test anywhere under the `tests` directory, if your PR gets accepted, that test will run in a virtual machine to ensure that future changes don't break your contributions!

<3 Team Plotly
