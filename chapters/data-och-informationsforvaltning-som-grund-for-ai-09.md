# Kapitel 9: Data och informationsförvaltning som grund för AI

## Varför detta kapitel finns

AI-strategi börjar ofta med frågor om teknik, verktyg och användningsfall. Men i en myndighet avgörs många AI-initiativ långt innan en modell väljs eller en pilot startar. De avgörs av hur myndigheten förstår, äger, beskriver, kvalitetssäkrar och delar sin information.

För en verksamhetsstrateg eller verksamhetsarkitekt är detta ett centralt perspektiv. AI är inte bara en ny teknisk komponent. AI är ett nytt sätt att använda information i verksamhetens beslut, arbetsflöden och tjänster. Därför måste AI-frågan kopplas till informationsförvaltning, begreppsmodeller, datakvalitet, informationssäkerhet, metadata, informationsägarskap och arkitektur.

I Nordiska Tull- och Gränsmyndigheten, NTG, blir detta tydligt. Myndigheten vill använda AI för att prioritera kontroller, stödja underrättelseanalys, granska dokument, upptäcka avvikande handelsmönster och hjälpa handläggare att hitta rätt information. Alla dessa initiativ kräver data. Men de kräver inte bara mycket data. De kräver rätt data, begriplig data, spårbar data och data som får användas i rätt sammanhang.

Det här kapitlet visar hur läsaren kan prata om data som en strategisk förutsättning för AI, utan att göra frågan onödigt teknisk.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara varför informationsförvaltning är en grundförmåga för AI,
- skilja mellan data, information, kunskap och verksamhetsbegrepp,
- identifiera vanliga dataproblem som bromsar AI-initiativ,
- koppla datastyrning till AI-governance,
- beskriva vad informationsägarskap betyder i praktiken,
- resonera om datakvalitet, metadata och informationsklassning,
- formulera en enkel målbild för AI-redo information.

## Data är inte samma sak som AI

När AI diskuteras i ledningsgrupper hamnar samtalet ofta snabbt i verktyg: språkmodeller, copiloter, analysplattformar eller automatiseringslösningar. Det är förståeligt, eftersom verktygen är konkreta. Men för myndigheter är det ofta informationen som är den egentliga begränsningen.

En AI-lösning kan bara ge värde om den har tillgång till relevant information och om informationen kan tolkas på rätt sätt. Om data är fragmenterad, otydlig, felklassad, inaktuell eller saknar ansvarig ägare blir AI-lösningen svår att använda på ett ansvarsfullt sätt.

Det gäller både generativ AI och mer traditionell analys-AI.

En generativ AI-assistent som ska hjälpa handläggare vid NTG behöver veta vilka styrdokument, rutiner, rättsliga ställningstaganden och operativa instruktioner som är gällande. Om gamla och nya dokument blandas utan tydlig status kan assistenten ge felaktiga svar.

En prediktiv riskmodell som ska stödja urval av varuflöden behöver historiska data med tillräcklig kvalitet. Om vissa typer av kontroller bara dokumenterats i fritext, om kodverk förändrats utan översättning eller om utfallet av kontroller inte registrerats konsekvent blir modellens resultat osäkert.

En AI-lösning för underrättelseanalys behöver kunna hantera källor, behörigheter, sekretess, spårbarhet och sammanhang. Om data delas utan kontroll kan myndigheten skapa både rättsliga och säkerhetsmässiga risker.

Därför bör en AI-strategi alltid innehålla en tydlig data- och informationsdimension. Det räcker inte att säga att myndigheten ska använda AI. Myndigheten behöver också beskriva vilken informationsförmåga som krävs för att AI ska kunna användas.

## Data, information och verksamhetsbegrepp

Ett vanligt misstag är att prata om data som om all data vore likadan. För strategiskt AI-arbete är det bättre att skilja mellan flera nivåer.

**Data** är registrerade värden. Det kan vara datum, koder, dokument, transaktionsrader, ärenden, loggar, bilder eller textfält.

