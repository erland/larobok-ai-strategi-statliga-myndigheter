# Kapitel 13: Genomföra piloter

## Varför detta kapitel finns

När en myndighet har formulerat strategi, målbild, styrning och portfölj uppstår en avgörande fråga: hur ska AI-principerna prövas i verkligheten utan att myndigheten går för fort fram, tappar kontroll eller fastnar i eviga förstudier?

Piloter är ofta svaret, men bara om de utformas rätt. En AI-pilot är inte en teknisk demonstration som visar att en modell kan producera ett imponerande resultat i ett avgränsat test. För en statlig myndighet behöver piloten visa om ett AI-stöd kan skapa verklig nytta i en kontrollerad verksamhetsmiljö, med rätt data, rätt ansvar, rätt arbetssätt och rätt riskhantering.

Det här kapitlet hjälper dig att se piloten som ett strategiskt lärandeformat. Piloten ska inte bara svara på frågan om tekniken fungerar. Den ska också svara på frågor om verksamheten är redo, om rättsliga och säkerhetsmässiga krav kan hanteras, om användarna förstår stödet, om ledningen får ett tillförlitligt beslutsunderlag och om lösningen har förutsättningar att bli en förmåga.

I Nordiska Tull- och Gränsmyndigheten, NTG, vill ledningen genomföra en första AI-pilot som stöd för dokumentgranskning i legala varuflöden. Samtidigt finns intresse för att pröva generativ AI som stöd för underrättelsesammanställningar. Båda idéerna verkar lovande. Men de har olika riskprofil, olika databehov, olika juridiska frågor och olika krav på mänsklig kontroll. Kapitlet visar hur NTG kan gå från entusiasm till en genomtänkt pilotdesign.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara skillnaden mellan en teknisk proof of concept, en verksamhetspilot och en förmågepilot,
- formulera tydliga hypoteser för vad en AI-pilot ska lära myndigheten,
- avgränsa pilotens omfattning, data, användare, beslutspåverkan och risknivå,
- beskriva vilka roller som behöver delta i en AI-pilot,
- välja mätetal som fångar nytta, kvalitet, risk, användbarhet och införbarhet,
- avgöra när en pilot bör skalas, göras om, pausas eller avslutas.

## Innan vi börjar

De tidigare kapitlen har byggt upp flera byggstenar som behövs här. AI-strategin anger varför myndigheten ska arbeta med AI. Målbilden beskriver vilka förmågor som ska utvecklas. Governance-modellen anger hur beslut, ansvar och kontroll ska fungera. Juridik, informationssäkerhet och etik ger ramar för vad som behöver prövas innan AI används i skarp verksamhet. Portföljen samlar initiativen och visar vilka beroenden som finns.

Piloten är den punkt där dessa byggstenar möter verkligheten. Därför bör piloten inte startas som ett isolerat experiment i en utvecklingsgrupp. Den bör vara en medvetet vald del av AI-portföljen, med en tydlig koppling till målbild och styrning.

En användbar utgångspunkt är att piloten ska besvara tre frågor:

- Skapar detta AI-stöd tillräcklig verksamhetsnytta?
- Kan stödet användas ansvarsfullt, säkert och rättssäkert?
- Har myndigheten förutsättningar att förvalta och skala lösningen?

Om piloten inte kan ge svar på dessa frågor riskerar den att bli en tillfällig demonstration snarare än ett steg mot verksamhetsförmåga.

## Vad en AI-pilot egentligen ska testa

Många organisationer använder ordet pilot när de egentligen menar väldigt olika saker. I AI-sammanhang är det viktigt att vara tydlig, eftersom olika typer av piloter kräver olika beslut och olika kontroll.

### Proof of concept

En proof of concept testar om en idé är tekniskt möjlig. Den kan genomföras med begränsad data, få användare och en tydligt avgränsad frågeställning. Syftet är inte att visa full verksamhetsnytta, utan att minska osäkerhet kring teknik, data eller modellens grundläggande förmåga.

