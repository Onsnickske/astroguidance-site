# content.py
# multilingual text for the 5-page Astroguidancelife site

COMMON_TEXTS = {
    "en": {
        "site_title": "Astroguidancelife",
        "site_subtitle": "Begin your journey with me",
        "menu_home": "Home",
        "menu_about": "About me",
        "menu_reports": "Astrology Reports",
        "menu_book": "Book Now",
        "menu_contact": "Contact Me",
        "footer": "© Astro Guidance Life. All rights reserved.",
        "footer_note": "Bookings are personal and non-refundable once preparation has started.",
        "book_prefix": "Book",  # used in reports small boxes
    },
    "es": {
        "site_title": "Astroguidancelife",
        "site_subtitle": "Empieza tu camino conmigo",
        "menu_home": "Inicio",
        "menu_about": "Sobre mí",
        "menu_reports": "Informes astrológicos",
        "menu_book": "Reservar",
        "menu_contact": "Contáctame",
        "footer": "© Astro Guidance Life. Todos los derechos reservados.",
        "footer_note": "Las consultas son personales y no reembolsables una vez iniciada su preparación.",
        "book_prefix": "Reservar",
    },
    "nl": {
        "site_title": "Astroguidancelife",
        "site_subtitle": "Begin je reis met mij",
        "menu_home": "Home",
        "menu_about": "Over mij",
        "menu_reports": "Astrologische rapporten",
        "menu_book": "Boek nu",
        "menu_contact": "Contact",
        "footer": "© Astro Guidance Life. Alle rechten voorbehouden.",
        "footer_note": "Consulten zijn persoonlijk en niet terug te betalen zodra de voorbereiding is begonnen.",
        "book_prefix": "Boek",
    },
}

