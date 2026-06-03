# Kapitel 10: Identifiera möjligheter

## Varför detta kapitel finns

När en myndighet har formulerat riktning, målbild, styrning och grundläggande riskramar uppstår nästa fråga: var ska AI faktiskt användas? Det är här många organisationer får problem. AI-arbetet börjar ofta i en lösningsidé, ett verktyg eller en trend, snarare än i ett tydligt verksamhetsproblem. Resultatet kan bli piloter som är intressanta men svåra att införa, svåra att följa upp och svåra att koppla till myndighetens uppdrag.

För en statlig myndighet räcker det inte att en AI-idé är tekniskt möjlig. Den måste också vara verksamhetsmässigt relevant, rättsligt hanterbar, informationsmässigt möjlig, säker, förklarbar på rätt nivå och möjlig att förvalta. Den måste dessutom passa in i myndighetens målbild och styrmodell. Därför behöver möjligheter identifieras systematiskt.

Det här kapitlet visar hur verksamhetsstrategen och verksamhetsarkitekten kan hitta, formulera och sortera AI-möjligheter utan att börja i tekniken. Vi använder Nordiska Tull- och Gränsmyndigheten, NTG, som genomgående exempel. NTG har både legala flöden och brottsbekämpande uppgifter. Det gör myndigheten till ett bra scenario eftersom AI-möjligheter kan se mycket olika ut beroende på om de gäller service till företag, riskbaserad kontroll, underrättelseanalys, utredningsstöd eller intern kunskapshantering.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- skilja mellan AI-idé, verksamhetsproblem, användningsfall och strategisk möjlighet,
- identifiera AI-möjligheter genom processer, information, problembilder och mål,
- formulera användningsfall så att de går att bedöma av ledning, juridik, säkerhet, arkitektur och utvecklingsorganisation,
- undvika vanliga fallgropar där AI-arbetet startar i teknik, hype eller lokala önskemål,
- skapa ett första möjlighetsunderlag som kan föras vidare till prioritering.

## Från idéjakt till möjlighetssökning

Ett vanligt första steg i AI-arbete är att samla idéer. Det kan vara värdefullt, men om arbetet stannar vid idéinsamling blir materialet ofta ojämnt. Några idéer är konkreta, andra är vaga. Några handlar om verkliga problem, andra om att prova ett nytt verktyg. Några är små förbättringar, andra skulle kräva omfattande förändring av arbetssätt, dataflöden och ansvar.

Därför behöver verksamhetsstrategen skilja mellan fyra nivåer:

| Nivå | Fråga | Exempel från NTG |
|---|---|---|
| AI-idé | Vad skulle vi kunna testa? | Använd generativ AI för att sammanfatta ärenden. |
| Verksamhetsproblem | Vilket problem behöver lösas? | Handläggare lägger mycket tid på att hitta och sammanställa tidigare ärendeinformation. |
| Användningsfall | I vilken situation kan AI skapa nytta? | Ett AI-stöd sammanfattar relevanta handlingar inför handläggarens granskning, med källhänvisningar. |
| Strategisk möjlighet | Vilken förmåga eller effekt stärker detta? | Kortare ledtider, jämnare kvalitet och bättre användning av erfarenhetsbaserad kunskap. |

Skillnaden är viktig. En AI-idé kan vara lockande men sakna tydlig nytta. Ett verksamhetsproblem kan vara viktigt men inte lämpa sig för AI. Ett användningsfall kan vara lovande men kräva data eller rättsliga förutsättningar som saknas. En strategisk möjlighet visar varför initiativet är relevant för myndighetens uppdrag.

Målet i detta kapitel är inte att avgöra vilka initiativ som ska genomföras. Det kommer i nästa kapitel. Målet är att skapa ett bättre råmaterial för prioritering: tydliga, jämförbara och verksamhetsförankrade AI-möjligheter.

## Fyra ingångar till AI-möjligheter

AI-möjligheter kan hittas på flera sätt. I praktiken bör myndigheten kombinera flera ingångar, eftersom varje ingång synliggör olika typer av nytta.

### Processingången

