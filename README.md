# facebook likes

[![Build Status](https://travis-ci.org/sloev/facebooklikes.svg?branch=master)](https://travis-ci.org/sloev/facebooklikes) [![Latest Version](https://img.shields.io/pypi/v/facebooklikes.svg)](https://pypi.python.org/pypi/facebooklikes) [![Python Support](https://img.shields.io/pypi/pyversions/facebooklikes.svg)](https://pypi.python.org/pypi/facebooklikes)

Python package to get facebook likes

### Features

* get facebook likes for pages
* get facebook likes for facebookurls

## Installation

Install the package from [PyPI](https://pypi.python.org/pypi/facebooklikes) using [pip](https://pip.pypa.io/):

```
pip install facebooklikes
```

## Getting Started

This client only uses stdlib and has no dependencies

### Usage

```
import facebooklikes

facebook_likes_for_beyonce_as_integer = facebooklikes.get_facebook_likes_for_page('beyonce')
facebook_likes_for_beyonce_as_integer = facebooklikes.get_facebook_likes_from_facebook_url('https://www.facebook.com/beyonce/')

```