**Information** är data som har betydelse i ett sammanhang. Ett varunummer, ett organisationsnummer eller ett beslutsdatum blir relevant först när man vet vad det avser, hur det har skapats och hur det används.

**Kunskap** uppstår när information kan tolkas, vägas och användas för handling. En riskanalytiker använder inte bara data om ett flöde. Analytikern använder erfarenhet, regler, tidigare mönster, hotbilder och förståelse för verksamheten.

**Verksamhetsbegrepp** är de ord och definitioner som gör att människor och system menar samma sak. Exempel kan vara sändning, deklaration, kontroll, beslag, underrättelseuppslag, riskindikator och operativ åtgärd.

För AI är begreppen särskilt viktiga. Om olika delar av myndigheten använder samma ord på olika sätt kan AI-lösningar förstärka förvirringen. Om ett kontrollutfall betyder en sak i gränsflödet och en annan sak i ett utredningssystem blir det svårt att träna, testa eller förklara en modell.

Verksamhetsarkitektens bidrag är att synliggöra dessa samband. En AI-diskussion bör därför inte bara innehålla frågan: "Vilka data har vi?" Den bör också innehålla frågorna: "Vad betyder informationen?", "Vem ansvarar för den?", "Hur används den?", "Vilken kvalitet krävs?" och "I vilka beslut får den påverka utfallet?"

## Informationsägarskap i praktiken

Informationsägarskap är ofta lätt att skriva in i en styrmodell men svårt att få att fungera i vardagen. I AI-sammanhang blir bristerna snabbt synliga.

En informationsägare behöver inte själv vara teknisk expert. Däremot behöver rollen ha mandat att svara på frågor som påverkar AI-användning:

- Vad betyder informationen?
- Vilken verksamhetsprocess skapar den?
- Vilka regler styr användningen?
- Vilken kvalitet är tillräcklig för olika syften?
- Vilka begränsningar finns för vidareanvändning?
- Vilka ändringar i begrepp, kodverk eller processer påverkar informationen?
- Hur ska fel, avvikelser och brister hanteras?

I NTG:s fall kan information om kontroller, varuflöden, tillstånd, underrättelseuppslag och beslag ligga i olika system och ägas av olika delar av organisationen. En AI-portfölj som använder dessa informationsmängder behöver därför veta vilka informationsägare som ska involveras tidigt.

Om ett AI-initiativ saknar tydlig informationsägare uppstår flera problem. Ingen kan säkert säga om informationen får användas. Ingen kan bedöma om kvaliteten är tillräcklig. Ingen kan prioritera förbättringar i källsystemen. Ingen kan förklara vad ändrade registreringsrutiner betyder för modellen.

En praktisk tumregel är därför: inget AI-initiativ bör gå från idé till pilot utan att ha identifierat sina viktigaste informationsmängder och deras informationsägare.

## Datakvalitet är situationsberoende

Datakvalitet betyder inte att all information måste vara perfekt. Det betyder att informationen är tillräckligt bra för sitt avsedda syfte och att bristerna är kända.

För AI är detta viktigt eftersom olika användningsfall kräver olika kvalitet. En intern AI-assistent som hjälper en handläggare att hitta relevanta styrdokument kräver framför allt att dokumenten är aktuella, rätt versionerade och tydligt märkta. En modell som prioriterar kontrollobjekt kräver att historiska utfall är registrerade på ett konsekvent sätt. En analys av handelsmönster kräver att kodverk, tidsperioder och källor kan jämföras över tid.

Datakvalitet kan beskrivas genom flera dimensioner:

- **Korrekthet:** stämmer uppgifterna med verkligheten?
- **Fullständighet:** saknas viktiga fält eller händelser?
- **Aktualitet:** är informationen uppdaterad?
- **Konsekvens:** används samma definitioner och kodverk på samma sätt?
- **Spårbarhet:** går det att se var informationen kommer från?
- **Relevans:** är informationen användbar för det beslut eller den analys som ska stödjas?
- **Förklarbarhet:** går det att förstå vad informationen betyder?