För NTG kan en proof of concept vara att undersöka om en språkmodell kan sammanfatta vissa typer av importdokument på ett begripligt sätt. Testet kan visa om dokumentstrukturen går att tolka och om sammanfattningarna håller tillräcklig språklig kvalitet för vidare prövning.

Det är däremot inte ett bevis för att stödet bör användas i handläggning. Där krävs fler frågor: vilka dokument får behandlas, vilka fel kan uppstå, hur påverkas kontrollprocessen, vem ansvarar för bedömningen och hur ska kvaliteten följas upp?

### Verksamhetspilot

En verksamhetspilot testar om AI-stödet fungerar i ett verkligt eller verklighetsnära arbetsflöde. Här prövas inte bara tekniken utan också användarnas arbetssätt, ansvarsfördelning, datatillgång, styrning, uppföljning och mottaglighet.

För NTG kan en verksamhetspilot innebära att ett begränsat antal handläggare använder ett AI-stöd för att prioritera dokument som bör granskas närmare. Handläggaren fattar fortfarande beslut om granskning, men AI-stödet föreslår en sortering eller markerar avvikelser. Piloten behöver då mäta både om handläggarna sparar tid och om kvaliteten i urvalet förbättras utan oönskad snedvridning.

### Förmågepilot

En förmågepilot testar om myndigheten kan bygga en återanvändbar förmåga, inte bara ett enskilt stöd. Då blir frågorna bredare: finns styrning, dataflöden, teknisk plattform, kompetens, förvaltningsmodell och uppföljning som kan återanvändas i fler AI-initiativ?

För NTG kan en förmågepilot vara att etablera ett gemensamt mönster för AI-stödd dokumentanalys som senare kan användas både i legala flöden och i brottsbekämpande analys, men med olika rättsliga ramar och åtkomstregler. Syftet blir då inte bara ett enskilt pilotresultat, utan lärande om arkitektur, governance och skalbarhet.

## Börja med hypoteser, inte lösningar

En vanlig svaghet i AI-piloter är att de startar med en lösning: vi vill testa en språkmodell, ett analysverktyg eller en automatiseringsplattform. Det är mer användbart att börja med hypoteser.

En hypotes är ett tydligt antagande som piloten ska pröva. Den bör formuleras så att det går att avgöra om den får stöd eller inte.

Exempel på hypoteser för NTG:s dokumentgranskningspilot:

- Handläggare kan minska tiden för första dokumentgenomgång med minst 25 procent utan att kvaliteten i bedömningen försämras.
- AI-stödet kan identifiera återkommande dokumentavvikelser med tillräcklig precision för att fungera som prioriteringsstöd.
- Användarna upplever stödet som begripligt och kontrollerbart när källor, markeringar och osäkerhet visas tydligt.
- Juridiska och informationssäkerhetsmässiga krav kan hanteras med avgränsad datamängd, loggning, åtkomststyrning och mänsklig kontroll.
- Pilotens tekniska mönster kan återanvändas i minst två andra användningsfall utan större ombyggnad.

Hypoteserna gör piloten styrbar. De hjälper ledningen att förstå vad piloten ska bevisa, och de hjälper projektgruppen att undvika att lägga tid på funktioner som inte besvarar de viktigaste frågorna.

## Piloter med generativ AI

Piloter med generativ AI behöver ofta utformas annorlunda än piloter med mer traditionell analys-AI. Det beror på att användarna snabbt kan uppleva lösningen som användbar även när kvalitet, källor och ansvar ännu inte är tillräckligt säkrade. En generativ AI-pilot ska därför inte bara testa om modellen kan skapa ett bra svar, utan om myndigheten kan använda svaren på ett kontrollerat sätt.

En bra pilot bör särskilja mellan tre lager:

- **Informationslagret:** vilka dokument, data och kunskapskällor får lösningen använda?
- **Interaktionslagret:** hur ställer användaren frågor, får svar, ser källor och lämnar återkoppling?
- **Styrningslagret:** hur hanteras loggning, behörighet, kvalitetssäkring, avvikelser, incidenter och ansvar?

För NTG kan en lämplig generativ AI-pilot vara en intern kunskapsassistent för handläggare som svarar utifrån ett begränsat urval av godkända vägledningar. Piloten bör då mäta mer än tidsbesparing. Den bör också mäta om handläggarna förstår svarens begränsningar, om källhänvisningarna är användbara, om fel upptäcks och om informationsägaren kan förvalta kunskapsunderlaget.

Undvik att starta med det mest känsliga användningsfallet. En pilot som berör brottsbekämpande underrättelsearbete, personuppgifter eller operativ prioritering kan vara viktig på sikt, men bör inte vara första steget om myndigheten ännu saknar erfarenhet av källstyrning, testmetodik och mänsklig kontroll för generativ AI.

## Avgränsa pilotens omfattning

En AI-pilot ska vara tillräckligt liten för att vara hanterbar men tillräckligt verklig för att ge relevant lärande. För snäv avgränsning ger ett snyggt test som inte säger mycket om verksamheten. För bred avgränsning ger risk för oklar styrning, svag uppföljning och för många beroenden.

En praktisk avgränsning bör beskriva minst sex delar.

### Verksamhetsområde

Vilken process, förmåga eller arbetsuppgift berörs? För NTG kan det vara dokumentgranskning av en viss typ av varuflöde, underrättelsesammanställning inom ett avgränsat ämnesområde eller prognosstöd för resursplanering i ett visst geografiskt område.

### Användare

Vilka roller använder stödet? Är det handläggare, analytiker, chefer, jurister, underrättelsepersonal eller verksamhetsutvecklare? Ju mer känsligt användningsfallet är, desto viktigare är att användarna har rätt kompetens och mandat.

### Data

Vilka informationsmängder används? Är data historisk, syntetisk, anonymiserad, pseudonymiserad eller skarp? Finns personuppgifter, sekretessbelagd information eller brottsbekämpande information? Datavalet påverkar både vad piloten kan visa och vilken risknivå den har.

### Beslutspåverkan

Påverkar AI-stödet faktiska beslut eller endast lärande i testmiljö? Ger stödet information, rekommendationer eller styrande prioriteringar? Detta är en central gräns. Ett stöd som bara sammanfattar material har en annan riskprofil än ett stöd som prioriterar vilka aktörer som ska kontrolleras.

### Tid och volym

Hur länge pågår piloten och hur många ärenden, dokument eller användartillfällen omfattar den? En pilot behöver tillräcklig volym för att ge lärande, men den ska inte smygövergå i permanent användning utan beslut.

### Stoppregler

När ska piloten pausas eller avbrytas? Stoppregler kan handla om felaktiga rekommendationer, oacceptabel databehandling, bristande användarförtroende, säkerhetsincidenter eller att nyttan inte kan mätas.

## Pilotens styrning och roller

En AI-pilot behöver en lätt men tydlig styrning. Den ska inte tyngas ner av samma process som ett stort flerårigt program, men den får inte heller drivas som ett informellt experiment utan ansvar.

För NTG bör pilotteamet minst omfatta följande roller:

- **Verksamhetsägare:** ansvarar för behov, nytta och förankring i berörd verksamhet.
- **Pilotledare:** håller ihop planering, genomförande, mätning och rapportering.
- **Verksamhetsstrateg eller verksamhetsarkitekt:** säkerställer koppling till målbild, förmågor, portfölj och arkitektur.
- **Juridisk kompetens:** bedömer rättslig grund, personuppgifter, sekretess, beslutspåverkan och dokumentationskrav.
- **Informationssäkerhet:** bedömer skyddsvärde, åtkomst, loggning, leverantörsrisker och säkerhetsåtgärder.
- **Data- och teknisk kompetens:** ansvarar för datakvalitet, modellval, integration, testmiljö och tekniska begränsningar.
- **Användarrepresentanter:** prövar stödet i arbetsflödet och beskriver faktisk användbarhet.
- **Uppföljningsansvarig:** säkerställer att mätetal, observationer och beslut dokumenteras.

