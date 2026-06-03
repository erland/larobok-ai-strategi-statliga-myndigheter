# Kapitel 15: Verksamhetsarkitektur för AI

## Varför detta kapitel finns

AI blir snabbt otydligt om det bara beskrivs som teknik. I en myndighet behöver AI förstås i relation till uppdrag, förmågor, processer, information, regelverk, organisation, system och beslut. Det är här verksamhetsarkitekturen blir avgörande.

Verksamhetsarkitektur hjälper myndigheten att se hur olika delar hänger ihop. Den gör det möjligt att beskriva vad som behöver förändras innan någon bestämmer vilken lösning som ska byggas eller köpas. För AI är detta särskilt viktigt eftersom tekniken ofta väcker snabba idéer: en chattbot här, ett beslutsstöd där, en analysmodell i ett befintligt system. Utan arkitektur riskerar myndigheten att skapa isolerade lösningar som är svåra att förvalta, svåra att styra och svåra att koppla till verklig verksamhetsnytta.

För verksamhetsstrategen eller verksamhetsarkitekten är uppgiften att göra AI begripligt som en del av myndighetens utveckling. Det handlar inte om att rita fler modeller än nödvändigt. Det handlar om att skapa en gemensam karta över vad AI ska stödja, vilka förmågor som behöver stärkas, vilken information som krävs, vilka risker som måste hanteras och hur lösningen passar in i den framtida verksamheten.

I den fiktiva Nordiska Tull- och Gränsmyndigheten, NTG, blir detta tydligt när flera AI-initiativ växer fram samtidigt. Ett initiativ handlar om AI-stödd dokumentgranskning i legala flöden. Ett annat handlar om sammanställning av underrättelseunderlag. Ett tredje handlar om riskanalys av transportmönster. Varje initiativ kan se rimligt ut för sig. Men först när de sätts in i en gemensam arkitektur går det att se vilka förmågor, informationsmängder, kontrollpunkter, systemberoenden och styrningsfrågor som återkommer.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara varför verksamhetsarkitektur är central för AI-införande,
- beskriva AI i relation till förmågor, processer, information och system,
- skilja mellan verksamhetsförmåga, lösningsförmåga och teknisk komponent,
- använda målarkitektur för att vägleda AI-initiativ,
- identifiera arkitekturella beroenden och risker i AI-användningsfall,
- beskriva hur AI påverkar informationsarkitektur och beslutsflöden,
- formulera arkitekturprinciper som gör AI mer styrbart och skalbart.

## Innan vi börjar

I tidigare kapitel har vi beskrivit AI-strategi, målbild, governance, risk, möjligheter, prioritering, portfölj, piloter och förändringsledning. Verksamhetsarkitekturen binder ihop dessa delar.

Strategin säger varför myndigheten ska utveckla AI-förmåga. Portföljen visar vilka initiativ som ska drivas. Piloterna prövar vad som fungerar. Förändringsledningen hjälper människor att börja arbeta på nya sätt. Verksamhetsarkitekturen visar hur allt detta passar in i myndighetens helhet.

Tre begrepp är särskilt viktiga:

- **Verksamhetsförmåga** beskriver vad myndigheten behöver kunna göra för att fullgöra sitt uppdrag.
- **Målarkitektur** beskriver en önskad framtida struktur för verksamhet, information, system och styrning.
- **Arkitekturprincip** är en vägledande regel som hjälper myndigheten att fatta konsekventa designbeslut.

Det här kapitlet använder begreppen praktiskt. Målet är inte att göra läsaren till teknisk lösningsarkitekt, utan att stärka förmågan att leda AI-arbete med arkitektonisk tydlighet.

## Verksamhetsarkitekturens roll i AI-arbetet

### AI behöver placeras i myndighetens helhet

Ett vanligt misstag är att börja med frågan: vilken AI-lösning ska vi använda? En bättre första fråga är: vilken del av myndighetens uppdrag behöver stärkas?

För NTG kan AI vara relevant i flera delar av uppdraget:

