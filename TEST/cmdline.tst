from xdict import cmdline
from xdict.jprint import pobj
currd = {'AutoPauseSpeed': 0, 'HRLimitLow': 125, 'Activity': 6, 'UseHRLimits': False, 'SpeedLimitLow': None, 'UseHRBelt': False, 'Id': 13336645, 'Ordinal': 2, 'SpeedLimitHigh': None, 'GPSInterval': 0, 'UseAutolap': True, 'Interval1Time': None, 'Interval2Time': None, 'BacklightMode': None, 'TapFunctionality': None, 'AutolapDistanceFootPOD': None, 'UseIntervals': False, 'AutolapDistanceSpeedPOD': None, 'AutoscrollDelay': 10, 'AutolapDistanceBikePOD': None, 'Interval2Distance': None, 'UseFootPOD': False, 'AltiBaroMode': 1, 'UseCadencePOD': None, 'UseInDevice': True, 'Name': 'Pool swimming', 'HRLimitHigh': 165, 'UseSpeedLimits': None, 'RuleIDs': [11516125, 11516163, 11516164], '__type': 'Suunto.BLL.CustomMode', 'Displays': [{'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 37, 'RuleID': None}, 'Row2': {'Row': None, 'RuleID': 11516125}, 'Views': [{'Row': None, 'RuleID': 11516163}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 39, 'RuleID': None}, 'Row2': {'Row': 41, 'RuleID': None}, 'Views': [{'Row': 40, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 38, 'RuleID': None}, 'Row2': {'Row': 68, 'RuleID': None}, 'Views': [{'Row': 10, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 48, 'RuleID': None}, 'Row2': {'Row': 49, 'RuleID': None}, 'Views': [{'Row': 50, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 51, 'RuleID': None}, 'Row2': {'Row': 52, 'RuleID': None}, 'Views': [{'Row': 53, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 54, 'RuleID': None}, 'Row2': {'Row': 56, 'RuleID': None}, 'Views': [{'Row': 57, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 58, 'RuleID': None}, 'Row2': {'Row': 59, 'RuleID': None}, 'Views': [{'Row': 12, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': None, 'RuleID': 11516164}, 'Row2': {'Row': 4, 'RuleID': None}, 'Views': [{'Row': 20, 'RuleID': None}]}], 'AutomaticLogRecording': None, 'AutoPause': None, 'LoggedRuleIDs': [11516163, 11516164, 11516125], 'RecordingInterval': 1, 'Display': None, 'IntervalRepetitions': 0, 'UsePowerPOD': False, 'Interval1Distance': None, 'UseAccelerometer': False, 'UseBikePOD': False, 'UseAutoscroll': False, 'AutolapDistance': 100, 'ShowNavigationSelection': 0, 'Tones': None}
cmdt = cmdline.cmdict(dict=currd,debug=1)
cmdt



# use cmd seperated by space as keys sequence:
cmdt['Displays 6 Views 0 Row']
cmdt['Displays 6 Views 0']
cmdt['Displays 6 Views']
cmdt['Displays 6']
cmdt['Displays'] 


cmdt[['Displays',6,'Views',0,'Row']]
cmdt[['Displays',6,'Views',0]]
cmdt[['Displays',6,'Views']]
cmdt[['Displays',6]]
cmdt[['Displays']]




cmdt['isplays 1']
cmdt['RuleID']
cmdt['LoggedRuleIDs']
cmdt['LoggedRuleIDs 0']
cmdt['LoggedRuleIDs 1']
cmdt['LoggedRuleIDs 2']


cmdt[['Displays',6,'Views','0','Row']]
cmdt[['Displays', 6, 'Views', 0, 'Row']]
cmdt.dict['Displays'][6]['Views'][0]['Row']






###########################



import xdict.cmdline as xcmd

html_text = '''
    <html>
          <head>
                <meta>
                </meta>
          </head>
          <body>
                  <header>
                     <a>
                     </a>
                      <ul>
                          <li>
                               <div>
                                    <div>
                                       <i>
                                       </i>
                                       <i>
                                       </i>
                                    </div>
                               </div>
                               <div>
                                    <div>
                                         <div>
                                         </div>
                                    </div>
                                    <div>
                                    </div>
                               </div>
                          </li>
                      </ul>
                  </header>
                  <script>
                  </script>
          </body>
    </html>
'''


tmp = xcmd.show_html_text_via_cmd('html body',html_text=html_text)

tmp = xcmd.show_html_text_via_cmd('html body header',html_text=html_text)



cmdlines_ltdict  = {
    0: 'client',
    1: 'client defaultActivityID',
    2: 'client formattingOptions',
    3: 'client formattingOptions decimalSeparator',
    4: 'client formattingOptions language',
    5: 'client formattingOptions startOfWeek',
    6: 'client formattingOptions unitSystem',
    7: 'client gender',
    8: 'client geoIPLocation',
    9: 'client geoIPLocation lat'
}




cmd_str = "client formatting"
xcmd.show_prompt_from_cmdlines_ltdict(cmd_str,cmdlines_ltdict)


cmd_str = "formattingOptions"
xcmd.show_prompt_from_cmdlines_ltdict(cmd_str,cmdlines_ltdict)










from xdict.jprint import pobj
from xdict.jprint import pdir
import xdict.cmdline as xcmd

html_text = '''
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookbook &mdash; ocrmypdf 5.6.0.post23+g84d120e documentation</title>
    <link rel="stylesheet" href="https://media.readthedocs.org/css/sphinx_rtd_theme.css" type="text/css" />
    <link rel="index" title="Index" href="genindex.html"/>
    <link rel="search" title="Search" href="search.html"/>
    <link rel="top" title="ocrmypdf 5.6.0.post23+g84d120e documentation" href="index.html"/>
    <link rel="next" title="Advanced features" href="advanced.html"/>
    <link rel="prev" title="Installing additional language packs" href="languages.html"/> 
    <script src="_static/js/modernizr.min.js"></script>
    <link rel="canonical" href="http://ocrmypdf.readthedocs.io/en/latest/cookbook.html" />
    <link rel="stylesheet" href="https://media.readthedocs.org/css/readthedocs-doc-embed.css" type="text/css" />
    <script type="text/javascript" src="_static/readthedocs-data.js"></script>
    <script type="text/javascript">
    </script>
    <script type="text/javascript" src="_static/readthedocs-dynamic-include.js">
    </script>
</head>
'''

html_entry = xcmd.show_html_text_via_cmd('ead met',html_text=html_text,style='nested')
 
html_entry = xcmd.show_html_text_via_cmd('ead met',html_text=html_text)
 
html_entry = xcmd.show_html_text_via_cmd('title',html_text=html_text,style='nested')
 
html_entry = xcmd.show_html_text_via_cmd('title',html_text=html_text)








