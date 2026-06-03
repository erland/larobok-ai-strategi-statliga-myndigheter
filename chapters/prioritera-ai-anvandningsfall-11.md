# Kapitel 11: Prioritera AI-användningsfall

## Varför detta kapitel finns

När AI-möjligheter har identifierats behöver de prioriteras. Det är ett mer krävande arbete än att bara välja de mest lockande idéerna. I en statlig myndighet måste prioritering väga flera sorters värde mot flera sorters begränsningar: verksamhetsnytta, rättsliga förutsättningar, informationssäkerhet, datakvalitet, arkitektur, kompetens, kostnad, förändringspåverkan och förtroende.

Många AI-satsningar fastnar inte för att idén är dålig, utan för att den valdes vid fel tidpunkt. Ett användningsfall kan vara principiellt klokt men för tidigt för organisationens mognad. Ett annat kan vara tekniskt enkelt men ge liten strategisk nytta. Ett tredje kan ge stor nytta men kräva sådan juridisk prövning, informationsklassning och förändringsledning att det först bör genomföras som ett begränsat lärandeinitiativ.

För verksamhetsstrategen och verksamhetsarkitekten är prioritering därför inte bara ett urval. Det är en översättning mellan strategi och genomförande. Prioriteringen ska hjälpa ledningen att fatta beslut, utvecklingsorganisationen att planera, verksamheten att förstå varför vissa initiativ går före andra och kontrollfunktioner att se hur risker hanteras.

I detta kapitel använder vi Nordiska Tull- och Gränsmyndigheten, NTG, som exempel. Myndigheten har identifierat AI-möjligheter inom legala varuflöden, kundservice, riskanalys, underrättelse, utredningsstöd och intern kunskapshantering. Nu behöver dessa möjligheter värderas på ett sätt som passar en myndighet med både serviceuppdrag och brottsbekämpande ansvar.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara varför AI-användningsfall behöver prioriteras bredare än utifrån teknisk möjlighet,
- använda en enkel prioriteringsmodell som väger nytta, genomförbarhet, risk och strategisk betydelse,
- skilja mellan snabb nytta, lärandeinitiativ, strategiska satsningar och högriskfall,
- formulera ett beslutsunderlag som gör prioriteringen begriplig för ledning och utvecklingsorganisation,
- känna igen vanliga fallgropar i prioritering av AI-satsningar.

## Vad som egentligen prioriteras

Det är lätt att säga att myndigheten ska prioritera “AI-användningsfall”. Men begreppet kan betyda olika saker. I ett möte kan en deltagare mena en verksamhetsidé, en annan ett teknikexperiment och en tredje ett färdigt införandeprojekt. För att prioriteringen ska bli meningsfull behöver objektet vara tillräckligt tydligt.

Ett användningsfall bör minst beskriva:

- vilket verksamhetsproblem eller vilken möjlighet det adresserar,
- vilken målgrupp eller process som påverkas,
- vilken information som behövs,
- vilken typ av AI-stöd som kan vara aktuellt,
- vilken mänsklig roll som finns kvar,
- vilken nytta som förväntas,
- vilka risker eller begränsningar som redan är kända,
- vad som behöver prövas innan införande.

Det betyder inte att allt måste vara färdigutrett. Men det måste vara tillräckligt tydligt för att jämföra med andra användningsfall.

Hos NTG kan tre idéer först låta likvärdiga:

- AI-stöd för att sammanfatta långa interna styrdokument.
- AI-stöd för att prioritera kontroll av varusändningar.
- AI-stöd för att hitta samband i underrättelsematerial.

Alla tre kan skapa nytta. Men de skiljer sig kraftigt åt i risk, databehov, juridik, arkitektur, påverkan på arbetssätt och krav på mänsklig kontroll. Därför kan de inte prioriteras med samma enkla fråga: “Vilken verkar mest spännande?”

## Fyra prioriteringsdimensioner

En användbar grundmodell är att bedöma varje användningsfall utifrån fyra dimensioner:

- **Nytta:** Vilket värde kan användningsfallet skapa för uppdraget, medborgare, företag, medarbetare eller samhällsskydd?
- **Genomförbarhet:** Hur möjligt är det att genomföra med nuvarande data, teknik, kompetens, arkitektur och organisation?
- **Risk och ansvar:** Vilka rättsliga, etiska, säkerhetsmässiga och förtroendemässiga risker finns?
- **Strategisk betydelse:** Hur väl stöder användningsfallet målbilden, framtida förmågor och myndighetens långsiktiga riktning?

