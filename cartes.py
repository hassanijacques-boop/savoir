# -*- coding: utf-8 -*-
"""Cartes de savoir islamique — méthode Deepstash (micro-cartes, preuve, action).
Règle absolue : aucune référence inventée. Coran = sourate:verset. Hadith = recueil + n° quand sûr.
"""

STACKS = [
 {"id":"tawhid","n":"Les trois fondements","ar":"الأُصُول الثَّلَاثَة","e":"🕌","c":"#D4AF37",
  "d":"Al-Usûl ath-Thalâtha de Muhammad ibn 'Abd al-Wahhâb : qui est ton Seigneur, quelle est ta religion, qui est ton prophète."},
 {"id":"kitab","n":"Le livre du Tawhîd","ar":"كِتَاب التَّوْحِيد","e":"📕","c":"#E8C86A",
  "d":"Les chapitres de Kitâb at-Tawhîd : ce qui annule l'unicité, et comment s'en préserver."},
 {"id":"hadiths","n":"Les 40 hadiths d'an-Nawawî","ar":"الأَرْبَعُون النَّوَاوِيَّة","e":"📜","c":"#34d399",
  "d":"Quarante hadiths qui résument la religion : intention, piliers, halal et haram, caractère."},
 {"id":"sira","n":"La Sîra du Prophète ﷺ","ar":"السِّيرَة النَّبَوِيَّة","e":"🌙","c":"#60a5fa",
  "d":"De la naissance à la mort : les étapes qui changent la compréhension du message."},
 {"id":"prophetes","n":"Les prophètes","ar":"الأَنْبِيَاء","e":"🕊️","c":"#a78bfa",
  "d":"Les 25 prophètes cités dans le Coran, et ce que chaque récit enseigne."},
 {"id":"savants","n":"Les savants","ar":"العُلَمَاء","e":"🖋️","c":"#fbbf24",
  "d":"Ceux qui ont porté le savoir : les quatre imams, les muhaddithûn, les contemporains."},
 {"id":"tahara","n":"La purification","ar":"الطَّهَارَة","e":"💧","c":"#38bdf8",
  "d":"Wudû', ghusl, tayammum : les conditions de validité de la prière."},
 {"id":"salat","n":"La prière","ar":"الصَّلَاة","e":"🕋","c":"#fb923c",
  "d":"Conditions, piliers, obligations et sunan : ce sans quoi la prière ne vaut pas."},
 {"id":"mariage","n":"Mariage & famille","ar":"النِّكَاح","e":"💍","c":"#f472b6",
  "d":"Contrat, droits et devoirs, vie commune : le foyer comme acte d'adoration."},
 {"id":"education","n":"Éducation des enfants","ar":"تَرْبِيَة الأَوْلَاد","e":"🌱","c":"#4ade80",
  "d":"Ce que la sunna ordonne, dans quel ordre, et à quel âge."},
 {"id":"adhkar","n":"Adhkâr & du'â","ar":"الأَذْكَار","e":"📿","c":"#22d3ee",
  "d":"Les invocations du quotidien, leur moment et leur sens."},
 {"id":"akhlaq","n":"Le caractère","ar":"الأَخْلَاق","e":"💛","c":"#facc15",
  "d":"L'akhlâq du Prophète ﷺ : ce qui pèse le plus lourd dans la balance."},
]

C = []
def c(s, t, q, a, src, act=""):
    C.append({"id":f"{s}{len(C)+1:03d}", "s":s, "t":t, "q":q, "a":a, "src":src, "act":act})

# ─────────────── TAWHÎD — LES TROIS FONDEMENTS ───────────────
c("tawhid","Pourquoi Allah nous a-t-il créés ?",
  "Quel est le but de notre création, et quel verset le dit ?",
  "Allah nous a créés pour L'adorer, Lui seul. « Je n'ai créé les djinns et les hommes que pour qu'ils M'adorent. » L'adoration n'est pas un moyen d'aller mieux : c'est la fonction pour laquelle l'humain existe.",
  "Coran, 51:56","Écrire cette phrase sur un papier et la relire avant chaque prière pendant 3 jours.")
c("tawhid","Les trois fondements",
  "Quels sont les trois fondements qu'Allah a imposés à tout être humain ?",
  "① La connaissance d'Allah ② la connaissance de l'islam ③ la connaissance du Prophète Muhammad ﷺ. Ce sont les trois questions auxquelles tout serviteur devra répondre.",
  "Al-Usûl ath-Thalâtha, Muhammad ibn 'Abd al-Wahhâb","Réciter les trois de mémoire, sans regarder.")
c("tawhid","La première des obligations",
  "Quelle est la toute première obligation du musulman ?",
  "Le Tawhîd : savoir qu'Allah est unique, et Lui vouer l'adoration. Avant la prière, avant le jeûne : la connaissance de Celui qu'on adore.",
  "Al-Usûl ath-Thalâtha ; Coran, 47:19","Nommer à voix haute les trois formes de tawhîd.")
c("tawhid","Les trois catégories du Tawhîd",
  "Quelles sont les trois catégories du Tawhîd ?",
  "① Ar-Rubûbiyya (Il crée, Il pourvoit, Il gère) ② Al-Ulûhiyya (Lui seul mérite l'adoration) ③ Al-Asmâ' wa-s-Sifât (Ses noms et attributs, sans altération). Les mécréants de La Mecque reconnaissaient la première et rejetaient la deuxième.",
  "Kitâb at-Tawhîd ; Al-'Aqîda al-Wâsitiyya, Ibn Taymiyya","Écrire pour chaque catégorie un exemple concret de ma vie.")
c("tawhid","Pourquoi la Rubûbiyya ne suffit pas",
  "Suffit-il de croire qu'Allah a créé l'univers ?",
  "Non. Les Quraysh croyaient qu'Allah crée et pourvoit — et ils étaient pourtant polythéistes, parce qu'ils adoraient d'autres que Lui. Le combat du message porte sur l'adoration, pas sur la création.",
  "Coran, 29:61-63 ; Kitâb at-Tawhîd, chap. 1","Repérer une chose que j'aime plus que je n'aime Allah, et la nommer.")
c("tawhid","Le sens de « Lâ ilâha illa Allâh »",
  "Que disent exactement les deux parties de la Chahâda ?",
  "« Lâ ilâha » nie toute divinité ; « illa Allâh » affirme qu'Allah seul est adoré. C'est une négation puis une affirmation : on vide le cœur des idoles, puis on y place Allah.",
  "Ma'ârij al-Qabûl, al-Hukamî","Dire la phrase en séparant les deux temps, à voix lente.")
c("tawhid","Les sept conditions de la Chahâda",
  "Cite les sept conditions de « Lâ ilâha illa Allâh ».",
  "Le savoir, la certitude, l'acceptation, la soumission, la sincérité, la véracité, l'amour — et le rejet de tout ce qui est adoré en dehors d'Allah.",
  "Ma'ârij al-Qabûl, al-Hukamî","En choisir une et vérifier honnêtement si elle est présente chez moi.")
c("tawhid","Le shirk, définition",
  "Qu'est-ce que le shirk, et pourquoi est-ce le plus grand des péchés ?",
  "C'est donner à autre qu'Allah une part d'adoration. C'est le seul péché qu'Allah ne pardonne pas s'il n'y a pas de repentir : « Allah ne pardonne pas qu'on Lui associe quoi que ce soit, mais Il pardonne ce qui est moindre. »",
  "Coran, 4:48","Lister trois formes de shirk subtil (ostentation, peur, espérance).")