PAGE_CONTENT = {
    # ---------------- HOME ----------------
    "home": {
        "en": {
            "title": "Home",
            "hero_title": "It's written in the stars",
            "hero_subtitle": "Begin your journey of healing, self-discovery and personal transformation through the art of astrology.",
            # this will show above the 3 cards
            "featured_title": "Most requested reports",
            "featured_intro": "Start with one of these readings.",
            "welcome_title": "Welcome to Astroguidancelife",
            "welcome_text": (
                "Are you looking to improve your love life, your career, or your health, but don't know where to start? "
                "Wherever you are in life, I can help guide you to begin your journey."
            ),
            "welcome_cta": "Find out more about me »",
            "what_is_astrology_title": "What is Astrology?",
            "what_is_astrology_text": (
                "Astrology is the study of the position and movements of the planets to interpret a person's "
                "characteristics and forecast life events."
            ),
        },
        "es": {
            "title": "Inicio",
            "hero_title": "Está escrito en las estrellas",
            "hero_subtitle": "Empieza tu camino de sanación, autodescubrimiento y transformación personal a través de la astrología.",
            "featured_title": "Informes más solicitados",
            "featured_intro": "Empieza con uno de estos informes.",
            "welcome_title": "Bienvenido a Astroguidancelife",
            "welcome_text": (
                "¿Quieres mejorar tu vida amorosa, tu carrera o tu salud y no sabes por dónde empezar? "
                "Estés donde estés, puedo acompañarte."
            ),
            "welcome_cta": "Saber más sobre mí »",
            "what_is_astrology_title": "¿Qué es la astrología?",
            "what_is_astrology_text": (
                "La astrología estudia la posición y el movimiento de los planetas para interpretar tu carácter "
                "y prever acontecimientos importantes."
            ),
        },
        "nl": {
            "title": "Home",
            "hero_title": "Het staat in de sterren",
            "hero_subtitle": "Begin je reis van heling, zelfkennis en persoonlijke groei via de astrologie.",
            "featured_title": "Meest gekozen rapporten",
            "featured_intro": "Begin met één van deze.",
            "welcome_title": "Welkom bij Astroguidancelife",
            "welcome_text": (
                "Wil je je relatie, werk of gezondheid verbeteren maar weet je niet waar te beginnen? "
                "Waar je ook staat, ik kan je begeleiden."
            ),
            "welcome_cta": "Meer over mij »",
            "what_is_astrology_title": "Wat is astrologie?",
            "what_is_astrology_text": (
                "Astrologie kijkt naar de positie van de planeten om je karakter en levenscycli te duiden."
            ),
        },
    },

    # ---------------- ABOUT ----------------
    "about": {
        "en": {
            "title": "About Me",
            "intro_1": "I can't predict the future, but I can guide you to make the right decisions in life.",
            "intro_2": (
                "In the 30 years I have been studying and practicing astrology, I have been able to help myself, "
                "my family and my friends to better understand how we can improve our lives."
            ),
            "intro_3": "Let me help you to find out how you can get the most out of this life.",
            "signature": "Michèle",
            "cta": "Begin your journey with me »",
            "work_title": "About My Work",
            "work_1": (
                "By looking at past and present issues we can analyse what blockages are holding us back from moving on "
                "and leading a happy life."
            ),
            "work_2": (
                "I will explain the meaning of the position of the planets at the exact moment you were born and "
                "the influence they have on your individual character."
            ),
            "work_3": (
                "My intent is to guide you to discover your weaknesses and strengths and empower you to better "
                "understand yourself and help you make important choices in life."
            ),
            "reports_teaser": "Below you can find the different astrology reports I offer.",
        },
        "es": {
            "title": "Sobre mí",
            "intro_1": "No puedo predecir el futuro, pero sí puedo guiarte para que tomes las decisiones correctas.",
            "intro_2": (
                "En los 30 años que llevo estudiando y practicando astrología he podido ayudarme a mí misma, "
                "a mi familia y a mis amigos a comprender mejor cómo mejorar nuestras vidas."
            ),
            "intro_3": "Déjame ayudarte a descubrir cómo aprovechar al máximo esta vida.",
            "signature": "Michèle",
            "cta": "Empieza tu camino conmigo »",
            "work_title": "Sobre mi trabajo",
            "work_1": (
                "Analizando el pasado y el presente podemos ver qué bloqueos te impiden avanzar y llevar una vida feliz."
            ),
            "work_2": (
                "Te explicaré el significado de la posición de los planetas en el momento de tu nacimiento "
                "y la influencia que tienen."
            ),
            "work_3": (
                "Mi intención es ayudarte a descubrir tus fortalezas y debilidades y empoderarte para tomar decisiones."
            ),
            "reports_teaser": "Aquí puedes ver los informes que ofrezco.",
        },
        "nl": {
            "title": "Over mij",
            "intro_1": "Ik kan de toekomst niet voorspellen, maar ik kan je wel helpen de juiste keuzes te maken.",
            "intro_2": (
                "In de 30 jaar dat ik met astrologie werk, heb ik mezelf, mijn familie en vrienden geholpen "
                "om ons leven beter te begrijpen."
            ),
            "intro_3": "Laat mij je helpen om het beste uit dit leven te halen.",
            "signature": "Michèle",
            "cta": "Begin je reis met mij »",
            "work_title": "Over mijn werk",
            "work_1": (
                "Door naar verleden en heden te kijken, zien we welke blokkades je tegenhouden om verder te gaan."
            ),
            "work_2": (
                "Ik leg je de planeetstanden bij je geboorte uit en wat die betekenen voor jouw karakter."
            ),
            "work_3": (
                "Mijn doel is je te begeleiden zodat je jezelf beter kent en goede keuzes kunt maken."
            ),
            "reports_teaser": "Hieronder vind je de astrologische rapporten.",
        },
    },

    # ---------------- REPORTS ----------------
    "reports": {
        "en": {
            "title": "Astrology Reports",
            "subtitle": "Book your initial consultation today and find out how your life can change for the better!",
            "intro": (
                "In the Natal Chart Analysis I will explain the meaning of the rising sign, "
                "the planets in house placement and the aspects the planets make."
            ),
            "intro_2": (
                "After this general overview I can go into more detail on a certain topic of your choice: "
                "career, love, health, etc."
            ),
            "reports_list": [
                {
                    "code": "natal",
                    "title": "Natal chart analysis",
                    "desc": "Find out how the position of the planets at your birth influence your entire life and personality.",
                    "price": "€80"
                },
                {
                    "code": "love",
                    "title": "Love & Compatibility",
                    "desc": "Find out if you and your love interest are soul mates, best friends, or a recipe for disaster.",
                    "price": "€60"
                },
                {
                    "code": "career",
                    "title": "Career Report",
                    "desc": "If you wonder if you are in the right job, making enough money and maintaining a good work/life balance, this report is for you!",
                    "price": "€60"
                },
                {
                    "code": "forecast",
                    "title": "12 Month Forecast",
                    "desc": "Prepare for what's ahead. Get personal guidance for the next 12 months on relationship, love, career, money, health, etc.",
                    "price": "€60"
                },
                {
                    "code": "health",
                    "title": "Health & Vitality",
                    "desc": "Medical astrology, or Health astrology, is the branch of astrology that deals primarily with health concerns. In your natal chart I can determine which, if any, health issues you are likely to experience throughout the course of your life.",
                    "price": "€60"
                },
                {
                    "code": "saturn",
                    "title": "Saturn return",
                    "desc": "Your Saturn return occurs every 27 to 29 years when the planet Saturn returns to the sign and degree it was at when you were born. It's a time of coming into alignment with your life's true path. The Saturn return calls for personal growth and major life changes.",
                    "price": "€60"
                },
                {
                    "code": "jupiter",
                    "title": "Jupiter return",
                    "desc": "Your Jupiter return is a time to plan. Jupiter returns to your natal sign and degree every 12 years. Your Jupiter return can be a tremendous growth period, materially, financially, intellectually, professionally and personally.",
                    "price": "€60"
                },
                {
                    "code": "pluto",
                    "title": "Pluto square Pluto",
                    "desc": "Your Pluto square Pluto transit happens once in your life and is a period of profound change and renewal.",
                    "price": "€60"
                },
            ],
            "bottom_cta": "Ready to explore one of these? Book your session and I’ll guide you.",
        },
        "es": {
            "title": "Informes astrológicos",
            "subtitle": "Reserva tu consulta inicial y descubre cómo tu vida puede mejorar.",
            "intro": (
                "En el análisis de carta natal explico el ascendente, la posición de los planetas en las casas "
                "y los aspectos que forman."
            ),
            "intro_2": (
                "Después puedo entrar en un tema concreto: amor, carrera, salud, etc."
            ),
            "reports_list": [
                {
                    "code": "natal",
                    "title": "Análisis de carta natal",
                    "desc": "Descubre cómo la posición de los planetas en tu nacimiento influye en toda tu vida y en tu personalidad.",
                    "price": "€80"
                },
                {
                    "code": "love",
                    "title": "Amor y compatibilidad",
                    "desc": "Averigua si tú y tu persona especial sois almas gemelas, mejores amigos… o una receta para el desastre.",
                    "price": "€60"
                },
                {
                    "code": "career",
                    "title": "Informe profesional",
                    "desc": "Si te preguntas si estás en el trabajo adecuado, si ganas lo suficiente o si tienes buen equilibrio vida/trabajo, este informe es para ti.",
                    "price": "€60"
                },
                {
                    "code": "forecast",
                    "title": "Pronóstico 12 meses",
                    "desc": "Prepárate para lo que viene. Obtén una guía personal para los próximos 12 meses sobre relaciones, amor, trabajo, dinero, salud, etc.",
                    "price": "€60"
                },
                {
                    "code": "health",
                    "title": "Salud y vitalidad",
                    "desc": "La astrología médica se ocupa de las cuestiones de salud. A partir de tu carta natal puedo ver qué áreas son más sensibles y qué temas pueden aparecer a lo largo de tu vida.",
                    "price": "€60"
                },
                {
                    "code": "saturn",
                    "title": "Retorno de Saturno",
                    "desc": "Tu retorno de Saturno ocurre cada 27-29 años, cuando Saturno vuelve al signo y grado de tu nacimiento. Es un momento de alinearte con tu camino real de vida y de hacer cambios importantes.",
                    "price": "€60"
                },
                {
                    "code": "jupiter",
                    "title": "Retorno de Júpiter",
                    "desc": "El retorno de Júpiter (cada 12 años) es un momento ideal para planificar. Suele traer crecimiento material, financiero, intelectual, profesional y personal.",
                    "price": "€60"
                },
                {
                    "code": "pluto",
                    "title": "Plutón cuadratura Plutón",
                    "desc": "La cuadratura de Plutón a Plutón sucede solo una vez en la vida y marca un período de cambio profundo y de renovación.",
                    "price": "€60"
                },
            ],
            "bottom_cta": "¿Quieres uno de estos informes? Reserva tu sesión.",
        },
        "nl": {
            "title": "Astrologische rapporten",
            "subtitle": "Boek je eerste consult en ontdek hoe je leven kan veranderen.",
            "intro": (
                "In de geboortehoroscoop leg ik ascendant, huizen en aspecten uit."
            ),
            "intro_2": (
                "Daarna kunnen we inzoomen op een thema: liefde, werk, gezondheid."
            ),
            "reports_list": [
                {
                    "code": "natal",
                    "title": "Analyse van de geboortehoroscoop",
                    "desc": "Ontdek hoe de stand van de planeten bij je geboorte je hele leven en je persoonlijkheid beïnvloedt.",
                    "price": "€80"
                },
                {
                    "code": "love",
                    "title": "Liefde & compatibiliteit",
                    "desc": "Kom te weten of jij en je partner / crush echte soulmates zijn, beste vrienden… of misschien toch een explosieve combinatie.",
                    "price": "€60"
                },
                {
                    "code": "career",
                    "title": "Carrière-rapport",
                    "desc": "Vraag je je af of je wel in de juiste job zit, voldoende verdient en een goed evenwicht hebt tussen werk en privé? Dan is dit rapport voor jou.",
                    "price": "€60"
                },
                {
                    "code": "forecast",
                    "title": "Voorspelling 12 maanden",
                    "desc": "Bereid je voor op wat eraan komt. Persoonlijke begeleiding voor de komende 12 maanden over relaties, liefde, werk, geld, gezondheid, enz.",
                    "price": "€60"
                },
                {
                    "code": "health",
                    "title": "Gezondheid & vitaliteit",
                    "desc": "Medische astrologie kijkt naar mogelijke gevoelige punten in je horoscoop. Zo kunnen we zien welke thema’s in de loop van je leven kunnen opduiken.",
                    "price": "€60"
                },
                {
                    "code": "saturn",
                    "title": "Saturnus-return",
                    "desc": "Je Saturnus-return komt om de 27 à 29 jaar, wanneer Saturnus terugkeert naar de plaats van je geboorte. Dat is een periode van heroriëntatie, volwassen worden en belangrijke levenskeuzes.",
                    "price": "€60"
                },
                {
                    "code": "jupiter",
                    "title": "Jupiter-return",
                    "desc": "Je Jupiter-return (ongeveer elke 12 jaar) is een ideaal moment om te plannen. Het kan een sterke periode van groei zijn — financieel, professioneel én persoonlijk.",
                    "price": "€60"
                },
                {
                    "code": "pluto",
                    "title": "Pluto vierkant Pluto",
                    "desc": "Deze transit gebeurt maar één keer in je leven en duidt op diepe transformatie en vernieuwing.",
                    "price": "€60"
                },
            ],
            "bottom_cta": "Klaar om te boeken? Laat het me weten.",
        },
    },

    # ---------------- BOOK ----------------
    "book": {
        "en": {
            "title": "Book now",
            "intro": "Choose the report that speaks to you and send your request. I will confirm by email.",
            "form_name": "Name",
            "form_email": "Email",
            "form_topic": "Which report would you like?",
            "book_button": "Send booking request",
            "success_msg": "Thank you — your booking request has been received.",
            "options": [
                {"value": "natal", "label": "Natal chart analysis – €80"},
                {"value": "love", "label": "Love & compatibility – €60"},
                {"value": "career", "label": "Career report – €60"},
                {"value": "forecast", "label": "12 month forecast – €60"},
                {"value": "health", "label": "Health & vitality – €60"},
                {"value": "saturn", "label": "Saturn return – €60"},
                {"value": "jupiter", "label": "Jupiter return – €60"},
                {"value": "pluto", "label": "Pluto square Pluto – €60"},
            ],
        },
        "es": {
            "title": "Reservar",
            "intro": "Elige el informe que necesitas y mándame tu solicitud. Te confirmaré por email.",
            "form_name": "Nombre",
            "form_email": "Correo electrónico",
            "form_topic": "¿Qué informe deseas?",
            "book_button": "Enviar reserva",
            "success_msg": "Gracias — he recibido tu solicitud.",
            "options": [
                {"value": "natal", "label": "Carta natal – 80 €"},
                {"value": "love", "label": "Amor y compatibilidad – 60 €"},
                {"value": "career", "label": "Informe profesional – 60 €"},
                {"value": "forecast", "label": "Pronóstico 12 meses – 60 €"},
                {"value": "health", "label": "Salud y vitalidad – 60 €"},
                {"value": "saturn", "label": "Retorno de Saturno – 60 €"},
                {"value": "jupiter", "label": "Retorno de Júpiter – 60 €"},
                {"value": "pluto", "label": "Plutón cuadratura Plutón – 60 €"},
            ],
        },
        "nl": {
            "title": "Boek nu",
            "intro": "Kies het rapport dat je wilt en ik bevestig per mail.",
            "form_name": "Naam",
            "form_email": "E-mail",
            "form_topic": "Welk rapport wil je?",
            "book_button": "Aanvraag versturen",
            "success_msg": "Dank je wel — je aanvraag is ontvangen.",
            "options": [
                {"value": "natal", "label": "Geboortehoroscoop – €80"},
                {"value": "love", "label": "Liefde & compatibiliteit – €60"},
                {"value": "career", "label": "Carrière-rapport – €60"},
                {"value": "forecast", "label": "Voorspelling 12 maanden – €60"},
                {"value": "health", "label": "Gezondheid & vitaliteit – €60"},
                {"value": "saturn", "label": "Saturnus-return – €60"},
                {"value": "jupiter", "label": "Jupiter-return – €60"},
                {"value": "pluto", "label": "Pluto vierkant Pluto – €60"},
            ],
        },
    },

    # ---------------- CONTACT ----------------
    "contact": {
        "en": {
            "title": "Contact Me",
            "hero_heading": "Don’t be afraid, be curious!",
            "hero_text": (
                "You have made an excellent choice of booking a reading with me.\n\n"
                "Every reading is personalized. I study your Natal Chart in detail and this usually takes around 8 hours.\n\n"
                "It is very important to start with a Natal Chart analysis. The “Natal Promise” in your chart is the basis "
                "for all other future analysis regarding all aspects of your life.\n\n"
                "I need your DATE, PLACE and (EXACT) TIME OF BIRTH. The more exact your time of birth, the more accurate my reading!\n\n"
                "Please give me 3 options of day and time that would suit you best for having the video-consultation.\n\n"
                "Send me your date, place and time of birth now and I will contact you shortly."
            ),
            "get_in_touch_title": "Get in Touch",
            "get_in_touch_text": "WhatsApp me: +34 616 026 333 · Email: michele.blindeman@gmail.com",
            "form_name": "First Name",
            "form_lastname": "Last Name",
            "form_email": "Email",
            "form_message": "Your Message",
            "form_button": "Send",
            "thanks": "Thank you, I will get back to you.",
            "disclaimer_title": "Terms and Conditions – Consultation disclaimer",
            "disclaimer_paragraphs": [
                "The services I offer can provide meaningful support for processes of self-actualization, "
                "but my consultations do not replace professional medical, legal or financial diagnoses or services.",
                "I do my best to analyse your horoscope on the basis of birth details provided by you. "
                "All information shared will be kept private and safely stored, and will not be shared unless explicit consent is given.",
                "My consultations are not psychic services or fortune telling. They are meant to offer insight into your personal life "
                "and are for guidance / entertainment purposes only.",
                "I can only guide you towards future possibilities. Your free will will always play a role. "
                "It’s divine guidance that one may or may not accept.",
                "You agree that under no circumstances shall I be held liable for your actions, or for direct or indirect damage arising "
                "out of your use of my services.",
                "I do not provide written notes or audio recordings of the consultation, but you may record and take notes for your own use.",
                "Payments must be made in full prior to the consultation and are in no circumstances refundable.",
                "By making the payment, you understand and agree that it reflects a compensation for the work to prepare for the consultation.",
                "I reserve the right to decline any consultation request at my discretion.",
            ],
        },
        "es": {
            "title": "Contáctame",
            "hero_heading": "No tengas miedo, sé curiosa/o",
            "hero_text": (
                "Has tomado una excelente decisión al reservar una lectura conmigo.\n\n"
                "Cada lectura es personalizada. Estudio tu carta natal en detalle y esto suele llevarme unas 8 horas.\n\n"
                "Es muy importante empezar con una carta natal. La “promesa natal” en tu carta es la base para todos los análisis futuros: "
                "amor, trabajo, salud, etc.\n\n"
                "Necesito tu FECHA, LUGAR y HORA (EXACTA) DE NACIMIENTO. Cuanto más exacta sea la hora, más precisa será la lectura.\n\n"
                "Indícame 3 opciones de día y hora que te vengan bien para la videoconsulta.\n\n"
                "Mándame tu fecha, lugar y hora de nacimiento ahora y te contactaré en breve."
            ),
            "get_in_touch_title": "Ponte en contacto",
            "get_in_touch_text": "WhatsApp: +34 616 026 333 · Email: michele.blindeman@gmail.com",
            "form_name": "Nombre",
            "form_lastname": "Apellidos",
            "form_email": "Correo electrónico",
            "form_message": "Tu mensaje",
            "form_button": "Enviar",
            "thanks": "Gracias, te contestaré en breve.",
            "disclaimer_title": "Términos y Condiciones – aviso sobre la consulta",
            "disclaimer_paragraphs": [
                "Los servicios que ofrezco pueden brindar apoyo valioso para procesos de crecimiento personal, "
                "pero no sustituyen diagnósticos ni servicios médicos, legales o financieros profesionales.",
                "Analizo tu carta en base a los datos de nacimiento que tú me proporcionas. "
                "La información compartida se mantendrá privada y no se compartirá sin tu consentimiento.",
                "Mis consultas no son servicios de videncia ni de adivinación. Están destinadas a darte claridad y orientación.",
                "Solo puedo guiarte hacia posibilidades futuras. Tu libre albedrío siempre cuenta.",
                "Aceptas que no puedo ser responsable de las decisiones que tomes ni de daños directos o indirectos derivados del uso de mis servicios.",
                "El pago debe hacerse por adelantado y no es reembolsable.",
                "Al pagar aceptas que es una compensación por el trabajo de preparación de la consulta.",
                "Me reservo el derecho de rechazar una consulta si lo considero necesario.",
            ],
        },
        "nl": {
            "title": "Neem contact op",
            "hero_heading": "Wees niet bang, wees nieuwsgierig",
            "hero_text": (
                "Je hebt een heel goede keuze gemaakt door een reading te boeken.\n\n"
                "Elke reading is persoonlijk. Ik bestudeer je geboortehoroscoop in detail en dat duurt meestal zo’n 8 uur.\n\n"
                "Het is belangrijk om te beginnen met de geboortehoroscoop. De ‘natal promise’ is de basis voor alle verdere analyses.\n\n"
                "Ik heb je DATUM, PLAATS en (EXACTE) TIJD van geboorte nodig. Hoe preciezer, hoe beter het resultaat.\n\n"
                "Geef me 3 opties van dag en tijd voor de video-sessie.\n\n"
                "Stuur me je gegevens en ik neem contact met je op."
            ),
            "get_in_touch_title": "Contact",
            "get_in_touch_text": "WhatsApp: +34 616 026 333 · Email: michele.blindeman@gmail.com",
            "form_name": "Voornaam",
            "form_lastname": "Achternaam",
            "form_email": "E-mail",
            "form_message": "Bericht",
            "form_button": "Versturen",
            "thanks": "Bedankt, ik laat snel iets weten.",
            "disclaimer_title": "Voorwaarden – Consult disclaimer",
            "disclaimer_paragraphs": [
                "Mijn consulten vervangen geen medisch, juridisch of financieel advies.",
                "Alles wat je deelt blijft privé.",
                "Consulten zijn bedoeld als inzicht/ begeleiding.",
                "Vrije wil blijft altijd meespelen.",
                "Betaling vooraf, niet terugbetaalbaar.",
            ],
        },
    },
}