Det strategiska arbetet handlar inte om att mäta allt överallt. Det handlar om att koppla datakvalitet till prioriterade AI-användningsfall. När NTG vill bygga ett stöd för riskbaserad kontroll behöver myndigheten veta vilka datakvalitetsbrister som påverkar just det stödet. När NTG vill införa en kunskapsassistent behöver myndigheten veta vilka dokument- och metadatafrågor som är mest kritiska.

## Metadata gör informationen användbar

Metadata är information om informationen. Det kan låta administrativt, men för AI är metadata ofta avgörande.

För dokument kan metadata beskriva dokumenttyp, version, giltighetstid, beslutsfattare, informationsklass, rättslig status, målgrupp och koppling till process. För ärendedata kan metadata beskriva källa, registreringstidpunkt, kvalitet, behörighetsnivå och relation till andra informationsmängder.

Utan metadata blir AI-lösningar blinda för sammanhang. En språkmodell kan läsa en text, men den vet inte automatiskt om texten är aktuell, beslutad, preliminär, sekretessbelagd eller ersatt av en ny version. En analysmodell kan bearbeta historiska rader, men den vet inte automatiskt när en kod ändrat betydelse.

I en myndighet kan detta få stora konsekvenser. Om en AI-assistent svarar utifrån gamla instruktioner kan den skapa fel i handläggning. Om en analysmodell blandar data före och efter en processändring kan den dra fel slutsatser. Om en lösning saknar informationsklassning kan känsliga uppgifter hamna i fel miljö.

Därför bör AI-strategin innehålla ett mål om bättre metadata för de informationsmängder som är strategiskt viktiga. Det behöver inte betyda ett stort metadataprogram från dag ett. Det kan börja med en enkel inventering: vilka informationsmängder används i våra prioriterade AI-initiativ, vilka metadata finns och vilka saknas?

## Informationsklassning och tillåten användning

AI-arbete måste också kopplas till informationsklassning och tillåten användning. Det gäller särskilt myndigheter med uppdrag inom brottsbekämpning, underrättelse och kontroll.

Alla data som finns i en myndighet är inte lämpliga att använda i alla AI-sammanhang. Vissa uppgifter omfattas av sekretess. Vissa får bara användas för särskilda ändamål. Vissa kräver särskilda behörigheter. Vissa kan användas för statistik och analys men inte för individuell påverkan. Vissa får användas internt men inte i externa molntjänster eller öppna AI-verktyg.

För NTG är detta centralt. Myndigheten kan ha uppgifter från deklarationer, underrättelsesamarbeten, operativa insatser, internationella partners och brottsutredningar. Att dessa uppgifter finns inom myndigheten betyder inte att de fritt kan kombineras eller användas för vilken AI-lösning som helst.

En verksamhetsstrateg bör därför se till att varje AI-initiativ kan svara på fyra frågor:

1. Vilka informationsmängder används?
2. Vilken klassning och rättslig grund gäller?
3. Vilken användning är tillåten?
4. Vilka tekniska och organisatoriska skydd krävs?

Detta är inte bara en juridisk kontroll. Det är en del av verksamhetsdesignen. Om ett användningsfall kräver information som inte får användas på det tänkta sättet behöver användningsfallet ändras, begränsas eller stoppas.

## Datastyrning som del av AI-governance

AI-governance och datastyrning bör inte byggas som två separata världar. AI-governance handlar om hur myndigheten styr AI-lösningar, ansvar, risker, beslut och uppföljning. Datastyrning handlar om hur myndigheten styr information, kvalitet, ägarskap och användning. I praktiken behöver de mötas.

En AI-styrmodell bör därför inkludera dataperspektivet i flera beslutspunkter:

- Vid idébedömning: finns nödvändiga informationsmängder?
- Vid prioritering: är datakvaliteten tillräcklig eller behöver den förbättras först?
- Vid pilotbeslut: finns informationsägare, klassning och tillåten användning?
- Vid produktionssättning: finns förvaltningsansvar för både AI-lösning och data?
- Vid uppföljning: mäts om datakvalitet eller processförändringar påverkar resultatet?