- i legala flöden där myndigheten vill göra deklarationshantering och dokumentgranskning mer träffsäker,
- i brottsbekämpning där analytiker behöver sammanställa stora mängder underrättelsematerial,
- i kontrollverksamhet där riskbedömningar behöver bli mer konsekventa,
- i ledning och planering där prognoser kan stödja resursfördelning,
- i intern kunskapshantering där medarbetare behöver hitta rätt vägledning snabbare.

Varje område kan beskrivas som ett tekniskt användningsfall, men arkitekturperspektivet gör något annat. Det kopplar användningsfallet till myndighetens förmågor. Då blir frågan inte bara om AI kan lösa en uppgift, utan om AI stärker rätt förmåga på rätt sätt.

En AI-lösning för dokumentgranskning är därför inte bara ett verktyg för att läsa filer. Den kan vara en del av förmågan att hantera legala flöden, upptäcka avvikelser, stödja handläggare och skapa enhetliga bedömningar. Den påverkar också informationshantering, roller, systemintegrationer, kontrollpunkter och ansvar.

### Förmågekartan som startpunkt

En förmågekarta beskriver vad myndigheten behöver kunna göra, oberoende av exakt organisation eller IT-system. För AI-strategiskt arbete är den ett kraftfullt verktyg eftersom den flyttar samtalet från lösningsidéer till verksamhetsbehov.

En förenklad förmågekarta för NTG kan innehålla områden som:

- hantera legala varu- och transportflöden,
- genomföra kontroller,
- bedriva underrättelsearbete,
- utreda brott,
- samverka med andra myndigheter och internationella aktörer,
- ge service och vägledning till företag och allmänhet,
- styra risk, kvalitet och regelefterlevnad,
- analysera information och skapa lägesbilder.

När AI-idéer placeras mot en sådan karta blir det tydligare var myndigheten bygger strategisk förmåga och var den bara inför isolerade verktyg. Om många initiativ hamnar inom analys, riskbedömning och beslutsstöd kan det signalera att myndigheten behöver en samlad AI-stödd analysförmåga, inte bara flera separata projekt.

Förmågekartan hjälper också ledningen att prioritera. Ett användningsfall kan vara tekniskt intressant men ligga långt från prioriterade förmågor. Ett annat kan vara mindre spektakulärt men stärka en kritisk förmåga med hög verksamhetsnytta.

### Processer visar var AI faktiskt möter arbetet

Förmågor visar vad myndigheten behöver kunna göra. Processer visar hur arbetet faktiskt går till. Båda behövs.

AI påverkar ofta konkreta arbetsflöden: en handläggare får ett förslag, en analytiker får en sammanställning, en chef får en prognos, en kontrollgrupp får en riskindikator. Därför måste verksamhetsarkitekturen visa var i processen AI används och vad som händer före och efter.

I NTG:s legala flöden kan en förenklad process se ut så här:

1. En deklaration eller handling kommer in.
2. Systemet gör grundläggande validering.
3. Ärendet klassificeras eller riskbedöms.
4. En handläggare granskar underlaget.
5. Komplettering begärs eller beslut fattas.
6. Ärendet dokumenteras och följs upp.

Om AI ska stödja dokumentgranskning behöver arkitekten beskriva exakt var stödet ligger. Ska AI sammanfatta handlingar innan handläggaren börjar? Ska AI föreslå avvikelser? Ska AI jämföra uppgifter mot tidigare ärenden? Ska AI bara användas som kunskapsstöd? Varje val påverkar ansvar, dokumentation och kontroll.

I brottsbekämpande arbete blir processfrågan ännu känsligare. Om AI används för att sammanställa underrättelsematerial måste det vara tydligt vad som är maskinell sammanställning, vad som är analytikerns bedömning och vad som kan ligga till grund för vidare åtgärder. Arkitekturen behöver därför synliggöra både informationsflödet och beslutsflödet.

### Informationsarkitektur är en grundförutsättning

AI är beroende av information. Det gäller både generativ AI, prediktiv AI och mer traditionella analysmodeller. Därför är informationsarkitektur en av de viktigaste delarna av AI-införande.

För en myndighet handlar informationsarkitektur inte bara om dataformat. Det handlar om:

- vilka informationsmängder som finns,
- vem som ansvarar för dem,
- vilken kvalitet de har,
- vilka rättsliga begränsningar som gäller,
- vilka säkerhetsklasser och skyddsvärden de har,
- hur länge information får sparas,
- vilka begrepp och definitioner som används,
- hur information får kombineras.

