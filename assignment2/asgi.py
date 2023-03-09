#  Copyright (c) 2023 - All rights reserved.
#  Created by Karthik Thovinakere for PROCTECH 4IT3/SEP 6IT3.
#  SoA Notice: I Karthik Thovinakere, 400140562 certify that this material is my original work.
#  I certify that no other person's work has been used without due acknowledgement.
#  I have also not made my work available to anyone else without their due acknowledgement.

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assignment2.settings')

application = get_asgi_application()
