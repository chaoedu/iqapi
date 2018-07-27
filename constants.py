# !usr/bin/python
# -*- coding: utf-8 -*-

from collections import OrderedDict


class ConstantFunction(object):
    OK = 0
    ON = 1
    OFF = 0
    BLOCKING = 0
    ARM_TRIGGER = 1
    CHECK_DATA = 2


class ConstantIQType(object):
    IQXEL = 1


class ConstantDutType(object):
    DUT_K2T = "K2T"
    DUT_KA50 = "KA50"
    DUT_K2M = "K2M"


class ConstantPort(object):
    # PORT_OFF = 1 # Port has been disabled.
    PORT_LEFT = 2 # RF uses left port(RF1).
    PORT_RIGHT = 3 # RF uses right port(RF2).
    # PORT_1 = PORT_LEFT  # RF uses RF1A/RF1B.
    # PORT_2 = PORT_RIGHT  # RF uses RF2A/RF2B.


class ConstantBand(object):
    BAND_2G4 = '2G4'
    BAND_5G = '5G'


class ConstantMode(object):
    MODE_11B = "MODE_11B"
    MODE_11G = "MODE_11G"
    MODE_11N = "MODE_11N"
    MODE_11A = "MODE_11A"
    MODE_11AC = "MODE_11AC"


class ConstantBandWidth(object):
    HT20 = "HT20"
    HT40 = "HT40"
    HT40PLUS = "HT40PLUS"
    HT40MINUS = "HT40MINUS"
    VHT20 = "VHT20"
    VHT40 = "VHT40"
    VHT80 = "VHT80"


class ConstantAntenna(object):
    ANT1 = "ANT1"
    ANT2 = "ANT2"
    ANT3 = "ANT3"
    ANT4 = "ANT4"


class ConstantTriggerType(object):
    TRIG_TYPE_IMMediate = 0
    TRIG_TYPE_VIDeo = 6