I mindre piloter kan samma person bära flera roller, men ansvaren bör ändå vara tydliga. Det viktiga är att ingen central fråga blir osynlig.

## Mät nytta, kvalitet och risk samtidigt

En pilot som bara mäter tidsbesparing kan ge en farligt smal bild. AI kan spara tid men försämra kvalitet, skapa otydligt ansvar eller öka beroendet av svårförståelig teknik. En bra AI-pilot mäter flera dimensioner samtidigt.

### Verksamhetsnytta

Verksamhetsnytta kan mätas som kortare ledtid, minskat dubbelarbete, bättre prioritering, ökad träffsäkerhet, förbättrad service eller snabbare sammanställning av underlag. För NTG:s dokumentgranskning kan det handla om hur snabbt handläggaren hittar relevanta avvikelser och hur mycket manuellt sorteringsarbete som minskar.

### Kvalitet

Kvalitet handlar om resultatens tillförlitlighet. Missar stödet viktiga avvikelser? Markerar det för mycket irrelevant? Är sammanfattningar korrekta? Går det att följa vilka källor som använts? Vid generativ AI är kvalitet särskilt viktig eftersom välformulerad text kan låta trovärdig även när den är ofullständig eller felaktig.

### Risk

Riskmätning bör omfatta juridiska, etiska, säkerhetsmässiga och verksamhetsmässiga risker. Det kan handla om felaktig beslutspåverkan, otillåten databehandling, bristande spårbarhet, snedvridning, överautomatisering eller att användare börjar lita för mycket på stödet.

### Användbarhet

Användbarhet handlar om om stödet passar arbetssättet. Förstår användarna vad stödet gör? Vet de när de ska lita på det och när de ska ifrågasätta det? Kan de ge återkoppling? Skapar stödet merarbete någon annanstans?

### Införbarhet

Införbarhet är ofta den mest underskattade dimensionen. En pilot kan fungera bra i liten skala men vara svår att skala om den kräver manuell datarensning, specialkompetens, otydliga avtal, hög kostnad eller en teknisk miljö som inte går att förvalta.

## Exempel: NTG:s pilot för dokumentgranskning

NTG väljer att genomföra en verksamhetspilot för AI-stödd dokumentgranskning i ett avgränsat legalt varuflöde. Syftet är att pröva om stödet kan hjälpa handläggare att snabbare hitta avvikelser i dokument och deklarationsunderlag.

Pilotens hypoteser är att handläggare kan minska tiden för första genomgång, att kvaliteten i identifierade avvikelser bibehålls eller förbättras och att stödet upplevs som kontrollerbart. Stödet får inte fatta beslut, inte automatiskt initiera kontrollåtgärder och inte användas för sanktionsbeslut. Det ska bara markera möjliga avvikelser och visa underlag för handläggarens egen bedömning.

Datamängden begränsas till ett urval av historiska och aktuella dokumenttyper där rättslig grund, sekretess och åtkomst är prövade. Känsligare brottsbekämpande information ingår inte i första piloten. Juridik och informationssäkerhet deltar från start, inte som granskare i slutet.

Under piloten följs fem mätområden:

- tid för första genomgång,
- antal relevanta avvikelser som identifieras,
- andel irrelevanta markeringar,
- användarnas förtroende och förståelse,
- tekniska och organisatoriska hinder för skalning.

Efter sex veckor visar piloten att tiden för första genomgång minskar, men också att stödet ibland markerar avvikelser utan tillräcklig förklaring. Handläggarna vill se tydligare källa och skäl till varje markering. Pilotens slutsats blir därför inte omedelbar skalning. I stället beslutar NTG att justera användargränssnittet, förbättra förklaringsstödet och genomföra en ny begränsad pilot innan beslut om bredare införande.

