import os
import re
import sh

import pytest
from binaryornot.check import is_binary

PATTERN = r"{{(\s?cookiecutter)[.](.*?)}}"
RE_OBJ = re.compile(PATTERN)


@pytest.fixture
def context():
    return {
      "full_name": "Your full name here",
      "email": "you@example.com",
      "github_username": "yourname",
      "project_name": "djangorestframework-package",
      "project_slug": "django-rest-framework-package",
      "project_slug": "rest_framework_package",
      "project_short_description": "Your project description goes in here",
      "year": "2015",
      "version": "0.1.0",
      "open_source_license": ["MIT", "BSD", "ISCL", "Apache Software License 2.0", "Not open source"]
    }


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, subdirs, files in os.walk(root_dir)
        for file_path in files
    ]


def check_paths(paths):
    """Method to check all paths have correct substitutions,
    used by other tests cases
    """
    # Assert that no match is found in any of the files
    for path in paths:
        if is_binary(path):
            continue

        for line in open(path, "r"):
            match = RE_OBJ.search(line)
            msg = "cookiecutter variable not replaced in {}"
            assert match is None, msg.format(path)

def test_default_configuration(cookies, context):
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == context["project_slug"]
    assert result.project.isdir()

    paths = build_files_list(str(result.project))
    assert paths
    check_paths(paths)

def test_readme(cookies):
    result = cookies.bake()

    readme_file = result.project.join('README.rst')
    readme_lines =[]
    with open(readme_file) as f:
        readme_lines.extend(f.readline() for x in range(2))

    assert readme_lines == [
        '=============================\n',
        'djangorestframework-package\n'
    ]

def test_flake8_compliance(cookies):
    """generated project should pass flake8"""
    result = cookies.bake()

    try:
        sh.flake8(str(result.project))
    except sh.ErrorReturnCode as e:
        pytest.fail(e)
