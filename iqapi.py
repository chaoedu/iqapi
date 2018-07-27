# !usr/bin/python
# -*- coding: utf-8 -*-

"""IQ API"""

import time
import logging

from ctypes import CDLL, c_int, c_double, c_char_p, byref, c_bool, c_ulong, create_string_buffer, pointer
from constants import Constant


class IQError(RuntimeError):
    """ IQ error class"""

    pass


class ErrorHandling(object):
    """error handling class"""

    def __init__(self):
        self.iqapi = None
        self.logger = logging.getLogger("IQAPI")

    def LP_GetErrorString(self, where, code):
        """Get the detailed error message for the specific error code"""
        msg = c_char_p(self.iqapi.LP_GetErrorString(code))
        err_msg = "%s failed: rc=%d (%s)" % (where, code, msg.value)
        self.logger.debug(err_msg)


class InstrumentControl(ErrorHandling):
    def __init__(self):
        self.iqapi = None
        self.logger = logging.getLogger("InstrumentControl")

    def LP_Init(self, IQtype=1, testerControlMethod=0):
        """Initialize the MATLAB environment for running IQmeasure

        """
        rc = self.iqapi.LP_Init(c_int(IQtype), c_int(testerControlMethod))
        if rc != Constant.OK:
            self.LP_GetErrorString("Init", rc)
            err_msg = "Failed to Initialize the MATLAB environment: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "MATLAB initialized OK"
            self.logger.debug(err_msg)

    def LP_Term(self):
        """Terminate the MATLAB environment
        
        """
        rc = self.iqapi.LP_Term()
        if rc != Constant.OK:
            self.LP_GetErrorString("Term", rc)
            err_msg = "Failed to terminate the MATLAB environment: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "MATLAB terminated OK"
            self.logger.debug(err_msg)

    def LP_InitTester(self, ipAddress, IQxelConnectionType=0):
        """Initialize a tester

        """
        rc = self.iqapi.LP_InitTester(ipAddress, IQxelConnectionType)
        if rc != Constant.OK:
            self.LP_GetErrorString("InitTester", rc)
            err_msg = "Failed to initialize a tester: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "The tester initialized OK"
            self.logger.debug(err_msg)

    def LP_InitTesterN(self, ipAddress):
        """initialize Testsers
        
        Arguments:
            ipAddress {str} -- ip address
        """
        rc = self.iqapi.LP_InitTesterN(c_char_p(ipAddress))
        if rc != Constant.OK:
            self.LP_GetErrorString("InitTesterN", rc)
            err_msg = "Failed to initialize a tester: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "The tester initialized OK"
            self.logger.debug(err_msg)

    def LP_SetTesterMode(self,
                         signalMode,
                         selectedModules=None,
                         numOfSelectedModules=1):
        """Configure testers based on different signal modes

        """
        
        rc = self.iqapi.LP_SetTesterMode(c_int(signalMode),
                                           byref(c_int(selectedModules)),
                                           c_int(numOfSelectedModules))
        if rc != Constant.OK:
            self.LP_GetErrorString("SetTesterMode", rc)
            err_msg = "Failed to configure testers: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "The testers configure OK"
            self.logger.debug(err_msg)

    def LP_GetVersion(self):
        """Get the version information

        """
        version = create_string_buffer(255)
        ver_size = 255
        rc = self.iqapi.LP_GetVersion(version, ver_size)
        if rc != Constant.OK:
            err_msg = "Get version failed: rc=%s" % rc
            raise IQError(err_msg)
        else:
            return version.value

    def LP_ConClose(self):
        """Close the connection tester(s)
        
        """
        rc = self.iqapi.LP_ConClose()
        if rc != Constant.OK:
            self.LP_GetErrorString("ConClose", rc)
            err_msg = "Failed to close the connection to tester(s): rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "The connection to tester(s) closed OK"
            self.logger.debug(err_msg)

    def LP_ConOpen(self):
        """Re-establish the connection to tester(s)
        
        """
        rc = self.iqapi.LP_ConOpen()
        if rc != Constant.OK:
            self.LP_GetErrorString("ConOpen", rc)
            err_msg = "Failed to re-establish the connection to tester(s): rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "The connection to tester(s) re-established OK"
            self.logger.debug(err_msg)


