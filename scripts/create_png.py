# -*- coding: utf-8 -*-
#!/usr/bin/env python

from PIL import Image
img = Image.new('RGB', (400, 400), (127, 127, 127))
img.save('../test-images/gray.png')

img = Image.new('RGB', (400, 400), (255, 255, 0))
img.save('../test-images/yellow.png')