Detta är ett gott resultat. En pilot som visar vad som behöver ändras har skapat värde. Misslyckandet hade varit att skala för tidigt bara för att den första demonstrationen såg lovande ut.

## Särskilt om brottsbekämpande användningsfall

AI-piloter i brottsbekämpande eller underrättelsenära verksamhet kräver särskild försiktighet. Det betyder inte att de aldrig ska göras, men pilotens syfte, data, åtkomst, ansvar och beslutspåverkan behöver vara mycket tydligt avgränsade.

För NTG kan ett AI-stöd för underrättelsesammanställning vara värdefullt om analytiker snabbare kan få överblick över stora textmängder, tidigare ärenden, öppna källor eller samverkansunderlag. Samtidigt finns risker: felaktiga samband kan framstå som säkra, personuppgifter kan behandlas på olämpligt sätt, sekretess kan hanteras fel, och stödet kan påverka prioriteringar utan att det syns.

En försiktig första pilot kan därför begränsas till sammanfattning och strukturering av redan tillåtet material, utan att AI-stödet föreslår misstänkta personer, tvångsåtgärder eller operativa åtgärder. Analytikern använder stödet för att navigera material, men ansvarar själv för bedömningen. Varje sammanfattning behöver kunna spåras till källmaterial och granskas kritiskt.

Verksamhetsstrategens och verksamhetsarkitektens uppgift är här att hjälpa organisationen att sätta rätt gräns. Frågan är inte bara vad tekniken kan göra, utan vilken användning som är förenlig med uppdrag, lag, tillit och myndighetens ansvar.

## Beslutsgrindar genom piloten

En pilot bör ha tydliga beslutspunkter. Det gör att ledningen kan styra utan att detaljstyra, och det gör att pilotteamet vet när det behöver lyfta frågor.

En enkel modell är fyra beslutspunkter.

### Beslutspunkt 1: Starta pilot

Här prövas om syfte, hypoteser, avgränsning, risknivå, resurser och ansvar är tillräckligt tydliga. Om dessa delar saknas bör piloten inte starta, även om tekniken finns tillgänglig.

### Beslutspunkt 2: Gå in i verksamhetstest

Efter teknisk och datamässig förberedelse prövas om stödet får användas i ett verkligt eller verklighetsnära arbetsflöde. Här bör juridik, informationssäkerhet och verksamhetsägare ha accepterat avgränsningen.

### Beslutspunkt 3: Fortsätta, justera eller pausa

Under piloten behöver teamet kunna agera på observationer. Om användare inte förstår stödet, om datakvaliteten är för svag eller om riskerna blir större än väntat ska piloten justeras eller pausas.

### Beslutspunkt 4: Skala, gör om eller avsluta

När piloten avslutas ska beslutet inte bara handla om teknisk framgång. Beslutet bör baseras på samlad bedömning av nytta, kvalitet, risk, användbarhet, kostnad, arkitektur och förvaltningsbarhet.

## Vanliga misstag

- **Misstag: Att kalla en demonstration för pilot.**
  - Varför det händer: tekniken ger snabbt imponerande exempel.
  - Hur du undviker det: definiera vilka verksamhetshypoteser som faktiskt ska testas.

- **Misstag: Att börja med för känsliga användningsfall.**
  - Varför det händer: de mest kritiska problemen känns mest angelägna.
  - Hur du undviker det: börja där lärandet är stort men riskerna går att kontrollera.

- **Misstag: Att mäta bara effektivisering.**
  - Varför det händer: tidsbesparing är lätt att kommunicera.
  - Hur du undviker det: mät även kvalitet, risk, användbarhet och införbarhet.

- **Misstag: Att involvera juridik och informationssäkerhet för sent.**
  - Varför det händer: pilotteamet vill komma igång snabbt.
  - Hur du undviker det: gör dem till en del av pilotdesignen, inte en slutgranskning.