class Configuration(ErrorHandling):
    def __init__(self):
        self.iqapi = None
        self.logger = logging.getLogger("Configuration")

    def LP_Agc(self, allTesters=True):
        """Performs AGC(Automatic Gain Control) on VSA
        
        """
        rfAmplDb = c_double()
        rc = self.iqapi.LP_Agc(pointer(rfAmplDb), c_bool(allTesters))
        if rc != Constant.OK:
            self.LP_GetErrorString("Agc", rc)
            err_msg = "Failed to perform AGC on VSA: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "Perform AGC on VSA OK"
            self.logger.debug(err_msg)
            return rfAmplDb.value

    def LP_SetVsg(self,
                  rfFreqHz,
                  rfPowerLeveldBm,
                  port,
                  setGapPowerOff=True,
                  dFreqShiftHz=0.0):
        """Sets up VSG
        
        """
        rc = self.iqapi.LP_SetVsg(c_double(rfFreqHz),
                                    c_double(rfPowerLeveldBm),
                                    c_int(port),
                                    c_bool(setGapPowerOff),
                                    c_double(dFreqShiftHz))
        if rc != Constant.OK:
            self.LP_GetErrorString("SetVsg", rc)
            err_msg = "Failed to set up VSG: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "VSG sets up OK"
            self.logger.debug(err_msg)

    def LP_SetVsg_Compensation(self, dcErrl, dcErrQ, phaseErr, gainErr,
                               delayErr):
        """Set up VSG Compensation Table

        """
        rc = self.iqapi.LP_SetVsg_Compensation(
            c_double(dcErrl),
            c_double(dcErrQ),
            c_double(phaseErr), c_double(gainErr), c_double(delayErr))
        if rc != Constant.OK:
            self.LP_GetErrorString("SetVsg_Compensation", rc)
            err_msg = "Failed to set up VSG Compensation Table: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "VSG Compensation Table sets up OK"
            self.logger.debug(err_msg)

    def LP_SetVsg_GapPower(self, rfFreqHz, rfPowerLeveldBm, port, gapPowerOff):
        """Set up VSG including gapPowerOff parameter

        """
        rc = self.iqapi.LP_SetVsg_GapPower(
            c_double(rfFreqHz),
            c_double(rfPowerLeveldBm), c_int(port), c_int(gapPowerOff))
        if rc != Constant.OK:
            self.LP_GetErrorString("SetVsg_GapPower", rc)
            err_msg = "Failed to set up VSG including gapPowerOff parameter: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "VSG including gapPowerOff parameter sets up OK"
            self.logger.debug(err_msg)

    def LP_SetVsg_PowerLevel(self, port, rfPowerLeveldBm):
        """Set up VSG PowerLevel

        """
        rc = self.iqapi.LP_SetVsg_PowerLevel(
            c_int(port), c_double(rfPowerLeveldBm))
        if rc != Constant.OK:
            self.LP_GetErrorString("SetVsg_PowerLevel", rc)
            err_msg = "Failed to set up VSG PowerLevel: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "VSG PowerLevel sets up OK"
            self.logger.debug(err_msg)

    def LP_SetVsg_triggerType(self,
                              rfFreqHz,
                              rfPowerLeveldBm,
                              port,
                              triggerType):
        """Set up VSG including selecting the triggerType

        """
        rc = self.iqapi.LP_SetVsg_triggerType(
            c_double(rfFreqHz),
            c_double(rfPowerLeveldBm),
            c_int(port),
            c_int(triggerType))
        if rc != Constant.OK:
            self.LP_GetErrorString("SetVsg_triggerType", rc)
            err_msg = "Failed to set up VSG including selecting the triggerType: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "VSG including selecting the triggerType sets up OK"
            self.logger.debug(err_msg)

    def LP_SetVsgModulation(self, modFileName, loadInternalWaveform=1):
        """Loads the modulation file (waveform) to VSG and performs auto transmit of the loaded VSG mod file in free run mode.

        """
        rc = self.iqapi.LP_SetVsgModulation(
            c_char_p(modFileName), c_int(loadInternalWaveform))
        if rc != Constant.OK:
            self.LP_GetErrorString("SetVsgModulation", rc)
            err_msg = "Failed to set VSG modulation: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "VSG modulation sets up OK"
            self.logger.debug(err_msg)

    def LP_SetVsa(self,
                  rfFreqHz,
                  rfAmplDb,
                  port,
                  exAttenDb=0.0,
                  triggerLevelDb=-25,
                  triggerPreTime=10e-6,
                  dFreqShiftHz=0.0,
                  dTriggerGapTime=6e-6):
        """Set up VSA for data capturing

        """
        rc = self.iqapi.LP_SetVsa(c_double(rfFreqHz),
                                    c_double(rfAmplDb),
                                    c_int(port),
                                    c_double(exAttenDb),
                                    c_double(triggerLevelDb),
                                    c_double(triggerPreTime),
                                    c_double(dFreqShiftHz),
                                    c_double(dTriggerGapTime))
        if rc != Constant.OK:
            self.LP_GetErrorString("SetVsa", rc)
            err_msg = "Failed to set up VSA for data capturing: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "VSA for data capturing sets up OK"
            self.logger.debug(err_msg)

    def LP_SetVsaAmplitudeTolerance(self, amplitudeToleranceDb):
        """Set Vsa amplitude tolerance in dB
        
        """
        rc = self.iqapi.LP_SetVsaAmplitudeTolerance(
            c_double(amplitudeToleranceDb))
        if rc != Constant.OK:
            self.LP_GetErrorString("SetVsaAmplitudeTolerance", rc)
            err_msg = "Failed to set up VSA amplitude tolerance in dB: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "VSA amplitude tolerance in dB sets up OK"
            self.logger.debug(err_msg)

    def LP_SetVsaTriggerTimeout(self, triggerTimeoutSec):
        """Set timeout for VSA Trigger process

        """
        rc = self.iqapi.LP_SetVsaTriggerTimeout(c_double(triggerTimeoutSec))
        if rc != Constant.OK:
            self.LP_GetErrorString("SetVsaTriggerTimeout", rc)
            err_msg = "Failed to set timeout for VSA Trigger process: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "Timeout for VSA Trigger process sets OK"
            self.logger.debug(err_msg)

    def LP_SetVsa_Trigger(self,
                          triggerSource=6,
                          triggerType=0,
                          triggerLevelDb=-25,
                          triggerMode=0,
                          triggerGapSec=6e-6,
                          triggerPreTime=10e-6,
                          triggerTimeoutSec=1.5):
        """Set VSA Trigger settings

        """
        rc = self.iqapi.LP_SetVsa_Trigger(
            c_int(triggerSource),
            c_int(triggerType),
            c_double(triggerLevelDb),
            c_double(triggerMode),
            c_int(triggerMode),
            c_double(triggerGapSec),
            c_double(triggerPreTime), c_double(triggerTimeoutSec))
        if rc != Constant.OK:
            self.LP_GetErrorString("SetVsa_Trigger", rc)
            err_msg = "Failed to set VS Trigger settings: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "VSA Trigger settings sets OK"
            self.logger.debug(err_msg)

    def LP_SetFrameCnt(self, frameCnt):
        """Set up the number of frames for VSG to transmit

        """
        rc = self.iqapi.LP_SetFrameCnt(c_int(frameCnt))
        if rc != Constant.OK:
            self.LP_GetErrorString("SetFrameCnt", rc)
            err_msg = "Failed to set up the number of frames for VSG to transmit: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "the number of frames for VSG to transmit sets up OK"
            self.logger.debug(err_msg)

    def LP_SetAnalysisParameterInteger(self, measurement, parameter, value):
        """Set VSA integer parameter before doing analysis

        """
        rc = self.iqapi.LP_SetAnalysisParameterInteger(
            pointer(c_char_p(measurement)),
            pointer(c_char_p(parameter)), c_int(value))
        if rc != Constant.OK:
            self.LP_GetErrorString("SetFrameCnt", rc)
            err_msg = "Failed to set up the number of frames for VSG to transmit: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "the number of frames for VSG to transmit sets up OK"
            self.logger.debug(err_msg)

    def LP_SetAgcWindowTime(self, WindowTime=0.005):
        """Set the AGC window time(for IQxel only)

        """
        rc = self.iqapi.LP_SetAgcWindowTime(c_double(WindowTime))
        if rc != Constant.OK:
            self.LP_GetErrorString("SetAgcWindowTime", rc)
            err_msg = "Failed to set the AGC window time: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "The AGC window time sets OK"
            self.logger.debug(err_msg)

    def LP_SetCaptureData(self, packetLengthUs, preTriggerTimeUs):
        """Specify capture packet data for analysis

        """
        rc = self.iqapi.LP_SetCaptureData(
            c_double(packetLengthUs), c_double(preTriggerTimeUs))
        if rc != Constant.OK:
            self.LP_GetErrorString("SetCaptureData", rc)
            err_msg = "Failed to set the specify capture packet data for analysis: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "The specify capture packet data for analysis sets OK"
            self.logger.debug(err_msg)

    def LP_SetDefault(self):
        """Set the tester to default(initial)status
        
        """
        rc = self.iqapi.LP_SetDefault()
        if rc != Constant.OK:
            self.LP_GetErrorString("Setdefault", rc)
            err_msg = "Failed to set the tester to default(initial) status: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "Set the tester to default(initial) status OK"
            self.logger.debug(err_msg)

    def LP_TxDone(self):
        """Check if TX is done
        
        """
        rc = self.iqapi.LP_TxDone()
        if rc != Constant.OK:
            self.LP_GetErrorString("TxDone", rc)
            err_msg = "TX is not done: rc=%s" % rc
        else:
            err_msg = "TX is done"
            self.logger.debug(err_msg)
        return rc

    def LP_SaveVsaSignalFile(self, sigFileName):
        """Save the captured data to a file(.sig)

        """
        rc = self.iqapi.LP_SaveVsaSignalFile(c_char_p(sigFileName))
        if rc != Constant.OK:
            self.LP_GetErrorString("SaveVsaSignalFile", rc)
            err_msg = "Failed to save the captured data to a file(.sig): rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "Save the captured data to a file(.sig) OK"
            self.logger.debug(err_msg)

    def LP_LoadVsaSignalFile(self, sigFileName):
        """Load the signal file(.sig) for analysis

        """
        rc = self.iqapi.LP_LoadVsaSignalFile(pointer(c_char_p(sigFileName)))
        if rc != Constant.OK:
            self.LP_GetErrorString("LoadVsaSignalFile", rc)
            err_msg = "Failed to load the signal file(.sig) for analysis: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "Load the signal file(.sig) for analysis OK"
            self.logger.debug(err_msg)

    def LP_EnableVsgRF(self, enabled):
        """Turn ON/OFF the first VSG RF
        
        """
        rc = self.iqapi.LP_EnableVsgRF(c_int(enabled))
        if rc != Constant.OK:
            self.LP_GetErrorString("EnableVsgRF", rc)
            if enabled == 1:
                err_msg = "Failed to turn on the first VSG RF: rc=%s" % rc
            elif enabled == 0:
                err_msg = "Failed to turn off the first VSG RF: rc=%s" % rc
            else:
                err_msg = "Wrong command, please use 1 for on and 0 for off: rc=%s" % rc
            raise IQError(err_msg)
        else:
            if enabled == 1:
                err_msg = "Turn on the first VSG RF OK"
            elif enabled == 0:
                err_msg = "Turn off the first VSG RF OK"
            self.logger.debug(err_msg)

    def LP_EnableSpecifiedVsaRF(self, enabled, vsaNumber=0):
        """Turn ON/OFF the first VSG RF
        
        """
        rc = self.iqapi.LP_EnableSpecifiedVsaRF(c_int(enabled), c_int(vsaNumber))
        if rc != Constant.OK:
            self.LP_GetErrorString("EnableVsgRF", rc)
            if enabled == 1:
                err_msg = "Failed to turn on the first VSA RF: rc=%s" % rc
            elif enabled == 0:
                err_msg = "Failed to turn off the first VSA RF: rc=%s" % rc
            else:
                err_msg = "Wrong command, please use 1 for on and 0 for off: rc=%s" % rc
            raise IQError(err_msg)
        else:
            if enabled == 1:
                err_msg = "Turn on the first VSA RF OK"
            elif enabled == 0:
                err_msg = "Turn off the first VSA RF OK"
            self.logger.debug(err_msg)

    def LP_ScpiCommandSet(self, cmd):
        """Send SCPI command to IQxel tester
        
        Arguments:
            cmd {str} -- the string of SCPI command
        """
        rc = self.iqapi.LP_ScpiCommandSet(c_char_p(cmd))
        if rc != Constant.OK:
            self.LP_GetErrorString("LP_ScpiCommandSet", rc)
            err_msg = "SCPI command %s set failed: rc=%s" % (cmd, rc)
            raise IQError(err_msg)
        else:
            err_msg = "SCPI command %s set success" % cmd
            self.logger.debug(err_msg)

    def LP_ScpiCommandQuery(self, query):
        """Send a SCPI command to IQ tester.
        
        """
        max_size = c_ulong(255)
        response = create_string_buffer(255)
        actual_size = c_ulong()
        rc = self.iqapi.LP_ScpiCommandQuery(c_char_p(query),max_size,response,pointer(actual_size))
        if rc != Constant.OK:
            self.LP_GetErrorString("LP_ScpiCommandQuery", rc)
            err_msg = "Query %s failed: rc=%s" % (query, rc)
            raise IQError(err_msg)
        else:
            err_msg = "Query %s success, return value %s" % (query, response.value)
            self.logger.debug(err_msg)
            return response.value