c("tawhid","Le shirk mineur",
  "Qu'est-ce que le shirk mineur, et comment le reconnaître ?",
  "Tout acte d'adoration mêlé d'ostentation : prier pour être vu, donner pour être loué. Le Prophète ﷺ a dit : « Ce que je crains le plus pour vous, c'est le shirk mineur » — on lui demanda : et qu'est-ce ? Il dit : « l'ostentation ».",
  "Musnad Ahmad ; rapporté aussi par al-Bukhârî dans al-Adab al-Mufrad","Avant un acte de bien, vérifier : pour qui est-ce que je le fais ?")
c("tawhid","L'ihsân",
  "Que veut dire l'ihsân, et quel hadith le définit ?",
  "« Adorer Allah comme si tu Le voyais, car si tu ne Le vois pas, Lui te voit. » C'est le troisième degré : après l'islam et l'iman, l'ihsân est la qualité du regard intérieur.",
  "Sahîh Muslim, n° 8 (hadith Jibrîl)","Prier une fois aujourd'hui en pensant consciemment qu'Allah me voit.")
c("tawhid","Les six piliers de la foi",
  "Quels sont les six piliers de l'iman ?",
  "Croire en Allah, en Ses anges, en Ses livres, en Ses messagers, au Jour dernier, et au décret — le bon et le mauvais.",
  "Sahîh Muslim, n° 8","Écrire le pilier qui me pose le plus de difficulté et chercher pourquoi.")
c("tawhid","Les cinq piliers de l'islam",
  "Quels sont les cinq piliers de l'islam ?",
  "La Chahâda, la prière, la zakât, le jeûne du Ramadan, le pèlerinage — pour celui qui en a les moyens.",
  "Sahîh al-Bukhârî, n° 8 ; Sahîh Muslim, n° 16","Vérifier lequel est le plus fragile chez moi en ce moment.")
c("tawhid","Le pacte de la fitra",
  "Quel est le verset qui parle du pacte originel ?",
  "« Et quand ton Seigneur tira des reins des fils d'Adam leur descendance, et les fit témoigner contre eux-mêmes : ne suis-je pas votre Seigneur ? Ils dirent : si, nous en témoignons. »",
  "Coran, 7:172","Se rappeler ce pacte une fois dans la journée, avant un choix difficile.")
c("tawhid","La hijra intérieure",
  "Que signifie la hijra dans le hadith « l'émigré est celui qui fuit ce qu'Allah a interdit » ?",
  "Que le vrai déplacement n'est pas géographique : c'est quitter ce qu'Allah a interdit. On peut être immobile et avoir fait sa hijra.",
  "Sahîh al-Bukhârî, n° 10","Choisir une chose interdite dont je m'éloigne aujourd'hui, concrètement.")
c("tawhid","Le tawakkul n'est pas la passivité",
  "Le tawakkul dispense-t-il d'agir ?",
  "Non. Le Prophète ﷺ a dit à celui qui laissait sa monture sans l'attacher : « Attache-la, puis place ta confiance en Allah. » Confiance dans le résultat, effort sur les moyens.",
  "Jâmi' at-Tirmidhî, n° 2517 (hasan)","Nommer l'action que je remets à demain « en attendant Allah ».")

# ─────────────── KITÂB AT-TAWHÎD ───────────────
c("kitab","Le droit d'Allah sur Ses serviteurs",
  "Quel est le droit d'Allah sur les serviteurs, et le droit des serviteurs sur Allah ?",
  "« Le droit d'Allah sur les serviteurs : qu'ils L'adorent sans rien Lui associer. Le droit des serviteurs sur Allah : qu'Il ne châtie pas celui qui ne Lui associe rien. »",
  "Sahîh al-Bukhârî, n° 2856 ; Sahîh Muslim, n° 30","Réciter les deux moitiés du hadith de mémoire.")
c("kitab","L'invocation des morts",
  "Pourquoi invoquer un mort est-il une porte du shirk ?",
  "Parce que le du'â est une adoration. Le Prophète ﷺ a dit : « L'invocation, c'est l'adoration. » On ne l'adresse qu'à Allah, vivant, entendant, puissant.",
  "Jâmi' at-Tirmidhî, n° 3372 ; Coran, 40:60","Vérifier à qui j'adresse mes demandes, même intérieurement.")
c("kitab","La peur du shirk",
  "Pourquoi Ibrahim lui-même craignait-il le shirk ?",
  "Il dit : « Et éloigne-moi, ainsi que mes fils, de l'adoration des idoles. » Si l'ami d'Allah craint pour lui-même, personne n'est à l'abri — la sécurité n'est pas une prétention, c'est une demande.",
  "Coran, 14:35 ; Kitâb at-Tawhîd, chap. sur la peur du shirk","Faire du'â pour être préservé du shirk, matin et soir.")
c("kitab","La confiance dans les causes",
  "La croyance aux causes est-elle permise ?",
  "Oui, à condition de ne pas s'y attacher : les causes ne produisent rien par elles-mêmes. Le Prophète ﷺ a interdit de dire « ce que Allah et untel ont voulu », et a enseigné « ce qu'Allah a voulu, puis ce qu'untel a voulu ».",
  "Sunan Abî Dâwûd, n° 4980","Repérer dans mes phrases le « si » qui donne le pouvoir à autre qu'Allah.")
c("kitab","Le talisman",
  "Peut-on porter un objet « protecteur » (amulette, grigri) ?",
  "Non. Le Prophète ﷺ a dit : « Celui qui porte une amulette a commis du shirk. » L'objet ne protège pas : c'est Allah qui protège, et l'attacher au cou est une croyance, pas un geste anodin.",
  "Musnad Ahmad, n° 17422 ; jugé sahîh par al-Albânî","Regarder ce que je porte ou garde « pour la chance ».")
c("kitab","La sorcellerie",
  "Pourquoi la sorcellerie est-elle de la mécréance ?",
  "Parce qu'elle prétend agir sur le destin par un pouvoir autre que celui d'Allah, et qu'elle passe par l'invocation des djinns. C'est l'un des sept péchés destructeurs.",
  "Coran, 2:102 ; Sahîh al-Bukhârî, n° 2766","Ne pas consulter de voyant, même « pour rire ».")
c("kitab","Le jugement par autre qu'Allah",
  "Que dit le Coran de celui qui juge par autre chose que ce qu'Allah a révélé ?",
  "Le verset dit de ceux qui ne jugent pas selon ce qu'Allah a révélé qu'ils sont les mécréants, les injustes, les pervers — selon les versets et selon l'objet du jugement.",
  "Coran, 5:44-47","Vérifier à qui je demande de trancher mes conflits.")
c("kitab","L'amour, condition du tawhîd",
  "Quel est le signe de l'amour véritable d'Allah ?",
  "Suivre le Prophète ﷺ. « Dis : si vous aimez Allah, suivez-moi, Allah vous aimera. » L'amour se prouve par la conformité, pas par l'émotion.",
  "Coran, 3:31","Choisir une sunna simple que je ne pratique pas encore, et la faire aujourd'hui.")
c("kitab","La crainte et l'espérance",
  "Comment équilibrer la crainte et l'espérance ?",
  "Les salaf disaient : « Celui qui adore Allah par l'amour seul est un zindîq, par la crainte seule est un hâribî, par l'espérance seule est un murjî. Le croyant réunit les trois. »",
  "Rapporté par Ibn al-Qayyim, Madârij as-Sâlikîn","Écrire ce qui domine chez moi : peur, espoir ou amour.")
