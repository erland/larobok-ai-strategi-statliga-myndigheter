# Kapitel 8: Informationssäkerhet, etik och tillit

## Varför detta kapitel finns

AI-strategi i en statlig myndighet kan inte skiljas från informationssäkerhet, etik och tillit. Det gäller särskilt när myndigheten hanterar både legala flöden och brottsbekämpande verksamhet. För Nordiska Tull- och Gränsmyndigheten, NTG, kan samma övergripande teknikidé påverka allt från företagsservice och deklarationsgranskning till underrättelseanalys och operativ kontroll. Det gör att frågan inte bara är om AI kan skapa nytta, utan också om myndigheten kan använda AI på ett sätt som är säkert, rättssäkert, begripligt och förtroendeskapande.

I tidigare kapitel har vi beskrivit AI-strategi, målbild, governance och juridiska ramar. Det här kapitlet bygger vidare på dessa delar och fokuserar på tre frågor som ofta avgör om AI-arbetet kan gå från idé till faktisk verksamhetsförmåga:

- Hur skyddar vi information, system och verksamhetskritiska processer?
- Hur säkerställer vi att AI används på ett etiskt och ansvarsfullt sätt?
- Hur bygger vi tillit hos medarbetare, ledning, samverkansparter, företag och allmänhet?

Kapitlet är skrivet för verksamhetsstrateger och verksamhetsarkitekter. Det betyder att vi inte går djupt in i tekniska säkerhetslösningar. Fokus ligger i stället på hur informationssäkerhet, etik och tillit behöver förstås, organiseras och byggas in i AI-arbetets styrning, arkitektur och införande.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara varför informationssäkerhet behöver vara en strategisk fråga i AI-arbetet,
- beskriva skillnaden mellan dataskydd, informationssäkerhet och verksamhetsskydd,
- identifiera typiska säkerhetsrisker vid AI-användning i en myndighet,
- resonera om etik som praktiskt beslutsstöd, inte bara som värdeord,
- beskriva hur tillit byggs genom transparens, kontroll, ansvar och uppföljning,
- vägleda ledning och utvecklingsorganisation i hur AI-initiativ kan prövas innan de införs.

## Innan vi börjar

Det är lätt att behandla informationssäkerhet och etik som hinder som dyker upp sent i ett projekt. Då blir de något som ska godkännas efter att lösningen redan är vald. För AI är det ett riskabelt arbetssätt. AI-system bygger ofta på stora mängder data, komplexa beroenden, externa tjänster, statistiska bedömningar och nya användarbeteenden. Om säkerhet och etik kommer in för sent kan myndigheten redan ha bundit sig vid en lösning som är svår att förklara, svår att kontrollera eller olämplig för den aktuella verksamheten.

Ett bättre arbetssätt är att se informationssäkerhet, etik och tillit som designvillkor. De ska inte bara granskas i slutet. De ska påverka hur problemet formuleras, vilka data som används, vilken lösningstyp som väljs, hur ansvar fördelas, hur piloten utformas och hur införandet följs upp.

För en verksamhetsstrateg eller verksamhetsarkitekt innebär det att frågorna behöver lyftas tidigt och konkret. Det räcker inte att säga att ett initiativ ska vara säkert och etiskt. Man behöver kunna beskriva vad det betyder för just den användningen.

## Tre nivåer av skydd

När en myndighet diskuterar AI blandas ofta flera skyddsfrågor ihop. Det kan leda till otydliga beslut. Ett AI-initiativ kan vara juridiskt möjligt men säkerhetsmässigt olämpligt. Det kan vara informationssäkerhetsmässigt hanterbart men etiskt problematiskt. Det kan vara tekniskt säkert men ändå skada förtroendet för myndigheten.

Ett praktiskt sätt att skapa ordning är att skilja mellan tre nivåer av skydd.

### Dataskydd