class ConstantModulation(object):
    MOD_DEFAULT = "./user/WiFi_OFDM-54.iqvsg"
    MOD_11A_HT20_MCS0 = "./user/WiFi_OFDM-6.iqvsg"
    MOD_11A_HT20_MCS1 = "./user/WiFi_OFDM-9.iqvsg"
    MOD_11A_HT20_MCS2 = "./user/WiFi_OFDM-12.iqvsg"
    MOD_11A_HT20_MCS3 = "./user/WiFi_OFDM-18.iqvsg"
    MOD_11A_HT20_MCS4 = "./user/WiFi_OFDM-24.iqvsg"
    MOD_11A_HT20_MCS5 = "./user/WiFi_OFDM-36.iqvsg"
    MOD_11A_HT20_MCS6 = "./user/WiFi_OFDM-48.iqvsg"
    MOD_11A_HT20_MCS7 = "./user/WiFi_OFDM-54.iqvsg"
    MOD_11B_HT20_MCS0 = "./user/WiFi_DSSS-1L.iqvsg"
    MOD_11B_HT20_MCS1 = "./user/WiFi_DSSS-2L.iqvsg"
    MOD_11B_HT20_MCS2 = "./user/WiFi_CCK-5_5L.iqvsg"
    MOD_11B_HT20_MCS3 = "./user/WiFi_CCK-11L.iqvsg"
    MOD_11G_HT20_MCS0 = "./user/WiFi_OFDM-6.iqvsg"
    MOD_11G_HT20_MCS1 = "./user/WiFi_OFDM-9.iqvsg"
    MOD_11G_HT20_MCS2 = "./user/WiFi_OFDM-12.iqvsg"
    MOD_11G_HT20_MCS3 = "./user/WiFi_OFDM-18.iqvsg"
    MOD_11G_HT20_MCS4 = "./user/WiFi_OFDM-24.iqvsg"
    MOD_11G_HT20_MCS5 = "./user/WiFi_OFDM-36.iqvsg"
    MOD_11G_HT20_MCS6 = "./user/WiFi_OFDM-48.iqvsg"
    MOD_11G_HT20_MCS7 = "./user/WiFi_OFDM-54.iqvsg"
    MOD_11N_HT20_MCS0 = "./user/WiFi_HT20_MCS0.iqvsg"
    MOD_11N_HT20_MCS1 = "./user/WiFi_HT20_MCS1.iqvsg"
    MOD_11N_HT20_MCS2 = "./user/WiFi_HT20_MCS2.iqvsg"
    MOD_11N_HT20_MCS3 = "./user/WiFi_HT20_MCS3.iqvsg"
    MOD_11N_HT20_MCS4 = "./user/WiFi_HT20_MCS4.iqvsg"
    MOD_11N_HT20_MCS5 = "./user/WiFi_HT20_MCS5.iqvsg"
    MOD_11N_HT20_MCS6 = "./user/WiFi_HT20_MCS6.iqvsg"
    MOD_11N_HT20_MCS7 = "./user/WiFi_HT20_MCS7.iqvsg"
    MOD_11N_HT40_MCS0 = "./user/WiFi_HT40_MCS0.iqvsg"
    MOD_11N_HT40_MCS1 = "./user/WiFi_HT40_MCS1.iqvsg"
    MOD_11N_HT40_MCS2 = "./user/WiFi_HT40_MCS2.iqvsg"
    MOD_11N_HT40_MCS3 = "./user/WiFi_HT40_MCS3.iqvsg"
    MOD_11N_HT40_MCS4 = "./user/WiFi_HT40_MCS4.iqvsg"
    MOD_11N_HT40_MCS5 = "./user/WiFi_HT40_MCS5.iqvsg"
    MOD_11N_HT40_MCS6 = "./user/WiFi_HT40_MCS6.iqvsg"
    MOD_11N_HT40_MCS7 = "./user/WiFi_HT40_MCS7.iqvsg"
    MOD_11AC_VHT20_MCS0 = "./user/WiFi_11AC_VHT20_S1_MCS0.iqvsg"
    MOD_11AC_VHT20_MCS1 = "./user/WiFi_11AC_VHT20_S1_MCS1.iqvsg"
    MOD_11AC_VHT20_MCS2 = "./user/WiFi_11AC_VHT20_S1_MCS2.iqvsg"
    MOD_11AC_VHT20_MCS3 = "./user/WiFi_11AC_VHT20_S1_MCS3.iqvsg"
    MOD_11AC_VHT20_MCS4 = "./user/WiFi_11AC_VHT20_S1_MCS4.iqvsg"
    MOD_11AC_VHT20_MCS5 = "./user/WiFi_11AC_VHT20_S1_MCS5.iqvsg"
    MOD_11AC_VHT20_MCS6 = "./user/WiFi_11AC_VHT20_S1_MCS6.iqvsg"
    MOD_11AC_VHT20_MCS7 = "./user/WiFi_11AC_VHT20_S1_MCS7.iqvsg"
    MOD_11AC_VHT20_MCS8 = "./user/WiFi_11AC_VHT20_S1_MCS8.iqvsg"
    MOD_11AC_VHT40_MCS0 = "./user/WiFi_11AC_VHT40_S1_MCS0.iqvsg"
    MOD_11AC_VHT40_MCS1 = "./user/WiFi_11AC_VHT40_S1_MCS1.iqvsg"
    MOD_11AC_VHT40_MCS2 = "./user/WiFi_11AC_VHT40_S1_MCS2.iqvsg"
    MOD_11AC_VHT40_MCS3 = "./user/WiFi_11AC_VHT40_S1_MCS3.iqvsg"
    MOD_11AC_VHT40_MCS4 = "./user/WiFi_11AC_VHT40_S1_MCS4.iqvsg"
    MOD_11AC_VHT40_MCS5 = "./user/WiFi_11AC_VHT40_S1_MCS5.iqvsg"
    MOD_11AC_VHT40_MCS6 = "./user/WiFi_11AC_VHT40_S1_MCS6.iqvsg"
    MOD_11AC_VHT40_MCS7 = "./user/WiFi_11AC_VHT40_S1_MCS7.iqvsg"
    MOD_11AC_VHT40_MCS8 = "./user/WiFi_11AC_VHT40_S1_MCS8.iqvsg"
    MOD_11AC_VHT40_MCS9 = "./user/WiFi_11AC_VHT40_S1_MCS9.iqvsg"
    MOD_11AC_VHT80_MCS0 = "./user/WiFi_11AC_VHT80_S1_MCS0.iqvsg"
    MOD_11AC_VHT80_MCS1 = "./user/WiFi_11AC_VHT80_S1_MCS1.iqvsg"
    MOD_11AC_VHT80_MCS2 = "./user/WiFi_11AC_VHT80_S1_MCS2.iqvsg"
    MOD_11AC_VHT80_MCS3 = "./user/WiFi_11AC_VHT80_S1_MCS3.iqvsg"
    MOD_11AC_VHT80_MCS4 = "./user/WiFi_11AC_VHT80_S1_MCS4.iqvsg"
    MOD_11AC_VHT80_MCS5 = "./user/WiFi_11AC_VHT80_S1_MCS5.iqvsg"
    MOD_11AC_VHT80_MCS6 = "./user/WiFi_11AC_VHT80_S1_MCS6.iqvsg"
    MOD_11AC_VHT80_MCS7 = "./user/WiFi_11AC_VHT80_S1_MCS7.iqvsg"
    MOD_11AC_VHT80_MCS8 = "./user/WiFi_11AC_VHT80_S1_MCS8.iqvsg"
    MOD_11AC_VHT80_MCS9 = "./user/WiFi_11AC_VHT80_S1_MCS9.iqvsg"