AI-projekt underskattar ofta detta. Man antar att informationen finns och är användbar. I praktiken kan samma begrepp betyda olika saker i olika delar av myndigheten. Ett "ärende", en "kontroll", en "avvikelse" eller en "riskindikator" kan ha olika betydelser beroende på process, system och rättslig kontext.

För NTG kan ett AI-initiativ som analyserar transportflöden behöva information från deklarationer, historiska kontroller, underrättelseuppslag, beslag, transportdata och internationellt informationsutbyte. Arkitekturfrågan blir då inte bara hur dessa datamängder tekniskt kopplas samman. Frågan är om myndigheten har rätt att använda dem tillsammans, om begreppen betyder samma sak, om kvaliteten räcker och om resultatet kan förklaras.

En verksamhetsarkitekt behöver därför driva informationsfrågor tidigt. Annars riskerar AI-initiativet att bli en teknisk prototyp som inte kan tas i bruk.

### Beslutsflöden måste beskrivas tydligt

AI i myndigheter hamnar ofta nära beslut. Det kan vara formella myndighetsbeslut, operativa prioriteringar, riskbedömningar, kontrollurval eller rekommendationer till handläggare. Verksamhetsarkitekturen måste därför visa hur beslut påverkas.

En enkel men viktig distinktion är mellan:

- AI som ger information,
- AI som ger förslag,
- AI som prioriterar,
- AI som rekommenderar åtgärd,
- AI som automatiserar ett moment.

Ju närmare AI kommer ett beslut, desto större krav ställs på spårbarhet, förklarbarhet, mänsklig kontroll, dokumentation och rättslig analys.

För NTG kan ett AI-stöd som sammanfattar en lång vägledning till en handläggare vara relativt avgränsat. Ett AI-stöd som föreslår vilka transporter som bör kontrolleras får större verksamhetsmässig och rättslig betydelse. Ett stöd som påverkar brottsbekämpande prioriteringar kräver ännu tydligare styrning.

Arkitekturmodellen bör därför visa beslutspunkter. Den bör också visa vem som fattar beslut, vilket underlag som används, hur AI-resultatet märks upp, hur avvikelser hanteras och hur uppföljning sker.

### Målarkitektur ger riktning över flera initiativ

En målarkitektur är inte en detaljerad ritning över varje framtida system. Den är en sammanhängande beskrivning av hur myndigheten vill att verksamhet, information, teknik och styrning ska fungera på sikt.

För AI kan målarkitekturen svara på frågor som:

- Vilka verksamhetsförmågor ska AI främst stärka?
- Vilka gemensamma informationsresurser behövs?
- Vilka AI-komponenter ska vara gemensamma och vilka ska vara lokala?
- Hur ska AI-lösningar kopplas till ärendehantering, analysmiljöer och kunskapsstöd?
- Hur ska loggning, uppföljning och kvalitetssäkring fungera?
- Vilka beslut ska alltid ha mänsklig kontroll?
- Vilka krav gäller för leverantörer, modeller och integrationer?

Utan målarkitektur blir varje initiativ tvunget att lösa dessa frågor själv. Det leder ofta till dubblering, olika säkerhetslösningar, olika begrepp, olika uppföljning och otydligt ansvar.

För NTG kan målarkitekturen exempelvis ange att AI-stöd för känsliga processer ska använda gemensamma principer för åtkomst, loggning, informationsklassning och mänsklig kontroll. Den kan också ange att återanvändbara komponenter för dokumentanalys, textsammanfattning och kvalitetssäkring ska prioriteras framför helt separata lösningar i varje verksamhetsgren.

### Arkitekturprinciper gör AI-arbetet mer konsekvent

Arkitekturprinciper hjälper myndigheten att fatta konsekventa beslut när detaljerna varierar. De ska vara tillräckligt konkreta för att kunna vägleda prioritering och design.

Exempel på AI-relevanta arkitekturprinciper för NTG kan vara:

- AI ska kopplas till prioriterade verksamhetsförmågor, inte införas som fristående teknikexperiment.
- AI-resultat som påverkar myndighetsutövning eller brottsbekämpande prioriteringar ska vara spårbara och kunna granskas.
- Mänskligt ansvar ska vara tydligt i alla processer där AI stödjer bedömningar.
- Informationsanvändning ska vara rättsligt förankrad innan teknisk lösning byggs.
- Gemensamma komponenter ska återanvändas när flera initiativ har liknande behov.
- Begrepp, metadata och klassningar ska harmoniseras innan information kombineras över processgränser.
- AI-lösningar ska designas för uppföljning, inte bara för införande.

Sådana principer är inte bara arkitekturdokument. De kan användas i portföljstyrning, prioriteringsmöten, upphandling, designgranskning och pilotutvärdering.

### Arkitektur hjälper till att upptäcka beroenden

AI-initiativ kan se små ut men ha stora beroenden. Ett pilotteam kan exempelvis vilja bygga ett stöd för att sammanfatta ärenden. Snart visar det sig att stödet kräver åtkomst till flera ärendesystem, enhetliga dokumenttyper, informationsklassning, loggning, användarhantering, beslut om lagring av prompts och svar, utbildning av handläggare och stöd för kvalitetssäkring.

Arkitekturens uppgift är inte att stoppa initiativet. Uppgiften är att synliggöra beroendena så tidigt att de kan hanteras.

För verksamhetsstrategen eller verksamhetsarkitekten är detta en central roll. När ledningen frågar varför ett AI-initiativ inte bara kan "testas snabbt" kan arkitekten förklara skillnaden mellan en avgränsad demonstration och en lösning som kan användas ansvarsfullt i myndighetens verksamhet.

Det betyder inte att allt måste lösas från början. Men det betyder att myndigheten behöver veta vilka beroenden som medvetet skjuts upp och vilka som måste hanteras redan i pilotfasen.

## Exempel: NTG bygger en målarkitektur för AI-stödd analys

NTG har efter flera piloter sett att många AI-idéer kretsar kring analys och sammanställning. Det gäller både legala flöden och brottsbekämpande arbete. Ledningen ber därför verksamhetsarkitekturfunktionen att ta fram en första målarkitektur för AI-stödd analys.

Arbetet börjar inte med teknikval. Det börjar med fyra frågor:

1. Vilka förmågor ska stärkas?
2. Vilken information behövs?
3. Vilka beslut eller bedömningar påverkas?
4. Vilken styrning krävs för att lösningarna ska kunna användas säkert?

Arkitekterna identifierar tre prioriterade förmågor: riskanalys, dokumentanalys och underrättelsesammanställning. De ser att alla tre behöver gemensamma lösningar för informationsklassning, åtkomststyrning, loggning och kvalitetssäkring. De ser också att användningen skiljer sig åt. Dokumentanalys i legala flöden kan ofta användas som handläggarstöd. Underrättelsesammanställning kräver striktare hantering av källor, skyddsvärden och analytikerns ansvar.

Resultatet blir en målarkitektur med tre nivåer:

- en verksamhetsnivå som visar förmågor, processer och beslutspunkter,
- en informationsnivå som visar centrala informationsmängder, begrepp, klassningar och ansvar,
- en lösningsnivå som visar återanvändbara AI-komponenter, integrationer och kontrollfunktioner.

NTG använder sedan målarkitekturen för att granska nya AI-initiativ. Ett nytt initiativ behöver inte passa perfekt från början, men det måste kunna förklara hur det förhåller sig till målarkitekturen. På så sätt blir arkitekturen ett praktiskt styrmedel och inte bara ett dokument.

## Vanliga misstag

- **Misstag: Att beskriva AI som en systemfråga i stället för en verksamhetsfråga.**
  - Varför det händer: Tekniken är synlig och lockar till snabba lösningsdiskussioner.
  - Hur du undviker det: Börja med förmåga, process, information och beslut innan du beskriver systemkomponenter.

- **Misstag: Att varje AI-initiativ får skapa sin egen arkitektur.**
  - Varför det händer: Piloter drivs ofta snabbt och lokalt.
  - Hur du undviker det: Skapa tidigt gemensamma principer för information, loggning, kvalitetssäkring och mänsklig kontroll.

