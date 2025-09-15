TASK_TEMPLATE = '{instruction}\n\n{examples}\n\n{post_prompt}'
USER_TEMPLATE = '<contesto>\n{context}\n</contesto>\n\nDomanda: {question}'
DEFAULT_TEMPLATE = f'{TASK_TEMPLATE}\n\n{USER_TEMPLATE}'

CUSTOM_SYSTEM_PROMPTS = {
    # https://github.com/dvlab-research/LongLoRA/blob/2345c6d030f61ac3a031906386a103a5b05e0e6f/inference.py#L18
    'LONGLORA_LLAMA2':
        ''
}


def get_formatted_input(context, question, examples, instruction, post_prompt, template=DEFAULT_TEMPLATE):
    # instruction - task instruction
    # examples - in-context examples
    # post_prompt - any additional instructions after examples
    # context - text to use for qa
    # question - question to answer based on context
    formatted_input = template.format(instruction=instruction, examples=examples, post_prompt=post_prompt,
                                      context=context.strip(), question=question)
    return formatted_input.strip()



DEFAULT_PROMPTS = {
    'qa1': {
        'instruction':
            "Ti fornirò il contesto con i fatti sulle posizioni di diverse persone nascoste in un testo casuale "
            "e una domanda. Devi rispondere alla domanda basandoti solo sulle informazioni ricavate dai fatti. "
            "Se una persona si trovava in luoghi diversi, usa la posizione più recente per rispondere alla domanda. ",
        'examples':
			"Questi sono due esempi di contesti con i fatti, domande e di risposte.\n"
            "Esempio 1:\n"
            "Carlo è andato in corridoio. Anna è tornata in cucina. Carlo si è diretto in balcone.\n"
			"Domanda: Dov'è Carlo?\n"
            "Risposta: La posizione più recente di Carlo è il balcone.\n\n"
            "Esempio 2:\n"
            "Matteo si è trasferito in garage. Carlo è andato in spiaggia. Matteo è andato in negozio. "
            "Carlo si è diretto in balcone.\n"
            "Domanda: Dov'è Matteo?\n"
            "Risposta: La posizione più recente di Matteo è in negozio.\n",
        'post_prompt':
            "La tua risposta deve contenere una sola parola, la posizione più recente della persona. Non scrivere altro dopo.",
	},
    'qa2': {
        'instruction':
            "Ti fornisco il contesto con i fatti su luoghi e azioni di diverse persone "
            "nascosti in un testo casuale e una domanda. "
            "Devi rispondere alla domanda basandoti solo sulle informazioni ricavate dai fatti. "
            "Se una persona ha raccolto un oggetto nel primo luogo e si è spostata nel secondo luogo "
            "anche l'oggetto si trova nel secondo luogo. "
            "Se una persona ha lasciato un oggetto nel primo luogo e si è spostata nel secondo luogo "
            "l'oggetto rimane nel primo luogo.",
        'examples':
            "<esempio>\n"
            "Carlo è andato in cucina. Carlo ha preso una bottiglia. Carlo si è spostato sul balcone. "
            "Dov'è la bottiglia?\n"
            "Risposta: La bottiglia è sul balcone.\n"
            "</esempio>\n"
            "<esempio>\n"
            "Matteo si è spostato in garage. Matteo ha preso un cacciavite. Matteo si è spostato in cucina. "
            "Dov'è il cacciavite?\n"
            "Risposta: Il cacciavite è in cucina.\n"
            "</esempio>",
        'post_prompt':
            "Restituisci sempre la tua risposta nel seguente formato: L' ’oggetto’ si trova in ’luogo’. "
            "Non scrivere altro dopo."
    },
    'qa3': {
        'instruction':
            "Ti fornisco il contesto con i fatti su luoghi e azioni di diverse persone "
            "nascosti in un testo casuale e una domanda. "
            "Devi rispondere alla domanda basandoti solo sulle informazioni ricavate dai fatti. "
            "Se una persona ha trovato un oggetto nel primo luogo e si è spostata nel secondo luogo "
            "anche l'oggetto si trova nel secondo luogo. "
            "Se una persona ha lasciato un oggetto nel primo luogo e si è spostata nel secondo luogo "
            "l'oggetto rimane nel primo luogo.",
        'examples':
           "<esempio>\n"
           "Giovanni è andato in camera. Maria ha preso la mela. Maria è tornata in bagno. "
           "Daniele è andato in camera. Daniele si è spostato in giardino. Maria è andata in cucina. "
           "Dov'era la mela prima di essere in cucina?\n"
           "Risposta: Prima di essere in cucina, la mela era in bagno.\n"
           "</esempio>\n"
           "<esempio>\n"
           "Giovanni è tornato in camera. Giovanni è tornato in giardino. Giovanni è tornato in cucina. "
           "Sandra ha preso il pallone. Sandra è andata in giardino. Sandra è andata in camera. "
           "Dov'era il pallone prima di essere in camera?\n"
           "Risposta: Prima di essere in camera, il pallone era in giardino.\n"
           "</esempio>",
        'post_prompt':
           "La tua risposta deve contenere una sola parola, il luogo dove si trovava prima l'oggetto. Non scrivere altro dopo.",
    },
    'qa4': {
        'instruction':
            "Ti fornirò il contesto con i fatti su diverse persone, la loro posizione e le loro azioni, nascosti in un testo casuale e una domanda. "
            "Devi rispondere alla domanda basandoti solo sulle informazioni dei fatti.",
        'examples':
            "<esempio>\n"
            "Il corridoio è a sud della cucina. La camera è a nord della cucina. "
            "La cucina è a sud di che cosa?\n"
            "Risposta: camera\n"
            "</esempio>\n"
            "<esempio>\n"
            "Il giardino è a ovest della camera. La camera è a ovest della cucina. Cosa c'è a ovest della camera?\n"
            "Risposta: giardino\n"
            "</esempio>",
        'post_prompt':
            "La tua risposta deve contenere una sola parola, il luogo. Non scrivere altro dopo.",
    },
    'qa5': {
        'instruction':
            "Ti fornirò il contesto con i fatti sui luoghi e le loro relazioni nascosti in un testo casuale "
            "e una domanda. Devi rispondere alla domanda basandoti solo sulle informazioni ricavate dai fatti.",
        'examples':
            "<esempio>\n"
            "Maria ha raccolto la mela lì. Maria ha dato la mela a Enrico. Maria si è spostata in camera. "
            "Daniele ha portato il latte lì. A chi ha dato la mela Maria?\n"
            "Risposta: Enrico\n"
            "</esempio>\n"
            "<esempio>\n"
            "Giovanni ha portato il pallone lì. Giovanni ha passato il pallone a Enrico. Giovanni ha preso il latte lì. "
            "Daniele è andato in camera. Chi ha dato il pallone?\n"
            "Risposta: Giovanni\n"
            "</esempio>\n"
            "<esempio>\n"
            "Enrico ha raccolto la mela lì. Enrico ha dato la mela a Daniele. Daniele è andato in camera. "
            "Giovanni è tornato in giardino. Cosa ha dato Enrico a Daniele?\n"
            "Risposta: mela\n"
            "</esempio>",
        'post_prompt':
            "La tua risposta deve contenere una sola parola. Non scrivere altro."
            "Non spiegare la tua risposta."
    }
}

#OLD PROMPTS:
# QA1
#   "Restituisci sempre la tua risposta nel seguente formato: "
#   "La posizione più recente di ’persona’ è ’luogo’. Non scrivere altro dopo."    },
# QA2
#   "Restituisci sempre la tua risposta nel seguente formato: L' ’oggetto’ si trova in ’luogo’. "
#   "Non scrivere altro dopo."
# QA3
#   "Restituisci sempre la tua risposta nel seguente formato: "
#   "Prima di ’luogo_1’, l' ’oggetto’ si trovava in ’luogo_2’. Non scrivere altro dopo.",


# NEW BAD PROMPTS
# QA2
#   "La tua risposta deve contenere una sola parola, il ’luogo’ dove si trova l'oggetto. Non scrivere altro dopo.",