Modellen är medvetet enkel. Syftet är inte att skapa en matematisk sanning, utan att tvinga fram ett balanserat samtal. Den hjälper också ledningen att förstå varför ett användningsfall med stor nytta kanske ändå inte bör startas först, och varför ett mindre användningsfall kan vara klokt om det bygger viktig förmåga.

## Nytta: mer än effektivisering

AI-nytta beskrivs ofta som tidsbesparing. Det är viktigt, men för myndigheter är det sällan tillräckligt. Nytta kan också handla om kvalitet, rättssäkerhet, likformighet, träffsäkerhet, arbetsmiljö, snabbare återkoppling, bättre beslutsunderlag eller stärkt samhällsskydd.

För NTG kan ett AI-stöd i legala flöden ge nytta genom att företag får snabbare återkoppling på deklarationer och färre enkla fel. Ett AI-stöd i brottsbekämpande verksamhet kan ge nytta genom att analytiker snabbare hittar avvikelser, samband eller riskmönster. Ett internt kunskapsstöd kan ge nytta genom att handläggare lättare hittar rätt vägledning och därmed arbetar mer enhetligt.

När nyttan bedöms bör verksamhetsstrategen ställa frågor som:

- Vilket konkret problem minskar eller löser användningsfallet?
- Vem får nytta och hur märks den?
- Är nyttan kopplad till myndighetens uppdrag eller mest till lokal bekvämlighet?
- Går nyttan att följa upp med rimliga mått?
- Är nyttan beroende av förändrade arbetssätt, beslut eller regelverk?

En risk i prioritering är att ge högt värde till användningsfall som låter stora men där nyttan är svår att realisera. “Bättre underrättelsearbete” är till exempel en viktig ambition, men som prioriteringsunderlag är det för brett. Ett bättre formulerat användningsfall kan vara: “AI-stöd för att sammanfatta och jämföra inkomna underrättelseuppslag så att analytiker snabbare kan identifiera dubbletter, samband och behov av manuell fördjupning.” Det är fortfarande komplext, men mer bedömningsbart.

## Genomförbarhet: vad krävs för att idén ska fungera?

Genomförbarhet handlar inte bara om teknisk utveckling. Den handlar om hela kedjan från information till användning. Ett användningsfall kan vara tekniskt möjligt men organisatoriskt svårt, eller organisatoriskt önskat men informationsmässigt omoget.

Bedömningen bör minst täcka:

- datatillgång och datakvalitet,
- informationsklassning och behörigheter,
- systemmiljö och integrationsbehov,
- kompetens i verksamhet och IT,
- beroenden till andra projekt,
- förvaltningsförmåga,
- möjlighet att mäta resultat,
- hur mycket arbetssättet behöver förändras.

Hos NTG kan ett AI-stöd för intern kunskapssökning vara relativt genomförbart om styrdokument, vägledningar och handböcker redan finns i ordnade informationsytor. Ett AI-stöd för riskprioritering i varuflöden kan kräva betydligt mer: datakällor från flera system, kvalitetssäkrade historiska uppgifter, tydliga riskindikatorer, spårbarhet, integration i kontrollprocessen och noggrann uppföljning.

Genomförbarhet bör inte användas för att alltid välja det enkla. Då riskerar AI-arbetet att fastna i lågriskverktyg med begränsad strategisk betydelse. Men låg genomförbarhet behöver synliggöras, eftersom den påverkar tid, kostnad, styrning och sannolikhet att lyckas.

## Risk och ansvar: inte ett nej, utan en styrsignal

Riskbedömning i AI-prioritering ska inte bara fungera som broms. Den ska hjälpa myndigheten att välja rätt angreppssätt. Ett användningsfall med hög risk kan fortfarande vara viktigt, men bör kanske hanteras med mer avgränsad pilot, starkare juridisk involvering, särskild dokumentation, tydligare mänsklig kontroll eller längre förberedelse.

För NTG blir skillnaden tydlig mellan tre typer av användning:

- Ett internt språkstöd som hjälper medarbetare att formulera utkast till mötesanteckningar.
- Ett beslutsstöd som föreslår vilka varuflöden som bör kontrolleras.
- Ett analysstöd som bearbetar underrättelseinformation om misstänkt organiserad brottslighet.

Alla kan vara relevanta. Men de kräver olika risknivåer, informationsskydd, loggning, kvalitetssäkring och ansvarsfördelning. I brottsbekämpande verksamhet kan felaktiga eller otydliga analyser få särskilt allvarliga konsekvenser för individer, utredningar, samverkan och förtroende. Därför behöver risk inte bara beskrivas som sannolikhet och konsekvens, utan också som påverkan på rättssäkerhet och legitimitet.

Frågor att använda i prioriteringen är:

- Påverkar användningsfallet enskilda personer, företag eller rättsliga bedömningar?
- Används känslig, sekretessbelagd eller brottsbekämpande information?
- Kan AI-resultatet uppfattas som ett beslut snarare än ett stöd?
- Finns risk för felaktig automatisering av bedömningar?
- Krävs särskild transparens, dokumentation eller mänsklig kontroll?
- Skulle ett fel kunna skada förtroendet för myndigheten?

Riskbedömningen ska dokumenteras på en nivå som passar prioriteringsskedet. Det är inte en fullständig juridisk analys, men det ska vara tillräckligt för att avgöra om användningsfallet kan gå vidare som snabb pilot, behöver fördjupad prövning eller bör parkeras.

## Strategisk betydelse: bygger användningsfallet framtida förmåga?

Ett användningsfall kan vara viktigt även om den första nyttan är begränsad. Det kan bygga dataförmåga, AI-governance, arkitekturmönster, kompetens, uppföljningsmetoder eller samarbetsformer som myndigheten behöver senare. Därför bör prioriteringen alltid innehålla frågan: hjälper detta oss att bygga den AI-förmåga vi behöver?

För NTG kan ett begränsat AI-stöd för att sammanfatta interna vägledningar ha strategisk betydelse om det etablerar säkra arbetssätt för generativ AI, informationsklassning, kvalitetssäkring och användarutbildning. Det kan vara en bra första satsning även om den inte är mest samhällsavgörande.

Samtidigt kan ett avancerat riskanalysstöd för varuflöden vara strategiskt betydelsefullt eftersom det direkt kopplar till myndighetens kärnuppdrag. Men om datagrunden, ansvarsfördelningen och uppföljningen inte är mogen kan det behöva delas upp i flera steg: först datakartläggning, sedan analytisk prototyp, därefter kontrollerad pilot och först senare införande.

Strategisk betydelse handlar alltså inte om att välja det största först. Det handlar om att välja en ordning som bygger riktning, lärande och förmåga.

## Särskilda prioriteringsfrågor för generativ AI

Generativ AI skapar ofta många idéer snabbt. Det kan vara frestande att prioritera de idéer som är enklast att demonstrera, till exempel en intern chatt eller ett stöd för att skriva text. Men en bra demonstration är inte samma sak som ett prioriterat verksamhetsinitiativ.

När generativa AI-användningsfall prioriteras bör myndigheten därför lägga till några särskilda frågor:

- **Är kunskapskällorna avgränsade och ägda?** Ett användningsfall som bygger på oklara dokumentlager, gamla rutiner eller blandade filytor kommer snabbt att få kvalitetsproblem.
- **Behöver svaret vara spårbart till källa?** Ju närmare användningen ligger rättstillämpning, kontroll eller brottsbekämpande analys, desto viktigare blir källhänvisning och granskningsbarhet.
- **Är användningen textstöd eller beslutsstöd?** Att sammanfatta ett underlag är något annat än att föreslå en åtgärd, prioritera ett ärende eller påverka en kontroll.
- **Vilken mänsklig kontroll krävs?** Generativ AI bör ofta vara ett stöd i arbetsflödet, inte en osynlig automatisering.
- **Kan användningsfallet återanvändas?** En kunskapsassistent med robust informationsstyrning kan bli en gemensam förmåga, medan en isolerad promptlösning sällan skalar.
- **Vilken typ av fel är acceptabla?** Ett språkligt förslag kan vara lätt att rätta. Ett felaktigt rättsligt påstående, en felaktig riskindikator eller ett missvisande beslutsunderlag kan få större konsekvenser.

