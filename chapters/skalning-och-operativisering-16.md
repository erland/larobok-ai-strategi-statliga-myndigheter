# Kapitel 16: Skalning och operativisering

## Varför detta kapitel finns

Många AI-satsningar börjar som en pilot, ett experiment eller ett avgränsat utvecklingsinitiativ. Det är ofta nödvändigt. En myndighet behöver kunna prova, lära, minska osäkerhet och bygga förtroende innan den förändrar ordinarie verksamhet. Men om AI-arbetet stannar i pilotform skapas sällan bestående verksamhetsnytta.

Det här kapitlet handlar om steget efter piloten: hur AI kan skalas och operativiseras så att det blir en del av myndighetens verkliga förmåga. För en verksamhetsstrateg eller verksamhetsarkitekt är detta ett avgörande perspektiv. Det räcker inte att visa att en AI-lösning fungerar tekniskt. Den måste också få en plats i arbetssätt, ansvar, styrning, informationshantering, uppföljning, kompetensförsörjning och långsiktig förvaltning.

I Nordiska Tull- och Gränsmyndigheten, NTG, har flera AI-piloter nu visat lovande resultat. En pilot har prövat generativ AI som stöd för att sammanfatta långa regelverk och interna vägledningar. En annan har testat prediktiv riskanalys för att identifiera avvikande varuflöden. En tredje har undersökt hur underrättelseanalytiker kan få stöd i att sammanställa stora mängder textmaterial. Frågan är inte längre bara om AI kan skapa nytta. Frågan är hur myndigheten går från lovande försök till stabil, ansvarsfull och skalbar användning.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara skillnaden mellan pilot, produkt, tjänst och verksamhetsförmåga,
- beskriva vad som krävs för att skala AI på ett ansvarsfullt sätt,
- identifiera vanliga hinder när AI ska införas i ordinarie verksamhet,
- formulera en operativ modell för AI-lösningar,
- beskriva hur förvaltning, uppföljning och kontinuerlig förbättring bör organiseras,
- hjälpa ledningen att förstå varför skalning kräver mer än teknik.

## Från pilot till verksamhetsförmåga

En pilot är ett kontrollerat försök. Den ska svara på frågor som ännu inte är tillräckligt säkra: fungerar tekniken, finns data, är nyttan rimlig, går riskerna att hantera och accepterar användarna lösningen? En verksamhetsförmåga är något annat. Den innebär att myndigheten återkommande kan utföra ett arbete med tillräcklig kvalitet, ansvar, resurser och styrning.

Skillnaden är viktig. En pilot kan drivas av ett litet engagerat team. En förmåga kräver organisatorisk uthållighet. En pilot kan acceptera manuella speciallösningar. En förmåga behöver stabila processer. En pilot kan leva på särskilt intresse. En förmåga måste fungera även när nyckelpersoner byter roll, när ärendetrycket ökar och när regler eller datakällor förändras.

För NTG innebär detta att riskanalysmodellen för varuflöden inte bara ska ge intressanta träffar i en testmiljö. Den måste kunna användas i verkliga kontrollflöden. Den måste passa in i prioriteringsprocessen, ge begripligt stöd till handläggare, hantera felaktiga signaler, följas upp av ansvariga chefer och vara möjlig att justera när nya smugglingstrender uppstår.

En bra fråga för verksamhetsstrategen är därför:

> Vad måste vara sant för att den här AI-lösningen ska fungera som en stabil del av myndighetens uppdrag, inte bara som ett lyckat projekt?

## Fyra nivåer av skalning

Skalning kan betyda olika saker. Om begreppet används slarvigt kan ledning, utveckling och verksamhet prata förbi varandra. I praktiken finns minst fyra nivåer.

### Teknisk skalning

Teknisk skalning handlar om att lösningen kan hantera fler användare, större datamängder, fler transaktioner eller högre tillgänglighetskrav. Det kan handla om driftmiljö, integrationer, prestanda, säkerhet, loggning, behörigheter och övervakning.

För AI-lösningar tillkommer ofta frågor om modelluppdatering, promptförvaltning, dataflöden, mätning av kvalitet och hantering av förändrad datakaraktär över tid. En modell som fungerade väl under piloten kan prestera sämre när den möter nya typer av ärenden eller när användningen breddas.

### Verksamhetsmässig skalning

Verksamhetsmässig skalning handlar om att lösningen fungerar i fler delar av organisationen eller i fler arbetsmoment. Det innebär ofta att processer, roller, instruktioner, beslutsvägar och utbildningsmaterial behöver anpassas.