Dataskydd handlar om skydd för enskilda personers uppgifter och rättigheter. I AI-arbete blir dataskydd relevant när personuppgifter används för analys, träning, test, drift, uppföljning eller kvalitetssäkring. Frågor om ändamål, rättslig grund, dataminimering, lagring, åtkomst och transparens blir centrala.

För NTG kan dataskydd bli aktuellt i både legala flöden och brottsbekämpande verksamhet. Ett stöd för att analysera deklarationer kan behandla uppgifter om företag, företrädare och transportörer. Ett underrättelsestöd kan hantera betydligt känsligare information om personer, nätverk, misstänkta mönster och samverkansdata.

### Informationssäkerhet

Informationssäkerhet handlar om att skydda informationens konfidentialitet, riktighet och tillgänglighet. För AI betyder det bland annat att rätt personer ska ha rätt åtkomst, att data inte får manipuleras, att modeller och utdata måste kunna kontrolleras och att systemet ska fungera även när belastning, incidenter eller fel uppstår.

För NTG kan informationssäkerhet handla om att en AI-lösning inte får läcka underrättelseinformation, att riskmodeller inte får påverkas av felaktig eller manipulerad data och att ett stöd för kontrollprioritering inte får bli otillgängligt i kritiska lägen.

### Verksamhetsskydd

Verksamhetsskydd handlar om att skydda myndighetens uppdrag, förmåga och förtroende. Ett AI-system kan vara tekniskt säkert men ändå skapa verksamhetsrisker om det leder till fel prioriteringar, otydliga ansvarsförhållanden eller minskat förtroende från berörda aktörer.

För NTG kan ett felaktigt utformat AI-stöd påverka handelsflöden, rättssäkerhet, brottsbekämpning och samverkan med andra myndigheter. Därför måste skyddsfrågan alltid kopplas till verksamhetskonsekvens, inte bara till teknisk risk.

## AI förändrar hotbilden

AI skapar inte en helt ny säkerhetsvärld, men AI förändrar flera risker. Vissa risker förstärks eftersom AI-lösningar ofta använder stora datamängder och många beroenden. Andra risker uppstår genom nya arbetssätt, till exempel när medarbetare använder generativa AI-tjänster för att sammanfatta, formulera eller analysera material.

För en myndighet som NTG är följande riskområden särskilt viktiga.

### Oavsiktlig informationsdelning

Generativa AI-tjänster kan kännas som vanliga skriv- eller sökverktyg. Det gör att användare kan frestas att klistra in information som inte får lämna myndighetens kontrollerade miljö. Det kan gälla känsliga ärenden, personuppgifter, underrättelseinformation, interna bedömningar eller säkerhetsklassad information.

Den strategiska frågan är inte bara vilka verktyg som är tillåtna. Den är också hur medarbetarna förstår skillnaden mellan öppna, interna och skyddade AI-miljöer. En policy som ingen förstår skapar inte säkerhet. En tydlig användningsmodell, däremot, kan hjälpa medarbetare att göra rätt.

### Manipulerad eller lågkvalitativ data

AI-system är beroende av data. Om data är felaktig, ofullständig, snedvriden eller manipulerad kan resultatet bli missvisande. I brottsbekämpande sammanhang kan detta få allvarliga konsekvenser. Ett riskstöd som bygger på bristfälliga historiska data kan förstärka gamla prioriteringsmönster. Ett analysstöd som påverkas av manipulerad information kan rikta uppmärksamhet åt fel håll.

Verksamhetsarkitekten behöver därför fråga hur datakällor förvaltas, kvalitetssäkras och spåras. Det räcker inte att fråga om data finns. Man behöver veta om data är lämplig för den användning som föreslås.

### Modell- och leverantörsberoenden

Många AI-lösningar bygger på externa modeller, plattformar eller molntjänster. Det kan vara rimligt och effektivt, men det skapar beroenden. Myndigheten behöver förstå var data behandlas, vem som kan påverka modellen, hur ändringar hanteras, hur loggning fungerar och vilka möjligheter som finns att granska, byta eller avveckla lösningen.