c("kitab","Le droit du voisin",
  "Quel est le droit du voisin en islam ?",
  "Le Prophète ﷺ a dit : « Il n'est pas croyant, celui qui passe la nuit rassasié alors que son voisin a faim. » Le droit du voisin est un droit réel, pas une politesse.",
  "Al-Adab al-Mufrad, al-Bukhârî, n° 112 ; Musnad Ahmad","Vérifier si je sais ce qu'il y a dans l'assiette de mon voisin.")
c("kitab","L'ordre de la da'wa",
  "Par quoi commence l'appel à l'islam ?",
  "Par le tawhîd. Le Prophète ﷺ a dit à Mu'âdh, envoyé au Yémen : « Que la première chose à laquelle tu les appelles soit qu'ils n'adorent qu'Allah. »",
  "Sahîh al-Bukhârî, n° 4347 ; Sahîh Muslim, n° 19","Corriger une idée fausse chez un proche, avec douceur, sur l'unicité.")
c("kitab","L'adoration du cœur",
  "Quelles adorations se font uniquement par le cœur ?",
  "La peur, l'espoir, l'amour, la confiance, l'humilité, le désir. Ces mouvements intérieurs sont des adorations : les diriger vers autre qu'Allah, c'est du shirk.",
  "Kitâb at-Tawhîd ; Ibn al-Qayyim, Madârij as-Sâlikîn","Nommer trois personnes dont l'avis pèse plus que celui d'Allah dans mes choix.")

# ─────────────── LES 40 HADITHS ───────────────
c("hadiths","Les actes et l'intention",
  "Quelle est la valeur d'un acte sans intention ?",
  "« Les actes ne valent que par les intentions, et chacun n'a que ce qu'il a intentionné. » Le même geste peut être une adoration ou une habitude : c'est l'intention qui tranche.",
  "Sahîh al-Bukhârî, n° 1 ; Sahîh Muslim, n° 1907","Avant une action aujourd'hui, formuler l'intention en une phrase.")
c("hadiths","L'islam, l'iman, l'ihsân",
  "Quels sont les trois degrés de la religion ?",
  "L'islam (les cinq actes), l'iman (les six croyances), l'ihsân (l'adoration consciente de la présence d'Allah). Le hadith de Jibrîl les réunit en une seule réponse.",
  "Sahîh Muslim, n° 8","Me situer honnêtement sur les trois degrés.")
c("hadiths","Le halal et le haram sont clairs",
  "Que dit le hadith du licite et de l'illicite « évidents » ?",
  "« Le licite est évident, l'illicite est évident, et entre les deux il y a des choses douteuses. Celui qui se préserve du doute préserve sa religion et son honneur. »",
  "Sahîh al-Bukhârî, n° 52 ; Sahîh Muslim, n° 1599","Identifier un doute concret dans mes revenus ou mes habitudes.")
c("hadiths","La religion est le conseil sincère",
  "Que veut dire « la religion, c'est le nasîha » ?",
  "Que la religion est un conseil sincère envers Allah, Son Livre, Son Messager, les musulmans et leurs dirigeants — pas un jugement des autres, mais une loyauté active.",
  "Sahîh Muslim, n° 55","Donner un conseil utile aujourd'hui, sans humilier.")
c("hadiths","Le croyant aime pour son frère",
  "Quel est le signe de la foi complète selon ce hadith ?",
  "« Nul d'entre vous ne croit vraiment jusqu'à ce qu'il aime pour son frère ce qu'il aime pour lui-même. » Le critère est la jalousie : ce qu'on ne souhaite pas aux autres révèle ce qu'on a dans le cœur.",
  "Sahîh al-Bukhârî, n° 13 ; Sahîh Muslim, n° 45","Faire du'â pour un proche ce que je demande pour moi.")
c("hadiths","Ce qui est douteux",
  "Comment gérer une situation dont je ne connais pas le statut ?",
  "La règle prophétique : « Laisse ce qui te fait douter pour ce qui ne te fait pas douter. » La tranquillité du cœur est un critère, pas une faiblesse.",
  "Jâmi' at-Tirmidhî, n° 2518 ; Musnad Ahmad","Choisir aujourd'hui la version qui me met en paix, même plus exigeante.")
c("hadiths","La foi et la colère",
  "Le fort est-il celui qui gagne le combat ?",
  "Non : « Le fort n'est pas celui qui terrasse les autres, mais celui qui se maîtrise quand il est en colère. » La force est une retenue, pas une démonstration.",
  "Sahîh al-Bukhârî, n° 6114 ; Sahîh Muslim, n° 2609","Ressentir la colère aujourd'hui et ne pas répondre pendant 10 secondes.")
c("hadiths","Allah regarde les cœurs",
  "Que regarde Allah dans nos actes ?",
  "« Allah ne regarde pas votre apparence ni vos corps, mais Il regarde vos cœurs et vos actes. » Ni la taille du geste, ni son apparence : le cœur et la conformité.",
  "Sahîh Muslim, n° 2564","Faire un petit acte aujourd'hui sans que personne ne le sache.")
c("hadiths","Le droit du voisin",
  "Quel hadith établit le droit du voisin ?",
  "« Il n'est pas croyant celui qui se rassasie alors que son voisin a faim. » La foi est liée à la faim de l'autre, pas à mes sensations.",
  "Al-Adab al-Mufrad, n° 112","Offrir quelque chose de simple à un voisin cette semaine.")
c("hadiths","Le meilleur des hommes",
  "Qui est le meilleur selon le Prophète ﷺ ?",
  "« Le meilleur d'entre vous est celui qui apprend le Coran et l'enseigne. » La supériorité est dans le savoir transmis, jamais dans la position.",
  "Sahîh al-Bukhârî, n° 5027","Enseigner à quelqu'un une seule chose que je sais.")
c("hadiths","La propreté",
  "Quelle est la place de la propreté dans la foi ?",
  "« La purification est la moitié de la foi. » Elle n'est pas un détail esthétique : c'est la condition extérieure d'un acte intérieur.",
  "Sahîh Muslim, n° 223","Vérifier aujourd'hui la propreté de mes vêtements pour la prière.")
c("hadiths","Le rire du Prophète ﷺ",
  "Comment le Prophète ﷺ riait-il ?",
  "Il souriait beaucoup et riait sans excès, la bouche entrouverte. La joie n'est pas contraire à la religion : l'excès et la moquerie le sont.",
  "Sahîh al-Bukhârî, n° 6092 (rires et sourires, chap.)","Sourire aujourd'hui à quelqu'un avec qui j'ai un différend.")

# ─────────────── SÎRA ───────────────
c("sira","La naissance",
  "Quand et où le Prophète ﷺ est-il né ?",
  "À La Mecque, en l'an de l'Éléphant (vers 570), un lundi. Son père 'Abdullâh était mort avant sa naissance ; il perd sa mère à six ans.",
  "Ar-Rahîq al-Makhtûm ; Ibn Kathîr, Al-Bidâya wa-n-Nihâya","Retenir : naissance 570, révélation à 40 ans, hijra 622.")
c("sira","Le début de la révélation",
  "Comment la révélation a-t-elle commencé ?",
  "À 40 ans, dans la grotte de Hirâ, Jibrîl vient et dit : « Lis ! » Il répond : « Je ne sais pas lire. » Le premier verset descendu : « Lis au nom de ton Seigneur qui a créé. »",
  "Coran, 96:1-5 ; Sahîh al-Bukhârî, n° 3","Lire le passage 96:1-5 en français, lentement.")
c("sira","Les trois ans silencieux",
  "Combien de temps la prédication a-t-elle été secrète ?",
  "Environ trois ans, avant l'ordre d'avertir publiquement : « Lève-toi et avertis ! »",
  "Coran, 74:1-7 ; Ar-Rahîq al-Makhtûm","Comprendre pourquoi on commence par les proches avant le public.")
