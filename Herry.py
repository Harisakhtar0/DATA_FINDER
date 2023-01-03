import os, platform

os.system('git pull')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from details64 import main

    main()

elif bit == '32bit':

    from details import main

    main()