- **Misstag: Att underskatta informationsarkitekturen.**
  - Varför det händer: Det är lätt att anta att data redan finns och kan användas.
  - Hur du undviker det: Kartlägg informationsmängder, begrepp, ägarskap, kvalitet, rättsliga villkor och skyddsvärden innan lösningen designas.

- **Misstag: Att målarkitekturen blir för detaljerad för tidigt.**
  - Varför det händer: Arkitekturarbete kan dras mot fullständighet.
  - Hur du undviker det: Börja med en tillräcklig målbild som kan vägleda beslut, och fördjupa den i takt med portföljen.

- **Misstag: Att inte beskriva beslutspunkter.**
  - Varför det händer: Processkartor fokuserar ofta på aktiviteter och system.
  - Hur du undviker det: Markera var bedömningar, prioriteringar, rekommendationer och formella beslut sker, och visa hur AI påverkar dem.

## Praktiska arbetsfrågor

När du arbetar med verksamhetsarkitektur för AI kan du använda följande frågor som stöd:

1. Vilken verksamhetsförmåga ska AI stärka?
2. Vilken process eller vilket arbetsflöde påverkas?
3. Vilken information används, skapas eller förändras?
4. Vilka begrepp behöver definieras gemensamt?
5. Vilka beslutspunkter påverkas?
6. Vem ansvarar för bedömning, kontroll och uppföljning?
7. Vilka system eller plattformar berörs?
8. Vilka gemensamma komponenter kan återanvändas?
9. Vilka risker uppstår om lösningen skalas?
10. Hur passar initiativet in i målarkitekturen?

Frågorna är enkla, men de förändrar samtalet. De gör det svårare att behandla AI som en isolerad teknikidé och lättare att se vad som krävs för att skapa en hållbar verksamhetsförmåga.

## Arkitekturprinciper för AI
Verksamhetsarkitekturkapitlet behöver särskilt hjälpa läsaren att omvandla strategi till strukturer som går att använda. Ett praktiskt verktyg är arkitekturprinciper för AI. De bör vara få, begripliga och möjliga att använda i både prioritering, design och granskning.

Exempel på principer för NTG:

- AI ska kopplas till en identifierad verksamhetsförmåga.
- AI-lösningar ska ha en utsedd verksamhetsägare.
- Data och informationskällor ska vara beskrivna innan pilot startar.
- Mänsklig kontroll ska utformas utifrån processens risk och konsekvens.
- Lösningar som påverkar rättigheter, skyldigheter eller ingripande åtgärder ska ha förstärkt spårbarhet.
- Återanvändbara komponenter och gemensamma plattformar ska prioriteras framför isolerade lösningar när det är möjligt.

Sådana principer hjälper arkitekten att hålla ihop målbild, lösningsdesign och styrning. De gör också dialogen med utvecklingsteam mer konkret, eftersom teamen får tydliga ramar utan att varje detalj behöver beslutas centralt.

## Arkitekturmognad för AI

Verksamhetsarkitekturens bidrag till AI ökar i takt med att myndigheten går från experiment till samlad förmåga. En enkel mognadsmodell kan användas för att se vilken roll arkitekturen spelar i nuläget:

| Nivå | Arkitekturmognad | Arkitekturens roll |
|---|---|---|
| 1. Osynlig | AI-initiativ drivs utan tydlig koppling till förmågor, processer och information | Arkitekturen blir reaktiv eller saknas helt |
| 2. Beskrivande | Arkitekturen dokumenterar nuläge och vissa beroenden | Initiativ får bättre överblick men styrs fortfarande separat |
| 3. Vägledande | Förmågekartor, informationsmodeller och principer används i prioritering | Arkitekturen påverkar vägval innan lösningar låses |
| 4. Styrande | Målarkitektur och referensarkitektur används för portfölj, finansiering och skalning | Återanvändning och långsiktig förvaltning stärks |
| 5. Lärande | Arkitekturen utvecklas genom uppföljning av nytta, risk, data och användning | Myndigheten justerar förmågor och principer över tid |

Denna modell hjälper verksamhetsarkitekten att undvika två ytterligheter. Den ena är att arkitektur blir en efterhandsdokumentation av tekniska lösningar. Den andra är att arkitektur blir så tung att den bromsar all utveckling. I en AI-mogen myndighet används arkitektur som ett praktiskt beslutsstöd: tillräckligt konkret för att påverka prioriteringar, men tillräckligt flexibel för att rymma lärande.