För NTG kan samma leverantörsberoende vara acceptabelt för ett internt språkstöd men olämpligt för ett underrättelsenära analysstöd. Det är användningen, informationen och konsekvensen som avgör.

### Övertro på AI-resultat

En av de största riskerna är inte att AI ger ett felaktigt svar, utan att människor behandlar svaret som mer tillförlitligt än det är. Detta kallas ofta automation bias. I praktiken innebär det att användare kan luta sig för mycket mot systemets rekommendationer, särskilt om de presenteras med hög precision eller auktoritativt språk.

För NTG är detta viktigt i kontrollprioritering, ärendegranskning och underrättelseanalys. Ett AI-stöd kan peka ut mönster, men det får inte ersätta professionell bedömning där sådan krävs. Mänsklig kontroll behöver vara verklig, inte bara formell.

## Etik som praktiskt beslutsstöd

Etik i AI-sammanhang blir ibland abstrakt. Organisationer skriver att AI ska vara rättvis, transparent, ansvarsfull och människocentrerad. Det är bra som riktning, men det hjälper inte alltid ett projektteam som ska fatta konkreta beslut om data, användning, gränssnitt och införande.

För att etik ska bli användbar behöver den översättas till frågor som kan påverka beslut. En verksamhetsstrateg kan använda följande frågeområden.

### Är användningen rimlig i relation till uppdraget?

AI bör kopplas till myndighetens uppdrag och lagliga ansvar. Bara för att något är tekniskt möjligt betyder det inte att det är lämpligt. Frågan är om användningen stärker myndighetens förmåga på ett sätt som är proportionerligt, begripligt och förenligt med förtroendet för myndigheten.

För NTG kan AI för dokumentgranskning i legala flöden vara relativt lätt att motivera om syftet är snabbare handläggning och bättre kvalitet. AI för att analysera personkopplingar i underrättelsearbete kräver en betydligt djupare etisk och rättslig prövning.

### Vem påverkas om systemet har fel?

Etik blir konkret när man frågar vem som bär konsekvensen av fel. Påverkas en handläggare, ett företag, en privatperson, en misstänkt person, en samverkanspart eller allmänhetens förtroende? Ju större konsekvens för enskilda eller samhällsviktiga funktioner, desto starkare krav bör ställas på kontroll, dokumentation, mänsklig bedömning och möjlighet till uppföljning.

### Finns risk för osaklig eller förstärkt snedvridning?

AI kan förstärka mönster i befintliga data. Om historiska beslut, kontroller eller prioriteringar har varit ojämnt fördelade kan AI lära sig att återskapa dessa mönster. Det betyder inte att AI alltid blir diskriminerande, men det betyder att myndigheten måste förstå vilka mönster som finns i data och vad de representerar.

För NTG kan exempelvis kontrollhistorik spegla tidigare prioriteringar, resurstillgång, tips, kampanjer och internationell samverkan. Den behöver inte vara en neutral bild av risk. En AI-modell som använder sådan historik måste därför prövas kritiskt.

### Kan användningen förklaras för berörda aktörer?

All AI-användning behöver inte vara fullt transparent i varje detalj, särskilt inte i brottsbekämpande verksamhet. Men myndigheten behöver kunna förklara principer, ansvar, kontrollmekanismer och gränser. Ledningen behöver förstå vad systemet gör. Användarna behöver förstå hur det ska användas. Granskande funktioner behöver kunna följa beslut och avvägningar.

Förklarbarhet handlar därför inte bara om teknisk modellförklaring. Det handlar om organisatorisk begriplighet.

## Tillit byggs genom styrning och beteende

Tillit skapas inte genom att myndigheten säger att AI är säkert. Tillit skapas när människor ser att myndigheten har kontroll, tar ansvar, följer upp effekter och kan korrigera fel. Det gäller både intern och extern tillit.

### Intern tillit

Medarbetare behöver förstå varför AI införs, hur deras professionella bedömning påverkas och vilka gränser som gäller. Om AI beskrivs som ett sätt att ersätta kompetens riskerar organisationen motstånd eller passiv användning. Om AI i stället beskrivs som ett stöd för kvalitet, prioritering, analys och avlastning kan tilliten bli större.

