## story 01
* greet
  - utter_greet

## story 02
* goodbye
  - utter_goodbye

## story 03
* give_banner
  - slot{"bannerid": "Q98237612"}

## story Ask About Name
* ask_name
  - utter_clarify_name
  > clarify name

## story Clarify Name System
> clarify name
* system_name
  - utter_ask_bannerid
* give_banner
    - slot {"bannerid": "b00123445"}
    - action_get_name
    - slot{"system_name": "David"}

## story Clarify Name Banner ID Exists
> clarify name
* system_name {"bannerid": "b00123445"}
  - action_get_name
  - slot{"system_name": "David"}

## story Clarify Name If system Name exisits
> clarify name
* system_name {"bannerid": "b00123445","system_name": "David"}
  - utter_system_name

## story Clarify Name If chat Name does not exist
> clarify name
* chat_name
  - action_chat_name
  - slot{"chat_name": "Jeff"}

## story Clarify Name If chat Name exisits
> clarify name
* chat_name{"chat_name": "Jeff"}
  - utter_chat_name

## story If someone randomly gives their banner id
* give_banner
    - slot {"bannerid": "b00123445"}

## Generated Story -2935573863199164787
* greet
    - utter_greet
* ask_name
    - utter_clarify_name
* system_name
    - utter_ask_bannerid
* give_banner{"bannerid": "b01239876"}
    - slot{"bannerid": "b01239876"}
    - action_get_name
    - slot{"system_name": "Jeff"}
* ask_name
    - utter_clarify_name
* system_name
    - utter_system_name

## Generated Story -2935573863699164234
* greet
    - utter_greet
* ask_name
    - utter_clarify_name
* system_name
    - utter_ask_bannerid
* give_banner{"bannerid": "b55578230"}
    - slot{"bannerid": "b55578230"}
    - action_get_name
    - slot{"system_name": "Jeff"}
* ask_name
    - utter_clarify_name
* system_name
    - utter_system_name

## Generated Story -4935573863699164234
* ask_name
    - utter_clarify_name
* system_name
    - utter_ask_bannerid
* give_banner{"bannerid": "b12398745"}
    - slot{"bannerid": "b12398745"}
    - action_get_name
    - slot{"system_name": "Jeff"}
* ask_name
    - utter_clarify_name
* system_name
    - utter_system_name

## Generated Story -2935573863199164787
* greet
    - utter_greet
* ask_name
    - utter_clarify_name
* system_name
    - utter_ask_bannerid
* give_banner{"bannerid": "b01239876"}
    - slot{"bannerid": "b01239876"}
    - action_get_name
    - slot{"system_name": "Jeff"}
* ask_name
    - utter_clarify_name
* system_name
    - utter_system_name

## Generated Story -2935573863199164787
* greet
    - utter_greet
* ask_name
    - utter_clarify_name
* chat_name
    - action_chat_name
    - slot{"chat_name": "Steve"}
* ask_name
    - utter_clarify_name
* chat_name
    - utter_chat_name

## Generated Story -3435573823467164709
* ask_name
    - utter_clarify_name
* chat_name
    - action_chat_name
    - slot{"chat_name": "Steve"}
* ask_name
    - utter_clarify_name
* chat_name
    - utter_chat_name

## Generated Story -3435573823467164709
* ask_name
    - utter_clarify_name
* chat_name
    - action_chat_name
    - slot{"chat_name": "Steve"}
* ask_name
    - utter_clarify_name
* system_name
    - utter_ask_bannerid
* give_banner{"bannerid": "b01239876"}
    - slot{"bannerid": "b01239876"}
    - action_get_name
    - slot{"system_name": "Jeff"}
* ask_name
    - utter_clarify_name
* system_name
    - utter_system_name

## Generated Story -3435573823467164709
* ask_name
    - utter_clarify_name
* chat_name
    - action_chat_name
    - slot{"chat_name": "Steve"}
* ask_name
    - utter_clarify_name
* system_name
    - utter_ask_bannerid
* give_banner{"bannerid": "b01239876"}
    - slot{"bannerid": "b01239876"}
    - action_get_name
    - slot{"system_name": "Jeff"}
* ask_name
    - utter_clarify_name
* chat_name
    - utter_chat_name

## Generated Story -4935573863699164234
* ask_name
    - utter_clarify_name
* system_name
    - utter_ask_bannerid
* give_banner{"bannerid": "b12398745"}
    - slot{"bannerid": "b12398745"}
    - action_get_name
    - slot{"system_name": "Jeff"}
* ask_name
    - utter_clarify_name
* chat_name
    - action_chat_name
    - slot{"chat_name": "Steve"}