Processingången börjar i hur arbetet faktiskt går till. Den passar när myndigheten vill förstå var tid, kvalitet, väntan, dubbelarbete eller avbrott uppstår. För NTG kan det handla om processen för deklarationsgranskning, tillståndsprövning, kontrollplanering eller underrättelsesammanställning.

Frågor som hjälper:

- Var i processen uppstår långa ledtider?
- Var görs mycket manuell sortering, läsning eller sammanställning?
- Var krävs erfarenhetsbaserade bedömningar som är svåra att sprida?
- Var uppstår återkommande fel, kompletteringar eller omtag?
- Var behöver medarbetare växla mellan många system eller informationskällor?

AI är ofta relevant där arbetet innehåller stora mängder information, återkommande mönster, klassificering, prioritering, sökning eller sammanfattning. Det betyder inte att hela processen ska automatiseras. Ofta är det mer realistiskt och ansvarsfullt att börja med ett stöd i ett avgränsat arbetsmoment.

Exempel: NTG ser att kontrollhandläggare lägger mycket tid på att läsa transportdokument, historik och tidigare avvikelser innan de kan bedöma om ett flöde bör granskas närmare. En AI-möjlighet kan då vara att skapa ett sammanfattande beslutsunderlag med källor, riskindikatorer och osäkerheter. Det är inte ett automatiskt beslut om kontroll, utan ett stöd inför mänsklig bedömning.

### Informationsingången

Informationsingången börjar i de informationsmängder myndigheten har eller behöver. Den passar särskilt bra för verksamhetsarkitekter eftersom den kopplar AI-möjligheter till informationsarkitektur, datakvalitet, åtkomst, klassning och spårbarhet.

Frågor som hjälper:

- Vilken information är central för myndighetens uppdrag men svår att använda?
- Finns information i ostrukturerad form, till exempel dokument, fritext, rapporter eller e-post?
- Finns informationsmängder där mönster, avvikelser eller samband är svåra att upptäcka manuellt?
- Finns kunskap som är spridd mellan system, enheter eller personer?
- Vilken information får inte användas fritt, och vilka begränsningar följer av rättsliga eller säkerhetsmässiga krav?

För NTG kan informationsingången visa möjligheter inom både legala flöden och brottsbekämpning. I legala flöden kan det handla om att klassificera dokument, upptäcka avvikelser i deklarationer eller ge bättre stöd till företag. I brottsbekämpning kan det handla om att sammanställa underrättelseinformation eller hitta mönster i beslag, transportvägar och tidigare ärenden.

Här är det avgörande att inte blanda ihop att information finns med att den får, bör eller kan användas. En AI-möjlighet behöver redan tidigt beskriva vilken information den bygger på, vilken känslighet informationen har och om användningen kräver särskild prövning.

### Problembildsingången

Problembildsingången börjar i det som skaver i verksamheten. Den är ofta lättast att använda i dialog med chefer och medarbetare, eftersom den utgår från upplevda hinder snarare än tekniska begrepp.

Frågor som hjälper:

- Vad hindrar oss från att nå våra mål?
- Vilka uppgifter tar oproportionerligt mycket tid?
- Var finns risk för ojämn kvalitet?
- Var får vi för många falska positiva eller falska negativa träffar?
- Var är det svårt att prioritera begränsade resurser?
- Var uppstår kunskapstapp när erfarna medarbetare byter roll eller slutar?

För NTG kan en problembild vara att riskurvalet i vissa flöden ger för många träffar som inte leder vidare. Det binder resurser och kan samtidigt skapa störningar för legitima aktörer. En AI-möjlighet kan då vara att förbättra prioriteringsunderlaget genom att kombinera historiska mönster, regelbaserade indikatorer och mänsklig expertkunskap. Men möjligheten behöver formuleras försiktigt: syftet är inte att ersätta professionell bedömning, utan att ge bättre underlag för att använda kontrollresurser där de gör störst nytta.

### Målbildsingången

Målbildsingången börjar i den framtida förmåga myndigheten vill utveckla. Den passar när myndigheten redan har en AI-strategi eller en verksamhetsstrategisk målbild. Den hjälper organisationen att undvika lösryckta initiativ.

Frågor som hjälper:

- Vilka framtida förmågor har myndigheten pekat ut?
- Vilka delar av målbilden kräver bättre informationsanvändning?
- Var behöver myndigheten bli mer proaktiv, träffsäker eller kunskapsdriven?
- Var behöver medarbetare få bättre stöd för komplexa bedömningar?
- Var finns strategiska beroenden till data, arkitektur, juridik och kompetens?

Om NTG:s målbild säger att myndigheten ska bli mer riskstyrd, datadriven och serviceorienterad kan AI-möjligheter kopplas till dessa förmågor. Exempelvis kan ett kunskapsstöd för handläggare bidra till service och kvalitet, medan ett analysstöd för underrättelseenheten kan bidra till tidigare upptäckt av organiserade upplägg.

Fördelen med målbildsingången är att den skapar strategisk relevans. Nackdelen är att den kan bli abstrakt om den inte kopplas tillbaka till konkreta processer, informationsmängder och problem.

## En enkel metod för att identifiera möjligheter

Ett praktiskt arbetssätt är att genomföra en strukturerad möjlighetskartläggning. Den kan göras som en workshopserie eller som intervjuer kombinerade med analys. För en ny verksamhetsstrateg eller verksamhetsarkitekt är det klokt att börja litet, med ett avgränsat verksamhetsområde.

### Steg 1: Välj område

Välj ett område där myndigheten har tydliga problem, engagerade verksamhetsrepresentanter och tillräckligt stark koppling till målbilden. Undvik att börja med det mest känsliga eller mest komplexa området om organisationen ännu saknar AI-mognad.

För NTG kan ett lämpligt första område vara dokumentgranskning i legala flöden. Det är verksamhetsnära, informationsintensivt och ofta lättare att avgränsa än operativ brottsbekämpning. Ett annat område kan vara intern kunskapssökning, där riskerna kan vara hanterbara om informationen avgränsas och behörigheter respekteras.

### Steg 2: Beskriv nuläge och friktion

Samla personer som kan beskriva arbetet i praktiken. Det räcker inte med processkartor. Fråga hur arbetet faktiskt görs, vilka genvägar som används, vilka informationskällor som kontrolleras och var osäkerhet uppstår.

Dokumentera friktioner som:

- tidskrävande läsning,
- många systembyten,
- svårighet att hitta tidigare beslut,
- varierande bedömningskvalitet,
- hög manuell belastning,
- otydliga prioriteringar,
- bristande spårbarhet,
- återkommande kompletteringar.

Var noga med att inte direkt skriva “AI kan lösa detta”. Först behöver problemet förstås.

### Steg 3: Koppla friktion till AI-mönster

När friktionerna är synliga kan de kopplas till vanliga AI-mönster. Några exempel:

| Friktion | Möjligt AI-mönster |
|---|---|
| Mycket text behöver läsas | Sammanfattning, informationsutvinning, semantisk sökning |
| Ärenden behöver sorteras | Klassificering, prioritering, regelstöd kombinerat med AI |
| Avvikelser är svåra att upptäcka | Mönsterigenkänning, avvikelseanalys |
| Belastning varierar | Prognoser, kapacitetsanalys |
| Medarbetare letar efter tidigare kunskap | Kunskapsstöd, sök- och frågestöd |
| Riskurval ger för många träffar | Prediktiv riskbedömning, förbättrad prioritering |

Detta steg kräver inte teknisk lösningsdesign. Det handlar om att översätta verksamhetsfriktion till möjliga typer av AI-stöd.

### Steg 4: Formulera användningsfall

Ett användningsfall ska vara så konkret att andra kan förstå vad som faktiskt avses. En bra formulering innehåller:

- vilken användare eller roll som berörs,
- vilket arbetsmoment det gäller,
- vilket problem som ska minska,
- vilken information som används,
- vilket AI-stöd som kan vara relevant,
- vilken nytta som förväntas,
- vilka risker eller osäkerheter som redan syns,
- vilken mänsklig kontroll som behövs.

Exempel från NTG:

“Kontrollhandläggare får ett AI-stött sammanfattningsunderlag inför granskning av inkommande transportdokument. Stödet lyfter fram relevanta uppgifter, tidigare avvikelser och möjliga riskindikatorer med källhänvisningar. Handläggaren ansvarar för bedömningen. Syftet är att minska lästid, öka spårbarhet och skapa jämnare kvalitet i den första granskningen.”

Detta är bättre än “AI för dokumentgranskning”, eftersom det går att diskutera, pröva och avgränsa.

### Steg 5: Gör en första genomförbarhetskontroll

Innan användningsfallen förs vidare till prioritering bör de kontrolleras översiktligt. Fråga:

- Finns informationen?
- Är informationen tillgänglig i rätt kvalitet?
- Finns tydlig verksamhetsägare?
- Är användningen rättsligt och säkerhetsmässigt möjlig att pröva?
- Går nyttan att beskriva?
- Är arbetsmomentet tillräckligt avgränsat?
- Finns risk för otillbörlig automatisering eller överdriven tillit?
- Behöver initiativet först lösa grundläggande data- eller processproblem?

Syftet är inte att stoppa svåra idéer för tidigt. Syftet är att undvika att uppenbart omogna idéer tar plats i prioriteringen utan rätt förberedelser.

## Möjlighetskarta för NTG

En möjlighetskarta är ett enkelt sätt att samla och sortera AI-möjligheter. Den kan börja som en tabell och senare utvecklas till en AI-pipeline eller portfölj.

| Område | Problem | Möjligt användningsfall | Förväntad nytta | Tidig riskfråga |
|---|---|---|---|---|
| Legala flöden | Mycket manuell dokumentläsning | Sammanfattning av transport- och deklarationsunderlag | Kortare ledtid och jämnare kvalitet | Källhänvisning och spårbarhet |
| Företagsservice | Återkommande frågor från företag | Kunskapsstöd för vägledning | Snabbare och mer konsekvent service | Risk för felaktiga svar |
| Kontrollplanering | Svårt att prioritera kontroller | AI-stött risk- och prioriteringsunderlag | Bättre resursanvändning | Transparens och mänsklig kontroll |
| Underrättelse | Spridd information i många material | Sammanställning av underrättelseunderlag | Snabbare analys och bättre överblick | Behörighet, sekretess och ändamål |
| Utredning | Stora ärendematerial | Sökning och tematisering i utredningsmaterial | Effektivare genomgång | Riktighet och bevisvärdering |
| Intern styrning | Svårt att följa initiativ | AI-pipeline med status och lärande | Bättre styrning och portföljöverblick | Datakvalitet i uppföljning |

Tabellen är inte ett beslutsunderlag i sig. Den är ett sätt att skapa gemensamt språk. Först när möjligheterna är formulerade på liknande sätt kan de jämföras.

## Särskilda överväganden för brottsbekämpande verksamhet

AI-möjligheter inom underrättelse, utredning och kontroll kan ha stor potential, men de kräver särskild försiktighet. Det beror på att informationen ofta är känslig, att konsekvenserna kan bli stora och att gränsen mellan beslutsstöd och faktisk beslutspåverkan kan vara svår att se.

För verksamhetsstrategen är det viktigt att ställa några tidiga frågor:

- Handlar användningsfallet om analysstöd, prioriteringsstöd eller beslutspåverkan?
- Vilka individer, företag eller grupper kan påverkas?
- Vilken information används, och för vilket ändamål samlades den in?
- Kan användaren förstå varför AI-stödet visar ett visst resultat?
- Hur dokumenteras mänsklig bedömning?
- Hur upptäcks fel, snedvridning eller överdriven tillit?
- Vilken roll har juridik, dataskydd, säkerhet och verksamhetsledning i nästa steg?

Ett AI-stöd för underrättelsesammanställning kan till exempel vara rimligt att börja med som ett verktyg för att hitta, sortera och sammanfatta material som behöriga analytiker redan får använda. Ett AI-stöd som däremot rangordnar personer, företag eller transporter för ingripande åtgärder kräver en helt annan nivå av prövning, transparens, styrning och uppföljning.

Det betyder inte att brottsbekämpande AI-möjligheter ska undvikas. Det betyder att de ska beskrivas noggrant och prövas med rätt allvar från början.