Detta skapar en viktig konsekvens: vissa AI-initiativ bör inte prioriteras som rena tekniska projekt. De bör prioriteras som kombinerade verksamhets-, data- och arkitekturinitiativ.

Om NTG vill förbättra riskbaserad kontroll kan det viktigaste första steget vara att förbättra registreringen av kontrollutfall. Om myndigheten vill skapa en kunskapsassistent kan det viktigaste första steget vara att skapa tydligare dokumentägarskap och versionshantering. Om myndigheten vill stödja underrättelseanalys kan det viktigaste första steget vara att kartlägga källor, sekretessnivåer och behörighetsmodeller.

## AI-redo information

En användbar målbild är att prata om AI-redo information. Det betyder inte att all information i myndigheten är perfekt, komplett eller omedelbart tillgänglig för AI. Det betyder att prioriterad information är tillräckligt beskriven, styrd och kvalitetssäkrad för de AI-användningsfall där den ska användas.

AI-redo information har några kännetecken:

- Den har en tydlig informationsägare.
- Den är kopplad till verksamhetsbegrepp och processer.
- Den har tillräcklig metadata.
- Den är informationsklassad.
- Tillåten användning är känd.
- Kvalitetsbrister är dokumenterade.
- Förändringar i källsystem och processer kan fångas upp.
- Den kan användas i en teknisk miljö som motsvarar säkerhets- och rättsliga krav.

För en myndighet är detta en mer realistisk målbild än att "samla all data på ett ställe". Vissa data ska inte samlas. Vissa data ska bara användas i särskilda miljöer. Vissa data behöver kunna analyseras utan att kopieras i onödan. AI-redo information handlar därför lika mycket om styrning och arkitektur som om datalagring.

## Genomgående exempel: NTG:s datafråga

NTG:s ledning har beslutat att myndigheten ska öka användningen av AI inom både legala flöden och brottsbekämpning. Tre initiativ lyfts fram:

- en AI-assistent för handläggarstöd,
- ett analysstöd för riskbaserad kontroll,
- ett stöd för underrättelsesammanställning.

På ytan ser initiativen ut som tre olika teknikprojekt. Men när verksamhetsarkitekten analyserar dem blir det tydligt att de delar flera datafrågor.

Handläggarassistenten kräver ordnade styrdokument, tydlig versionshantering och metadata om giltighet. Riskstödet kräver konsekvent registrerade kontrollutfall, historiska data och förståelse för urvalsbias. Underrättelsestödet kräver behörighetsstyrning, källhantering, sekretessbedömning och spårbarhet.

Arkitektens slutsats blir att NTG inte bara behöver tre AI-piloter. Myndigheten behöver ett gemensamt förbättringsspår för AI-redo information. Det spåret omfattar informationsägarskap, prioriterade informationsmängder, metadata, klassning och datakvalitet.

Detta förändrar ledningens bild. AI-arbetet blir inte bara en fråga om att köpa eller bygga lösningar. Det blir en fråga om att stärka myndighetens informationsförmåga.

## Vanliga misstag

- **Misstag: Att börja med verktyget i stället för informationen.**
  - Varför det händer: AI-verktyg är synliga och lätta att demonstrera.
  - Hur du undviker det: Kräv att varje AI-initiativ beskriver sina viktigaste informationsmängder och informationsägare.

- **Misstag: Att tro att mer data alltid är bättre.**
  - Varför det händer: AI förknippas ofta med stora datamängder.
  - Hur du undviker det: Utgå från användningsfallet och fråga vilken information som är relevant, tillåten och tillräckligt kvalitetssäkrad.

- **Misstag: Att behandla datakvalitet som en generell IT-fråga.**
  - Varför det händer: Datakvalitet ses ofta som något tekniskt eller administrativt.
  - Hur du undviker det: Koppla datakvalitet till beslut, risker, verksamhetsnytta och ansvar.