class DataCapture(ErrorHandling):
    def __init__(self):
        self.iqapi = None
        self.logger = logging.getLogger("DataCapture")

    def LP_VsaDataCapture(self,
                          samplingTimeSecs,
                          triggerType=6,
                          sampleFreqHz=160e6,
                          ht40Mode=Constant.OFF,
                          nonBlockingState=Constant.BLOCKING):
        """Perform VSA data capture.
        
        """
        count = 5
        while(count):
            try:
                rc = self.iqapi.LP_VsaDataCapture(c_double(samplingTimeSecs), c_int(triggerType), c_double(sampleFreqHz), ht40Mode, nonBlockingState)
            except BaseException:
                pass
            if rc == Constant.OK:
                break
            count -= 1
            time.sleep(2)
        if rc != Constant.OK:
            self.LP_GetErrorString("VsaDataCapture", rc)
            err_msg = "Failed to perform VSA data capture: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "Perform VSA data capture OK"
            self.logger.debug(err_msg)


class Analysis(ErrorHandling):
    def __init__(self):
        self.iqapi = None
        self.logger = logging.getLogger("Analysis")

    def LP_Analyze80211b(self,
                         eq_taps=1,
                         DCremove11b_flag=0,
                         method_11b=1,
                         prePowStartSec=8.8e-6,
                         prePowStopSec=15.2e-6):
        """Perform 802.11b Analysis on current capture

        """
        rc = self.iqapi.LP_Analyze80211b(
            c_int(eq_taps),
            c_int(DCremove11b_flag),
            c_int(method_11b),
            c_double(prePowStartSec), c_double(prePowStopSec))
        if rc != Constant.OK:
            self.LP_GetErrorString("Analyze80211b", rc)
            err_msg = "Failed to perform 802.11b Analysis on current capture: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "perform 802.11b Analysis on current capture OK"
            self.logger.debug(err_msg)

    def LP_Analyze80211ag(self,
                          ph_corr_mode=2,
                          ch_estimate=1,
                          sym_tim_corr=2,
                          freq_sync=2,
                          ampl_track=1,
                          prePowStartSec=8.8e-6,
                          prePowStopSec=15.2e-6):
        """Perform 802.11 a/g Analysis on current capture

        """
        rc = self.iqapi.LP_Analyze80211ag(
            c_int(ph_corr_mode),
            c_int(ch_estimate),
            c_int(sym_tim_corr),
            c_int(freq_sync),
            c_int(ampl_track),
            c_double(prePowStartSec), c_double(prePowStopSec))
        if rc != Constant.OK:
            self.LP_GetErrorString("Analyze80211ag", rc)
            err_msg = "Failed to perform 802.11a/g Analysis on current capture: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "Perform 802.11a/g Analysis on current capture OK"
            self.logger.debug(err_msg)

    def LP_Analyze80211n(self,
                         type="EWC",
                         mode="nxn",
                         enablePhaseCorr=1,
                         enableSymTimingCorr=1,
                         enableAmplitudeTracking=0,
                         decodePSDU=1,
                         enableFullPacketChannelEst=0,
                         referenceFile="",
                         packetFormat=0,
                         frequencyCorr=2,
                         prePowStartSec=8.8e-6,
                         prePowStopSec=15.2e-6):
        """Perform 802.11n Analysis on current capture

        """
        rc = self.iqapi.LP_Analyze80211n(
            c_char_p(type),
            c_char_p(mode),
            c_int(enablePhaseCorr),
            c_int(enableSymTimingCorr),
            c_int(enableAmplitudeTracking),
            c_int(decodePSDU),
            c_int(enableFullPacketChannelEst),
            c_char_p(referenceFile),
            c_int(packetFormat),
            c_int(frequencyCorr),
            c_double(prePowStartSec), c_double(prePowStopSec))
        if rc != Constant.OK:
            self.LP_GetErrorString("Analyze80211n", rc)
            err_msg = "Failed to perform 802.11n Analysis on current capture: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "perform 802.11n Analysis on current capture OK"
            self.logger.debug(err_msg)

    def LP_Analyze80211ac(self,
                          mode="nxn",
                          enablePhaseCorr=1,
                          enableSymTimingCorr=1,
                          enableAmplitudeTracking=0,
                          decodePSDU=0,
                          enableFullPacketChannelEst=0,
                          frequencyCorr=2,
                          referenceFile="",
                          packetFormat=0,
                          numberOfPacketToAnalysis=1,
                          prePowStartSec=8.8e-6,
                          prePowStopSec=15.2e-6):
        """Perform 802.11ac Analysis on current capture

        """
        rc = self.iqapi.LP_Analyze80211ac(
            c_char_p(mode),
            c_int(enablePhaseCorr),
            c_int(enableSymTimingCorr),
            c_int(enableAmplitudeTracking),
            c_int(decodePSDU),
            c_int(enableFullPacketChannelEst),
            c_int(frequencyCorr),
            c_char_p(referenceFile),
            c_int(packetFormat),
            c_int(numberOfPacketToAnalysis),
            c_double(prePowStartSec),
            c_double(prePowStopSec))
        if rc != Constant.OK:
            self.LP_GetErrorString("Analyze80211ac", rc)
            err_msg = "Failed to perform 802.11ac Analysis on current capture: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "perform 802.11ac Analysis on current capture OK"
            self.logger.debug(err_msg)

    def LP_AnalyzePower(self, T_interval=0.0, max_pow_diff_dB=0.0):
        """Perform power Analysis on current capture.
        
        """
        rc = self.iqapi.LP_AnalyzePower(
            c_double(T_interval), c_double(max_pow_diff_dB))
        if rc != Constant.OK:
            self.LP_GetErrorString("AnalyzePower", rc)
            err_msg = "Failed to perform power Analysis on current capture: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "Perform power Analysis on current capture OK"
            self.logger.debug(err_msg)