- **Misstag: Att skala från ett för smalt test.**
  - Varför det händer: en positiv pilot skapar förväntningar.
  - Hur du undviker det: kontrollera att piloten testat verkliga beroenden, användare och risker.

## Reflektionsfrågor för läsaren

1. Vilket AI-initiativ i din organisation skulle kunna prövas som en kontrollerad verksamhetspilot snarare än som ett stort införande?
2. Vilka hypoteser skulle en sådan pilot behöva besvara för att ge ledningen ett bra beslutsunderlag?
3. Vilka data skulle kunna användas i första steget utan att risknivån blir onödigt hög?
4. Vilka roller behöver delta redan innan piloten startar?
5. Vilka stoppregler skulle vara rimliga om piloten visar oväntade risker?

## Praktiskt beslutsstöd: pilotkort

Ett enkelt pilotkort kan användas för att skapa gemensam tydlighet innan piloten startar.

| Fråga | Svar att fylla i |
|---|---|
| Vilket verksamhetsproblem prövas? | |
| Vilka hypoteser ska piloten testa? | |
| Vilka användare deltar? | |
| Vilka informationsmängder används? | |
| Vilken beslutspåverkan får AI-stödet ha? | |
| Vilka juridiska och säkerhetsmässiga avgränsningar gäller? | |
| Vilka mätetal används för nytta, kvalitet och risk? | |
| Vilka stoppregler gäller? | |
| Vilka beslut ska fattas efter piloten? | |

Pilotkortet bör inte bli en pappersprodukt. Det ska användas i dialog mellan verksamhet, ledning, juridik, informationssäkerhet, arkitektur och utveckling.

## Piloten måste pröva hela införandet
En AI-pilot som bara visar att en modell eller tjänst fungerar tekniskt ger begränsat beslutsunderlag. I myndighetsmiljö behöver piloten också pröva om lösningen fungerar i rättsligt, organisatoriskt, informationsmässigt och förändringsmässigt hänseende.

För NTG bör en pilot därför besvara frågor som:

- Förstår användarna vad AI-stödet gör och inte gör?
- Passar stödet in i befintligt arbetssätt?
- Kan resultatet dokumenteras och granskas?
- Är informationskällorna tillräckligt kvalitetssäkrade?
- Finns tydlig ansvarsfördelning när AI-stödet har fel?
- Påverkas rättssäkerhet, likabehandling eller tillit?

Det innebär att pilotens framgång inte bara ska mätas med precision, tidsbesparing eller användarnöjdhet. Den ska också mätas mot införandeförmåga. Om piloten visar att tekniken fungerar men att arbetssätt, dataägarskap eller juridisk styrning saknas är det fortfarande ett värdefullt resultat.

## Snabb sammanfattning

- En AI-pilot ska testa mer än teknik. Den ska testa nytta, ansvar, data, arbetssätt, risk och införbarhet.
- Skillnaden mellan proof of concept, verksamhetspilot och förmågepilot behöver vara tydlig.
- Bra piloter börjar med hypoteser och avgränsningar, inte med lösningsentusiasm.
- Mätetal bör omfatta verksamhetsnytta, kvalitet, risk, användbarhet och skalbarhet.
- Brottsbekämpande och underrättelsenära användningsfall kräver särskild försiktighet, tydlig beslutspåverkan och stark spårbarhet.
- Ett gott pilotresultat kan vara att myndigheten lär sig vad som behöver ändras innan skalning.
- Pilotens viktigaste leverans är ett trovärdigt beslutsunderlag för nästa steg.

## Nästa steg

När piloten är utformad och genomförd uppstår nästa strategiska fråga: hur får organisationen människor, kultur, kompetens och ledarskap att följa med? Nästa kapitel handlar om förändringsledning och kompetens. Där flyttas fokus från pilotens design till myndighetens förmåga att ta emot, förstå och använda AI på ett hållbart sätt.
