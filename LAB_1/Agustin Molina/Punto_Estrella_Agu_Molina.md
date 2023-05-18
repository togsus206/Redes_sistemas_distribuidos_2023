# Encoding en nombres de dominio

##### Redes y sistemas Distribuidos : Primer laboratorio

###### Agustín A. Molina

Los nombres de los dominios internacionalizados
(Internationalized Domain Name o IDN) varían, algunos sé
conforman con caracteres latinos, europeos e incluso
emojis, que rompen estándar de nombres de dominio, para
una solución se optó por el cambio del estándar o
diferentes formas de convertir los nombres de dominios
Internacionalizados en ASCII estándar.   

Aquí toma relevancia el **encoding**, proceso que toma un texto entendible por humanos y lo transforma en una secuencia de caracteres entendible por las computadoras para ser enviado, guardado o representado. Así todos los caracteres son traducidos a una serie de números. Al momento de realizar el proceso inverso, como la representación de texto almacenado en pantalla, la computadora utiliza una tabla de encoding para la traducción inversa de los números a caracteres. **UTF-8** es uno de los encodings más usados, representa los caracteres con cantidades variadas de bits, de 1 a 4 bytes, puede representar todos los caracteres de Unicode que es un estándar de codificación de caracteres de múltiples idiomas e incluso lenguas muertas. Unicode también es uno de los esquemas más completos de codificación de caracteres.

Volviendo a UTF-8, el IETF **requiere que todos los protocolos de Internet indiquen qué codificación utilizan para los textos y que UTF-8 sea una de las codificaciones contempladas**. Es decir, en el caso de estar en una página, el texto que introducimos se convertirá de acuerdo al encoding del navegador, cuyo resultado será recibido por una base de datos que también trabajara con un encoding, el lenguaje de programación que constituye la página también tiene su encoding, etc. Esto plantea problemas en el uso de un encoding incorrecto, llegando a representar los números que constituían en principio un mensaje a una serie de caracteres sin sentido.

---

#### ASCII O NO ASCII

  La traducción de un nombre de dominio es mediante las funciones **ToASCII** y **ToUnicode**. Estas
se aplican a las partes, etiquetas, ejemplo: teniendo el nombre de dominio es
www.aprendiendo.com, obtenemos las etiquetas www, aprendiendo y com. Ambas funciones se
aplican en las etiquetas.

**ToASCII** no tiene efectos sobre caracteres ASCII, si en cuales no son caracteres ASCII. Aquí se pasa todo el nombre de dominio a minúscula, luego mediante **Punycode**, explicado mas adelante, obtenemos la traducción a ASCII.


  **ToUnicode** hace el proceso inverso a ToASCII, usa el algoritmo de decodificación Punycode.

Para que el IDN 中文.tw funcione, se emplea la codificación **Punycode**, que usa una cadena Unicode para luego ser traducida a una cadena de caracteres compatible con los nombres de red. Punycode es utilizada para IDNA (Internacionalización de Nombres de Dominio en Aplicaciones en inglés). Los caracteres 中文, al igual que los emojis, son aceptados por algunos navegadores y en casos contrarios remplazados por otros.
Cada emoji está representado mediante una cadena de caracteres universales llamada Unicode. Como Punycode solo acepta letras, dígitos y guiones, al tomar un dominio como 🍺🍺🍺.ws le agrega "xn--" al comienzo y remplaza sus emojis por la codificación correspondiente,

![budweiser](/Agustin Molina/bud.png)

Ejemplo si tomamos el dominio 🦄.ws y lo convertimos a Punycode obtenemos xn--3s9h.ws, y no
solo se aplica a emojis, ejemplo diseño.com se codifica como xn--diseo-rta.com. "xn --" es
llamado prefijo ACE(ASCII Compatible Encoding).

---

Los dominios emojis no se pueden aplicar con tanta facilidad. La **ICANN** (Internet Corporation for Assigned Names and Numbers), si bien elaboro políticas para todos los dominios genéricos de nivel superior, las **ccTLD**, conocidas como dominios del país, aplican sus propias políticas. La principal preocupación de ICANN es el phishing, teniendo en cuenta que la cantidad de emojis que un celular contiene es abrumadora, es alta la posibilidad que alguien no perciba la diferencia entre un emoji y otro, pudiendo colocar datos, contraseñas y demás en sitios peligrosos. La mayoría de los países tomo las políticas de ICANN, mientras que otros permiten el uso de emojis en sus dominios como: .ws (Samoa Occidental), .LA (Laos), .AI (Anguilla) y .TO (Tonga).

Bibliografía:

- [ICANN](https://www.icann.org/en/system/files/files/sac-095-en.pdf)
- [Nombre de Dominio](https://es.wikipedia.org/wiki/Nombre_de_dominio_internacionalizado)
- [Punycode](https://es.wikipedia.org/wiki/Punycode)
- [Emoji Domains Are the Future (Maybe)](https://gizmodo.com/emoji-domains-are-the-future-maybe-1823319626)
- [Dnacademy](https://www.dnacademy.com/emoji-domains)