c("sira","La première réaction de Quraysh",
  "Qu'ont reproché les Quraysh en premier lieu ?",
  "Non pas le jeûne ni la prière, mais l'unicité : ils soupçonnaient qu'il parlait mal de leurs idoles et divisait le clan. La première opposition porte toujours sur le tawhîd.",
  "Coran, 38:4-5 ; Ar-Rahîq al-Makhtûm","Comparer avec mon propre entourage : où est la vraie résistance ?")
c("sira","L'Aqaba et les Ansâr",
  "Quel événement a préparé l'émigration vers Médine ?",
  "Les serments d'al-'Aqaba, par lesquels les gens de Médine s'engagent à défendre le Prophète ﷺ — puis la hijra en 622.",
  "Ar-Rahîq al-Makhtûm ; Ibn Hishâm, Sîra","Situer la hijra : an 1 de l'Hégire, 622.")
c("sira","La hijra",
  "Où le Prophète ﷺ s'est-il réfugié en quittant La Mecque ?",
  "Dans la grotte de Thawr, avec Abû Bakr. Abû Bakr s'inquiète, il répond : « Ne t'afflige pas, Allah est avec nous. »",
  "Coran, 9:40 ; Sahîh al-Bukhârî, n° 3653","Relire le verset 9:40 et le retenir.")
c("sira","La construction de la mosquée",
  "Quelle est la première décision à Médine ?",
  "Construire la mosquée — centre de culte, d'enseignement et de décision. Puis la fraternisation entre émigrés et Ansâr.",
  "Ar-Rahîq al-Makhtûm","Observer : quelle place tient la mosquée dans ma semaine ?")
c("sira","Badr",
  "Que s'est-il passé à Badr, et en quelle année ?",
  "En l'an 2 H, la première grande bataille : 313 musulmans face à un millier de Quraysh. La victoire est attribuée à Allah seul : « Allah vous a secourus à Badr alors que vous étiez méprisés. »",
  "Coran, 3:123 ; Ar-Rahîq al-Makhtûm","Retenir le chiffre : 313 contre ~1000, an 2 H.")
c("sira","Uhud",
  "Quelle leçon vient de la défaite partielle d'Uhud ?",
  "En l'an 3 H, les archers quittent leurs postes pour le butin, et la ligne se retourne. La leçon : la discipline collective est un ordre, et l'épreuve suit la victoire.",
  "Coran, 3:152-153 ; Ar-Rahîq al-Makhtûm","Identifier une règle que j'abandonne quand le profit apparaît.")
c("sira","Al-Hudaybiyya",
  "Pourquoi le traité d'al-Hudaybiyya est-il appelé une « victoire éclatante » ?",
  "En l'an 6 H, les musulmans acceptent des conditions en apparence défavorables, et le calme qui suit permet à la prédication de s'étendre. « Nous t'avons accordé une victoire éclatante. »",
  "Coran, 48:1 ; Ar-Rahîq al-Makhtûm","Retenir : une paix imparfaite peut valoir plus qu'une victoire d'orgueil.")
c("sira","La conquête de La Mecque",
  "Comment le Prophète ﷺ entre-t-il à La Mecque en l'an 8 H ?",
  "Sans vengeance de masse : « Allez, vous êtes libres. » Il pardonne à ceux qui l'ont chassé et humilié. La victoire sert à effacer, pas à écraser.",
  "Ar-Rahîq al-Makhtûm ; Ibn Hishâm","Nommer une personne que je dois pardonner cette semaine.")
c("sira","Le pèlerinage d'adieu",
  "Que dit le Prophète ﷺ dans son dernier sermon ?",
  "Il rappelle le caractère sacré du sang, des biens et de l'honneur, l'égalité entre les humains, le droit des femmes, et qu'il laisse deux choses : le Livre d'Allah et sa Sunna.",
  "Ar-Rahîq al-Makhtûm ; Sahîh Muslim, n° 1218","Relire l'idée d'égalité : elle est proclamée avant d'être comprise.")
c("sira","La mort du Prophète ﷺ",
  "Quand et à quel âge le Prophète ﷺ est-il mort ?",
  "En l'an 11 H (632), à Médine, à 63 ans, un lundi. Il est enterré dans la chambre de 'Â'isha.",
  "Ar-Rahîq al-Makhtûm ; Sahîh al-Bukhârî","Retenir les repères : 570, 610, 622, 632.")
c("sira","Son caractère",
  "Que dit 'Â'isha du caractère du Prophète ﷺ ?",
  "« Son caractère était le Coran. » Il ne récitait pas seulement le Livre : il l'incarnait au point qu'on pouvait le décrire en le lisant.",
  "Sahîh Muslim, n° 746 ; Ahmad","Lire une sourate en cherchant le comportement qu'elle décrit.")

# ─────────────── LES PROPHÈTES ───────────────
c("prophetes","Le premier prophète",
  "Qui est le premier prophète, et sa première épreuve ?",
  "Âdam, créé puis installé au Paradis avec Hawwâ'. Après la faute, il ne nie pas : il reconnaît et demande pardon. « Seigneur, nous avons été injustes envers nous-mêmes. »",
  "Coran, 7:23 ; 2:37","Retenir : le modèle d'Âdam est le repentir, pas l'excuse.")
c("prophetes","Nûh et l'appel long",
  "Combien de temps Nûh a-t-il appelé son peuple ?",
  "950 ans selon le Coran — et peu l'ont suivi. La leçon : le résultat n'appartient pas au prédicateur, la constance lui appartient.",
  "Coran, 29:14 ; 71:1-28","Penser à une action juste que j'ai abandonnée trop vite.")
c("prophetes","Ibrâhîm et les idoles",
  "Comment Ibrâhîm a-t-il démontré la faiblesse des idoles ?",
  "Il brise les idoles sauf la plus grande, pour forcer son peuple à réfléchir : une idole incapable de se défendre ne peut rien pour vous.",
  "Coran, 21:51-67","Nommer une « idole » moderne qui ne peut rien me donner.")
c("prophetes","Ibrâhîm et le feu",
  "Que dit Allah au feu qui entoure Ibrâhîm ?",
  "« Ô feu, sois fraîcheur et paix sur Ibrâhîm. » La protection vient d'Allah, pas de la force du serviteur.",
  "Coran, 21:69","Retenir l'image : le feu perd sa nature par l'ordre d'Allah.")
c("prophetes","Le sacrifice",
  "Quel acte d'Ibrâhîm est commémoré chaque année ?",
  "Sa disposition à sacrifier son fils, remplacé par un bélier. La leçon : ce qui compte n'est pas la perte, mais l'obéissance.",
  "Coran, 37:99-107","Écrire une chose que je dois « remettre » symboliquement.")
c("prophetes","Mûsâ et Pharaon",
  "Quelle est la demande de Mûsâ quand Allah l'envoie à Pharaon ?",
  "« Seigneur, élargis ma poitrine, facilite ma tâche, dénoue ma langue. » L'envoyé demande des moyens spirituels avant des moyens matériels.",
  "Coran, 20:25-28","Réciter cette du'â avant une tâche difficile.")
c("prophetes","Mûsâ et le khadir",
  "Quelle leçon sort du récit de Mûsâ et du serviteur d'Allah ?",
  "Que l'on ne comprend pas toujours la sagesse d'un événement sur le moment. Ce qui semble une injustice peut être une protection.",
  "Coran, 18:60-82","Repenser à une épreuve passée dont j'ai compris le sens plus tard.")
