# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import os
h=["appstream","apt-config-icons","dconf-gsettings-backend","gnome-software-common","gsettings-desktop-schemas","libappstream-glib8","libatk1.0-0","libc6","libcairo2","libfwupd2"
,"libgdk-pixbuf2.0-0"
,"libglib2.0-0"
,"libgnome-desktop-3-17",
"libgspell-1-1","libgtk-3-0","libgtk3-perl","libgudev-1.0-0","libjson-glib-1.0-0","libpackagekit-glib2-18","libpolkit-gobject-1-0","libsecret-1-0","libsoup2.4-1","packagekit","software-properties-gtk"]

for x in h:

    os.system(f"sudo apt-get install {x} >> a.txt")