class ResultRetrieving(ErrorHandling):
    def __init__(self):
        self.iqapi = None
        self.logger = logging.getLogger("ResultRetrieving")

    def LP_GetScalarMeasurement(self, measurement, index=0):
        """Get a scalar measurement result

        """
        rc = self.iqapi.LP_GetScalarMeasurement(c_char_p(measurement),c_int(index))
        if rc == c_double(-99999.99):
            err_msg = "No measurement available: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "Get a scalar measurement result OK"
            self.logger.debug(err_msg)
            return rc

    def LP_GetStringMeasurement(self, measurement):
        string_buffer = create_string_buffer(255)
        buf_size = 255
        rc = self.iqapi.LP_GetStringMeasurement(c_char_p(measurement),string_buffer,buf_size)
        if rc != Constant.OK:
            self.LP_GetErrorString("GetStringMeasurement", rc)
            err_msg = "Failed to get string measurement result: rc=%s" % rc
            raise IQError(err_msg)
        else:
            err_msg = "Get string measurement OK"
            self.logger.debug(err_msg)
        return string_buffer.value


class IQAPI(Constant, InstrumentControl, Configuration, DataCapture, Analysis, ResultRetrieving):
    """IQ API class
    
    """

    def __init__(self):
        self.logger = logging.getLogger("IQAPI")
        self.__import_iqapi_dll()


    def __import_iqapi_dll(self):
        """Import the dll file 
        
        """

        self.iqapi = CDLL("IQmeasure.dll")
