"""ST-Link Automation Example"""

import stlink


if __name__ == '__main__':
    print(stlink.find_probe_and_sn())
    print(stlink.find_com_and_sn())

