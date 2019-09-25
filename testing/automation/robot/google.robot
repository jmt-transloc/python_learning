*** Settings ***
Library     Selenium2Library

*** Variables ***

${URL}              https://www.google.com
${BROWSER}          chrome
${SEARCH_PHRASE}    Pandaren

*** Test Cases ***

Open Google
    Navigate To Google
    Verify Page Contains Google

Process A Google Search
    Navigate To Google
    Search For A Phrase
    Verify Links Appear
    Verify Search Input Contains Phrase

*** Keywords ***

Navigate To Google
    Open Browser    ${URL}  ${BROWSER}

Verify Page Contains Google
    ${Get_title}=       Get Title
    Should Be Equal As Strings      ${Get_title}    Google
    Close Browser

Search For A Phrase
    Press Keys      name:q      ${SEARCH_PHRASE}
    Press Keys      name:q      RETURN

Verify Links Appear
    ${count}=       Get Element Count   class:rc    
    Should Be True      ${count} > 0

Verify Search Input Contains Phrase
    Textfield Value Should Be      name:q      ${SEARCH_PHRASE}
    Close Browser