För NTG:s handläggare, analytiker och kontrollpersonal är det viktigt att AI inte bara införs som ett centralt tekniskt beslut. Användarna behöver vara delaktiga i att pröva resultat, identifiera felkällor och forma arbetssätt.

### Ledningens tillit

Ledningen behöver kunna fatta informerade beslut om AI. Det kräver underlag som visar nytta, risk, kostnad, ansvar, beroenden och uppföljning. Ett AI-initiativ som endast presenteras som innovation blir svårt att styra. Ett AI-initiativ som presenteras som verksamhetsförändring blir möjligt att leda.

Verksamhetsstrategens roll är att hjälpa ledningen att se både möjligheter och villkor. Det innebär att kunna säga: detta kan skapa stor nytta, men bara om vi samtidigt investerar i dataförvaltning, kompetens, informationssäkerhet och uppföljning.

### Extern tillit

Företag, medborgare, samverkansparter och allmänhet behöver kunna lita på att myndigheten använder AI ansvarsfullt. I legala flöden kan det handla om att företag förstår varför vissa kontroller sker och hur automatisering påverkar service och handläggning. I brottsbekämpande verksamhet kan full insyn vara begränsad, men ansvar, rättssäkerhet och kontrollmekanismer måste ändå finnas.

Extern tillit kräver därför en medveten kommunikationsstrategi. Myndigheten behöver kunna beskriva vad AI används till, vad AI inte används till, hur mänsklig kontroll fungerar och hur fel hanteras.

## NTG:s säkerhets- och etikprövning

NTG överväger att införa ett AI-stöd som sammanställer information inför kontrollprioritering. Stödet ska kunna kombinera deklarationsdata, tidigare kontrollutfall, öppna informationskällor och interna underrättelsebedömningar. På ytan är detta ett tydligt nyttocase: bättre prioritering, snabbare analys och mer träffsäkra kontroller.

Men när verksamhetsarkitekten kartlägger användningen visar det sig att initiativet innehåller flera olika delanvändningar:

- sammanfattning av ärendeinformation för handläggare,
- riskindikatorer i legala varuflöden,
- underrättelsenära analys av aktörer och mönster,
- beslutsstöd inför operativ kontroll,
- uppföljning av kontrollutfall.

Varje delanvändning har olika riskprofil. En sammanfattningsfunktion kan vara relativt låg risk om den används internt, bygger på redan tillgänglig information och tydligt visar källor. Underrättelsenära analys kräver däremot strikt åtkomststyrning, loggning, ändamålsbegränsning, mänsklig bedömning och tydliga regler för hur resultat får användas. Operativ kontrollprioritering kräver särskild prövning eftersom fel kan påverka både rättssäkerhet och resursanvändning.

NTG väljer därför att inte behandla initiativet som ett enda AI-projekt. Myndigheten delar upp det i flera användningsfall och prövar varje del utifrån nytta, informationsklassning, dataskydd, etisk risk, mänsklig kontroll och förvaltningsansvar. Det gör arbetet långsammare i början, men minskar risken för att myndigheten bygger ett system som senare inte kan införas.

## En praktisk prövningsmodell

För att stödja AI-governance kan myndigheten använda en enkel prövningsmodell innan ett AI-initiativ går vidare till pilot. Modellen behöver inte ersätta juridisk granskning, informationssäkerhetsklassning eller arkitekturgranskning. Den fungerar som ett gemensamt första filter.