För NTG innebär detta att en generativ AI-lösning för att sammanfatta interna riktlinjer kan vara en lämplig tidig kandidat om källorna är styrda och svaren tydligt hänvisar till dokument. En lösning som sammanfattar underrättelseunderlag för operativa beslut kan däremot kräva betydligt mer styrning, loggning och kvalitetssäkring även om tekniken ser liknande ut.

## En enkel prioriteringsmatris

En praktisk metod är att använda en matris med fyra bedömningsnivåer per dimension. Exempelvis:

| Dimension | Låg | Medel | Hög | Mycket hög |
|---|---|---|---|---|
| Nytta | Lokal bekvämlighet | Tydlig förbättring i avgränsad process | Betydande verksamhetsnytta | Direkt koppling till kärnuppdrag och samhällsnytta |
| Genomförbarhet | Många okända beroenden | Kräver flera förberedelser | Möjligt med rimlig insats | Kan startas med befintliga förutsättningar |
| Risk och ansvar | Låg påverkan | Hanterbar risk | Kräver särskild prövning | Hög påverkan på rättssäkerhet, säkerhet eller förtroende |
| Strategisk betydelse | Svag koppling till målbild | Stöder viss utveckling | Bygger viktig förmåga | Central för målbild och framtida operativ modell |

Matrisen ska inte automatiskt räkna fram ett svar. Den ska skapa ett gemensamt språk. En myndighet kan till exempel besluta att användningsfall med mycket hög risk aldrig får starta utan särskild styrgruppsprövning. Den kan också besluta att minst några initiativ i portföljen ska ha hög strategisk betydelse, även om de inte ger snabb nytta.

## Fyra kategorier av användningsfall

Efter bedömningen kan användningsfallen sorteras i fyra kategorier.

### Snabb nytta

Detta är användningsfall med tydlig nytta, relativt låg risk och hög genomförbarhet. De är bra för att skapa förtroende, praktisk erfarenhet och konkret verksamhetsvärde.

Hos NTG kan detta vara ett internt stöd för att hitta i styrdokument, sammanfatta öppna eller interna vägledningar, eller hjälpa handläggare att skapa första utkast till kommunikation som sedan granskas av människa.

### Lärandeinitiativ

Detta är användningsfall där den direkta nyttan kanske är begränsad, men där myndigheten lär sig något viktigt om data, juridik, teknik, arbetssätt eller styrning. De bör utformas med tydliga lärandefrågor.

Ett exempel hos NTG kan vara en kontrollerad prototyp för att jämföra historiska riskindikatorer i varuflöden, utan att resultatet används operativt. Syftet kan vara att förstå datakvalitet, förklarbarhet och vilka kompetenser som krävs.

### Strategiska satsningar

Detta är användningsfall med hög strategisk betydelse och tydlig koppling till målbilden. De kan kräva mer tid och styrning, men bör inte försvinna bakom enklare initiativ.

Hos NTG kan en strategisk satsning vara att bygga en samlad förmåga för riskbaserad prioritering i kontrollverksamheten, där AI på sikt kan stödja både legala flöden och brottsbekämpande analys.

### Högriskfall som kräver särskild prövning

Detta är användningsfall där påverkan på individer, företag, rättsliga bedömningar, sekretess, brottsbekämpning eller förtroende är så stor att de inte bör hanteras som vanliga utvecklingsinitiativ.

Hos NTG kan detta gälla AI-stöd som används i underrättelsearbete, utredningsnära analys eller riskbedömningar som kan påverka kontrollurval. De kan vara mycket relevanta, men kräver tydliga ramar, dokumentation, mänsklig kontroll och ofta stegvis utveckling.

## Exempel: NTG prioriterar fem användningsfall

Anta att NTG har identifierat fem möjliga användningsfall:

1. Generativt kunskapsstöd för interna vägledningar.
2. Automatisk sammanfattning av inkomna företagsfrågor.
3. AI-stödd prioritering av varusändningar för kontroll.
4. Analysstöd för underrättelseuppslag.
5. Prognosstöd för resursplanering vid större varuflöden.

En första prioritering kan se ut så här:

| Användningsfall | Nytta | Genomförbarhet | Risk och ansvar | Strategisk betydelse | Rekommenderad hantering |
|---|---|---|---|---|---|
| Internt kunskapsstöd | Medel | Hög | Medel | Hög | Starta som kontrollerad pilot |
| Sammanfattning av företagsfrågor | Medel | Hög | Medel | Medel | Starta efter informationsklassning |
| Prioritering av varusändningar | Mycket hög | Medel | Hög | Mycket hög | Förstudie och stegvis pilot |
| Underrättelseanalys | Hög | Medel | Mycket hög | Mycket hög | Särskild prövning och avgränsad prototyp |
| Resursprognoser | Hög | Medel | Medel | Hög | Lärandeinitiativ med tydliga mått |

Denna tabell är inte beslutet i sig. Den är ett samtalsunderlag. Den gör det möjligt att säga: “Vi börjar inte med underrättelseanalys som brett införande, trots hög strategisk betydelse. Vi behöver först pröva ramarna. Däremot kan vi starta ett internt kunskapsstöd för att bygga arbetssätt för generativ AI och samtidigt förbereda en förstudie för riskbaserad prioritering.”

## Från poängsättning till portföljtänkande

Det kan vara frestande att ge varje användningsfall poäng och sedan välja de tre med högst totalpoäng. Det är ibland användbart, men riskerar att dölja viktiga skillnader. Ett högriskfall kan få hög totalpoäng eftersom nyttan och strategisk betydelse är stor, men ändå kräva särskild hantering. Ett enkelt användningsfall kan få lägre totalpoäng men vara rätt första steg.

Därför bör prioriteringen mynna ut i en balanserad portfölj, inte bara en rangordnad lista. En första AI-portfölj kan innehålla:

- ett eller två användningsfall som ger snabb nytta,
- ett lärandeinitiativ som bygger metod och mognad,
- en strategisk satsning som förbereds mer långsiktigt,
- ett högriskfall som utreds med särskild styrning snarare än startas direkt.

Detta gör att myndigheten både kan visa framdrift och bygga långsiktig förmåga. Nästa kapitel fördjupar just detta: hur en AI-portfölj byggs och styrs.

## Beslutsunderlag för ledningen

En prioritering behöver översättas till ett beslutsunderlag som ledningen kan använda. Underlaget bör vara kort, tydligt och ärligt. Det ska inte sälja in AI, utan visa hur myndigheten kan gå vidare ansvarsfullt.

Ett bra beslutsunderlag innehåller:

- sammanfattning av rekommenderad prioritering,
- koppling till strategi och målbild,
- föreslagna användningsfall och varför de valts,
- vilka användningsfall som parkeras eller kräver mer prövning,
- huvudsakliga risker och hanteringssätt,
- beroenden till data, juridik, säkerhet, arkitektur och kompetens,
- föreslaget nästa steg,
- vad ledningen behöver besluta.

För NTG kan ett sådant underlag exempelvis rekommendera att myndigheten startar ett kontrollerat internt kunskapsstöd, genomför en förstudie för riskbaserad prioritering i varuflöden och tillsätter en särskild beredning för underrättelsenära AI-användning. Det ger både framdrift, lärande och kontroll.

## Verksamhetsstrategens och verksamhetsarkitektens bidrag

I prioriteringen har verksamhetsstrategen och verksamhetsarkitekten olika men överlappande bidrag.

Verksamhetsstrategen säkerställer att prioriteringen utgår från uppdrag, mål, nytta, styrning och ledningens behov av beslutsunderlag. Verksamhetsarkitekten säkerställer att användningsfallen förstås i relation till förmågor, processer, information, system, ansvar och målarkitektur.

Tillsammans kan de ställa de frågor som ofta saknas när AI-idéer drivs för snabbt:

- Vilken förmåga stärker detta?
- Vilket problem löser vi egentligen?
- Vilka data krävs och får de användas?
- Vilket beslut eller arbetsmoment påverkas?
- Vem ansvarar om AI-stödet ger fel signal?
- Hur ska nyttan mätas?
- Vad måste vara sant för att detta ska kunna skalas?

Detta är en av de viktigaste rollerna i myndighetens AI-arbete: att göra prioriteringen både modig och ansvarsfull.

## Vanliga misstag