class ConstantFreqency(object):
    FREQ_2G4 = [2412, 2417, 2422, 2427, 2432, 2437, 2442, 2447, 2452, 2457, 2462, 2467, 2472, 2477, 2482]
    FREQ_5G = [5180, 5190, 5200, 5210, 5220, 5230, 5240, 5745, 5755, 5765, 5775, 5785, 5795, 5805, 5825]


class ConstantTest(object):
    MCS = {
        "MODE_11B":
        {
            "HT20":
            {
                "MCS0": {"rate": [1], "min_sense": -86, "max_sense": -10},
                "MCS1": {"rate": [2], "min_sense": -83, "max_sense": -10},
                "MCS2": {"rate": [5.5], "min_sense": -79, "max_sense": -10},
                "MCS3": {"rate": [11], "min_sense": -76, "max_sense": -10}
            }
        },
        "MODE_11G":
        {
            "HT20":
            {
                "MCS0": {"rate": [6], "min_sense":-82, "max_sense": -20},
                "MCS1": {"rate": [9], "min_sense": -81, "max_sense": -20},
                "MCS2": {"rate": [12], "min_sense": -79, "max_sense": -20},
                "MCS3": {"rate": [18], "min_sense": -77, "max_sense": -20},
                "MCS4": {"rate": [24], "min_sense": -74, "max_sense": -20},
                "MCS5": {"rate": [36], "min_sense": -70, "max_sense": -20},
                "MCS6": {"rate": [48], "min_sense": -66, "max_sense": -20},
                "MCS7": {"rate": [54], "min_sense": -65, "max_sense": -20}
            }
        },
        "MODE_11N":
        {
            "HT20":
            {
                "MCS0": {"rate": [6.5, 7.2], "min_sense": -82, "max_sense": -20},
                "MCS1": {"rate": [13, 14.4], "min_sense": -79, "max_sense": -20},
                "MCS2": {"rate": [19.5, 21.7], "min_sense": -77, "max_sense": -20},
                "MCS3": {"rate": [26, 28.9], "min_sense": -74, "max_sense": -20},
                "MCS4": {"rate": [39, 43.3], "min_sense": -70, "max_sense": -20},
                "MCS5": {"rate": [52, 57.8], "min_sense": -66, "max_sense": -20},
                "MCS6": {"rate": [58.5, 65], "min_sense": -65, "max_sense": -20},
                "MCS7": {"rate": [65, 72.2], "min_sense": -64, "max_sense": -20}
            },
            "HT40":
            {
                "MCS0": {"rate": [13.5, 15], "min_sense": -79, "max_sense": -20},
                "MCS1": {"rate": [27, 30], "min_sense": -76, "max_sense": -20},
                "MCS2": {"rate": [40.5, 45], "min_sense": -74, "max_sense": -20},
                "MCS3": {"rate": [54, 60], "min_sense": -71, "max_sense": -20},
                "MCS4": {"rate": [81, 90], "min_sense": -67, "max_sense": -20},
                "MCS5": {"rate": [108, 120], "min_sense": -63, "max_sense": -20},
                "MCS6": {"rate": [121.5, 135], "min_sense": -62, "max_sense": -20},
                "MCS7": {"rate": [135, 150], "min_sense": -61, "max_sense": -20}
            },
            "HT40PLUS":
            {
                "MCS0": {"rate": [13.5, 15], "min_sense": -79, "max_sense": -20},
                "MCS1": {"rate": [27, 30], "min_sense": -76, "max_sense": -20},
                "MCS2": {"rate": [40.5, 45], "min_sense": -74, "max_sense": -20},
                "MCS3": {"rate": [54, 60], "min_sense": -71, "max_sense": -20},
                "MCS4": {"rate": [81, 90], "min_sense": -67, "max_sense": -20},
                "MCS5": {"rate": [108, 120], "min_sense": -63, "max_sense": -20},
                "MCS6": {"rate": [121.5, 135], "min_sense": -62, "max_sense": -20},
                "MCS7": {"rate": [135, 150], "min_sense": -61, "max_sense": -20}
            },
            "HT40MINUS":
            {
                "MCS0": {"rate": [13.5, 15], "min_sense": -79, "max_sense": -20},
                "MCS1": {"rate": [27, 30], "min_sense": -76, "max_sense": -20},
                "MCS2": {"rate": [40.5, 45], "min_sense": -74, "max_sense": -20},
                "MCS3": {"rate": [54, 60], "min_sense": -71, "max_sense": -20},
                "MCS4": {"rate": [81, 90], "min_sense": -67, "max_sense": -20},
                "MCS5": {"rate": [108, 120], "min_sense": -63, "max_sense": -20},
                "MCS6": {"rate": [121.5, 135], "min_sense": -62, "max_sense": -20},
                "MCS7": {"rate": [135, 150], "min_sense": -61, "max_sense": -20}
            }
        },
        "MODE_11A":
        {
            "HT20":
            {
                "MCS0": {"rate": [6], "min_sense": -82, "max_sense": -30},
                "MCS1": {"rate": [9], "min_sense": -81, "max_sense": -30},
                "MCS2": {"rate": [12], "min_sense": -79, "max_sense": -30},
                "MCS3": {"rate": [18], "min_sense": -77, "max_sense": -30},
                "MCS4": {"rate": [24], "min_sense": -74, "max_sense": -30},
                "MCS5": {"rate": [36], "min_sense": -70, "max_sense": -30},
                "MCS6": {"rate": [48], "min_sense": -66, "max_sense": -30},
                "MCS7": {"rate": [54], "min_sense": -65, "max_sense": -30}
            }
        },
        "MODE_11AC":
        {
            "VHT20":
            {
                "MCS0": {"rate": [6.5, 7.2], "min_sense": -82, "max_sense": -30},
                "MCS1": {"rate": [13, 14.4], "min_sense": -79, "max_sense": -30},
                "MCS2": {"rate": [19.5, 21.7], "min_sense": -77, "max_sense": -30},
                "MCS3": {"rate": [26, 28.9], "min_sense": -74, "max_sense": -30},
                "MCS4": {"rate": [39, 43.3], "min_sense": -70, "max_sense": -30},
                "MCS5": {"rate": [52, 57.8], "min_sense": -66, "max_sense": -30},
                "MCS6": {"rate": [58.5, 65], "min_sense": -65, "max_sense": -30},
                "MCS7": {"rate": [65, 72.2], "min_sense": -64, "max_sense": -30},
                "MCS8": {"rate": [78, 86.7], "min_sense": -59, "max_sense": -30}
            },
            "VHT40":
            {
                "MCS0": {"rate": [13.5, 15], "min_sense": -79, "max_sense": -30},
                "MCS1": {"rate": [27, 30], "min_sense": -76, "max_sense": -30},
                "MCS2": {"rate": [40.5, 45], "min_sense": -74, "max_sense": -30},
                "MCS3": {"rate": [54, 60], "min_sense": -71, "max_sense": -30},
                "MCS4": {"rate": [81, 90], "min_sense": -67, "max_sense": -30},
                "MCS5": {"rate": [108, 120], "min_sense": -63, "max_sense": -30},
                "MCS6": {"rate": [121.5, 135], "min_sense": -62, "max_sense": -30},
                "MCS7": {"rate": [135, 150], "min_sense": -61, "max_sense": -30},
                "MCS8": {"rate": [162, 180], "min_sense": -56, "max_sense": -30},
                "MCS9": {"rate": [180, 200], "min_sense": -54, "max_sense": -30}
            },
            "VHT80":
            {
                "MCS0": {"rate": [29.3, 32.5], "min_sense": -76, "max_sense": -30},
                "MCS1": {"rate": [58.5, 65], "min_sense": -73, "max_sense": -30},
                "MCS2": {"rate": [87.8, 97.5], "min_sense": -71, "max_sense": -30},
                "MCS3": {"rate": [117, 130], "min_sense": -68, "max_sense": -30},
                "MCS4": {"rate": [175.5, 195], "min_sense": -64, "max_sense": -30},
                "MCS5": {"rate": [234, 260], "min_sense": -60, "max_sense": -30},
                "MCS6": {"rate": [263.3, 292.5], "min_sense": -59, "max_sense": -30},
                "MCS7": {"rate": [292.5, 325], "min_sense": -58, "max_sense": -30},
                "MCS8": {"rate": [351, 390], "min_sense": -53, "max_sense": -30},
                "MCS9": {"rate": [390, 433.3], "min_sense": -51, "max_sense": -30}
            }
        }
    }
    


class Constant(ConstantFunction, ConstantIQType, ConstantDutType, ConstantPort, ConstantMode,
               ConstantBandWidth, ConstantAntenna, ConstantBand, ConstantTriggerType,
               ConstantModulation, ConstantFreqency, ConstantTest):
    pass