I NTG kan ett stöd för dokumentgranskning först användas av en mindre grupp specialister. När det sedan sprids till fler regioner och enheter uppstår nya frågor. Har alla samma begrepp och arbetssätt? Ska stödet användas före eller efter manuell granskning? Vem får ändra instruktionerna? Hur hanteras avvikelser? Hur dokumenteras användningen?

### Styrningsmässig skalning

Styrningsmässig skalning handlar om beslut, ansvar och uppföljning. När AI används i större skala ökar behovet av tydliga mandat. Det måste framgå vem som äger lösningen, vem som ansvarar för risker, vem som beslutar om förändringar och hur ledningen följer upp nytta och oönskade effekter.

Utan styrningsmässig skalning riskerar myndigheten att få många lokala AI-lösningar som saknar gemensamma principer. Det kan skapa dubbelarbete, säkerhetsrisker, oklar rättslig grund och svårigheter att förklara verksamhetens samlade AI-användning.

### Kulturell och kompetensmässig skalning

Kulturell skalning handlar om att användningen av AI blir begriplig, accepterad och ansvarsfull i vardagen. Medarbetare behöver veta när AI-stöd är lämpligt, när det inte är lämpligt och vilket mänskligt ansvar som alltid kvarstår. Chefer behöver kunna leda en verksamhet där vissa arbetsmoment stöds av AI utan att förlora kontroll över kvalitet, rättssäkerhet eller arbetsmiljö.

För NTG kan detta vara särskilt viktigt i brottsbekämpande delar. AI-stöd i underrättelsearbete får inte skapa en kultur där sannolikhet behandlas som bevis eller där automatiska sammanställningar ersätter professionell bedömning. Det måste finnas ett moget språk för osäkerhet, källkritik och ansvar.

## Operativisering: att göra AI användbar i vardagen

Operativisering betyder att AI-lösningen får en konkret plats i myndighetens löpande arbete. Det är här mycket av värdet realiseras, men också här många problem blir synliga.

En AI-lösning är inte operativiserad bara för att den är tillgänglig i ett system. Den är operativiserad när den används i ett definierat arbetsflöde, med tydliga roller, kända begränsningar, utbildade användare, uppföljning och förvaltning.

För verksamhetsarkitekten är operativisering nära kopplat till målarkitektur och förmågekartor. Frågan är hur AI-lösningen förändrar relationen mellan människor, processer, information, regler och teknik.

Ett enkelt operativiseringsunderlag kan innehålla:

- vilket arbetsmoment AI-stödet ska stödja,
- vilka användargrupper som berörs,
- vilket beslut eller vilken bedömning stödet påverkar,
- vilken information stödet använder,
- vilka risker och begränsningar som finns,
- hur användaren ska agera vid låg tillit till resultatet,
- hur användningen dokumenteras,
- vem som följer upp kvalitet och nytta,
- hur ändringar i lösningen beslutas.

Detta är inte bara administration. Det är grunden för att AI-stöd ska bli möjligt att förstå, styra och försvara.

## Exempel: NTG skalar ett stöd för underrättelsesammanställning

NTG har genomfört en pilot där underrättelseanalytiker använder generativ AI för att sammanfatta stora mängder öppna källor, interna rapporter och historiska ärenden. Piloten visar att analytikerna snabbare kan få en första överblick över materialet. Samtidigt visar piloten flera begränsningar: AI-stödet kan missa sammanhang, blanda ihop liknande aktörer och formulera preliminära samband med för stor säkerhet.

Ledningen vill nu skala lösningen. Verksamhetsstrategen föreslår att frågan inte ska behandlas som ett enkelt utrullningsbeslut. I stället delas skalningen upp i fem steg.

### Steg 1: Tydliggör användningsområdet

AI-stödet ska inte användas för att dra slutsatser om skuld, fatta beslut om tvångsmedel eller ersätta analytisk bedömning. Det ska användas för första sortering, sammanfattning, jämförelse av material och stöd vid hypotesformulering.

Detta minskar risken för att lösningen ges för stort mandat.

### Steg 2: Definiera mänskligt ansvar

Analytikern ansvarar alltid för slutsatser, källkritik och vidare användning. AI-genererade sammanfattningar får inte användas i externa underlag utan granskning. Om stödet används för att skapa en preliminär lägesbild ska detta framgå.

Här blir principen om human oversight konkret. Den beskrivs inte bara i en policy, utan översätts till arbetssätt.

### Steg 3: Etablera informationsregler

NTG beslutar vilka typer av material som får behandlas i lösningen, vilka som kräver särskild hantering och vilka som inte får användas. Behörigheter kopplas till uppdrag och skyddsvärde. Loggning och spårbarhet införs.