- **Misstag: Att sakna metadata för dokument och kunskapskällor.**
  - Varför det händer: Dokumenthantering har ofta byggts för människor, inte för AI-assistenter.
  - Hur du undviker det: Börja med dokumentstatus, ägare, giltighet, version och informationsklassning.

- **Misstag: Att inte involvera informationsägare tidigt.**
  - Varför det händer: AI-initiativ drivs ibland som teknikpiloter.
  - Hur du undviker det: Gör informationsägare till obligatoriska deltagare i idébedömning och pilotförberedelse.

## Reflektionsfrågor

1. Vilka informationsmängder är mest strategiska för AI i din myndighet?
2. Finns tydliga informationsägare för dessa informationsmängder?
3. Vilka datakvalitetsbrister skulle kunna ge felaktiga AI-resultat?
4. Vilka dokument eller kunskapskällor skulle behöva bättre metadata innan de används av generativ AI?
5. Vilka informationsmängder får inte användas fritt, även om de tekniskt sett är tillgängliga?
6. Vilka AI-initiativ borde kanske börja som informationsförvaltningsinitiativ?

## Datamognad: från informationslager till AI-redo information

Datamognad handlar inte om hur mycket data myndigheten har. Det handlar om hur väl informationen kan förstås, delas, kvalitetssäkras, skyddas och användas i rätt sammanhang. För AI-arbete kan datamognad beskrivas i fem nivåer:

| Nivå | Datamognad | Kännetecken |
|---|---|---|
| 1. Fragmenterad | Data finns i silor och förstås lokalt | Begrepp, kvalitet och ägarskap varierar mellan enheter |
| 2. Kartlagd | Centrala informationsmängder är identifierade | Myndigheten vet vilka data som är viktiga men använder dem ojämnt |
| 3. Styrd | Informationsägare, metadata och kvalitetskrav är etablerade | Data kan användas mer kontrollerat i prioriterade AI-initiativ |
| 4. Återanvändbar | Informationsprodukter och gemensamma begrepp stödjer flera användningsfall | AI-lösningar kan byggas snabbare och säkrare |
| 5. Lärande | Datakvalitet, användning och risk följs upp löpande | Informationsförvaltningen utvecklas tillsammans med verksamhetsnyttan |

En viktig konsekvens är att AI-portföljen bör prioriteras utifrån datamognad, inte bara verksamhetsnytta. Ett användningsfall med mycket hög tänkt nytta kan behöva senareläggas om informationen är splittrad, oklassad eller saknar tydligt ägarskap. Omvänt kan ett mindre spektakulärt användningsfall vara lämpligt tidigt om informationen är väl förvaltad och riskerna är begripliga.

För NTG innebär detta att information om legala varuflöden, tillstånd och deklarationer kan ha en annan mognadsprofil än underrättelseinformation, beslagshistorik eller samverkansinformation från andra aktörer. En gemensam datamognadsbedömning hjälper myndigheten att välja rätt startpunkt och att formulera förbättringsåtgärder innan AI-lösningen byggs.

## Snabb sammanfattning

- AI bygger på information, men all information är inte automatiskt användbar för AI.
- Informationsförvaltning, datakvalitet och metadata är strategiska förutsättningar för AI.
- Informationsägarskap behöver vara praktiskt, inte bara formellt.
- Datakvalitet ska bedömas utifrån användningsfall, inte som ett abstrakt ideal.
- Informationsklassning och tillåten användning är särskilt viktiga i myndigheter med brottsbekämpande uppdrag.
- AI-governance och datastyrning behöver kopplas samman.
- En realistisk målbild är AI-redo information för prioriterade användningsfall.

## Nästa steg

När informationen är kartlagd och de viktigaste dataförutsättningarna är synliga kan myndigheten gå vidare till att identifiera konkreta AI-möjligheter. Nästa kapitel visar hur verksamhetsstrategen och verksamhetsarkitekten kan hitta relevanta möjligheter genom processanalys, informationsanalys, problembilder och verksamhetsmål.