c("prophetes","'Îsâ",
  "Que dit le Coran de 'Îsâ ?",
  "Il est un serviteur et un prophète, né sans père par un miracle d'Allah, qui parlait au berceau et guérissait par la permission d'Allah. Il n'est ni dieu ni fils de dieu.",
  "Coran, 3:45-59 ; 19:16-36","Retenir : prophète, pas divinité.")
c("prophetes","Yûsuf",
  "Quelle est la phrase de Yûsuf après l'épreuve ?",
  "« Il n'y a pas de reproche contre vous aujourd'hui. » Après la trahison de ses frères, il choisit le pardon avant la justice qu'il pouvait exercer.",
  "Coran, 12:92","Pardonner une petite chose aujourd'hui, explicitement.")
c("prophetes","Ayyûb",
  "Comment Ayyûb a-t-il réagi à la maladie ?",
  "Il ne s'est pas plaint d'Allah : il s'est plaint à Allah. « Le mal m'a touché, et Tu es le plus miséricordieux. » La plainte à Allah n'est pas la plainte d'Allah.",
  "Coran, 21:83 ; 38:41-44","Distinguer dans ma plainte : à qui je m'adresse ?")
c("prophetes","Le sceau des prophètes",
  "Quel est le statut de Muhammad ﷺ parmi les prophètes ?",
  "Il est le dernier : « Muhammad n'est le père d'aucun de vos hommes, mais il est le Messager d'Allah et le sceau des prophètes. » Aucun prophète après lui.",
  "Coran, 33:40","Retenir : la prophétie est close, la porte de l'innovation est fermée.")
c("prophetes","Le nombre de prophètes",
  "Combien de prophètes le Coran nomme-t-il ?",
  "Vingt-cinq sont nommés, parmi les 124 000 évoqués par la sunna. Ceux qui sont nommés sont des repères, pas la totalité.",
  "Coran, 6:83-86 ; 4:163","En citer au moins dix de mémoire.")

# ─────────────── LES SAVANTS ───────────────
c("savants","Abû Hanîfa",
  "Qui est Abû Hanîfa et quelle est sa particularité ?",
  "Fondateur de l'école hanafite, à Kûfa (80-150 H). Maître du raisonnement analogique (qiyâs) et de la jurisprudence, il refusait les fonctions officielles du pouvoir.",
  "Târîkh Baghdâd ; Ibn 'Abd al-Barr, Al-Intiqâ'","Retenir sa ville : Kûfa.")
c("savants","Mâlik ibn Anas",
  "Quel livre a fondé l'école malikite ?",
  "Al-Muwatta', compilé à Médine (93-179 H). Il y réunit hadiths et pratiques des gens de Médine — la Constitution médinoise du fiqh.",
  "Al-Muwatta' ; Ibn 'Abd al-Barr","Retenir : Médine, al-Muwatta'.")
c("savants","Ash-Shâfi'î",
  "Quelle est la contribution majeure d'ash-Shâfi'î ?",
  "La science des fondements du droit (usûl al-fiqh) avec Ar-Risâla : il fixe les règles d'extraction du droit à partir du Coran, de la sunna, du consensus et de l'analogie. Mort en 204 H.",
  "Ar-Risâla ; Ibn Kathîr","Retenir les quatre sources qu'il hiérarchise.")
c("savants","Ahmad ibn Hanbal",
  "Pourquoi Ahmad est-il un symbole de résistance ?",
  "Il a refusé la thèse officielle du pouvoir califal sur la création du Coran, et a subi la prison et les coups (164-241 H). Il n'a pas plié pour une faveur.",
  "Ibn Kathîr, Al-Bidâya wa-n-Nihâya ; Târîkh Baghdâd","Nommer une position que je tiens même sous pression.")
c("savants","Al-Bukhârî",
  "Que représente le Sahîh d'al-Bukhârî ?",
  "Le recueil de hadiths le plus rigoureux : il y sélectionne ses hadiths parmi des centaines de milliers entendus, avec des chaînes vérifiées. Mort en 256 H.",
  "Sahîh al-Bukhârî ; Târîkh Baghdâd","Retenir : 256 H, le principe de la chaîne vérifiée.")
c("savants","Muslim",
  "Quelle est la singularité du Sahîh de Muslim ?",
  "Il regroupe les différentes versions d'un même hadith sous un seul chapitre, ce qui facilite la comparaison des chaînes. Mort en 261 H.",
  "Sahîh Muslim","Retenir : Muslim = les variantes réunies.")
c("savants","An-Nawawî",
  "Que doit-on à an-Nawawî ?",
  "Les Quarante hadiths, Riyâd as-Sâlihîn et le commentaire de Sahîh Muslim : il rend la sunna utilisable par les non-spécialistes. De Damas, mort en 676 H.",
  "Al-Arba'în an-Nawawiyya ; Riyâd as-Sâlihîn","Lire un hadith des 40 avec son commentaire.")
c("savants","Ibn Taymiyya",
  "Quel est le cœur de la pensée d'Ibn Taymiyya ?",
  "Faire remonter la religion aux textes et au sens des salaf, et refuser les ajouts. Il a écrit sur le tawhîd, la raison et la révélation. Mort en prison à Damas en 728 H.",
  "Al-'Aqîda al-Wâsitiyya ; Dar' Ta'ârud al-'Aql wa-n-Naql","Retenir : la primauté du texte sur la coutume.")
c("savants","Ibn al-Qayyim",
  "Quel est l'apport d'Ibn al-Qayyim ?",
  "Élève d'Ibn Taymiyya, il décrit la foi de l'intérieur : Zâd al-Ma'âd sur la sîra et les adorations, Madârij as-Sâlikîn sur le cœur. Mort en 751 H.",
  "Zâd al-Ma'âd ; Madârij as-Sâlikîn","Lire une page de Zâd al-Ma'âd sur la prière.")
c("savants","Ibn Kathîr",
  "Quel est l'apport principal d'Ibn Kathîr ?",
  "Son Tafsîr, qui rassemble les explications des salaf verset par verset, et sa chronique Al-Bidâya wa-n-Nihâya. Mort en 774 H.",
  "Tafsîr Ibn Kathîr","Lire son commentaire d'un verset court.")
c("savants","Muhammad ibn 'Abd al-Wahhâb",
  "Quels livres a écrit Muhammad ibn 'Abd al-Wahhâb ?",
  "Al-Usûl ath-Thalâtha, Kitâb at-Tawhîd et Nawâqid al-Islâm : des traités courts qui exposent l'unicité par les textes. Mort en 1206 H.",
  "Al-Usûl ath-Thalâtha ; Kitâb at-Tawhîd","Retenir : trois courts traités, pas une doctrine à part.")
c("savants","Al-Albânî",
  "Que doit-on à al-Albânî ?",
  "Le travail d'authentification des hadiths : il a trié le sahîh du faible dans les recueils, et rendu au public l'accès à la valeur réelle des traditions. Mort en 1999.",
  "Silsilat al-Ahâdîth as-Sahîha ; ses annotations","Retenir : vérifier avant de transmettre.")
c("savants","Ibn Bâz et Ibn 'Uthaymîn",
  "Quel rôle ont joué Ibn Bâz et Ibn 'Uthaymîn ?",
  "Ils ont enseigné et commenté les traités de tawhîd pour le grand public : leurs sharh d'al-Usûl ath-Thalâtha et de Kitâb at-Tawhîd sont les portes d'entrée les plus lisibles.",
  "Sharh al-Usûl ath-Thalâtha ; Sharh Kitâb at-Tawhîd","Choisir un sharh et lire l'explication d'un chapitre.")

