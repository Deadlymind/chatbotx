intents = [
    {
        "tag": "greeting",
        "patterns": ["bonjour", "salut", "alo", "cc", "coucou", "y-a t'il quelqu'un?", "bonsoir", "hey", "selem", "j'ai des questions", "probleme", "oo"],
        "responses": ["salut cher operateur!, je suis Mikou! votre chatbot du service clientèle de Tunisie Telecom. Comment puis-je vous aider aujourd'hui? Si vous avez des questions sur votre compte, des préoccupations techniques ou des demandes spécifiques, n'hésitez pas à me les faire savoir."],
        "context_set": ""
    },
    {
        "tag": "au revoir",
        "patterns": ["bye", "ok merci", "ok", "", "au revoir"],
        "responses": ["Merci d'avoir utilisé le service clientèle de Tunisie Telecom, Mikou! Si vous avez d'autres questions à l'avenir, n'hésitez pas à revenir. Nous sommes là pour vous aider. Bonne journée!"],
        "context_set": ""
    },
    {"tag": "recharge de la ligne ",
          "patterns": ["comment je peux recharger ma ligne","comment se fait le recharge de la ligne, comment effectuer une recharge"],
         "responses": ["tapez *123*code secret de la carte #"],
         "context_set": ""
    },
    {"tag": "consultation solde et bonus| solde |bonus",
         "patterns": ["comment je peux consulter mon solde" , "comment je peux consulter mon bonus"] ,
         "responses": ["tapez *122#"] ,
         "context_set": ""
        },
        {"tag": "suivie de forfait internet mobile",
         "patterns": ["comment je peux suivie mon forfait internet mobile"," comment je peux consulter ma consommation d'internet"],
         "responses": ["tapper *122*2#"],
         "context_set": ""
        },
         {"tag": "suivi de la recharge internet",
         "patterns": ["comment je peux suivi mon recharge  internet mobile"],
         "responses": ["tapper *122*10#"],
         "context_set": ""
        },
        {"tag": "solde de credit",
         "patterns": ["Comment puis-je vérifier mon solde de crédit sur ma ligne mobile Tunisie Telecom ?"],
         "responses": ["Vous pouvez composer *#123# et appuyer sur la touche d'appel pour vérifier votre solde de crédit."],
         "context_set": ""
        },
        {"tag": " démarche pour consulter le solde de mon bonus internet",
         "patterns": ["Quelle est la démarche pour consulter le solde de mon bonus internet"],
         "responses": ["Envoyez un SMS au numéro 1020 avec le texte 'Solde Internet' pour vérifier le solde de votre bonus internet."],
         "context_set": ""
        },
        {"tag": " application mobile pour suivre mon solde et bonus",
         "patterns": ["Y a-t-il une application mobile pour suivre mon solde et bonus"],
         "responses": [" Oui, vous pouvez télécharger l'application officielle de Tunisie Telecom 'My TT ' est disponible sur playstore et vous povez la telecharger dés l' instant  et suivre votre solde ainsi que vos bonus via l'interface conviviale."],
         "context_set": ""
        },
        {"tag": "service SMS pour recevoir des notifications de solde",
         "patterns": ["Existe-t-il un service SMS pour recevoir des notifications de solde ?"],
         "responses": ["Oui, vous pouvez activer les notifications de solde en envoyant 'Solde' au 1198 par SMS."],
         "context_set": ""
        },
        {"tag": "les différents forfaits qui offrent un suivi de solde",
         "patterns": ["Pouvez-vous m'informer sur les différents forfaits qui offrent un suivi de solde en temps réel ?"],
         "responses": ["Oui, plusieurs forfaits proposent un suivi en temps réel. Vous pouvez consulter notre site web ou contacter le service client pour plus d'informations"],
         "context_set": ""
        },
        {"tag": "la procédure pour connaître le solde",
         "patterns": ["Quelle est la procédure pour connaître le solde de mon compte prépayé par téléphone ?"],
         "responses": ["Composez le *122# et appuyez sur la touche d'appel pour recevoir un message avec votre solde actuel.\n"],
         "context_set": ""
        },
        {"tag": " applications tierces",
         "patterns": ["Y a-t-il des applications tierces recommandées pour surveiller mon solde ?"],
         "responses": [" Nous recommandons d'utiliser les applications officielles pour garantir la sécurité des informations. Vous pouvez télécharger l'application Tunisie Telecom sur les plateformes de téléchargement."],
         "context_set": ""
        },
        {"tag": "alertes par e-mail",
         "patterns": ["Puis-je recevoir des alertes par e-mail pour mon solde ?"],
         "responses": ["Actuellement, nous n'offrons pas de service d'alerte par e-mail. Cependant, vous pouvez activer les notifications SMS"],
         "context_set": ""
        },
        {"tag": "consulter le solde via le site web",
         "patterns": ["Comment puis-je consulter le solde de mon compte via le site web ?"],
         "responses": ["Connectez-vous à votre compte sur le site web de Tunisie Telecom et vous trouverez l'option pour vérifier votre solde."],
         "context_set": ""
        },
        {"tag": "fréquence de mise à jour du solde",
         "patterns": ["Quelle est la fréquence de mise à jour du solde sur l'application mobile ?"],
         "responses": ["Le solde sur l'application mobile est généralement mis à jour en temps réel, mais cela peut varier en fonction de la connectivité réseau.."],
         "context_set": ""
        },
        {"tag": "",
         "patterns": ["Comment puis-je vérifier la date d'expiration de mon crédit prépayé ?"],
         "responses": ["Envoyez un SMS au 1020 avec le texte 'Date d'expiration' pour obtenir cette information."],
         "context_set": ""
        },
         {"tag": "promotions ",
         "patterns": ["Existe-t-il des promotions spéciales pour recharger mon crédit ?"],
         "responses": ["Oui, vous pouvez consulter les promotions en cours sur notre site web ou en envoyant 'Promo' au 1198 par SMS ou consulter l' aplication My TT."],
         "context_set": ""
        },
        {"tag": "",
         "patterns": ["Comment puis-je activer une offre spéciale sur mon numéro ?"],
         "responses": ["appelez 1198."],
         "context_set": ""
        },
        {"tag": "unrecognized",
        "patterns": ["*"],
        "responses": ["Vous pouvez appeler le 1198 car je n'ai pas compris votre question. Notre équipe Tunisie telecome sera ravie de vous aider!"],
          "context_set": ""
        },
  {"tag": "des détails sur les forfaits postpayés disponibles",
         "patterns": ["Pouvez-vous me fournir des détails sur les forfaits postpayés disponibles ?"],
         "responses": [" Oui, veuillez visiter notre site web ou contacter le service client pour obtenir des informations détaillées sur nos forfaits postpayés.."],
         "context_set": ""
        },
        {"tag": "des promotions spéciales pour recharger mon crédit",
         "patterns": ["Existe-t-il des promotions spéciales pour recharger mon crédit ?"],
         "responses": ["oui,vous pouvez consulter les promotions en cours sur notre site web ou en envoyant 'promo' au 1198 par SMS"],
         "context_set": ""
        },
        {"tag": "des applications partenaires pour vérifier mon solde",
          "patterns": ["Y a-t-il des applications partenaires pour vérifier mon solde ?"],
         "responses": [" Nous collaborons avec certaines applications tierces. Veuillez vérifier notre site web pour la liste des partenaires officiels. "],
         "context_set": ""
        },
        {"tag": "recharger mon crédit en ligne",
         "patterns": ["Comment puis-je recharger mon crédit en ligne ?"] ,
         "responses": [" Vous pouvez utiliser notre site web ou des applications de paiement mobile pour recharger votre crédit en ligne."] ,
         "context_set": ""
        },
        {"tag": "les options de paiement disponibles pour les factures postpayées ?",
         "patterns": ["Quelles sont les options de paiement disponibles pour les factures postpayées ?"],
         "responses": ["Vous pouvez régler votre facture postpayée en ligne, par virement bancaire ou en visitant l'une de nos agences. "],
         "context_set": ""
        },
         {"tag": "les horaires d'ouverture du service client ",
         "patterns": ["Quels sont les horaires d'ouverture du service client ?"],
         "responses": [" Le service client est disponible 24/7. Vous pouvez nous contacter à tout moment au 1111."],
         "context_set": ""
        },
        {
        "tag": "désactiver les notifications SMS promotionnelles",
        "patterns": ["Comment puis-je désactiver les notifications SMS promotionnelles ?"],
        "responses": ["Envoyez 'Stop Promo' au 1198 pour désactiver les notifications SMS promotionnelles"],
        "context_set": ""
        },
         {"tag": " la vérification du solde via l'application mobile ",
         "patterns": ["Y a-t-il des frais associés à la vérification du solde via l'application mobile ?"],
         "responses": [" Non, la vérification du solde via l'application mobile est gratuite."],
         "context_set": ""
        },
        {"tag": "activer le roaming international sur ma ligne ",
         "patterns": ["Comment puis-je activer le roaming international sur ma ligne ?"],
         "responses": ["Contactez le service clientèle au 1111 pour activer le roaming international."],
         "context_set": ""
        },
          {"tag": "les destinations couvertes par le forfait de roaming international ",
         "patterns": ["Quelles sont les destinations couvertes par le forfait de roaming international ?"],
         "responses": ["Vous pouvez trouver la liste des destinations incluses sur notre site web ou en contactant le service client. "],
         "context_set": ""
        },
        {"tag": "partager mon solde avec d'autres numéros ",
         "patterns": ["Puis-je partager mon solde avec d'autres numéros ?"],
         "responses": [" Oui, vous pouvez utiliser le service de transfert de solde en composant 123 suivi du numéro de destination et du montant..\n"],
         "context_set": ""
        },
        {"tag": " les mesures de sécurité pour protéger ma vie privée lors de l'utilisation de l'application mobile ",
         "patterns": ["Quelles sont les mesures de sécurité pour protéger ma vie privée lors de l'utilisation de l'application mobile ?"],
         "responses": [" L'application utilise des protocoles de sécurité avancés pour assurer la confidentialité de vos informations.."],
         "context_set": ""
        },
        {"tag": " bloquer un numéro indésirable ou spam ",
         "patterns": ["Comment puis-je bloquer un numéro indésirable ou spam ?"],
         "responses": [" Envoyez 'Bloque,[numéro]', au 1198 pour bloquer un numéro spécifique"],
         "context_set": ""
        },
        {"tag":" les promotions actuelles pour les nouveaux abonnés ",
         "patterns": ["Quelles sont les promotions actuelles pour les nouveaux abonnés ?"],
         "responses": [" Consultez notre site web ou appelez le service client pour connaître les promotions en cours."],
         "context_set": ""
        },
        {
        "tag": "perte de mon téléphone",
        "patterns": ["Que faire en cas de perte de mon téléphone ?"],
        "responses": ["Contactez immédiatement le service client au 1111 pour suspendre votre ligne et prendre des mesures de sécurité."],
        "context_set": ""
        },
         {"tag": "options de paiement sont disponibles pour recharger mon crédit ",
         "patterns": ["Quelles options de paiement sont disponibles pour recharger mon crédit ?"],
         "responses": ["Vous pouvez recharger votre crédit via les kiosques de recharge, les points de vente autorisés, les applications de paiement mobile ou en ligne sur notre site web.."],
         "context_set": ""
        },
        {"tag": " des réductions spéciales pour les recharges en ligne  ",
         "patterns": ["Y a-t-il des réductions spéciales pour les recharges en ligne ?"],
         "responses": [" Oui, certaines promotions offrent des réductions exclusives pour les recharges en ligne. Consultez notre site web pour les détails."],
         "context_set": ""
        },
        {"tag": "activer des services à valeur ajoutée tels que la messagerie vocale ou la conférence téléphonique ",
         "patterns": ["Comment puis-je activer des services à valeur ajoutée tels que la messagerie vocale ou la conférence téléphonique ?"],
         "responses": ["Envoyez un SMS au 1198 avec le code du service que vous souhaitez activer. Vous pouvez également le faire via l'application mobile."],
         "context_set": ""
        },
        {"tag": " les options pour souscrire à des forfaits internet mensuels ",
        "patterns": ["Quelles sont les options pour souscrire à des forfaits internet mensuels ?"],
        "responses": ["Vous pouvez souscrire à des forfaits internet en envoyant un SMS au 1020 ou en visitant notre site web."],
          "context_set": ""
        }





        




    
    # Rest of your intents...
    # Copy-paste the rest of the intents here following the same structure
    
]