## Vanliga misstag

- **Misstag: Att börja med verktyget i stället för verksamhetsproblemet.**
  - Varför det händer: Generativ AI och nya plattformar är synliga, konkreta och lätta att demonstrera.
  - Hur du undviker det: Kräv alltid en problemformulering, ett arbetsmoment och en förväntad effekt innan idén går vidare.

- **Misstag: Att kalla allt för användningsfall.**
  - Varför det händer: Begreppet används ofta brett och otydligt.
  - Hur du undviker det: Skilj mellan idé, problem, användningsfall och strategisk möjlighet.

- **Misstag: Att underskatta informationsfrågan.**
  - Varför det händer: AI diskuteras ofta som teknik, men i myndigheter avgörs möjligheten ofta av data, kvalitet, behörighet, sekretess och ändamål.
  - Hur du undviker det: Beskriv alltid vilken information användningsfallet bygger på och vilka begränsningar som finns.

- **Misstag: Att välja det mest spektakulära området först.**
  - Varför det händer: Ledning och verksamhet vill gärna se tydliga effekter snabbt.
  - Hur du undviker det: Börja med områden där nytta, avgränsning, risk och lärande är i balans.

- **Misstag: Att hoppa över mänsklig kontroll i formuleringen.**
  - Varför det händer: Fokus hamnar på vad AI kan producera, inte hur resultatet ska användas.
  - Hur du undviker det: Beskriv alltid vem som tar ansvar för bedömning, beslut och uppföljning.

## Reflektionsfrågor

1. Vilka tre verksamhetsproblem i din myndighet skulle bli tydligare om de beskrevs utan att nämna AI?
2. Finns det informationsmängder som många behöver men få kan använda effektivt?
3. Vilka AI-idéer är egentligen lösningsförslag på otydliga problem?
4. Vilka möjligheter skulle vara lämpliga som lärande första initiativ, snarare än som största tänkbara satsning?
5. Var behöver juridik, informationssäkerhet eller arkitektur kopplas in redan innan prioritering?

## Leta efter beslutssituationer, inte bara processsteg
När verksamheten letar AI-möjligheter är det lätt att börja med processkartor och fråga var arbetet tar lång tid. Det är användbart, men inte tillräckligt. AI skapar ofta störst värde i beslutssituationer där människor behöver tolka stora mängder information, väga osäkerhet eller prioritera mellan många alternativ.

För NTG kan sådana beslutssituationer finnas i exempelvis:

- urval av kontroller i legala flöden,
- prioritering av underrättelseuppslag,
- bedömning av vilka ärenden som behöver fördjupad analys,
- sammanställning av information inför utredning,
- identifiering av återkommande mönster i dokument eller deklarationer.

Verksamhetsstrategen bör därför komplettera processanalysen med en beslutsanalys. Fråga: vilka beslut fattas, av vem, med vilket underlag, med vilken osäkerhet och med vilka konsekvenser om det blir fel? Det gör AI-möjligheterna mer konkreta och hjälper myndigheten att skilja mellan enkla effektiviseringsidéer och strategiskt viktiga förmågeförbättringar.

## Snabb sammanfattning

- AI-möjligheter bör identifieras systematiskt, inte bara samlas in som lösa idéer.
- En AI-idé är inte samma sak som ett användningsfall.
- Bra möjligheter kan hittas genom processer, information, problembilder och målbild.
- Ett användningsfall behöver beskriva roll, arbetsmoment, information, nytta, risk och mänsklig kontroll.
- I brottsbekämpande verksamhet behöver användningsfall beskrivas med särskild tydlighet eftersom påverkan, sekretess och ansvar ofta är större.
- Resultatet av kapitlet är en bättre möjlighetskarta som kan användas i nästa steg: prioritering.

## Nästa steg

Nästa kapitel handlar om hur myndigheten prioriterar AI-användningsfall. När möjligheterna är identifierade behöver de vägas mot varandra utifrån nytta, genomförbarhet, risk, mognad och strategisk betydelse. Det är först då myndigheten kan avgöra vilka initiativ som bör bli piloter, vilka som kräver förarbete och vilka som bör vänta.