| Frågeområde | Nyckelfråga | Varför det spelar roll |
|---|---|---|
| Uppdrag | Är användningen tydligt kopplad till myndighetens uppdrag? | Hindrar teknikdriven lösningsjakt |
| Information | Vilken information används och hur känslig är den? | Avgör skyddsnivå och åtkomst |
| Påverkan | Vem påverkas om systemet ger fel stöd? | Styr krav på kontroll och uppföljning |
| Mänsklig kontroll | Var krävs professionell bedömning? | Motverkar övertro och ansvarsglidning |
| Förklarbarhet | Kan användningen beskrivas begripligt? | Stärker styrning och tillit |
| Leverantör | Vilka externa beroenden finns? | Påverkar säkerhet, kostnad och kontroll |
| Uppföljning | Hur mäts nytta, kvalitet och risk över tid? | Gör införandet styrbart |

Prövningsmodellen bör användas tidigt. Den ska inte ses som en blankett som fylls i efter att projektet redan är beslutat. Den ska hjälpa organisationen att välja rätt väg: avstå, utreda mer, genomföra begränsad pilot eller gå vidare mot införande.

## Arkitekturens roll

Verksamhetsarkitektur kan göra säkerhets- och etikfrågor konkreta. Det sker genom att koppla AI-användning till förmågor, information, processer, roller, system och styrning. I stället för att fråga om en AI-lösning är säker i allmänhet kan arkitekten fråga:

- I vilken verksamhetsförmåga används AI-stödet?
- Vilka beslut, bedömningar eller prioriteringar påverkas?
- Vilken information används, skapas och lagras?
- Vilka roller får se, ändra, godkänna eller följa upp resultat?
- Vilka befintliga kontroller påverkas?
- Vilka nya beroenden skapas?
- Hur avvecklas eller pausas stödet om riskerna ökar?

Denna typ av frågor hjälper myndigheten att undvika ett vanligt misstag: att AI diskuteras som ett fristående system. I praktiken blir AI en del av verksamhetsarkitekturen. Det påverkar arbetssätt, information, ansvar och styrning.

## Vanliga misstag

- **Misstag: Att se informationssäkerhet som ett slutgodkännande.**
  - Varför det händer: Projekt vill snabbt visa teknisk möjlighet och tar in säkerhetsfrågor sent.
  - Hur du undviker det: Gör informationssäkerhet till ett designvillkor redan när användningsfallet formuleras.

- **Misstag: Att använda samma risknivå för alla AI-initiativ.**
  - Varför det händer: Organisationen vill ha en enkel och enhetlig process.
  - Hur du undviker det: Använd riskbaserad styrning där låg, medel och hög risk får olika krav.

- **Misstag: Att förväxla juridisk möjlighet med strategisk lämplighet.**
  - Varför det händer: När en jurist säger att något kan vara möjligt tolkas det som att det bör göras.
  - Hur du undviker det: Pröva även etik, tillit, verksamhetskonsekvens och långsiktig förmåga.

- **Misstag: Att glömma användarnas beteende.**
  - Varför det händer: Fokus hamnar på systemet, inte på hur människor faktiskt använder det.
  - Hur du undviker det: Utforma arbetssätt, utbildning, gränser och uppföljning tillsammans med användarna.

- **Misstag: Att kommunicera AI som magi eller hot.**
  - Varför det händer: AI väcker starka förväntningar och oro.
  - Hur du undviker det: Beskriv konkret vad AI gör, vad det inte gör, vem som ansvarar och hur resultat följs upp.

## Reflektionsfrågor för ledning och styrforum

1. Vilka typer av information får användas i olika AI-miljöer?
2. Vilka AI-användningar kräver särskild säkerhetsprövning innan pilot?
3. Var i våra processer finns risk att AI-resultat får för stor praktisk påverkan?
4. Vilka användningsfall kräver tydligare mänsklig kontroll?
5. Vilka externa beroenden är acceptabla för legala flöden men olämpliga för brottsbekämpande verksamhet?
6. Hur ska vi kommunicera AI-användning internt och externt på ett förtroendeskapande sätt?
7. Hur följer vi upp om AI-stödet leder till oönskade effekter?

## Tillit byggs genom användbar kontroll
Tillit till AI uppstår inte genom att myndigheten säger att lösningen är säker. Tillit uppstår när kontrollen är begriplig, användbar och integrerad i arbetssättet. Handläggare, analytiker och chefer behöver förstå när AI-stödet är relevant, när det ska ifrågasättas och hur avvikelser ska hanteras.