Vid NTG kan arkitekturmognaden exempelvis bedömas separat för legala flöden, underrättelseanalys och utredningsstöd. Det kan visa att vissa förmågeområden har tydliga processer och informationsmodeller, medan andra kräver mer grundarbete innan AI kan skalas ansvarsfullt.

## Snabb sammanfattning

- AI behöver beskrivas som en del av myndighetens verksamhet, inte bara som teknik.
- Förmågekartor hjälper myndigheten att koppla AI till uppdrag och strategiska prioriteringar.
- Processkartor visar var AI faktiskt möter handläggare, analytiker, chefer och andra användare.
- Informationsarkitektur är en grundförutsättning för ansvarsfull AI.
- Beslutsflöden måste synliggöra hur AI påverkar bedömningar, prioriteringar och myndighetsutövning.
- Målarkitektur ger riktning över flera AI-initiativ och minskar risken för isolerade lösningar.
- Arkitekturprinciper gör AI-arbetet mer konsekvent och styrbart.
- Verksamhetsarkitektens roll är att göra beroenden, ansvar och vägval synliga innan lösningar låses.

## Reflektionsfrågor

1. Vilka verksamhetsförmågor i din myndighet skulle tydligast kunna stärkas av AI?
2. Finns det AI-idéer som i dag diskuteras som tekniska lösningar, men som egentligen borde beskrivas som förmågeutveckling?
3. Vilka informationsmängder skulle vara mest kritiska för AI i din verksamhet?
4. Var i era processer skulle AI kunna påverka bedömningar eller prioriteringar?
5. Vilka arkitekturprinciper skulle behövas för att undvika isolerade AI-lösningar?
6. Hur skulle en första målarkitektur för AI kunna användas i portföljstyrning och ledningsdialog?

## Nästa steg

I nästa kapitel går vi vidare från arkitektur till skalning och operativisering. När målbild, governance, portfölj, piloter, förändringsledning och arkitektur finns på plats uppstår nästa fråga: hur går myndigheten från enskilda initiativ till en fungerande operativ AI-förmåga?

Där blir fokus på arbetssätt, förvaltning, ansvar, plattformar, uppföljning och kontinuerlig förbättring.

## Förmågekartor för AI-mogna myndigheter

En förmågekarta (Capability Map) hjälper myndigheten att beskriva vad organisationen måste kunna göra oberoende av organisation, system eller teknik. För AI-arbetet är detta ofta ett mer stabilt perspektiv än processkartor eftersom förmågor förändras långsammare än arbetssätt och tekniska lösningar.

I den fiktiva Nordiska Tull- och Gränsmyndigheten kan exempelvis följande AI-relaterade förmågor identifieras:

- Riskanalys och underrättelsebearbetning
- Kunskapsstöd för handläggare och utredare
- Informationsförvaltning och datastyrning
- Automatiserad dokumentanalys
- AI-governance och modellstyrning
- Kontinuerlig uppföljning av AI-nytta

## Informationsarkitektur för AI

AI är beroende av information av tillräcklig kvalitet. Därför behöver verksamhetsarkitekten förstå informationsdomäner, informationsägarskap och informationsflöden.

- Vilka informationsmängder används av AI-lösningen?
- Vem ansvarar för informationskvaliteten?
- Hur klassificeras informationen?
- Vilka juridiska begränsningar finns?
- Hur kan information delas mellan verksamhetsområden?

## Referensarkitektur för AI i offentlig sektor

En typisk referensarkitektur omfattar informationskällor, integrationslager, dataplattformar, AI-tjänster, verksamhetssystem samt styrnings- och säkerhetskomponenter. Syftet är att skapa återanvändbarhet och långsiktig förvaltbarhet.

## Arkitektens roll i AI-portföljstyrning

Verksamhetsarkitekten bör delta aktivt i prioritering och uppföljning av AI-initiativ. Bedömningar bör omfatta arkitekturpåverkan, beroenden, informationskrav, förvaltningskonsekvenser och skalbarhet.
