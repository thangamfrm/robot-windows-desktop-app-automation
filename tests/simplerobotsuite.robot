*** Settings ***
Documentation    Suite description
| Resource       |  ..${/}resources${/}common.robot |
| Library |  ${LIB_DIR}/SimpleTestLibrary.py |

| Test Setup | setup simple test library |
| Test Teardown | teardown simple test library |

*** Test Cases ***
| VerifySimpleTestLibrary |
|  | say hello world |
| VerifyTestFailing |
|  | say fail |