- **Misstag: Att prioritera efter teknisk entusiasm.**
  - Varför det händer: AI-idéer som låter moderna och kraftfulla får ofta mest uppmärksamhet.
  - Hur du undviker det: Kräv alltid koppling till verksamhetsproblem, målbild och ansvar.

- **Misstag: Att välja enbart lågriskfall.**
  - Varför det händer: Organisationen vill komma igång utan friktion.
  - Hur du undviker det: Bygg en portfölj där snabb nytta kombineras med strategiska satsningar och lärandeinitiativ.

- **Misstag: Att se riskbedömning som ett stopp.**
  - Varför det händer: Juridik, säkerhet och etik uppfattas som hinder.
  - Hur du undviker det: Använd risk som styrsignal för rätt tempo, rätt avgränsning och rätt kontrollnivå.

- **Misstag: Att blanda idéer, piloter och införandeprojekt i samma lista.**
  - Varför det händer: Alla initiativ kallas “AI-case” oavsett mognad.
  - Hur du undviker det: Markera varje användningsfalls mognadsgrad och nästa beslutspunkt.

- **Misstag: Att underskatta förändringspåverkan.**
  - Varför det händer: Fokus hamnar på modell, verktyg och data.
  - Hur du undviker det: Bedöm alltid påverkan på roller, ansvar, arbetssätt, utbildning och uppföljning.

## Reflektionsfrågor

1. Vilka AI-användningsfall i din myndighet skulle sannolikt ge snabb nytta men begränsad strategisk betydelse?
2. Vilka användningsfall är strategiskt viktiga men kräver mer förberedelse innan pilot?
3. Finns det idéer som bör parkeras eftersom datagrund, juridik eller ansvarsfördelning är för oklar?
4. Hur skulle ledningen reagera om prioriteringen presenterades som en portfölj i stället för en rangordnad lista?
5. Vilka kontrollfunktioner behöver involveras innan prioriteringen blir ett beslut?

## Prioritering behöver vara transparent
Prioritering av AI-användningsfall är känsligt eftersom olika delar av myndigheten ofta har olika bilder av vad som är viktigast. Ledningen kan vilja se strategisk effekt, verksamheten kan vilja lösa vardagsproblem, IT kan se tekniska beroenden och juristfunktionen kan fokusera på risk. Därför behöver prioriteringen vara transparent.

En bra prioriteringsprocess bör visa:

- vilka kriterier som används,
- hur kriterierna viktas,
- vilka antaganden som ligger bakom bedömningen,
- vilka risker som accepterats eller kräver åtgärd,
- varför vissa idéer väljs bort eller skjuts upp.

I NTG kan ett användningsfall som ger stor effektivisering i ett administrativt flöde prioriteras efter ett mindre men mer strategiskt underrättelsestöd om det senare bygger en förmåga som myndigheten behöver långsiktigt. Det är inte ett tecken på dålig prioritering. Det är ett tecken på att myndigheten prioriterar både kortsiktig nytta och framtida kapacitet.

Transparent prioritering gör det också lättare att återkomma till idéer när data, juridik, teknik eller verksamhetsmognad förändras.

## Snabb sammanfattning

- Prioritering av AI-användningsfall måste väga nytta, genomförbarhet, risk och strategisk betydelse.
- Hög nytta betyder inte automatiskt att användningsfallet bör startas först.
- Risk ska användas som styrsignal, inte bara som stopp.
- En balanserad AI-portfölj bör innehålla snabb nytta, lärandeinitiativ, strategiska satsningar och högriskfall med särskild prövning.
- Verksamhetsstrategen och verksamhetsarkitekten hjälper myndigheten att prioritera modigt, begripligt och ansvarsfullt.

## Nästa steg

När användningsfallen har prioriterats behöver de samlas i en styrbar helhet. Nästa kapitel handlar därför om hur myndigheten bygger en AI-portfölj med roadmaps, beroenden, finansiering, ansvar, lärande och beslutspunkter. Det är där prioriteringen går från urval till faktisk styrning.

## Ledningsperspektiv och beslutsunderlag

Som verksamhetsstrateg eller verksamhetsarkitekt behöver du kunna översätta AI-frågor till verksamhetsnytta, risker och prioriteringar som ledningen kan fatta beslut om. Beslutsunderlag bör beskriva förväntad nytta, riskbild, resursbehov, beroenden och hur initiativet stödjer myndighetens uppdrag.
