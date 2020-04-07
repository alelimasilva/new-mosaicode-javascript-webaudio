#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Bandpass class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Filter(BlockModel):

    # --------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "javascript"
        self.framework = "webaudio"
        self.label = "Filter"
        self.color = "50:150:50:150"
        self.group = "Sound"

        self.ports = [{"type": "mosaicode_lib_javascript_webaudio.extensions.ports.sound",
                       "name": "sound_input",
                       "conn_type": "Input",
                       "label": "Sound"},
                       {"type":"mosaicode_lib_javascript_webaudio.extensions.ports.sound",
                        "label":"Frequency",
                        "conn_type":"Input",
                        "name":"osc_freq"},
                      {"type": "mosaicode_lib_javascript_webaudio.extensions.ports.float",
                       "name": "freq",
                       "conn_type": "Input",
                       "label": "Frequency"},
                      {"type": "mosaicode_lib_javascript_webaudio.extensions.ports.float",
                       "name": "gain",
                       "conn_type": "Input",
                       "label": "Gain"},
                      {"type": "mosaicode_lib_javascript_webaudio.extensions.ports.float",
                       "name": "q",
                       "conn_type": "Input",
                       "label": "Q"},
                      {"type": "mosaicode_lib_javascript_webaudio.extensions.ports.sound",
                       "label": "Sound",
                       "conn_type": "Output",
                       "name": "output"}
                      ]
        self.properties = [
           {"name": "type",
            "label": "Type",
            "type": MOSAICODE_COMBO,
            "values": ["allpass",
                        "bandpass",
                        "highshelf",
                        "highpass",
                        "lowpass",
                        "lowshelf",
                        "notch",
                        "peaking",
                       ],
            "value": "highpass"
            },
            {"name": "freq",
             "label": "Frequency",
             "type": MOSAICODE_FLOAT,
             "lower": 0,
             "upper": 48000,
             "step": 1,
             "value": 200
             },
            {"name": "gain",
             "label": "Gain",
             "type": MOSAICODE_FLOAT,
             "lower": 0,
             "upper": 100,
             "step": 0.1,
             "value": 1
             },
            {"name": "Q",
             "label": "Q",
             "type": MOSAICODE_FLOAT,
             "lower": 0,
             "upper": 48000,
             "step": 1,
             "value": 200
             }
            ]
        self.codes["declaration"] = """

// block_$id$ = $label$
var block_$id$ = context.createBiquadFilter();
var $port[osc_freq]$ = block_$id$.frequency;
block_$id$.type = '$prop[type]$';
block_$id$.frequency.value = '$prop[freq]$';
block_$id$.gain.value = $prop[gain]$;
block_$id$.Q.value = $prop[Q]$;

var $port[freq]$ = function(value){
    block_$id$.frequency.value = parseFloat(value);
    return true;
    };

var $port[q]$ = function(value){
    block_$id$.Q.value = parseFloat(value);
    return true;
    };

var $port[gain]$ = function(value){
    block_$id$.gain.value = parseFloat(value);
    return true;
    };

var $port[sound_input]$ = block_$id$;
var $port[output]$ = block_$id$;
"""