# ─────────────── PURIFICATION ───────────────
c("tahara","La purification, moitié de la foi",
  "Pourquoi la purification est-elle une condition de la prière ?",
  "Parce que la prière est un face-à-face : on ne s'y présente pas en état d'impureté. Le Prophète ﷺ a dit : « Allah n'accepte pas la prière de celui qui est en état d'impureté jusqu'à ce qu'il se purifie. »",
  "Sahîh al-Bukhârî, n° 135 ; Sahîh Muslim, n° 224","Vérifier l'état de mes ablutions avant chaque prière aujourd'hui.")
c("tahara","Les obligations du wudû'",
  "Quelles parties sont obligatoires dans les ablutions ?",
  "Le visage, les deux mains jusqu'aux coudes, la tête, les deux pieds jusqu'aux chevilles — dans cet ordre, selon le verset.",
  "Coran, 5:6","Faire le wudû' en nommant chaque partie à voix basse.")
c("tahara","Ce qui annule le wudû'",
  "Qu'est-ce qui annule les ablutions ?",
  "Tout ce qui sort des deux voies, le sommeil profond, et la perte de conscience. La base : le hadith « rien ne sort de lui sans qu'il refasse ses ablutions ».",
  "Sahîh al-Bukhârî, n° 135 ; Abû Dâwûd","Identifier ce qui m'arrive le plus souvent et y prêter attention.")
c("tahara","Le ghusl",
  "Quand le ghusl est-il obligatoire ?",
  "Après la relation conjugale, après la fin des menstrues et des lochies, et à l'émission de liquide séminal. Sans ghusl, ni prière ni jeûne ne sont valables.",
  "Coran, 4:43 ; 5:6 ; Sahîh Muslim, n° 315","Retenir : 4 causes, pas de liste approximative.")
c("tahara","Le tayammum",
  "Dans quel cas fait-on le tayammum ?",
  "En l'absence d'eau ou en cas de maladie : on frappe les mains sur une surface pure et on s'essuie le visage et les mains. C'est une facilité légiférée, pas un raccourci.",
  "Coran, 4:43 ; 5:6","Mémoriser les gestes, pour pouvoir les faire sans hésiter.")
c("tahara","Les khuffayn",
  "Quelle est la durée du mas-h sur les chaussettes de cuir ?",
  "Un jour et une nuit pour le résident, trois jours et trois nuits pour le voyageur, à compter du premier mas-h après les ablutions.",
  "Sahîh Muslim, n° 276","Retenir les deux durées.")
c("tahara","Les ablutions avant le sommeil",
  "Que gagne-t-on à faire ses ablutions avant de dormir ?",
  "Le Prophète ﷺ a enseigné de faire le wudû' avant de se coucher, puis de se coucher sur le côté droit, puis de faire du'â — celui qui meurt cette nuit meurt sur la fitra.",
  "Sahîh al-Bukhârî, n° 6311 ; Muslim","Faire le wudû' ce soir avant de dormir.")
c("tahara","Le siwâk",
  "Quelle est la place du siwâk ?",
  "« Si je ne craignais de charger ma communauté, j'aurais ordonné le siwâk à chaque prière. » La propreté de la bouche prépare à la parole de la prière.",
  "Sahîh al-Bukhârî, n° 887 ; Muslim, n° 252","Brosser les dents avant la prière de l'aube.")
c("tahara","Les grandes ablutions du vendredi",
  "Le ghusl du vendredi est-il obligatoire ?",
  "Il est fortement recommandé (ou obligatoire selon certains savants pour les circonstances décrites dans le hadith), et le Prophète ﷺ l'a lié au jour du rassemblement.",
  "Sahîh al-Bukhârî, n° 877 ; Muslim, n° 846","Le prendre soin vendredi avant la prière.")

# ─────────────── PRIÈRE ───────────────
c("salat","La première chose dont on rendra compte",
  "Quel acte est jugé en premier au Jour dernier ?",
  "La prière. « La première chose dont le serviteur rendra compte le Jour de la Résurrection, c'est sa prière. » Si elle est bonne, le reste suit.",
  "Jâmi' at-Tirmidhî, n° 413 ; Sunan an-Nasâ'î","Vérifier mes cinq prières pendant trois jours, sans les enchaîner.")
c("salat","Les cinq prières",
  "Quelles sont les cinq prières et leurs horaires ?",
  "Al-Fajr (aube), adh-Dhuhr (après le zénith), al-'Asr (après-midi), al-Maghrib (coucher), al-'Ishâ' (nuit). Chacune a une fenêtre qui se ferme.",
  "Coran, 17:78 ; Sahîh Muslim, n° 612","Écrire mes horaires de prière pour cette semaine et les afficher.")
c("salat","Les piliers de la prière",
  "Quels sont les piliers (arkân) de la prière ?",
  "La station debout, la takbîra d'entrée, la récitation d'al-Fâtiha, l'inclinaison, le redressement, la prosternation, l'assise entre les deux, la salutation finale, et l'ordre.",
  "Sahîh al-Bukhârî, n° 793 (hadith du mendiant)","Refaire une prière en vérifiant un pilier à la fois.")
c("salat","Le takbîr et l'intention",
  "La prière commence par quoi ?",
  "Par la takbîra « Allâhu akbar », avec l'intention formulée dans le cœur — jamais à voix haute. Le takbîr rend le monde extérieur silencieux.",
  "Sahîh al-Bukhârî, n° 1 ; Sunan at-Tirmidhî","Prier une fois en disant le takbîr très lentement.")
c("salat","La Fatiha",
  "Pourquoi al-Fâtiha est-elle obligatoire dans chaque unité ?",
  "« Celui qui ne récite pas la Fâtiha n'a pas de prière. » C'est le dialogue : la moitié pour Allah, la moitié pour le serviteur.",
  "Sahîh al-Bukhârî, n° 756 ; Sahîh Muslim, n° 394","Réciter la Fâtiha une fois en regardant le sens de chaque verset.")
c("salat","La prière dans le temps",
  "Que faire si je manque une prière ?",
  "On la rattrape dès qu'on se souvient ou qu'on se réveille : « Celui qui oublie une prière ou dort par-dessus, son expiation est de la prier quand il s'en souvient. »",
  "Sahîh Muslim, n° 684","Vérifier : combien de prières ai-je manquées cette semaine ?")
c("salat","Les sunan de la prière",
  "Quelle différence entre pilier et sunna dans la prière ?",
  "Le pilier manquant rend la prière invalide et doit être rattrapé ; la sunna manquante n'invalide pas mais coûte des points, et se compense par la prosternation d'oubli.",
  "Al-Majmû' an-Nawawî ; Ibn 'Uthaymîn, ash-Sharh al-Mumti'","Demander à quelqu'un de vérifier si je fais bien la prosternation d'oubli.")
c("salat","La concentration",
  "Que faire de l'« oubli » de ce qu'on dit pendant la prière ?",
  "Le Prophète ﷺ a recommandé de ne pas se disputer avec soi-même : on a dit « la prière est un moment d'humilité ». La solution est de ralentir, pas de se reprocher.",
  "Coran, 23:1-2 ; Sahîh Muslim, n° 2202","Prier une fois deux fois plus lentement que d'habitude.")
c("salat","La prière du Vendredi",
  "Quel est le statut du vendredi ?",
  "La prière du Jumu'a remplace adh-Dhuhr pour les hommes libres résidents, avec la khutba : le Prophète ﷺ a dit que celui qui la déserte trois fois sans excuse voit son cœur scellé.",
  "Sahîh Muslim, n° 865 ; Abû Dâwûd, n° 1052","Arriver tôt vendredi et écouter la khutba sans téléphone.")
