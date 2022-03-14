# Tankar/ Idéer

Nedan är tankar/idéer som jag ville implementera men som inte hann realiseras


Jag valde en mer komplicerad databas modell med "chattrum" än en simpel direkt 1-1 chatt
 - Det är lätt att expandera till gruppchatter i framtiden
 - Jag tittade på möjligheterna att skapa en realtids app med Django Channels.
   Det kändes lite för komplicerat för de US:ar som jag skulle implementera 
   men denna strukturen borde göra det simplare att gå över till t.ex Channels i framtiden om behovet uppstår




Vill inte ha rena PK:s i API:t för att förhindra att folk gissar sig till chatrum man inte har tillgång till
Eller lär sig mer om databasen än vad man borde.
Just att förhindra folk från att hitta rum dom inte borde kan man göra med permissions.
Är du en del av chatrummet så kommer du åt endpoint:en


Paginerat resultat av messages för att förhindra för stor datamängd


När man skapar ett rum så borde man endast ange en lista på de andra personerna som man vill ha med
Dig själv borde man inte behöva ange eftersom det är ganska självklart att du borde vara en del av rummet


Namnet på ett chatrum borde vara autogenererat utifrån deltagarnas namn
Möjlighet att ändra på det i efterhand ska finnas


Om man försöker skapa en chat som redan finns, dvs en chatt med samma deltagare existerar som den du försöker skapa,
så ska den returnera den existerade chatten istället för att skapa en ny


Tester...
Det är inte produktionsredo kod om det inte finns tester...