För NTG kan detta betyda att ett AI-stöd för riskanalys alltid visar vilken typ av faktorer som påverkat en rekommendation, vilken osäkerhet som finns och vilka steg användaren måste dokumentera innan en åtgärd vidtas. Det räcker inte med att modellen ger en poäng eller prioritet. Verksamheten behöver kunna arbeta med resultatet på ett rättssäkert sätt.

En bra kontrollmiljö kombinerar därför:

- tekniska skydd,
- organisatoriska roller,
- dokumenterade arbetssätt,
- utbildning,
- spårbarhet,
- uppföljning av fel och avvikelser.

Det är först när dessa delar samverkar som AI kan användas i känsliga myndighetsprocesser med rimlig tillit.

## Mognad i risk, etik och tillit

Tillit till AI kan inte beslutas fram. Den behöver byggas stegvis genom ökande mognad i styrning, riskhantering och praktiskt beteende. Ett enkelt sätt att bedöma läget är att skilja mellan fem nivåer:

| Nivå | Risk- och tillitsmognad | Typiskt beteende |
|---|---|---|
| 1. Reaktiv | Risker upptäcks sent eller efter incidenter | Varje initiativ hanterar frågorna själv |
| 2. Grundläggande | Det finns checklistor och enskilda prövningar | Risker hanteras men inte alltid jämförbart |
| 3. Integrerad | Risk, etik, dataskydd och informationssäkerhet ingår i ordinarie AI-styrning | Styrforum kan fatta avvägda beslut |
| 4. Förutsägbar | Roller, metoder och kontroller är etablerade och återanvänds | Nya initiativ startar med tydliga skyddskrav |
| 5. Lärande | Incidenter, avvikelser och användarerfarenheter leder till förbättrad styrning | Tillit utvecklas genom uppföljning över tid |

För verksamhetsstrategen och verksamhetsarkitekten är poängen inte att skapa ännu en administrativ modell. Poängen är att kunna se om myndigheten har tillräcklig mognad för den typ av AI-användning som diskuteras. Ett lågriskstöd för intern dokumentklassificering kan kräva en annan mognadsnivå än ett beslutsstöd i brottsbekämpande underrättelsearbete.

Vid NTG kan exempelvis generativ AI för intern kunskapssökning införas med relativt begränsad risk om informationen är rätt klassad, källorna är spårbara och användaren får tydliga instruktioner. Ett AI-stöd som påverkar riskurval i kontroller kräver däremot högre mognad i dokumentation, uppföljning, förklarbarhet och ansvarsfördelning.

## Snabb sammanfattning

- Informationssäkerhet, etik och tillit är strategiska villkor för AI, inte sena kontrollpunkter.
- Dataskydd, informationssäkerhet och verksamhetsskydd behöver hållas isär men hanteras samordnat.
- AI förändrar riskbilden genom stora datamängder, externa beroenden, nya användarbeteenden och risk för övertro.
- Etik blir användbar först när den översätts till konkreta beslut om uppdrag, påverkan, data, förklarbarhet och kontroll.
- Tillit byggs genom tydligt ansvar, mänsklig kontroll, uppföljning och begriplig kommunikation.
- NTG:s AI-initiativ bör delas upp i separata användningsfall eftersom legala flöden och brottsbekämpande verksamhet har olika riskprofil.
- Verksamhetsarkitektur hjälper myndigheten att placera AI i rätt sammanhang och göra skyddsfrågor konkreta.

## Nästa steg

När informationssäkerhet, etik och tillit är integrerade i styrningen kan myndigheten börja arbeta mer aktivt med möjlighetsidentifiering. Nästa kapitel handlar därför om hur verksamhetsstrategen och verksamhetsarkitekten kan hitta AI-möjligheter i processer, informationsflöden, beslutsstöd, samverkan och verksamhetsförmågor utan att fastna i teknikdrivna idéer.