c("salat","Les raisons d'être dispensé de la prière",
  "Qui est dispensé de la prière en communauté ?",
  "La femme en état de menstrues pour sa prière, le malade, etc. — les dispenses sont prévues par le texte, jamais décidées par soi-même.",
  "Sahîh al-Bukhârî, n° 331 ; Muslim, n° 335","Ne pas inventer une dispense sans source.")

# ─────────────── MARIAGE ───────────────
c("mariage","Le mariage est une sunna",
  "Quel est le statut du mariage dans la religion ?",
  "C'est une sunna des prophètes : « Le mariage fait partie de ma sunna ; celui qui ne suit pas ma sunna n'est pas des miens. » Il est un contrat et un acte d'adoration, pas un simple arrangement social.",
  "Sunan Ibn Mâja, n° 1846 (jugé sahîh par al-Albânî)","Relire les finalités du mariage : sérénité (sakîna), descendance, chasteté.")
c("mariage","Les conditions du contrat",
  "Quelles sont les conditions de validité du mariage ?",
  "Le consentement des deux époux, le tuteur (walî) pour la femme, deux témoins justes, et l'absence de tout empêchement légal (parenté, allaitement, religion pour la femme musulmane).",
  "Coran, 4:22-24 ; Ibn 'Uthaymîn, ash-Sharh al-Mumti'","Vérifier, pour un mariage proche, que les conditions sont réunies.")
c("mariage","Le mahr",
  "Qu'est-ce que le mahr, et qui le fixe ?",
  "C'est le don obligatoire offert par le mari à l'épouse, dont elle dispose librement. Il n'a pas de plafond, et le réduire à une formalité le vide de son sens.",
  "Coran, 4:4 ; 4:24","Comprendre : le mahr appartient à la femme, pas à sa famille.")
c("mariage","Le choix du conjoint",
  "Que recommandait le Prophète ﷺ dans le choix d'une épouse ?",
  "« Choisissez pour votre religion » — la femme est épousée pour quatre raisons : ses biens, sa noblesse, sa beauté et sa religion ; privilégie celle qui a la religion.",
  "Sahîh al-Bukhârî, n° 5090 ; Sahîh Muslim, n° 1466","Lister les trois critères que je regarde en premier chez un conjoint.")
c("mariage","La bénédiction du mariage",
  "Quelle est la formule de félicitation ?",
  "« Bârakallâhu laka, wa bâraka 'alayka, wa jama'a baynakumâ fî khayr » — qu'Allah te bénisse, bénissez en lui, et vous réunisse dans le bien.",
  "Sunan Abî Dâwûd, n° 2130 ; at-Tirmidhî","Mémoriser la formule et l'utiliser à un mariage.")
c("mariage","Le bon traitement",
  "Quel hadith établit le critère du bon mari ?",
  "« Le meilleur d'entre vous est le meilleur envers sa famille, et je suis le meilleur d'entre vous envers ma famille. » Le critère se mesure à la maison, pas dehors.",
  "Jâmi' at-Tirmidhî, n° 3895 (hasan sahîh)","Demander à mon épouse un point concret à améliorer.")
c("mariage","La consultation mutuelle",
  "Que dit le Coran de la prise de décision dans le couple ?",
  "« Et délibérez entre vous de bonne manière. » La décision se partage : la consultation (shûrâ) fait partie de la vie du foyer.",
  "Coran, 65:6 ; 2:233","Prendre une décision familiale en demandant l'avis de l'autre avant.")
c("mariage","L'écoute et la parole douce",
  "Que dit le Prophète ﷺ du fait de parler à sa femme ?",
  "Il restait à l'écoute, plaisantait et prenait soin : « Rien n'a été pesé de plus lourd que le bon caractère. » La douceur dans le langage est une adoration.",
  "Jâmi' at-Tirmidhî, n° 2003","Dire aujourd'hui une parole douce à mon épouse, sans raison.")
c("mariage","Le conseil entre époux",
  "Comment corriger un défaut chez son conjoint ?",
  "Par la douceur, à huis clos, sans humilier : le Prophète ﷺ a enseigné l'usage du « si je te conseille c'est par amour ». La correction publique est une violence.",
  "Sahîh Muslim, n° 2593 ; Riyâd as-Sâlihîn, chap. de la douceur","Corriger une chose à la maison, calmement, sans reproche.")
c("mariage","L'équilibre entre les droits",
  "Les droits du mari et de la femme sont-ils identiques ?",
  "Ils sont réciproques mais pas identiques : le mari assure la dépense (nafaqa), la femme garde ses biens ; chacun a des obligations propres. « Les femmes ont des droits équivalents à leurs obligations, conformément à ce qui est convenable. »",
  "Coran, 2:228 ; 4:34","Lister mes obligations concrètes dans le foyer.")

# ─────────────── ÉDUCATION DES ENFANTS ───────────────
c("education","Le premier enseignement",
  "Qu'enseigner en priorité à un enfant ?",
  "La base du tawhîd : « Ô mon fils, ne fais pas d'associé à Allah. » Avant la prière, avant les détails, avant la mémorisation : d'abord à qui l'on appartient.",
  "Coran, 31:13 ; Al-Usûl ath-Thalâtha","Expliquer à un enfant « qui est Allah » avec ses mots.")
c("education","L'ordre de la prière",
  "À quel âge ordonne-t-on la prière à l'enfant ?",
  "À sept ans on l'y ordonne, à dix ans on l'y contraint avec douceur si nécessaire. Le Prophète ﷺ a établi cette progression.",
  "Sunan Abî Dâwûd, n° 495 ; Ahmed","Vérifier l'âge de mes enfants et adapter mon exigence.")
c("education","L'exemple avant la parole",
  "Pourquoi l'exemple est-il plus efficace que le discours ?",
  "Parce que l'enfant apprend par imitation. Le Prophète ﷺ faisait précéder l'ordre par l'exemple, et le Coran dit : « Vous êtes pour les gens un modèle. »",
  "Coran, 2:44 ; Sahîh al-Bukhârî","Faire une prière devant mes enfants sans rien commenter.")
c("education","L'équité entre les enfants",
  "Que dit le Prophète ﷺ du cadeau fait à un seul enfant ?",
  "Il a refusé qu'un père donne un cadeau à un seul enfant sans les autres : « Craignez Allah et soyez justes entre vos enfants. » L'injustice entre enfants laisse des traces longues.",
  "Sahîh al-Bukhârî, n° 2587 ; Muslim, n° 1623","Vérifier si mes cadeaux ou attentions sont équilibrés.")
c("education","Le jeu",
  "Le jeu est-il contraire à l'éducation ?",
  "Non : le Prophète ﷺ a autorisé et encouragé le jeu et la course avec les enfants. Le divertissement encadré fait partie de l'équilibre, comme le temps de l'étude.",
  "Sunan Abî Dâwûd ; Ar-Rahîq al-Makhtûm","Jouer 15 minutes avec un enfant aujourd'hui, sans écran.")
c("education","La responsabilité du parent",
  "Quelle est la responsabilité du parent ?",
  "« Chacun de vous est un berger et responsable de son troupeau. » Le parent ne répond pas seulement de la scolarité : il répond de l'âme qui lui est confiée.",
  "Sahîh al-Bukhârî, n° 893 ; Sahîh Muslim, n° 1829","Écrire une chose que je délègue alors que je devrais la porter.")
