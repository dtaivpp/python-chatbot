## story 01
* greet
  - utter_greet

## story 02
* goodbye
  - utter_goodbye

## story 03
* give_banner{"bannerid": "B00021212"}
  - slot{"bannerid": "Q98237612"}

## story Ask About Name
* ask_name
  - utter_clarify_name
  > clarify name

## story Clarify Name System
> clarify name
* system_name
  - utter_ask_bannerid
* give_banner{"bannerid": "b00123445"}
    - slot{"bannerid": "b00123445"}
    - action_get_name
    - slot{"system_name": "David"}

## story Clarify Name Banner ID Exists
> clarify name
* system_name
  - action_get_name
  - slot{"system_name": "David"}

## story Clarify Name If system Name exisits
> clarify name
* system_name
  - utter_system_name

## story Clarify Name If chat Name does not exist
> clarify name
* chat_name
  - action_chat_name
  - slot{"chat_name": "Jeff"}

## story Clarify Name If chat Name exisits
> clarify name
* chat_name
  - utter_chat_name

## Generated Story -9141996978150608537
* greet
    - utter_greet
* ask_name
    - utter_clarify_name
* identity
    - utter_ask_bannerid
* give_banner{"bannerid": "B4483908"}
    - slot{"bannerid": "B4483908"}
    - action_get_name
    - slot{"system_name": "David"}
* goodbye
    - export

## Generated Story 3463728431311073381
* greet
    - utter_greet
* ask_name
    - utter_clarify_name
* identity
    - utter_ask_bannerid
* give_banner{"bannerid": "B12340987"}
    - slot{"bannerid": "B12340987"}
    - action_get_name
    - slot{"system_name": "David"}

## Generated Story -731408576064569120
* greet
    - utter_greet
* ask_name
    - utter_clarify_name
* system_name
    - utter_ask_bannerid
* give_banner{"bannerid": "b01387654"}
    - slot{"bannerid": "b01387654"}
    - action_get_name
    - slot{"system_name": "David"}
* ask_name
    - utter_clarify_name
* system_name
    - utter_system_name
    - export

## Generated Story 5971866882167688474
* greet
    - utter_greet
* ask_name
    - utter_clarify_name
* chat_name
    - action_chat_name
    - slot{"chat_name": "Jeff"}
* ask_name
    - utter_clarify_name
* chat_name
    - utter_chat_name
    - export

## Generated Story -8196297735095787928
* greet
    - utter_greet
* ask_name
    - utter_clarify_name
* chat_name
    - action_chat_name
    - slot{"chat_name": "Jeff"}
* system-name
    - utter_ask_bannerid
* give_banner{"bannerid": "W12983456"}
    - slot{"bannerid": "W12983456"}
    - action_get_name
    - slot{"system_name": "David"}

## Generated Story -7483959658455300560
* greet
    - utter_greet
* ask_name
    - utter_clarify_name
* system_name
    - utter_ask_bannerid
* give_banner{"bannerid": "b76584920"}
    - slot{"bannerid": "b76584920"}
    - action_get_name
    - slot{"system_name": "David"}
* system-name
    - utter_system_name


## Generated Story -6524902323323538930
* ask_name
    - utter_clarify_name
* chat_name
    - action_chat_name
    - slot{"chat_name": "Jeff"}
* chat_name
    - utter_chat_name
    - export

