Name:		python-markdown2
Version:	2.5.5
Release:	1
Summary:	A fast and complete Python implementation of Markdown
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/markdown2/
Source0:	markdown2-2.5.5.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch

%prep -a
# Upstream installs tox.ini as data_files into /usr/testing.
sed -i '/data_files/d' setup.py

%description
A fast and complete Python implementation of Markdown.

%files
%{py_sitedir}/*
%{_bindir}/*
