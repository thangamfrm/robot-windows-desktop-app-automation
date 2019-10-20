| *** Settings *** |        |
| Resource       |  ..${/}resources${/}common.robot |
| Library |  ${LIB_DIR}/EclipseIDELibrary.py |
| Test Setup | open eclipse ide |
| Test Teardown | close eclipse ide |


| *** Test Cases *** |
| VerifyEclipseIDEAboutWindow |
|   | click menu | Help |
|   | click menu | About Eclipse |
|   | click button | OK |