Detta är avgörande eftersom underrättelsearbete ofta hanterar känslig information.

### Steg 4: Skapa uppföljning

NTG följer upp både nytta och risk. Nytta mäts exempelvis genom minskad tid för första sammanställning, bättre spårbarhet i källhantering och användarnas upplevda stöd. Risk följs upp genom felklassificeringar, överdriven tillit, brister i källhänvisning och incidenter.

Uppföljningen används inte bara för rapportering till ledningen. Den används för att förbättra instruktioner, promptar, utbildning och teknisk konfiguration.

### Steg 5: Besluta om förvaltningsansvar

AI-stödet får en verksamhetsägare, en teknisk förvaltningsansvarig och en informationsägare. En tvärfunktionell förvaltningsgrupp hanterar förändringsförslag, incidenter, uppföljning och behov av ny riskbedömning.

Därmed går lösningen från projekt till kontrollerad verksamhetskomponent.

## Den operativa modellen

När flera AI-lösningar ska skalas behöver myndigheten en operativ modell. Den beskriver hur AI används, styrs, förvaltas och förbättras i vardagen.

En operativ modell för AI bör minst besvara sex frågor.

### Vem äger användningen?

Varje AI-lösning behöver en tydlig verksamhetsägare. Det är den funktion som ansvarar för att lösningen har ett legitimt syfte, skapar nytta och används enligt beslutade ramar. Ägarskapet kan inte ligga enbart hos IT eller utveckling, eftersom AI-lösningen påverkar verksamhetsbedömningar, arbetssätt och ansvar.

### Vem äger informationen?

AI är beroende av information. Informationsägarskapet behöver därför vara tydligt. Vilka datakällor används? Vilken kvalitet har de? Vilka skyddskrav gäller? Vem beslutar om nya datakällor får kopplas på? Vem ansvarar när informationen ändrar karaktär?

För en tull- och gränsmyndighet är detta särskilt viktigt eftersom samma lösning kan beröra administrativa uppgifter, företagsinformation, underrättelsematerial och personuppgifter.

### Vem ansvarar för teknisk drift och säkerhet?

AI-lösningen behöver övervakas tekniskt. Det handlar om tillgänglighet, säkerhetsuppdateringar, integrationer, loggning, åtkomststyrning och incidenthantering. För generativa AI-lösningar kan det även handla om modellversioner, leverantörsberoenden och förändringar i underliggande tjänster.

### Vem följer upp kvalitet?

AI-kvalitet är inte statisk. En lösning kan bli sämre när omvärlden förändras, när användarna ändrar beteende eller när nya datamönster uppstår. Därför behövs en funktion som följer upp träffsäkerhet, fel, användarbeteenden och konsekvenser.

Kvalitetsuppföljning bör göras både tekniskt och verksamhetsmässigt. Det räcker inte att modellen ger statistiskt bra resultat om den samtidigt leder till dåliga prioriteringar i praktiken.

### Vem beslutar om förändringar?

AI-lösningar förändras över tid. Nya datakällor, justerade modeller, ändrade promptar eller nya användargrupper kan förändra riskbilden. Därför behöver det finnas en förändringsprocess. Vissa ändringar kan hanteras inom förvaltningen. Andra kräver ny riskbedömning, juridisk granskning eller ledningsbeslut.

### Hur avvecklas lösningen?

Operativisering handlar också om att kunna sluta använda en lösning. Om nyttan uteblir, riskerna blir för stora eller bättre alternativ finns, måste myndigheten kunna avveckla AI-stöd på ett kontrollerat sätt. Det kräver dokumentation, beslut, kommunikation och ibland migrering av information eller arbetssätt.

## Vanliga hinder vid skalning

AI-skalning misslyckas sällan av en enda orsak. Ofta handlar det om flera små glapp mellan strategi, teknik och verksamhet.

### Oklart ägarskap

När ingen tydligt äger lösningen efter piloten faller ansvaret mellan stolarna. Projektteamet går vidare, IT ansvarar bara för drift och verksamheten antar att någon annan följer upp effekterna. Resultatet blir att lösningen antingen inte används eller används utan tillräcklig styrning.

### För tidig utrullning

Ett vanligt misstag är att en pilot bedöms som lyckad för snabbt. Det kan bero på entusiasm, ledningstryck eller vilja att visa resultat. Men om användningsområdet, riskerna och förvaltningen inte är klara kan en snabb utrullning skapa mer skada än nytta.

### För smal nyttomätning