c("education","La douceur",
  "Que change la douceur dans l'éducation ?",
  "Le Prophète ﷺ a dit : « La douceur n'est jamais dans une chose sans l'embellir, et n'est jamais retirée d'une chose sans l'enlaidir. » La dureté obtient l'obéissance, jamais l'amour du bien.",
  "Sahîh Muslim, n° 2594","Remplacer une fois la réprimande par une explication.")
c("education","Le choix des amis",
  "Pourquoi surveiller les amis d'un enfant ?",
  "Parce que l'ami façonne le comportement : « L'homme suit la religion de son ami, que chacun regarde qui il fréquente. » Ce n'est pas de la méfiance, c'est de la protection.",
  "Sunan Abî Dâwûd, n° 4833 ; at-Tirmidhî","Connaître le nom des amis de mes enfants cette semaine.")

# ─────────────── ADHKÂR ───────────────
c("adhkar","L'invocation est l'adoration",
  "Quel hadith donne au du'â son statut ?",
  "« L'invocation, c'est l'adoration. » Le Prophète ﷺ désigne le du'â comme l'acte même par lequel on reconnaît Allah — pas un supplément facultatif.",
  "Jâmi' at-Tirmidhî, n° 3372 ; Coran, 40:60","Faire une du'â aujourd'hui, sans demander de bien matériel.")
c("adhkar","Allah est proche",
  "Que dit le Coran de la proximité d'Allah ?",
  "« Et quand Mes serviteurs t'interrogent sur Moi, Je suis tout proche : Je réponds à l'appel de celui qui M'appelle. » Pas d'intermédiaire nécessaire.",
  "Coran, 2:186","Adresser une du'â à voix basse, comme une conversation.")
c("adhkar","L'invocation du matin",
  "Quelle invocation ouvrir la journée ?",
  "« Allâhumma bika asbahnâ, wa bika amsaynâ, wa bika nahyâ, wa bika namût » — c'est par Toi que nous atteignons le matin, le soir, la vie et la mort.",
  "Jâmi' at-Tirmidhî, n° 3391 (hasan)","La dire demain matin, avant le téléphone.")
c("adhkar","Le dhikr du soir",
  "Pourquoi faire un dhikr le soir ?",
  "Pour clore la journée en conscience : « Souvenez-vous de Moi, Je Me souviendrai de vous. » Le souvenir n'est pas un rituel vide, c'est un lien maintenu.",
  "Coran, 2:152 ; Riyâd as-Sâlihîn, chap. du dhikr","Poser un rappel à 20 h pour le dhikr du soir.")
c("adhkar","L'istighfâr",
  "Que fait l'istighfâr dans une vie ?",
  "Il efface et ouvre : « Demandez pardon à Allah, Il vous enverra du ciel des pluies abondantes. » Le pardon ne concerne pas que l'au-delà : il répare aussi ici-bas.",
  "Coran, 71:10-12 ; 11:3","Dire 100 istighfâr aujourd'hui, en comptant.")
c("adhkar","La du'â du voyage",
  "Que dit-on en montant dans un véhicule ?",
  "« Subhâna alladhî sakhkhara lanâ hâdhâ wa mâ kunnâ lahu muqrinîn » — gloire à Celui qui nous l'a soumis, alors que nous n'aurions pu le maîtriser.",
  "Coran, 43:13-14","La réciter au prochain trajet, à voix audible.")
c("adhkar","Les deux rak'ât de la consultation",
  "Que fait-on quand on doit prendre une décision ?",
  "La prière de la consultation (istikhâra) : deux rak'ât puis la du'â enseignée, en demandant à Allah de rendre possible ce qui est bon et d'écarter ce qui ne l'est pas.",
  "Sahîh al-Bukhârî, n° 1166 ; Musnad Ahmad","L'apprendre avant de l'utiliser, pour ne pas la improviser.")
c("adhkar","La du'â pour les parents",
  "Quelle du'â fait-on pour ses parents ?",
  "« Rabbi-rhamhumâ kamâ rabbayânî saghîrâ » — Seigneur, fais-leur miséricorde comme ils m'ont élevé enfant.",
  "Coran, 17:24","La dire aujourd'hui pour son père et sa mère, en citant leurs prénoms.")

# ─────────────── AKHLÂQ ───────────────
c("akhlaq","Ce qui pèse le plus lourd",
  "Quel acte pèsera le plus lourd dans la balance ?",
  "Le bon caractère. Quand on demanda au Prophète ﷺ ce qui fait entrer le plus de gens au Paradis, il répondit : « la crainte d'Allah et le bon caractère ».",
  "Jâmi' at-Tirmidhî, n° 2004","Choisir une qualité à améliorer et la travailler une semaine.")
c("akhlaq","La bonté envers les parents",
  "Quel est le rang des parents dans l'islam ?",
  "Après Allah, l'obéissance aux parents est citée immédiatement : « Et ton Seigneur a décrété que vous n'adoriez que Lui, et la bonté envers les parents. »",
  "Coran, 17:23-24 ; Sahîh al-Bukhârî, n° 5971","Appeler ses parents aujourd'hui, sans autre motif.")
c("akhlaq","Le silence",
  "Quel conseil le Prophète ﷺ donne-t-il sur la parole ?",
  "« Que celui qui croit en Allah et au Jour dernier dise du bien ou se taise. » Le silence n'est pas une faiblesse : c'est une maîtrise.",
  "Sahîh al-Bukhârî, n° 6018 ; Muslim, n° 47","S'abstenir aujourd'hui d'un commentaire inutile.")
c("akhlaq","La mauvaise langue",
  "Qu'est-ce que la ghiba, et pourquoi est-ce si grave ?",
  "Parler de quelqu'un en son absence de ce qu'il déteste. Le Prophète ﷺ a comparé cela à manger la chair de son frère mort, selon l'image du Coran.",
  "Coran, 49:12 ; Sahîh Muslim, n° 2589","Interrompre une conversation qui médit aujourd'hui.")
c("akhlaq","L'honnêteté",
  "Que dit le Prophète ﷺ du mensonge ?",
  "« Le mensonge ne peut être une croyance : le mensonge conduit à la perversité, et la perversité au Feu. » L'honnêteté est une pratique quotidienne, pas une qualité abstraite.",
  "Sahîh al-Bukhârî, n° 6094 ; Muslim, n° 2607","Ne pas arrondir la vérité dans une seule phrase aujourd'hui.")
c("akhlaq","La patience",
  "Que dit le Coran de la sabr ?",
  "« Allah est avec les patients. » La patience n'est pas la résignation, c'est la tenue de l'âme dans l'épreuve et l'action juste qui l'accompagne.",
  "Coran, 2:153 ; Riyâd as-Sâlihîn","Nommer ce qui m'énerve et décider d'une réponse patiente.")
c("akhlaq","L'envie",
  "L'envie est-elle interdite ?",
  "Oui, elle ronge les œuvres comme le feu le bois. Seule exception : envier sans souhaiter la disparition du bien d'autrui, c'est la concurrence dans le bien (ghibta).",
  "Sunan Abî Dâwûd, n° 4903 ; Sahîh al-Bukhârî, n° 5025","Repérer une personne que j'envie et faire du'â pour elle.")
c("akhlaq","La miséricorde",
  "Qui obtient la miséricorde d'Allah ?",
  "Les miséricordieux : « Faites miséricorde à ceux qui sont sur terre, Celui qui est au ciel vous fera miséricorde. » La miséricorde se pratique d'abord dans le concret.",
  "Sunan Abî Dâwûd, n° 4941 ; Jâmi' at-Tirmidhî, n° 1924","Faire une chose miséricordieuse aujourd'hui, même minuscule.")
