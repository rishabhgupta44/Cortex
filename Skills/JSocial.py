# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import os,requests,bs4
url = "https://www.google.com/search?q=hello"
RequestImage = requests.get(url)
RequestInit = RequestImage.text
INside = bs4.BeautifulSoup(RequestInit,'html.parser')
print(RequestImage.text)