Om nyttan bara mäts som tidsbesparing kan viktiga effekter missas. AI kan också påverka kvalitet, likvärdighet, arbetsmiljö, rättssäkerhet, transparens och förtroende. Vissa nyttor uppstår först när arbetssätt förändras, inte när verktyget införs.

### Bristande kompetensspridning

En pilot kan fungera eftersom den drivs av särskilt kunniga personer. När lösningen sprids till fler användare behöver utbildning, stödmaterial och chefskap följa med. Annars uppstår ojämn användning, missförstånd och överdriven tillit till systemets resultat.

### Ingen plan för kontinuerlig förbättring

AI kräver lärande. Om myndigheten saknar process för återkoppling, uppdatering och förbättring riskerar lösningen att stagnera. Det som var relevant vid införandet kan bli fel när regler, hotbilder, flöden eller arbetsformer förändras.

## Verksamhetsstrategens roll i skalningen

Verksamhetsstrategen behöver hjälpa ledningen att se skalning som en styrningsfråga, inte bara som en utrullningsfråga. Det innebär att formulera rätt beslutsunderlag.

Ett bra beslutsunderlag inför skalning bör inte bara fråga om lösningen fungerar. Det bör fråga:

- vilken verksamhetsförmåga lösningen stärker,
- vilka användargrupper och processer som påverkas,
- vilka risker som förändras vid bredare användning,
- vilket ägarskap och vilken förvaltning som krävs,
- hur nyttan ska följas upp,
- vilka beroenden som finns till data, teknik, juridik och kompetens,
- vilken takt som är lämplig för införandet.

Verksamhetsstrategen kan också hjälpa till att undvika två ytterligheter. Den ena ytterligheten är att myndigheten skalar för snabbt, utan kontroll. Den andra är att myndigheten aldrig vågar lämna pilotstadiet. Den mogna vägen ligger mellan dessa: kontrollerad, lärande och stegvis skalning.

## Verksamhetsarkitektens roll i operativiseringen

Verksamhetsarkitekten behöver visa hur AI-lösningen passar in i helheten. Det handlar om att beskriva förändringen i förmågor, processer, information, systemstöd, roller och styrning.

I NTG kan verksamhetsarkitekten exempelvis visa hur ett AI-stöd för riskanalys påverkar förmågan att välja kontrollobjekt. Förmågan består inte bara av modellen. Den består av datakällor, riskregler, analytikerkompetens, kontrollresurser, ledningsprioriteringar, rättsliga ramar, dokumentation och uppföljning.

När detta synliggörs blir det också lättare att se vad som måste vara på plats före skalning. Kanske behöver informationsmodellen förbättras. Kanske behöver ansvarsfördelningen mellan underrättelse och operativ kontroll förtydligas. Kanske behöver ett nytt forum skapas för att följa upp modellens effekter.

Verksamhetsarkitektur gör AI mindre mystiskt. Den visar att AI är en komponent i en större verksamhetsförändring.

## En enkel mognadsmodell för skalning

Myndigheten kan använda en enkel mognadsmodell för att bedöma om ett AI-initiativ är redo att skalas.

| Dimension | Fråga | Låg mognad | Högre mognad |
|---|---|---|---|
| Syfte | Är nyttan tydligt kopplad till uppdraget? | Allmänt intresse för AI | Tydlig verksamhetsnytta och målbild |
| Användning | Är arbetsflödet definierat? | Oklart när stödet ska användas | Tydliga arbetssätt och instruktioner |
| Ansvar | Finns ägare och beslutade roller? | Projektberoende ansvar | Verksamhetsägare och förvaltning |
| Information | Är datakällor och skyddskrav kända? | Delvis kända datakällor | Dokumenterad informationshantering |
| Risk | Är risker bedömda och hanterade? | Översiktlig riskdiskussion | Beslutade kontroller och uppföljning |
| Kompetens | Är användarna förberedda? | Några experter kan använda stödet | Utbildning, stöd och chefskap finns |
| Uppföljning | Mäts nytta och oönskade effekter? | Enstaka pilotmått | Löpande mätning och förbättring |

Modellen är enkel, men den hjälper ledningen att se att skalning kräver flera samtidiga förutsättningar. Den gör det också möjligt att besluta om stegvis införande i stället för allt eller inget.

## Checklista inför skalningsbeslut

Inför ett beslut om att skala en AI-lösning kan verksamhetsstrategen använda följande checklista:

- Är användningsområdet tydligt avgränsat?
- Är nyttan kopplad till en prioriterad verksamhetsförmåga?
- Är berörda processer och roller beskrivna?
- Finns verksamhetsägare, informationsägare och tekniskt ansvar?
- Är juridiska, etiska och informationssäkerhetsmässiga risker bedömda?
- Är mänskligt ansvar och mänsklig granskning tydligt beskrivet?
- Finns utbildning och stöd för användare och chefer?
- Finns plan för uppföljning av nytta, kvalitet och oönskade effekter?
- Finns process för förändringar, incidenter och avveckling?
- Är införandet planerat i en takt som organisationen klarar?

Om flera svar är nej bör myndigheten inte nödvändigtvis stoppa initiativet. Men den bör inte heller skala fullt ut. Då är nästa steg att stärka de svaga områdena.

## Vanliga misstag

- **Misstag: Att tro att skalning betyder fler användare.**
  - Varför det händer: Det är enkelt att mäta utrullning i antal konton eller enheter.
  - Hur man undviker det: Beskriv skalning som ökad verksamhetsförmåga, inte bara ökad åtkomst.

- **Misstag: Att lämna över AI-lösningen till förvaltning utan förändrat arbetssätt.**
  - Varför det händer: Organisationen behandlar AI som ett vanligt IT-system.
  - Hur man undviker det: Säkerställ att processer, instruktioner, ansvar och uppföljning följer med.

- **Misstag: Att skala innan riskerna är begripliga.**
  - Varför det händer: En lyckad pilot skapar stark vilja att visa resultat.
  - Hur man undviker det: Gör en särskild skalningsbedömning där riskbilden vid bred användning analyseras.

- **Misstag: Att underskatta chefens roll.**
  - Varför det händer: Fokus hamnar på användare och teknik.
  - Hur man undviker det: Ge chefer stöd att leda, följa upp och korrigera AI-stödd verksamhet.

- **Misstag: Att sakna plan för avveckling.**
  - Varför det händer: Införande upplevs som framåtriktat medan avveckling känns avlägset.
  - Hur man undviker det: Beskriv redan från början vilka kriterier som kan leda till paus, ändring eller avveckling.

## Reflektionsfrågor

1. Vilka AI-piloter i din organisation riskerar att stanna som isolerade experiment?
2. Vilka förmågor skulle behöva stärkas för att AI ska bli en del av ordinarie verksamhet?
3. Finns det tydligt ägarskap för AI-lösningar efter projektfasen?
4. Hur följer organisationen upp oönskade effekter, inte bara nytta?
5. Vilka delar av skalning är svagast i dag: teknik, verksamhet, styrning eller kompetens?

## Skala inte bara lösningen, skala ansvarssystemet
När ett AI-initiativ går från pilot till bred användning förändras ansvarssituationen. Det som fungerade med ett litet expertteam och nära uppföljning kan bli otillräckligt när många användare, flera processer och större datamängder berörs.

För NTG innebär skalning av ett AI-stöd för kontrollurval inte bara att fler kontor eller flöden ansluts. Myndigheten behöver också skala:

- utbildning,
- support,
- modellövervakning,
- avvikelsehantering,
- juridisk uppföljning,
- informationssäkerhetskontroller,
- verksamhetsansvar,
- kommunikation till berörda grupper.

Det är därför operativisering bör ses som etablering av ett ansvarssystem. Frågan är inte bara om AI-lösningen kan köras i större skala, utan om myndigheten kan äga, förklara, följa upp och förbättra den över tid.

## Snabb sammanfattning

Skalning handlar inte bara om att fler får tillgång till en AI-lösning. Det handlar om att AI blir en stabil, styrd och ansvarsfull del av myndighetens verksamhetsförmåga. För att lyckas krävs teknisk skalning, verksamhetsmässig skalning, styrningsmässig skalning samt kulturell och kompetensmässig skalning.

Operativisering innebär att AI-stödet får en tydlig plats i vardagens arbetsflöden. Det kräver definierade användningsområden, mänskligt ansvar, informationsregler, uppföljning och förvaltning. Verksamhetsstrategen hjälper ledningen att fatta mogna skalningsbeslut. Verksamhetsarkitekten visar hur AI-lösningen passar in i förmågor, processer, information och systemlandskap.

För NTG blir skalning särskilt viktigt eftersom AI används både i legala flöden och i brottsbekämpande verksamhet. Ju större påverkan på bedömningar, prioriteringar och rättssäkerhet, desto viktigare blir styrning, uppföljning och mänskligt ansvar.

## Nästa steg

Nästa kapitel tar ett bredare perspektiv. När AI-lösningar har börjat skalas behöver myndigheten se AI som en långsiktig verksamhetsförmåga. Det handlar inte bara om enskilda initiativ, utan om hur myndigheten organiserar lärande, styrning, kompetens och utvecklingskraft över tid.
